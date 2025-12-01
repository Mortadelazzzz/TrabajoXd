from View.Ui_inicioSistema import Ui_MainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
import sys
import sistemaVentasVivo
import sistemaVentasBeneficiado
import serial
import time
import socket
import pulsosArduino
from datetime import datetime
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve

# Importación de Base de Datos
import DataBase.database_conexion # El archivo database_conexion.py

# Puertos COM
COMAR = ""
COM1 = ""
COM2 = ""

appVentaBeneficiado = False
appVentaVivo = False

pesoBalanza1 = False
pesoBalanza2 = False

listCodClienteCambiarPesada = []
listEstadoClienteCambiarPesada = []
indexListaCambiarPesada = 0
codigoClienteCambiarPesada = 0

""" Creamos hilo para la ejecución en segundo plano del Indicador , de esta forma
evitamos que la aplicación se detenga por la lectura constante """

class WorkerThread(QThread):
    update_peso = pyqtSignal(str)
    update_estado = pyqtSignal(str)
    update_baliza = pyqtSignal(str)
    
    def run(self):
        COMINDICADOR1 = "COM" + COM1
        serialIndicador = None

        while True:
            try:
                if serialIndicador is None or not serialIndicador.is_open:
                    serialIndicador = serial.Serial(COMINDICADOR1, baudrate=9600, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
                
                result = serialIndicador.readline().decode('utf-8').strip()
                if not result:
                    self.update_peso.emit("+0.00")
                    self.update_baliza.emit("+0.00")
                    self.update_estado.emit("0")
                else:
                    # self.update_peso.emit(result[6:14]) # Tscale
                    # self.update_baliza.emit(result[6:14]) # Tscale 
                
                    self.update_peso.emit(result[6:13]) # Weight
                    self.update_baliza.emit(result[6:13]) # Weight

                    # self.update_peso.emit(result[2:10]) # Yaohua 
                    # self.update_baliza.emit(result[2:10]) # Yaohua 
                    self.update_estado.emit("1")
            except Exception as e:
                # print("WT IN: " + str(e))
                time.sleep(1)
                # Cerrar la conexión serial si hay una excepción
                if serialIndicador is not None and serialIndicador.is_open:
                    serialIndicador.close()
    
    def stop(self):
        print("Thread Stopped")
        self.terminate()
        
""" Creamos hilo para la ejecución en segundo plano para subir los datos al servidor """

class WorkerThreadSubirDatosBase(QThread):
    # Tarea a ejecutarse cada determinado tiempo.
    def run(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            try:
                s.connect(("www.google.com", 80))
            except (socket.gaierror, socket.timeout):
                print("Sin conexión a internet")
            else:
                print("Con conexión a internet")
                try:
                    self.conexion = DataBase.database_conexion.Conectar()
                    self.conexion.actualizar_datos_servidor_pesadas()
                    self.conexion.actualizar_datos_local_a_servidor_comentarios()
                    self.conexion.actualizar_datos_local_a_servidor_prestamos()
                except Exception as e:
                    print(f"Error al interactuar con la base de datos: {e}")
                    print('ERROR')
                else:
                    s.close()
            time.sleep(240)
            
class WorkerThreadTraerDatosDeOtraPc(QThread):
    # Tarea a ejecutarse cada determinado tiempo.
    def run(self):
        while True:
            try:
                self.conexion = DataBase.database_conexion.Conectar()
                self.conexion.db_traer_pesadas_desde_otra_pc()
            except Exception as e:
                print(f"Error al interactuar con la base de datos: {e}")
                print('ERROR')

            time.sleep(120)

""" Creamos hilo para la ejecución en segundo plano del Arduino, de esta forma
evitamos que la aplicación se detenga por la lectura constante  """
            
class WorkerThreadAR(QThread):
    def __init__(self):
        super().__init__()
        self.serialArduino = None
        self.user_input_arduino = ""
        self.contador = 3

    def run(self):
        try:
            COMARDUINO = "COM" + COMAR
            # Configura los parámetros del puerto serie
            self.serialArduino = serial.Serial()
            self.serialArduino.baudrate = 9600
            self.serialArduino.bytesize = serial.EIGHTBITS
            self.serialArduino.parity = serial.PARITY_NONE
            self.serialArduino.stopbits = serial.STOPBITS_ONE 

            # Reemplaza 'COMX' por el nombre del puerto en tu sistema (p. ej., 'COM3' en Windows, '/dev/ttyUSB0' en Linux)
            self.serialArduino.port = COMARDUINO
            
            while self.contador > 1 and not self.serialArduino.is_open:
                if self.serialArduino is None or not self.serialArduino.is_open:
                    self.serialArduino.open()
                    
                self.contador = self.contador - 1
            
            if self.serialArduino.is_open:
                print("Conectado al puerto Arduino en", self.serialArduino.port)
                time.sleep(2)
                self.serialArduino.write(str("x").encode('utf8'))
            else:
                print("No se pudo abrir el puerto Arduino.")
        except serial.SerialException as e:
            # print("Serial Exception: " + str(e))
            time.sleep(1)  # Espera antes de intentar reconectar
        except Exception as e:
            print("Other Exception: " + str(e))

    def stop(self):
        print("Thread Stopped")
        if self.serialArduino:
            self.serialArduino.close()
        self.terminate()
        
def fn_declararPuertoArduino():
    global COMAR
            
    puertoArduino = DataBase.database_conexion.Conectar().db_seleccionaPuertoArduino()
    COMAR = str(puertoArduino[0])
        
fn_declararPuertoArduino()
        
workerAR = WorkerThreadAR()  # Instancia de WorkerThreadAR
workerAR.start()  # Inicia el hilo

# ===============================
# Creación de la Clase Principal
# ===============================

class InicioSistema(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.conexion = DataBase.database_conexion.Conectar()
        
        self.moduloVentasVivo = sistemaVentasVivo.Inicio()
        self.moduloVentasBeneficiado = sistemaVentasBeneficiado.Inicio()
        self.pulsosArduino = pulsosArduino
        
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QtGui.QIcon("Imagenes/iconoApp.png"))
        self.setWindowTitle('SISTEMA INTEGRAL || BALINSA')
        
        self.ui.imgVentaBeneficiado.setPixmap(QPixmap("Imagenes/Pollo_Beneficiado.png"))
        self.ui.imgVentaVivo.setPixmap(QPixmap("Imagenes/Pollo_Vivo.png"))
        self.ui.lblmimizar.setPixmap(QPixmap("Imagenes/minimizar.png"))
        self.ui.lblcerrar.setPixmap(QPixmap("Imagenes/cerrar.png"))
        self.ui.img_unidad_mantenimiento.setPixmap(QPixmap("Imagenes/configuraciones.png"))
        self.ui.imgFondo.setPixmap(QPixmap("Imagenes/imgFondo.jpg"))
        self.ui.imgPrestamo.setPixmap(QPixmap("Imagenes/prestamo.png"))
        
        self.ui.btnCerrar.clicked.connect(self.fn_cerrarPrograma)
        self.ui.btnminimizar.clicked.connect(self.fn_minimizarPrograma)
        self.ui.btnUnidadMantenimiento.clicked.connect(self.fn_unidadMantenimiento)
        self.ui.btnCerrarFrmAlerta.clicked.connect(self.fn_cerrarUnidadMantenimiento)
        self.ui.btnAbrirVentanaPrestamo.clicked.connect(self.fn_abrirFrmPrestamo)
        self.ui.btnCerrarFrmPrestamoCubetasJabas.clicked.connect(self.fn_cerrarFrmPrestamo)
        self.ui.btnGuardarFrmPrestamoCubetasJabas.clicked.connect(self.fn_guardarPrestamo)
        self.ui.btnCambiarClientePrestamoCubetasJabas.clicked.connect(self.fn_cambiarClienteCambiarPesada)
        
        self.ui.txtCodigoClienteCambiarPesada.textChanged.connect(self.fn_recepcionaCodigoTrabajadorCambiarPesada)
        self.ui.txtCantidadPrestamo.textChanged.connect(self.fn_validarEntradaNumerica)
        
        self.ui.btnOnLedVerde.clicked.connect(self.pulsosArduino.fn_encenderPulsoVerde)
        self.ui.btnOffLedVerde.clicked.connect(self.pulsosArduino.fn_apagarPulsoVerde)
        self.ui.btnOnLedRojo.clicked.connect(self.pulsosArduino.fn_encenderPulsoRojo)
        self.ui.btnOffLedRojo.clicked.connect(self.pulsosArduino.fn_apagarPulsoRojo)
        self.ui.btnOnBuzzer.clicked.connect(self.pulsosArduino.fn_encenderPulsoBuzzer)
        self.ui.btnOffBuzzer.clicked.connect(self.pulsosArduino.fn_apagarPulsoBuzzer)
        self.ui.btnActivaPulsoOnOff.clicked.connect(self.pulsosArduino.fn_activarPulsoEnciendeApagaIndicador)
        self.ui.btnActivaPulsoZero.clicked.connect(self.pulsosArduino.fn_activarPulsoZero)
        
        self.fn_declararPuertoIndicadores()
        
        self.worker = WorkerThread() # Hilo Balanza 1
        self.worker.start()
        self.worker.update_peso.connect(self.moduloVentasVivo.evt_actualizar_peso)
        self.worker.update_estado.connect(self.moduloVentasVivo.evt_actualizar_estado)
        self.worker.update_baliza.connect(self.moduloVentasVivo.evt_actualizar_baliza)
        
        self.worker.update_peso.connect(self.moduloVentasBeneficiado.evt_actualizar_peso)
        self.worker.update_estado.connect(self.moduloVentasBeneficiado.evt_actualizar_estado)
        self.worker.update_baliza.connect(self.moduloVentasBeneficiado.evt_actualizar_baliza)
        
        self.fn_traerDatosServidor() 
        self.workerBase = WorkerThreadSubirDatosBase() # Actualización Base de Datos de Local a Servidor
        self.workerBase.start()
        
        self.workerReplicaTabla = WorkerThreadTraerDatosDeOtraPc()
        self.workerReplicaTabla.start()
        
        self.ui.frmSombra.setHidden(True)
        self.ui.frmAlertaUnidadDeMantenimiento.setHidden(True)
        self.ui.frmIngresarPassword.setHidden(True)
        self.ui.frmPrestamoCubetasJabas.setHidden(True)
        self.ui.frmAlerta.setHidden(True)
        
        tablaDePesos = self.ui.tblDetallePrestamo
        tablaDePesos.setColumnWidth(0, 50)
        tablaDePesos.setColumnWidth(1, 300)
        tablaDePesos.setColumnWidth(2, 150)
        tablaDePesos.setColumnWidth(3, 150)
        tablaDePesos.setColumnWidth(4, 100)
        tablaDePesos.setColumnWidth(5, 100)
        tablaDePesos.setColumnHidden(6, True)
        tablaDePesos.setAlternatingRowColors(True)
    
    def fn_traerDatosServidor(self):
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.settimeout(5)
        try:
            s2.connect(("www.google.com", 80))
        except (socket.gaierror, socket.timeout):
            print("Sin conexión a internet")
        else:
            print("Con conexión a internet")
            try:
                self.conexion.actualizar_datos_servidor_a_local_clientes()
                self.conexion.actualizar_datos_servidor_a_local_precios()
                self.conexion.actualizar_datos_servidor_a_local_password()
                self.conexion.actualizar_datos_servidor_a_local_pedidos()
                print("Exito al interactuar con la base de datos")
            except Exception as e:
                print(f"Error al interactuar con la base de datos: {e}")
            else:
                s2.close()
    
    def fn_declararPuertoIndicadores(self):
        global COM1
        global COM2
        
        puertoIndicadores = self.conexion.db_seleccionaPuertoIndicadores()
        COM1 = str(puertoIndicadores[0][0])
        COM2 = str(puertoIndicadores[0][1])
        
    def fn_cerrarPrograma(self):
        
        self.pulsosArduino.fn_activarPulsoEnciendeApagaIndicador()
            
        time.sleep(1)
                        
        # Cerrar la instancia de Ventas en Vivo si existe
        if self.moduloVentasVivo and self.moduloVentasVivo.isVisible():
            self.moduloVentasVivo.close()

        # Cerrar la instancia de Ventas Beneficiado si existe
        if self.moduloVentasBeneficiado and self.moduloVentasBeneficiado.isVisible():
            self.moduloVentasBeneficiado.close()

        # Cerrar la ventana principal
        self.close()
    
    def fn_minimizarPrograma(self):
        self.showMinimized()
        
    def fn_unidadMantenimiento(self):
        self.ui.frmSombra.setHidden(False)
        self.ui.frmIngresarPassword.setHidden(False)
        self.ui.txtPasswordUnidadMantenimiento.setFocus(True)
        self.ui.txtPasswordUnidadMantenimiento.setText("")
        
    def fn_cerrarUnidadMantenimiento(self):
        self.ui.frmSombra.setHidden(True)
        self.ui.frmAlertaUnidadDeMantenimiento.setHidden(True)
        
    def fn_validarEntradaNumerica(self):
        sender = self.sender()

        if sender is not None and isinstance(sender, QLineEdit):
            texto = sender.text()

            texto_valido = ''.join(filter(str.isdigit, texto))

            sender.setText(texto_valido)
    
    def fn_cerrarFrmPrestamo(self):
        self.ui.frmSombra.setHidden(True)
        self.ui.frmPrestamoCubetasJabas.setHidden(True)
        
    def fn_abrirFrmPrestamo(self):
        global codigoClienteCambiarPesada
        global indexListaCambiarPesada
        
        codigoClienteCambiarPesada = 0
        indexListaCambiarPesada = 0
        
        self.ui.frmSombra.setHidden(False)
        self.ui.frmPrestamoCubetasJabas.setHidden(False)
        self.ui.txtCodigoClienteCambiarPesada.setHidden(False)
        self.ui.txtCodigoClienteCambiarPesada.setText("")
        self.ui.txtCantidadPrestamo.setText("")
        self.ui.txtCodigoClienteCambiarPesada.setFocus(True)
        self.ui.lwListaClientesCambiarPesada.setHidden(False)
        
        self.fn_listarPrestamos()
        
    def fn_recepcionaCodigoTrabajadorCambiarPesada(self):
        global listCodClienteCambiarPesada
        global listEstadoClienteCambiarPesada
        
        self.ui.lwListaClientesCambiarPesada.clear()
        listCodClienteCambiarPesada.clear()
        listEstadoClienteCambiarPesada.clear()
        valor = self.ui.txtCodigoClienteCambiarPesada.text()

        if (valor != "" and len(valor) >= 1):

            nombreClienteSeleccionar = self.conexion.db_buscaCliente(valor)

            if (len(nombreClienteSeleccionar) > 0):
                self.ui.lwListaClientesCambiarPesada.setHidden(False)
                for item in nombreClienteSeleccionar:
                    self.ui.lwListaClientesCambiarPesada.addItem(item[0])
                    listCodClienteCambiarPesada.append(item[1])
                    listEstadoClienteCambiarPesada.append(item[2])
                self.ui.lwListaClientesCambiarPesada.setCurrentRow(0)
                           
    def fn_ArribaListaCambiarPesada(self):
        global indexListaCambiarPesada
        
        if (indexListaCambiarPesada != 0):
            indexListaCambiarPesada -= 1
            self.ui.lwListaClientesCambiarPesada.setCurrentRow(indexListaCambiarPesada)

    def fn_AbajoListaCambiarPesada(self):
        global indexListaCambiarPesada
        
        numClientes = self.ui.lwListaClientesCambiarPesada.count()
        if (indexListaCambiarPesada < numClientes-1):
            indexListaCambiarPesada += 1
            self.ui.lwListaClientesCambiarPesada.setCurrentRow(indexListaCambiarPesada)
            
    def fn_seleccionarClienteCambiarPesada(self):
        global codigoClienteCambiarPesada
        global indexListaCambiarPesada
        
        indice = self.ui.lwListaClientesCambiarPesada.currentIndex().row()
        codClienteCambiarPesada = listCodClienteCambiarPesada[indice]

        item = QListWidgetItem(self.ui.lwListaClientesCambiarPesada.currentItem())
        
        self.ui.txtNombreClienteCambiarPesada.setText(str(item.text()))
        self.ui.lwListaClientesCambiarPesada.setHidden(True)
        self.ui.txtCodigoClienteCambiarPesada.setHidden(True)
        
        codigoClienteCambiarPesada = codClienteCambiarPesada
        indexListaCambiarPesada = 0
        
        self.fn_calcularPrestamo()
    
    def fn_cambiarClienteCambiarPesada(self):
        global codigoClienteCambiarPesada
        global indexListaCambiarPesada
        
        codigoClienteCambiarPesada = 0
        indexListaCambiarPesada = 0
            
        self.ui.txtCodigoClienteCambiarPesada.setHidden(False)
        self.ui.txtCodigoClienteCambiarPesada.setText("")
        self.ui.txtCodigoClienteCambiarPesada.setFocus(True)
        self.ui.lwListaClientesCambiarPesada.setHidden(False)
        
    def fn_guardarPrestamo(self):
        
        horaPeso = datetime.now().strftime('%H:%M:%S')
        fechaPeso = datetime.now().strftime('%Y-%m-%d')
        
        tipo = 0 # 1 = Prestamo , 2 = Devolucion
        variedad = 0 # 1 = Cubetas , 2 = Jabas
        mensaje = ""
        
        if self.ui.radioBtnPrestamo.isChecked():
            tipo = 1
            mensaje = "Préstamo guardado correctamente"
        elif self.ui.radioBtnDevolucion.isChecked():
            tipo = 2
            mensaje = "Devolución guardado correctamente"
        
        if self.ui.radioBtnCubetas.isChecked():
            variedad = 1
        elif self.ui.radioBtnJabas.isChecked():
            variedad = 2
            
        cantidad = self.ui.txtCantidadPrestamo.text()
        
        if cantidad != "" and cantidad != "0" and cantidad != 0 and tipo != 0 and variedad != 0 and codigoClienteCambiarPesada != 0:
            self.conexion.db_registrarPrestamo(codigoClienteCambiarPesada,tipo,variedad,cantidad,fechaPeso,horaPeso) 
            
            self.ui.txtCantidadPrestamo.setText("")
            self.fn_mostrarAlerta(mensaje)
            self.fn_listarPrestamos()
            self.fn_calcularPrestamo()
            
    def fn_mostrarAlerta(self, mensaje):
        self.ui.frmAlerta.setHidden(False)
        # timer = QtCore.QTimer()
        # timer.singleShot(2000, lambda: self.ui.frmAlerta.setHidden(True))
        self.ui.lblAlerta.setText(mensaje)

        self.animacion1 = QPropertyAnimation(self.ui.frmAlerta, b"geometry")
        self.animacion1.setDuration(500)
        self.animacion1.setStartValue(QRect(1920, 10, 470, 80))
        self.animacion1.setEndValue(QRect(1440, 10, 470, 80))
        self.animacion1.setEasingCurve(QEasingCurve.OutQuad)

        self.animacion2 = QPropertyAnimation(self.ui.frmAlerta, b"geometry")
        self.animacion2.setDuration(500)
        self.animacion2.setStartValue(QRect(1440, 10, 470, 80))
        self.animacion2.setEndValue(QRect(1920, 10, 470, 80))
        self.animacion2.setEasingCurve(QEasingCurve.InQuad)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.animacion2.start)

        self.animacion1.finished.connect(self.timer.start)
        self.timer.setInterval(1000)

        self.animacion1.start()
        
    def fn_listarPrestamos(self):
        
        tablaDePesos = self.ui.tblDetallePrestamo
        tablaDePesos.clearContents()
        tablaDePesos.setRowCount(0)
        
        prestamosListarTabla = self.conexion.db_listarDatosPrestamos()
        
        if prestamosListarTabla != "" and prestamosListarTabla != None:
            if len(prestamosListarTabla) > 0:
            
                for row_number, row_data in enumerate(prestamosListarTabla):
                    
                        tablaDePesos.insertRow(row_number)
                        
                        for column_number, data in enumerate(row_data):
                            if column_number == 0:
                                data = (row_number - len(prestamosListarTabla))*-1
                            if column_number == 2:
                                if data == "1":
                                    data = "Préstamo"
                                elif data == "2":
                                    data = "Devolución"
                            if column_number == 3:
                                if data == "1":
                                    data = "Cubetas"
                                elif data == "2":
                                    data = "Jabas"
                            if column_number == 5 :
                                hours, remainder = divmod(data.seconds, 3600)
                                minutes, seconds = divmod(remainder, 60)
                                data = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

                            item = QTableWidgetItem(str(data))
                            item.setTextAlignment(Qt.AlignCenter)
                            tablaDePesos.setItem(row_number, column_number, item)
                            
    def fn_calcularPrestamo(self):
        
        if codigoClienteCambiarPesada != "" and codigoClienteCambiarPesada != 0 :
        
            datosPrestamo = self.conexion.db_traerPrestamo(codigoClienteCambiarPesada)
            
            totalJabasPrestadas = 0
            totalCubetasPrestadas = 0
            
            totalJabasDevueltas = 0
            totalCubetasDevueltas = 0
            
            if(datosPrestamo):
                for item in datosPrestamo:
                    tipo_prestamo = int(item[0])
                    variedad_prestamo = int(item[1])
                    cantidad_prestamo = int(item[2])
                    
                    if(tipo_prestamo == 1 and variedad_prestamo == 1):
                        totalCubetasPrestadas += cantidad_prestamo
                    elif(tipo_prestamo == 1 and variedad_prestamo == 2):
                        totalJabasPrestadas += cantidad_prestamo
                    elif(tipo_prestamo == 2 and variedad_prestamo == 1):
                        totalCubetasDevueltas += cantidad_prestamo
                    elif(tipo_prestamo == 2 and variedad_prestamo == 2):
                        totalJabasDevueltas += cantidad_prestamo
            
            resultado = (totalJabasPrestadas - totalJabasDevueltas) + (totalCubetasPrestadas - totalCubetasDevueltas)
            self.ui.txtCantidadPrestada.setText(str(resultado))

    # ======================== Eventos con el Teclado ========================
         
    def keyReleaseEvent(self, event):
        global appVentaBeneficiado
        global appVentaVivo
        
        if (event.key() == Qt.Key_Left):
            appVentaBeneficiado = True
            appVentaVivo = False
            self.ui.imgVentaBeneficiado.setStyleSheet("background-color: rgb(36, 211, 21);border-radius: 15px;border: 2px solid black;border-color: rgb(0, 0, 0);")
            self.ui.imgVentaVivo.setStyleSheet("background-color: transparent;border-radius: 15px;border: 2px solid black;border-color: rgb(0, 0, 0);")
            
        if (event.key() == Qt.Key_Right):
            appVentaVivo = True
            appVentaBeneficiado = False
            self.ui.imgVentaVivo.setStyleSheet("background-color: rgb(36, 211, 21);border-radius: 15px;border: 2px solid black;border-color: rgb(0, 0, 0);")
            self.ui.imgVentaBeneficiado.setStyleSheet("background-color: transparent;border-radius: 15px;border: 2px solid black;border-color: rgb(0, 0, 0);")
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and appVentaVivo == True and appVentaBeneficiado == False and not self.ui.frmIngresarPassword.isVisible() and not self.ui.frmPrestamoCubetasJabas.isVisible():
            if not self.moduloVentasVivo:
                self.moduloVentasVivo = sistemaVentasVivo.Inicio()
            elif not self.moduloVentasVivo.isVisible():
                self.moduloVentasVivo.show()
            else:
                self.moduloVentasVivo.showNormal()
                self.moduloVentasVivo.activateWindow()
                
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and appVentaBeneficiado == True and appVentaVivo == False and not self.ui.frmIngresarPassword.isVisible() and not self.ui.frmPrestamoCubetasJabas.isVisible():
            if not self.moduloVentasBeneficiado:
                self.moduloVentasBeneficiado = sistemaVentasBeneficiado.Inicio()
            elif not self.moduloVentasBeneficiado.isVisible():
                self.moduloVentasBeneficiado.show()
            else:
                self.moduloVentasBeneficiado.showNormal()
                self.moduloVentasBeneficiado.activateWindow()
                
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and self.ui.frmIngresarPassword.isVisible():
            passwordExtraido = self.ui.txtPasswordUnidadMantenimiento.text()
            if "20608165585" == str(passwordExtraido):
                self.ui.frmIngresarPassword.setHidden(True)
                self.ui.frmAlertaUnidadDeMantenimiento.setHidden(False)
        
        if event.key() == Qt.Key_Minus:
            if (self.ui.frmIngresarPassword.isVisible()):
                self.ui.frmIngresarPassword.setHidden(True)
                self.ui.frmSombra.setHidden(True)
                
        if (event.key() == Qt.Key_Plus) and not self.ui.lwListaClientesCambiarPesada.isVisible():
            self.fn_cambiarClienteCambiarPesada()
            
        if event.key() == Qt.Key_Up and self.ui.lwListaClientesCambiarPesada.isVisible():
            self.fn_ArribaListaCambiarPesada()
            
        if event.key() == Qt.Key_Down and self.ui.lwListaClientesCambiarPesada.isVisible():
            self.fn_AbajoListaCambiarPesada()
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and self.ui.lwListaClientesCambiarPesada.isVisible():
            if (len(listCodClienteCambiarPesada)):
                indice = self.ui.lwListaClientesCambiarPesada.currentIndex().row()
                estadoDelCliente = listEstadoClienteCambiarPesada[indice]
                if (estadoDelCliente == 1):
                    self.fn_seleccionarClienteCambiarPesada()
                else:
                    self.fn_cambiarClienteCambiarPesada()
    
    # ======================== Termina eventos con el Teclado ========================
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = InicioSistema()
    gui.show()
    sys.exit(app.exec_())
    
# DISEÑADO Y DESARROLLADO POR SANTOS VILCHEZ EDINSON PASCUAL
# LA UNIÓN - PIURA - PERU ; 2024