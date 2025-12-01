# Importación de Librerias
from PyQt5.QtWidgets import QMainWindow, QLabel, QTableWidgetItem , QWidget, QLabel, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime
from PyQt5.QtGui import QPixmap
import time
import socket
from PyQt5.QtGui import QMovie, QColor, QFont
import threading
import re
import inicioSistema
import ast
import win32print

# Importación de los Layout
from View.Ui_sistemaVentasVivo import Ui_MainWindow # La clase Ui_MainWindow del archivo ui_Principal.py 

# Importación de Base de Datos
import DataBase.database_conexion # El archivo database_conexion.py

# BalanzaSeleccionada
balanzaSeleccionada = 1
pesoAnterior = False

# Contraseña para eliminar
passwordEliminar = ""

# Variables para selección de Clientes
listCodCliente = []
listEstadoCliente = []
indexLista = 0
arreglo_id_reporte = []

listCodClienteCambiarPesada = []
listEstadoClienteCambiarPesada = []
indexListaCambiarPesada = 0
codigoClienteCambiarPesada = 0
precioClienteCambiarPesada = 0

precioCambiarEspecie = 0
idEspecieCambiarEspecie = 0

# Id de cada Especie
primerEspecie = 0
segundaEspecie = 0
terceraEspecie = 0
cuartaEspecie = 0
quintaEspecie = 0
sextaEspecie = 0
septimaEspecie = 0
octavaEspecie = 0
novenaEspecie = 0
decimaEspecie = 0
decimaPrimeraEspecie = 0
decimaSegundaEspecie = 0
decimaTerceraEspecie = 0
decimaCuartaEspecie = 0
decimaQuintaOtrasEspecies = 0
decimaSextaEspecie = 0
decimaSeptimaEspecie = 0
decimaOctavaEspecie = 0
decimaNovenaEspecie = 0
vigesimaEspecie = 0
vigesimaPrimeraEspecie = 0
vigesimaSegundaEspecie = 0
vigesimaTerceraEspecie = 0

# Nombre de cada Especie
nombrePrimerEspecie = ""
nombreSegundaEspecie = ""
nombreTerceraEspecie = ""
nombreCuartaEspecie = ""
nombreQuintaEspecie = ""
nombreSextaEspecie = ""
nombreSeptimaEspecie = ""
nombreOctavaEspecie = ""
nombreNovenaEspecie = ""
nombreDecimaEspecie = ""
nombreDecimaPrimeraEspecie = ""
nombreDecimaSegundaEspecie = ""
nombreDecimaTerceraEspecie = ""
nombreDecimaCuartaEspecie = ""
nombreDecimaQuintaOtrasEspecies = ""
nombreDecimaSextaEspecie = ""
nombreDecimaSeptimaEspecie = ""
nombreDecimaOctavaEspecie = ""
nombreDecimaNovenaEspecie = ""
nombreVigesimaEspecie = ""
nombreVigesimaPrimeraEspecie = ""
nombreVigesimaSegundaEspecie = ""
nombreVigesimaTerceraEspecie = ""

# Cantidad Colores de Jabas
cantidadPrimerColor = 0
cantidadSegundoColor = 0
cantidadTercerColor = 0
cantidadCuartaColor = 0
cantidadQuintoColor = 0
cantidadSextoColor = 0
cantidadSeptimoColor = 0

pesoPrimerColor = 0
pesoSegundoColor = 0
pesoTercerColor = 0
pesoCuartaColor = 0
pesoQuintoColor = 0
pesoSextoColor = 0
pesoSeptimoColor = 0

# Variables de Clientes por Balanza
codCliente1 = 0
codCliente2 = 0
especieCli1 = 0
especieCli2 = 0
especieDesCli1 = 0
especieDesCli2 = 0

idPesadaEditarOEliminar = 0

# Variables de Precio
precioPrimerEspecie = 0
precioSegundaEspecie = 0
precioTerceraEspecie = 0
precioCuartaEspecie = 0
precioQuintaEspecie = 0
precioSextaEspecie = 0
precioSeptimaEspecie = 0
precioOctavaEspecie = 0
precioNovenaEspecie = 0
precioDecimaEspecie = 0
precioDecimaPrimeraEspecie = 0
precioDecimaSegundaEspecie = 0
precioDecimaTerceraEspecie = 0
precioDecimaCuartaEspecie = 0
precioDecimaQuintaOtrasEspecies = 0
precioDecimaSextaEspecie = 0
precioDecimaSeptimaEspecie = 0
precioDecimaOctavaEspecie = 0
precioDecimaNovenaEspecie = 0
precioVigesimaEspecie = 0
precioVigesimaPrimeraEspecie = 0
precioVigesimaSegundaEspecie = 0
precioVigesimaTerceraEspecie = 0

precioPrimerEspecie_ant = 0
precioSegundaEspecie_ant = 0
precioTerceraEspecie_ant = 0
precioCuartaEspecie_ant = 0
precioQuintaEspecie_ant = 0
precioSextaEspecie_ant = 0
precioSeptimaEspecie_ant = 0
precioOctavaEspecie_ant = 0
precioNovenaEspecie_ant = 0
precioDecimaEspecie_ant = 0
precioDecimaPrimeraEspecie_ant = 0
precioDecimaSegundaEspecie_ant = 0
precioDecimaTerceraEspecie_ant = 0
precioDecimaCuartaEspecie_ant = 0
precioDecimaQuintaOtrasEspecies_ant = 0
precioDecimaSextaEspecie_ant = 0
precioDecimaSeptimaEspecie_ant = 0
precioDecimaOctavaEspecie_ant = 0
precioDecimaNovenaEspecie_ant = 0
precioVigesimaEspecie_ant = 0
precioVigesimaPrimeraEspecie_ant = 0
precioVigesimaSegundaEspecie_ant = 0
precioVigesimaTerceraEspecie_ant = 0

# Variables de Nombres de Cliente por Balanza
nombresCliBalanza = ""
nombresCliBalanza1 = ""
nombresCliBalanza2 = ""

# Variables bandera
frmRegistrarCantidad = False
frmAlertaEliminarPeso = False
frmEliminarPeso = False
frmAlerta = False
frmRegistrarDescuento = False
frmEditarCantidad = False
frmInicioProceso = False
frmRegistrarJabas = False
frmRegistrarDescuentoCan = False
frmEditarCantidadTara = False
frmEditarCantidadDescuento = False
frmSeleccionarTipoTrozado = False
frmIngresarNumeroPesadaEditar = False
frmIngresarNumeroPesadaEliminar = False
frmIngresarNumeroColoresEditar = False
frmRegistrarColoresJabas = False
frmSeleccionarTipoTrozadoDesc = False
frmRegistrarColoresJabasEditar = False
frmDecidirReporte = False
frmIngresarNumeroPesoJabaEditar = False
frmSeleccionaPesadasReporte = False
frmIngresarNumeroPesadaEditarEspecie = False
frmSeleccionarEspecieEditarPesada = False
frmCambiarPesadaCliente = False
frmIngresarNumeroCambiarPesada = False
frmAlertaDesicionEnvio = False
frmAlertaIngresaNumeroEnvio = False
frmAlertaDesicionResponsable = False
frmAlertaIngresaResponsablesDeEnvio = False
frmAlertaIngresaNombreVenta = False
frmIngresarPrecioVenta = False

imprimePrecio = False
modoOscuro = False

incluyeEnvio = False
incluyeResponsable = False
numeroEnvio = 0
enviaTodoReporteImprimir = False
diccionarioResponsablesDeEnvio  = None

# Variables para la Base de Datos
numProceso = 0
idEspecie = 0
pesoNeto = 0
horaPeso = datetime.now().strftime('%H:%M:%S')
codCliente = 0
fechaPeso = datetime.now().strftime('%Y-%m-%d')
cantidadRegistro = 0
precioCliente = 0
pesoNetoJabas = 0
numeroJabasPes = 0
numeroCubetasPes = 0
estadoPeso = 1
estadoWebPeso = 1
tipoCubetas = ""
coloresJabas = ""
observacionPes = ""

# Variantes de las variables para la Base de datos pero para Descuento
precioClienteDesc = 0
idEspecieDesc = 0

# Variables para los kg de pollo trozado
pesoKgPechuga = 0.00
pesoKgPierna = 0.00
pesoKgAlas = 0.00
pesoKgMenudencia = 0.00
pesoKgDorso = 0.00
pesoKgOtros = 0.00

# Variable que indica si esta listo para realizar acciones 
listoParaAccionar = False
btnActualizar = True
contadorActualizar = 30

# Variables de rutas de imagenes para alerta
correcto = "imagenes/correcto.png"
error = "imagenes/error.png"
descuento = "imagenes/seleccionado.png"
loading = "imagenes/loading.gif"

identificador = ""
gramosExtrasActivo = False
gramosExtras = 0

ipImpresora = "192.168.0.104"
valores_individuales_pesadas = []

def obtener_estilo(letra):
        colores = {'R': QColor('red'), 'C': QColor('cyan'), 'A': QColor('blue'),
               'V': QColor('green'), 'N': QColor('orange'), 'D': QColor('gold'),
               'O': QColor('white')}
    
        fuente = QFont()
        fuente.setBold(True)

        return colores.get(letra, QColor('black')), fuente
    
def is_color_dark(color):
    # Calcula el brillo según la fórmula YIQ
    yiq = (color.red() * 299 + color.green() * 587 + color.blue() * 114) / 1000
    return yiq < 128

class LetrasWidget(QWidget):
    def __init__(self, letras):
        super().__init__()

        layout = QHBoxLayout(self)

        # Verifica si todos los números son cero
        todos_cero = all(letra[1:] == '0' for letra in letras)

        # Si todos los números son cero, crea un QLabel con el número 0 transparente
        if todos_cero:
            fuente = QFont()
            fuente.setBold(True)
        
            label = QLabel('0')
            label.setStyleSheet("border-radius: 5px; color: transparent; border: none; padding: 4px; text-align: center; background-color: transparent;")
            label.setFont(fuente)
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)
        else:
            for letra in letras:
                color, fuente = obtener_estilo(letra[0])

                # Determina el color del texto en función del color de fondo
                text_color = QColor('white') if is_color_dark(color) else QColor('black')
                
                numero = letra[1:]
                if int(numero) != 0:
                    label = QLabel(numero)
                    label.setStyleSheet(f"border-radius: 5px; color: {text_color.name()}; background-color: {color.name()}; border: 1px solid #000000; padding: 4px; text-align: center")
                    label.setFont(fuente)
                    label.setAlignment(Qt.AlignCenter)
                    layout.addWidget(label)
""" Creamos hilo para la ejecución en segundo plano de la Fecha y Hora, de esta forma
evitamos que la aplicación se detenga por la lectura constante """

class WorkerThreadFechaHora(QThread):
    # Tarea a ejecutarse cada determinado tiempo.
    update_fecha = pyqtSignal(str)
    update_hora = pyqtSignal(str)
    def run(self):
        try:
            while True:
                hora_actual = datetime.now().time()
                hora = int(hora_actual.strftime("%H"))
                minutos = hora_actual.strftime("%M")
                segundos = hora_actual.strftime("%S")
                periodo = "AM" if hora < 12 else "PM"
                hora = hora if hora <= 12 else hora - 12
                hora_formateada = "{:02d} : {:02d} : {:02d} {}".format(hora, int(minutos), int(segundos), periodo)
                self.update_hora.emit(hora_formateada)

                fecha_actual = datetime.now().date()
                año = fecha_actual.year
                mes = fecha_actual.month
                dia = fecha_actual.day
                dia_semana = fecha_actual.weekday()
                dia_semana = ["Lunes", 
                            "Martes", 
                            "Miércoles", 
                            "Jueves", 
                            "Viernes", 
                            "Sábado", 
                            "Domingo"][int(dia_semana)]
                meses = {
                    1: "Enero",
                    2: "Febrero",
                    3: "Marzo",
                    4: "Abril",
                    5: "Mayo",
                    6: "Junio",
                    7: "Julio",
                    8: "Agosto",
                    9: "Septiembre",
                    10: "Octubre",
                    11: "Noviembre",
                    12: "Diciembre"
                }
                fecha_formateada = "{} {} de {} del {}".format(dia_semana, dia, meses[mes], año)

                self.update_fecha.emit(fecha_formateada)
                time.sleep(1)
        except Exception as e:
            print("WT FH"+str(e))  
    
    def stop(self):
        print("Thread Stopped")
        self.terminate()

# ===============================
# Creación de la Clase Principal
# ===============================

class Inicio(QMainWindow):
    _instancia_conexion = DataBase.database_conexion.Conectar()
    
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conexion = self._instancia_conexion
        self.moduloInicioSistema = inicioSistema
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QtGui.QIcon("Imagenes/iconoApp.png"))
        self.setWindowTitle('SISTEMA INTEGRAL || BALINSA')
        
        self.workerFechaHora = WorkerThreadFechaHora() # Hilo de Fecha y Hora
        self.workerFechaHora.start() # Iniciamos el hilo
        self.workerFechaHora.update_fecha.connect(self.mostrar_fecha) # Llamamos a la función mostrar_fecha
        self.workerFechaHora.update_hora.connect(self.mostrar_hora) # Llamamos a la función mostrar_hora
        
        threadBtn = threading.Thread(target=self.fn_temporizadorBtn)
        threadBtn.start()

        self.ui.imgLogo.setPixmap(QPixmap("Imagenes/iconoPC.png"))
        self.ui.imgImpresora.setPixmap(QPixmap("Imagenes/impresora.png"))
        self.ui.imgSincronizacion.setPixmap(QPixmap("Imagenes/transferencia-de-datos.png"))
        self.ui.lblNumBalanza.setText("Cliente N° 1")
        self.ui.imgLogo.setHidden(True)
        self.ui.lblNombreHeader.setHidden(True)
        self.ui.lblSubNombreHeader.setHidden(True)
        
        self.fn_declaraEspecie()
        self.fn_declaraPassword()

        self.ui.txtCodigoCliente.setEnabled(True)
        self.ui.txtCodigoCliente.setFocus(True)
        self.ui.txtCodigoCliente.textChanged.connect(self.fn_recepcionaCodigoTrabajador)
        self.ui.txtCodigoClienteCambiarPesada.textChanged.connect(self.fn_recepcionaCodigoTrabajadorCambiarPesada)
        self.ui.btnOnOffIndicador.clicked.connect(self.fn_encender_apagar_indicador)
        self.ui.btnPulsoZeroIndicador.clicked.connect(self.fn_pulso_zero_indicador)
        self.ui.btnAgregarComentario.clicked.connect(self.fn_traer_agregar_comentario)
        self.ui.btnCerrarFrmIngresaComentario.clicked.connect(self.fn_cerrar_comentario)
        self.ui.btnCancelarFrmIngresaComentario.clicked.connect(self.fn_cerrar_comentario)
        self.ui.btnAceptarFrmIngresaComentario.clicked.connect(self.fn_guardarActualizar_comentario)
        self.ui.lblPesoIndicador.setText("10.00")
        
        self.ui.frmIngresarCantidad.setHidden(True)
        self.ui.frmAlerta.setHidden(True)
        self.ui.frmAplicarDescuento.setHidden(True)
        self.ui.frmIngresarPassword.setHidden(True)
        self.ui.frmAlertaEliminar.setHidden(True)
        self.ui.frmColores.setHidden(True)
        self.ui.frmIngresarCantidadJabas.setHidden(True)
        self.ui.frmIngresarNumeroPesada.setHidden(True)
        self.ui.frmDecidirReporte.setHidden(True)
        self.ui.frmIntervaloDePesadas.setHidden(True)
        self.ui.frmCambiarEspecie.setHidden(True)
        self.ui.frmCambiarPesadaCliente.setHidden(True)
        self.ui.frmAlertaDesicionEnvio.setHidden(True)
        self.ui.frmAlertaIngresaNumeroEnvio.setHidden(True)
        self.ui.frmAlertaDesicionResponsable.setHidden(True)
        self.ui.frmAlertaIngresaResponsablesDeEnvio.setHidden(True)
        self.ui.frmAlertaIngresaNombreVenta.setHidden(True)
        self.ui.frmSombra.setHidden(True)
        self.ui.frmIngresarPrecioVenta.setHidden(True)
        self.ui.frmIngresaComentario.setHidden(True)
        
        self.ui.txtCantidadParaIngresar.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtCantidadDescuento.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtNumeroDePesada.textChanged.connect(self.fn_validarEntradaNumerica)
        
        self.ui.txtCantidadPrimerColor.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtCantidadSegundoColor.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtCantidadTercerColor.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtCantidadCuartoColor.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtCantidadQuintoColor.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtCantidadSextoColor.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtCantidadSeptimoColor.textChanged.connect(self.fn_validarEntradaNumerica)
        self.ui.txtNumeroDeEnvio.textChanged.connect(self.fn_validarEntradaNumerica)
        
        self.ui.txtIngresarValorImprimir.textChanged.connect(self.fn_validarEntradaNumericaReporte)
        
        self.ui.btnCerrarFrmAlerta.clicked.connect(self.fn_btnCerrarFrmAlerta)
        
        tablaDePesos = self.ui.tblDetallePesadas
        tablaDePesos.setColumnWidth(0, 50)
        tablaDePesos.setColumnWidth(1, 250)
        tablaDePesos.setColumnWidth(2, 80)
        tablaDePesos.setColumnWidth(3, 150)
        tablaDePesos.setColumnWidth(4, 100)
        tablaDePesos.setColumnWidth(5, 125)
        tablaDePesos.setColumnWidth(6, 125)
        tablaDePesos.setColumnWidth(7, 125)
        tablaDePesos.setColumnWidth(8, 125)
        tablaDePesos.setColumnWidth(9, 250)
        tablaDePesos.setColumnWidth(10, 100)
        
        tablaDePesos.setColumnHidden(11, True)
        tablaDePesos.setColumnHidden(12, True)
        tablaDePesos.setColumnHidden(13, True)
        tablaDePesos.setAlternatingRowColors(True)
        self.fn_asignarPesos()
        self.fn_declararPuertoImpresora()
        
        self.ui.btnAgregarGramosExtras.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.lblNumeroSistemaBalanza.setText("SISTEMA DE \n BALANZA N° 1")
        
        tablaDePedidos = self.ui.tblDetallePedidos
        tablaDePedidos.setColumnWidth(0, 200)
        tablaDePedidos.setColumnWidth(1, 110)
        tablaDePedidos.setColumnWidth(2, 90)
        
    # ======================== Funciones llamadas por los Hilos ========================
    
    def fn_declararPuertoImpresora(self):
        global ipImpresora

        puertoHostIp = self.conexion.db_seleccionaPuertoHostIp()
        ipImpresora = str(puertoHostIp[0])
    
    def fn_asignarPesos(self):
        global pesoPrimerColor
        global pesoSegundoColor
        global pesoTercerColor
        global pesoCuartaColor
        global pesoQuintoColor
        global pesoSextoColor
        global pesoSeptimoColor
        
        pesosAsignarJabas = self.conexion.db_asignarPesosJabas()
        
        pesoPrimerColor = float(pesosAsignarJabas[0])
        pesoSegundoColor = float(pesosAsignarJabas[1])
        pesoTercerColor = float(pesosAsignarJabas[2])
        pesoCuartaColor = float(pesosAsignarJabas[3])
        pesoQuintoColor = float(pesosAsignarJabas[4])
        pesoSextoColor = float(pesosAsignarJabas[5])
        pesoSeptimoColor = float(pesosAsignarJabas[6])
    
    def evt_actualizar_peso(self, val):
        
        if (balanzaSeleccionada == 1 or balanzaSeleccionada == 2) :
            try:
                signo = val[0:1]
                val = float(val[1:8])
                
                if (signo == "-") and val != 0:
                    self.ui.lblPesoIndicador.setText("-"+str(format(val, ".2f")))
                else:
                    self.ui.lblPesoIndicador.setText(format(val, ".2f"))
            except ValueError:
                self.ui.lblPesoIndicador.setText("-----")

    def evt_actualizar_baliza(self, val):
        global start_time
        global pesoAnterior
        
        try:
            signo = val[0:1]
            val = float(val[1:9])
            pesoBalanza1 = inicioSistema.pesoBalanza1
            user_input_arduino = inicioSistema.workerAR.user_input_arduino
            
            if not pesoBalanza1:
                if val > 0.2:
                    if user_input_arduino != "ce":
                        inicioSistema.workerAR.user_input_arduino = "ce"
                        if inicioSistema.workerAR.serialArduino.is_open:
                            inicioSistema.workerAR.serialArduino.write(str("ce").encode('utf8'))
                elif val < 0.2:
                    if user_input_arduino != "ge":
                        inicioSistema.workerAR.user_input_arduino = "ge"
                        if inicioSistema.workerAR.serialArduino.is_open:
                            inicioSistema.workerAR.serialArduino.write(str("ge").encode('utf8'))
            elif pesoBalanza1 and val < 0.2:
                inicioSistema.pesoBalanza1 = False
                if user_input_arduino != "e":
                    inicioSistema.workerAR.user_input_arduino = "e"
                    if inicioSistema.workerAR.serialArduino.is_open:
                        inicioSistema.workerAR.serialArduino.write(str("e").encode('utf8'))
            
            if signo == "-" and val != 0:
                if pesoAnterior == False:
                    start_time = time.time()
                    pesoAnterior = True
                        
                # Verifica si ha pasado 1 segundo
                if 'start_time' in globals():
                    elapsed_time = time.time() - start_time    
                    if elapsed_time >= 1:
                        if signo == "-" and val != 0:
                            inicioSistema.workerAR.user_input_arduino = "z"
                            if inicioSistema.workerAR.serialArduino.is_open:
                                inicioSistema.workerAR.serialArduino.write(str("z").encode('utf8'))
                                pesoAnterior = False
           
        except ValueError:
           pass

    def evt_actualizar_estado(self, val):
        if (balanzaSeleccionada == 1 or balanzaSeleccionada == 2) :
            if (val == "0"):
                self.ui.lblEstadoBalanzas.setText("FUERA DE LINEA")
                self.ui.lblPesoIndicador.setText("-----")
                self.ui.lblEstadoBalanzas.setStyleSheet("background-color: rgb(234, 29, 49);color: rgb(255, 255, 255);")
            elif (val == "1"):
                self.ui.lblEstadoBalanzas.setText("EN LINEA")
                self.ui.lblEstadoBalanzas.setStyleSheet("background-color: rgb(32, 176, 20);color: rgb(255, 255, 255);")
            
    # def evt_actualizar_peso2(self, val):
        
    #     if (balanzaSeleccionada == 2) :
    #         try:
    #             signo = val[0:1]
    #             val = float(val[1:9])
                
    #             if (signo == "-") and val != 0:
    #                 self.ui.lblPesoIndicador.setText("-"+str(format(val, ".2f")))
    #             else:
    #                 self.ui.lblPesoIndicador.setText(format(val, ".2f"))
    #         except ValueError:
    #             self.ui.lblPesoIndicador.setText("0.00")

    # def evt_actualizar_estado2(self, val):
    #     if (balanzaSeleccionada == 2) :
    #         if (val == "0"):
    #             self.ui.lblEstadoBalanzas.setText("FUERA DE LINEA")
    #             self.ui.lblPesoIndicador.setText("0.00")
    #             self.ui.lblEstadoBalanzas.setStyleSheet("background-color: rgb(234, 29, 49);color: rgb(255, 255, 255);")
    #         elif (val == "1"):
    #             self.ui.lblEstadoBalanzas.setText("EN LINEA")
    #             self.ui.lblEstadoBalanzas.setStyleSheet("background-color: rgb(32, 176, 20);color: rgb(255, 255, 255);")

    # def evt_actualizar_baliza2(self, val):

    #     try:

    #         val = float(val[1:9])

    #         if (inicioSistema.pesoBalanza2 == False and float(val)> 0.2):
    #             inicioSistema.workerAR.user_input_arduino = "df"
    #         elif (inicioSistema.pesoBalanza2 == False and float(val)< 0.2):
    #             inicioSistema.workerAR.user_input_arduino = "hf"
            
    #         if (inicioSistema.pesoBalanza2 == True and float(val) < 0.2):
    #             inicioSistema.pesoBalanza2 = False
    #             inicioSistema.workerAR.user_input_arduino = "f"
           
    #     except ValueError:
    #        pass
    
    def fn_pulsoLuzVerdeBuzzer(self):
        inicioSistema.workerAR.user_input_arduino = "agi"
        if inicioSistema.workerAR.serialArduino.is_open:
            inicioSistema.workerAR.serialArduino.write(str("agi").encode('utf8'))
        time.sleep(1)
        inicioSistema.workerAR.user_input_arduino = "k"
        if inicioSistema.workerAR.serialArduino.is_open:
            inicioSistema.workerAR.serialArduino.write(str("k").encode('utf8'))
        
    def mostrar_hora(self,val):
        self.ui.lblHora.setText(val)
        
    def mostrar_fecha(self,val):
        self.ui.lblFecha.setText(val)
        
    # ======================== Termina funciones llamadas por los Hilos ========================
    
    # ======================== Eventos con el Teclado ========================
    
    def condiciones_base(self):
        return (
            not frmRegistrarCantidad and
            not frmAlertaEliminarPeso and
            not frmEliminarPeso and
            not frmAlerta and
            not frmRegistrarDescuento and
            not frmEditarCantidad and
            not frmRegistrarJabas and 
            not frmRegistrarColoresJabas and
            not frmRegistrarDescuentoCan and
            not frmSeleccionarTipoTrozado and
            not frmIngresarNumeroPesadaEditar and
            not frmIngresarNumeroPesadaEliminar and
            not frmSeleccionarTipoTrozadoDesc and
            not frmRegistrarColoresJabasEditar and
            not frmIngresarNumeroColoresEditar and
            not frmDecidirReporte and
            not frmIngresarNumeroPesoJabaEditar and
            not frmSeleccionaPesadasReporte and
            not frmSeleccionarEspecieEditarPesada and
            not frmIngresarNumeroPesadaEditarEspecie and
            not frmCambiarPesadaCliente and
            not frmIngresarNumeroCambiarPesada and
            not frmAlertaDesicionEnvio and
            not frmAlertaIngresaNumeroEnvio and
            not frmAlertaDesicionResponsable and
            not frmAlertaIngresaResponsablesDeEnvio and
            not frmAlertaIngresaNombreVenta and
            not frmIngresarPrecioVenta
        )
        
    def condiciones_alertas(self):
        return (
            not self.ui.frmIngresarCantidad.isVisible() and
            not self.ui.frmAlerta.isVisible() and
            not self.ui.frmAplicarDescuento.isVisible() and
            not self.ui.frmIngresarPassword.isVisible() and
            not self.ui.frmAlertaEliminar.isVisible() and
            not self.ui.frmColores.isVisible() and
            not self.ui.frmIngresarCantidadJabas.isVisible() and
            not self.ui.frmIngresarNumeroPesada.isVisible() and
            not self.ui.frmDecidirReporte.isVisible() and
            not self.ui.frmIngresarCantidadJabas.isVisible() and
            not self.ui.frmIntervaloDePesadas.isVisible() and
            not self.ui.frmCambiarEspecie.isVisible() and
            not self.ui.frmIntervaloDePesadas.isVisible() and
            not self.ui.frmCambiarEspecie.isVisible() and
            not self.ui.frmCambiarPesadaCliente.isVisible() and
            not self.ui.frmAlertaDesicionEnvio.isVisible() and
            not self.ui.frmAlertaIngresaNumeroEnvio.isVisible() and
            not self.ui.frmAlertaDesicionResponsable.isVisible() and
            not self.ui.frmAlertaIngresaResponsablesDeEnvio.isVisible() and
            not self.ui.frmAlertaIngresaNombreVenta.isVisible() and
            not self.ui.frmIngresarPrecioVenta.isVisible()and
            not self.ui.frmIngresaComentario.isVisible()
        )
        
    def condiciones_alertas_sombra(self):
        return (
            not self.ui.frmIngresarCantidad.isVisible() and
            not self.ui.frmAplicarDescuento.isVisible() and
            not self.ui.frmIngresarPassword.isVisible() and
            not self.ui.frmAlertaEliminar.isVisible() and
            not self.ui.frmColores.isVisible() and
            not self.ui.frmIngresarCantidadJabas.isVisible() and
            not self.ui.frmIngresarNumeroPesada.isVisible() and
            not self.ui.frmDecidirReporte.isVisible() and
            not self.ui.frmIngresarCantidadJabas.isVisible() and
            not self.ui.frmIntervaloDePesadas.isVisible() and
            not self.ui.frmCambiarEspecie.isVisible() and
            not self.ui.frmIntervaloDePesadas.isVisible() and
            not self.ui.frmCambiarEspecie.isVisible() and
            not self.ui.frmCambiarPesadaCliente.isVisible() and
            not self.ui.frmAlertaDesicionEnvio.isVisible() and
            not self.ui.frmAlertaIngresaNumeroEnvio.isVisible() and
            not self.ui.frmAlertaDesicionResponsable.isVisible() and
            not self.ui.frmAlertaIngresaResponsablesDeEnvio.isVisible() and
            not self.ui.frmAlertaIngresaNombreVenta.isVisible() and
            not self.ui.frmIngresarPrecioVenta.isVisible() and
            not self.ui.frmIngresaComentario.isVisible()
        )
            
    def keyReleaseEvent(self, event):
        global balanzaSeleccionada
        global frmRegistrarCantidad
        global frmAlertaEliminarPeso
        global frmEliminarPeso
        global frmAlerta
        global frmRegistrarDescuento
        global frmInicioProceso
        global frmEditarCantidad
        global frmRegistrarJabas
        global frmRegistrarDescuentoCan
        global idEspecieDesc
        global frmEditarCantidadTara
        global frmEditarCantidadDescuento
        global btnActualizar
        global contadorActualizar
        global frmSeleccionarTipoTrozado
        global frmIngresarNumeroPesadaEditar
        global frmIngresarNumeroPesadaEliminar
        global idPesadaEditarOEliminar
        global frmRegistrarColoresJabas
        global frmSeleccionarTipoTrozadoDesc
        global frmRegistrarColoresJabasEditar
        global frmIngresarNumeroColoresEditar
        global frmDecidirReporte
        global frmIngresarNumeroPesoJabaEditar
        global frmSeleccionaPesadasReporte
        global frmIngresarNumeroPesadaEditarEspecie
        global frmSeleccionarEspecieEditarPesada
        global frmCambiarPesadaCliente
        global frmIngresarNumeroCambiarPesada
        global frmAlertaDesicionEnvio
        global frmAlertaIngresaNumeroEnvio
        global frmAlertaDesicionResponsable
        global frmAlertaIngresaResponsablesDeEnvio
        global numeroEnvio
        global incluyeEnvio
        global incluyeResponsable
        global imprimePrecio
        global precioCambiarEspecie
        global identificador
        global idEspecieCambiarEspecie
        global codigoClienteCambiarPesada
        global frmAlertaIngresaNombreVenta
        global enviaTodoReporteImprimir
        global frmIngresarPrecioVenta
        
        if (event.key() == Qt.Key_F12):
            frmRegistrarCantidad = False
            frmAlertaEliminarPeso = False
            frmEliminarPeso = False
            frmAlerta = False
            frmRegistrarDescuento = False
            frmEditarCantidad = False
            frmRegistrarJabas = False
            frmRegistrarColoresJabas = False
            frmRegistrarDescuentoCan = False
            frmSeleccionarTipoTrozado = False
            frmIngresarNumeroPesadaEditar = False
            frmIngresarNumeroPesadaEliminar = False
            frmSeleccionarTipoTrozadoDesc = False
            frmRegistrarColoresJabasEditar = False
            frmIngresarNumeroColoresEditar = False
            frmDecidirReporte = False
            frmIngresarNumeroPesoJabaEditar = False
            frmSeleccionaPesadasReporte = False
            frmSeleccionarEspecieEditarPesada = False
            frmIngresarNumeroPesadaEditarEspecie = False
            frmCambiarPesadaCliente = False
            frmIngresarNumeroCambiarPesada = False
            frmAlertaDesicionEnvio = False
            frmAlertaIngresaNumeroEnvio = False
            frmAlertaDesicionResponsable = False
            frmAlertaIngresaResponsablesDeEnvio = False
            frmAlertaIngresaNombreVenta = False
            frmIngresarPrecioVenta = False
            self.ui.frmIngresarCantidad.setHidden(True)
            self.ui.frmAlerta.setHidden(True)
            self.ui.frmAplicarDescuento.setHidden(True)
            self.ui.frmIngresarPassword.setHidden(True)
            self.ui.frmAlertaEliminar.setHidden(True)
            self.ui.frmColores.setHidden(True)
            self.ui.frmIngresarCantidadJabas.setHidden(True)
            self.ui.frmIngresarNumeroPesada.setHidden(True)
            self.ui.frmDecidirReporte.setHidden(True)
            self.ui.frmIntervaloDePesadas.setHidden(True)
            self.ui.frmCambiarEspecie.setHidden(True)
            self.ui.frmCambiarPesadaCliente.setHidden(True)
            self.ui.frmAlertaDesicionEnvio.setHidden(True)
            self.ui.frmAlertaIngresaNumeroEnvio.setHidden(True)
            self.ui.frmAlertaDesicionResponsable.setHidden(True)
            self.ui.frmAlertaIngresaResponsablesDeEnvio.setHidden(True)
            self.ui.frmAlertaIngresaNombreVenta.setHidden(True)
            self.ui.frmIngresarPrecioVenta.setHidden(True)
            self.ui.frmIngresaComentario.setHidden(True)
            print("Todos los valores han sido asignados a False")
        
        if (event.key() == Qt.Key_R) and not self.ui.lwListaClientes.isVisible() and self.ui.frmColores.isVisible() and (frmRegistrarColoresJabas == True or frmRegistrarColoresJabasEditar == True):
            self.ui.txtCantidadPrimerColor.setFocus(True)
        elif (event.key() == Qt.Key_C) and not self.ui.lwListaClientes.isVisible() and self.ui.frmColores.isVisible() and (frmRegistrarColoresJabas == True or frmRegistrarColoresJabasEditar == True):
            self.ui.txtCantidadSegundoColor.setFocus(True)
        elif (event.key() == Qt.Key_A) and not self.ui.lwListaClientes.isVisible() and self.ui.frmColores.isVisible() and (frmRegistrarColoresJabas == True or frmRegistrarColoresJabasEditar == True):
            self.ui.txtCantidadTercerColor.setFocus(True)
        elif (event.key() == Qt.Key_V) and not self.ui.lwListaClientes.isVisible() and self.ui.frmColores.isVisible() and (frmRegistrarColoresJabas == True or frmRegistrarColoresJabasEditar == True):
            self.ui.txtCantidadCuartoColor.setFocus(True)
        elif (event.key() == Qt.Key_N) and not self.ui.lwListaClientes.isVisible() and self.ui.frmColores.isVisible() and (frmRegistrarColoresJabas == True or frmRegistrarColoresJabasEditar == True):
            self.ui.txtCantidadQuintoColor.setFocus(True)
        elif (event.key() == Qt.Key_D) and not self.ui.lwListaClientes.isVisible() and self.ui.frmColores.isVisible() and (frmRegistrarColoresJabas == True or frmRegistrarColoresJabasEditar == True):
            self.ui.txtCantidadSextoColor.setFocus(True)
        elif (event.key() == Qt.Key_O) and not self.ui.lwListaClientes.isVisible() and self.ui.frmColores.isVisible() and (frmRegistrarColoresJabas == True or frmRegistrarColoresJabasEditar == True):
            self.ui.txtCantidadSeptimoColor.setFocus(True)
        
        if (event.key() == Qt.Key_Right) and self.condiciones_base() and self.condiciones_alertas():
            balanzaSeleccionada = 2
            self.fn_seleccionaBalanza()
            self.fn_seleccionarEspecie(idEspecie)
            self.fn_seleccionarEspecieDescuento(idEspecieDesc)
            self.fn_verificarProceso()
            self.fn_listarVenta()
            self.fn_listarPedidos()
            frmSeleccionarTipoTrozado = False
            frmSeleccionarTipoTrozadoDesc = False
        
        if (event.key() == Qt.Key_Left) and self.condiciones_base() and self.condiciones_alertas():
            balanzaSeleccionada = 1
            self.fn_seleccionaBalanza()
            self.fn_seleccionarEspecie(idEspecie)
            self.fn_seleccionarEspecieDescuento(idEspecieDesc)
            self.fn_verificarProceso()
            self.fn_listarVenta()
            self.fn_listarPedidos()
            frmSeleccionarTipoTrozado = False
            frmSeleccionarTipoTrozadoDesc = False
            
        if event.key() == Qt.Key_Up and self.ui.lwListaClientes.isVisible():
            self.fn_ArribaLista()
        elif event.key() == Qt.Key_Down and self.ui.lwListaClientes.isVisible():
            self.fn_AbajoLista()
            
        if event.key() == Qt.Key_Up and self.ui.lwListaClientesCambiarPesada.isVisible():
            self.fn_ArribaListaCambiarPesada()
        elif event.key() == Qt.Key_Down and self.ui.lwListaClientesCambiarPesada.isVisible():
            self.fn_AbajoListaCambiarPesada()
            
        if (event.key() == Qt.Key_Plus) and self.condiciones_base() and not self.ui.txtCodigoCliente.hasFocus():
            self.fn_cambiarCliente()
            
        if (event.key() == Qt.Key_Plus) and frmCambiarPesadaCliente == True and not self.ui.lwListaClientesCambiarPesada.isVisible():
            self.fn_cambiarClienteCambiarPesada()
            
        if (event.key() == Qt.Key_1) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(primerEspecie) #primerEspecie
        elif (event.key() == Qt.Key_2) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(decimaSeptimaEspecie) #decimaSeptimaEspecie
        elif (event.key() == Qt.Key_3) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(terceraEspecie) #terceraEspecie
        elif (event.key() == Qt.Key_4) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(decimaOctavaEspecie) #decimaOctavaEspecie
        elif (event.key() == Qt.Key_5) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(vigesimaEspecie) #vigesimaEspecie
        elif (event.key() == Qt.Key_6) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(vigesimaSegundaEspecie) #vigesimaPrimeraEspecie
        elif (event.key() == Qt.Key_7) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(vigesimaTerceraEspecie) #vigesimaSegundaEspecie
        elif (event.key() == Qt.Key_8) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(decimaNovenaEspecie) #vigesimaTerceraEspecie
        elif (event.key() == Qt.Key_9) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(sextaEspecie) #decimaNovenaEspecie
        elif (event.key() == Qt.Key_F1) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            self.fn_seleccionarEspecie(vigesimaPrimeraEspecie)
        elif (event.key() == Qt.Key_F2) and not self.ui.lwListaClientes.isVisible() and self.condiciones_base() and self.condiciones_alertas():
            if (gramosExtrasActivo == False):
                self.fn_activarGramosExtrasPorCantidad()
            elif (gramosExtrasActivo == True):
                self.fn_desactivarGramosExtrasPorCantidad()
            
        if (event.key() == Qt.Key_1) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            if int(self.ui.txtCantYugoVivo.text().split()[0].strip()) > 0 :
                self.fn_seleccionarEspecieDescuento(primerEspecie)
            else:
                idEspecieDesc = 0
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombrePrimerEspecie),1500)
        elif (event.key() == Qt.Key_2) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            if int(self.ui.txtCantBrasaYugo.text().split()[0].strip()) > 0 :
                self.fn_seleccionarEspecieDescuento(decimaSeptimaEspecie)
            else:
                idEspecieDesc = 0
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreDecimaSeptimaEspecie),1500)
            # if int(self.ui.txtCantYugoPelado.text().split()[0].strip()) > 0 :
            #     self.fn_seleccionarEspecieDescuento(segundaEspecie)
            # else:
            #     idEspecieDesc = 0
            #     self.fn_seleccionarEspecieDescuento(idEspecieDesc)
            #     self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreSegundaEspecie),1500)
        elif (event.key() == Qt.Key_3) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            if int(self.ui.txtCantTecnicoVivo.text().split()[0].strip()) > 0 :
                self.fn_seleccionarEspecieDescuento(terceraEspecie)
            else:
                idEspecieDesc = 0
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreTerceraEspecie),1500)
        elif (event.key() == Qt.Key_4) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            if int(self.ui.txtCantBrasaTecnico.text().split()[0].strip()) > 0 :
                self.fn_seleccionarEspecieDescuento(decimaOctavaEspecie)
            else:
                idEspecieDesc = 0
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreDecimaOctavaEspecie),1500)
            # if int(self.ui.txtCantTecnicoPelado.text().split()[0].strip()) > 0 :
            #     self.fn_seleccionarEspecieDescuento(cuartaEspecie)
            # else:
            #     idEspecieDesc = 0
            #     self.fn_seleccionarEspecieDescuento(idEspecieDesc)
            #     self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreCuartaEspecie),1500)
        elif (event.key() == Qt.Key_5) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            if int(self.ui.txtCantGallinaDoble.text().split()[0].strip()) > 0 :
                self.fn_seleccionarEspecieDescuento(vigesimaEspecie)
            else:
                idEspecieDesc = 0
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreQuintaEspecie),1500)
        elif (event.key() == Qt.Key_6) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            if int(self.ui.txtCantAhogados.text().split()[0].strip()) > 0 :
                self.fn_seleccionarEspecieDescuento(vigesimaPrimeraEspecie)
            else:
                idEspecieDesc = 0
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreSextaEspecie),1500)
        elif (event.key() == Qt.Key_7) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            if int(self.ui.txtCantGallo.text().split()[0].strip()) > 0 :
                self.fn_seleccionarEspecieDescuento(vigesimaSegundaEspecie)
            else:
                idEspecieDesc = 0
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreSeptimaEspecie),1500)
        elif (event.key() == Qt.Key_8) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            # if int(self.ui.txtCantPolloMaltratado.text().split()[0].strip()) > 0 :
            self.fn_seleccionarEspecieDescuento(vigesimaTerceraEspecie)
            # else:
            #     idEspecieDesc = 0
            #     self.fn_seleccionarEspecieDescuento(idEspecieDesc)
            #     self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreOctavaEspecie),1500)
        elif (event.key() == Qt.Key_9) and not self.ui.lwListaClientes.isVisible() and self.ui.frmAplicarDescuento.isVisible() and frmRegistrarDescuento == True and frmRegistrarDescuentoCan == False and frmSeleccionarTipoTrozadoDesc == False:
            if int(self.ui.txtCantPolloXx.text().split()[0].strip()) > 0 :
                self.fn_seleccionarEspecieDescuento(decimaNovenaEspecie)
            else:
                idEspecieDesc = 0
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                self.fn_alerta("¡ADVERTENCIA!",error,"No puede seleccionar la especie {} porque la cantidad es 0.".format(nombreDecimaSextaEspecie),1500)
            # self.fn_seleccionarEspecieDescuento(decimaEspecie)
            # self.ui.btnDescPolloTrozado.setText("{} \n {} (9)".format(nombreNovenaEspecie,nombreDecimaEspecie))
            
        if (event.key() == Qt.Key_Slash) and self.condiciones_base() and self.condiciones_alertas() and not self.ui.lwListaClientes.isVisible():
            if listoParaAccionar == True :
                self.ui.imgIconDesc.setPixmap(QPixmap(""))
                self.ui.txtCantidadDescuento.setText("")
                self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                frmSeleccionarTipoTrozadoDesc = False
                self.ui.txtCantidadDescuento.setEnabled(False)
                self.ui.frmAplicarDescuento.setHidden(False)
                frmRegistrarDescuento = True
                self.ui.frmSombra.setHidden(False)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"En este momento no puedes realizar un descuento por que no hay registros.",2500)
            
        if (event.key() == Qt.Key_Period) and self.condiciones_base() and self.condiciones_alertas() and not self.ui.lwListaClientes.isVisible():
            if listoParaAccionar == True :
                idPesadaEditarOEliminar = 0
                self.ui.txtNumeroDePesada.setText("")
                self.ui.txtNumeroDePesada.setFocus(True)
                self.ui.frmIngresarNumeroPesada.setHidden(False)
                frmIngresarNumeroPesadaEliminar = True
                self.ui.frmSombra.setHidden(False)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"En este momento no puedes eliminar por que no hay registros.",2500)
            
        if (event.key() == Qt.Key_Asterisk) and self.condiciones_base() and frmInicioProceso == True and self.condiciones_alertas() and not self.ui.lwListaClientes.isVisible():
            if listoParaAccionar == True :
                idPesadaEditarOEliminar = 0
                self.ui.frmIngresarNumeroPesada.setHidden(False)
                self.ui.txtNumeroDePesada.setText("")
                self.ui.txtNumeroDePesada.setFocus(True)
                frmIngresarNumeroPesadaEditar = True
                self.ui.frmSombra.setHidden(False)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"En este momento no puedes editar por que no hay registros.",3000)
            
        if (event.key() == Qt.Key_0) and self.condiciones_base() and frmInicioProceso == True and self.condiciones_alertas() and not self.ui.lwListaClientes.isVisible():
            if listoParaAccionar == True :
                idPesadaEditarOEliminar = 0
                self.ui.txtNumeroDePesada.setText("")
                self.ui.txtNumeroDePesada.setFocus(True)
                self.ui.frmIngresarNumeroPesada.setHidden(False)
                frmIngresarNumeroPesoJabaEditar = True
                frmRegistrarJabas = False
                self.ui.frmSombra.setHidden(False)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"En este momento no puedes editar por que no hay registros.",2500)
            
        if (event.key() == Qt.Key_Shift) and self.condiciones_base() and self.condiciones_alertas() and not self.ui.lwListaClientes.isVisible():
            if codCliente == 24 or codCliente == 69:
                self.ui.frmSombra.setHidden(False)
                self.ui.frmDecidirReporte.setHidden(True)
                frmDecidirReporte = False
                imprimePrecio = True
                # self.fn_imprimirReporte()
                frmSeleccionaPesadasReporte = True
                self.ui.txtIngresarValorImprimir.setText("")
                self.ui.frmIntervaloDePesadas.setHidden(False)
                self.ui.txtIngresarValorImprimir.setFocus(True)
                enviaTodoReporteImprimir = False
                incluyeResponsable = False
                incluyeEnvio = False
            else:
                self.ui.frmDecidirReporte.setHidden(False)
                frmDecidirReporte = True
                self.ui.frmSombra.setHidden(False)
            
        if event.key() == Qt.Key_Slash and frmInicioProceso == True:
            if (self.ui.frmIntervaloDePesadas.isVisible()):
                frmSeleccionaPesadasReporte = False
                frmDecidirReporte = False
                self.ui.frmIntervaloDePesadas.setHidden(True)
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmAlertaIngresaResponsablesDeEnvio.isVisible()):
                self.ui.frmAlertaIngresaResponsablesDeEnvio.setHidden(True)
                frmAlertaIngresaResponsablesDeEnvio = False
                self.ui.frmSombra.setHidden(True)
            
        if event.key() == Qt.Key_Minus and frmInicioProceso == True:
            if (self.ui.frmIngresarCantidad.isVisible()):
                self.ui.frmIngresarCantidad.setHidden(True)
                frmRegistrarCantidad = False
                frmEditarCantidad = False
                frmEditarCantidadTara = False
                frmEditarCantidadDescuento = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmIngresarCantidadJabas.isVisible()):
                self.ui.frmIngresarCantidadJabas.setHidden(True)
                frmRegistrarJabas = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmAplicarDescuento.isVisible()) and frmSeleccionarTipoTrozadoDesc == False:
                self.ui.frmAplicarDescuento.setHidden(True)
                frmRegistrarDescuento = False
                frmRegistrarDescuentoCan = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmAlertaEliminar.isVisible()):
                self.ui.frmAlertaEliminar.setHidden(True)
                frmAlertaEliminarPeso = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmIngresarPassword.isVisible()):
                self.ui.frmIngresarPassword.setHidden(True)
                frmEliminarPeso = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmIngresarNumeroPesada.isVisible()):
                self.ui.frmIngresarNumeroPesada.setHidden(True)
                frmIngresarNumeroPesadaEditar = False
                frmIngresarNumeroPesadaEliminar = False
                frmIngresarNumeroColoresEditar = False
                frmIngresarNumeroPesoJabaEditar = False
                frmIngresarNumeroPesadaEditarEspecie = False
                frmIngresarNumeroCambiarPesada = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmColores.isVisible()):
                self.ui.frmColores.setHidden(True)
                frmRegistrarColoresJabas = False
                frmRegistrarColoresJabasEditar = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmDecidirReporte.isVisible()):
                self.ui.frmDecidirReporte.setHidden(True)
                frmDecidirReporte = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmCambiarEspecie.isVisible()):
                self.ui.frmCambiarEspecie.setHidden(True)
                frmSeleccionarEspecieEditarPesada = False
                frmIngresarNumeroPesadaEditarEspecie = False
                self.ui.frmSombra.setHidden(True)   
            elif (self.ui.frmCambiarPesadaCliente.isVisible()):
                self.ui.frmCambiarPesadaCliente.setHidden(True)
                frmCambiarPesadaCliente = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmAlertaDesicionEnvio.isVisible()):
                self.ui.frmAlertaDesicionEnvio.setHidden(True)
                frmAlertaDesicionEnvio = False   
                self.ui.frmSombra.setHidden(True) 
            elif (self.ui.frmAlertaIngresaNumeroEnvio.isVisible()):
                self.ui.frmAlertaIngresaNumeroEnvio.setHidden(True)
                frmAlertaIngresaNumeroEnvio = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmAlertaDesicionResponsable.isVisible()):
                self.ui.frmAlertaDesicionResponsable.setHidden(True)
                frmAlertaDesicionResponsable = False
                self.ui.frmSombra.setHidden(True)
            elif (self.ui.frmAlertaIngresaNombreVenta.isVisible()):
                self.ui.frmAlertaIngresaNombreVenta.setHidden(True)
                frmAlertaIngresaNombreVenta = False
                self.ui.frmSombra.setHidden(True)
                
        if event.key() == Qt.Key_F5 and not self.ui.frmAlerta.isVisible():
            if not btnActualizar and contadorActualizar == 0:
                btnActualizar = True
                contadorActualizar = 30
                threadBtn = threading.Thread(target=self.fn_temporizadorBtn)
                threadBtn.start()
                self.ui.frmSombra.setHidden(False)
                self.fn_abrirAnimacion()
            else:
                self.fn_alerta("ADVERTENCIA", error, "Debe esperar {} segundos antes de volver a actualizar.".format(contadorActualizar), 1000)
            
        if event.key() == Qt.Key_F6 and self.condiciones_base() and self.condiciones_alertas() and not self.ui.lwListaClientes.isVisible():
            if listoParaAccionar == True :
                idPesadaEditarOEliminar = 0
                self.ui.txtCantidadPrimerColor.setText("")
                self.ui.txtCantidadSegundoColor.setText("")
                self.ui.txtCantidadTercerColor.setText("")
                self.ui.txtCantidadCuartoColor.setText("")
                self.ui.txtCantidadQuintoColor.setText("")
                self.ui.txtCantidadSextoColor.setText("")
                self.ui.txtCantidadSeptimoColor.setText("")
                self.ui.txtCantidadParaIngresar.setText("")
                self.ui.frmIngresarNumeroPesada.setHidden(False)
                self.ui.txtNumeroDePesada.setText("")
                self.ui.txtNumeroDePesada.setFocus(True) 
                frmIngresarNumeroColoresEditar = True
                self.ui.frmSombra.setHidden(False)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"En este momento no puedes editar por que no hay registros.",3000)
        
        if (event.key() == Qt.Key_F7) and self.condiciones_base() and frmInicioProceso == True and self.condiciones_alertas() and not self.ui.lwListaClientes.isVisible():
            if listoParaAccionar == True :
                idPesadaEditarOEliminar = 0
                self.ui.frmIngresarNumeroPesada.setHidden(False)
                self.ui.txtNumeroDePesada.setText("")
                self.ui.txtNumeroDePesada.setFocus(True)
                frmIngresarNumeroPesadaEditarEspecie = True
                self.ui.frmSombra.setHidden(False)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"En este momento no puedes editar por que no hay registros.",3000)
                
        if (event.key() == Qt.Key_1) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(primerEspecie)
        if (event.key() == Qt.Key_2) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(decimaSeptimaEspecie)
        if (event.key() == Qt.Key_3) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(terceraEspecie)
        if (event.key() == Qt.Key_4) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(decimaOctavaEspecie)
        if (event.key() == Qt.Key_5) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(vigesimaEspecie)
        if (event.key() == Qt.Key_6) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(vigesimaPrimeraEspecie)
        if (event.key() == Qt.Key_7) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(vigesimaSegundaEspecie)
        if (event.key() == Qt.Key_8) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(vigesimaTerceraEspecie)
        if (event.key() == Qt.Key_9) and not self.ui.lwListaClientes.isVisible() and self.ui.frmCambiarEspecie.isVisible() and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEliminar == False:
            self.fn_seleccionarEspecieCambiar(decimaNovenaEspecie)
            
        if (event.key() == Qt.Key_F8) and self.condiciones_base() and frmInicioProceso == True and self.condiciones_alertas() and not self.ui.lwListaClientes.isVisible():
            if listoParaAccionar == True :
                idPesadaEditarOEliminar = 0
                self.ui.frmIngresarNumeroPesada.setHidden(False)
                self.ui.txtNumeroDePesada.setText("")
                self.ui.txtNumeroDePesada.setFocus(True)
                frmIngresarNumeroCambiarPesada = True
                self.ui.frmSombra.setHidden(False)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"En este momento no puedes editar por que no hay registros.",3000)
                
        if (event.key() == Qt.Key_F9) and frmInicioProceso == True and frmCambiarPesadaCliente == True and not self.ui.lwListaClientesCambiarPesada.isVisible() and codigoClienteCambiarPesada != 0:
            self.ui.frmCambiarPesadaCliente.setHidden(True)
            self.fn_cambiarPesadaCliente()
            frmCambiarPesadaCliente = False
        
        if (event.key() == Qt.Key_F10) and frmInicioProceso == True and not self.ui.lwListaClientesCambiarPesada.isVisible() and self.condiciones_alertas():
            btnActualizar = True
            contadorActualizar = 30
            threadBtn = threading.Thread(target=self.fn_temporizadorBtn)
            threadBtn.start()
            
            self.ui.btnCerrarFrmAlerta.setHidden(True)
            self.ui.lblAlertaTitulo.setStyleSheet("color: #3A93B3")
            self.ui.frmAlerta.setHidden(False)
            self.ui.frmSombra.setHidden(False)
            self.ui.lblAlertaTitulo.setText("Sincronizando Datos")
            
            movie = QMovie(loading)  # Crea una instancia de QMovie
            self.ui.imgIconAlerta.setMovie(movie)  # Asocia la QMovie con el QLabel
            movie.start()  # Inicia la animación
            self.ui.lblAlertaTexto.setStyleSheet("font-size:16pt;")
            self.ui.lblAlertaTexto.setText("Espere por favor los datos se están sincronizando.")
            
            conexionCierre = DataBase.database_conexion.Conectar()
            conexionCierre.cerrar_conexion()
            conexionAbrir = DataBase.database_conexion.Conectar()
            conexionAbrir.abrir_conexion()
            
            timer = QtCore.QTimer()
            timer.singleShot(3000, lambda: self.ui.frmAlerta.setHidden(True))
            timer2 = QtCore.QTimer()
            timer2.singleShot(3000, lambda: self.ui.frmSombra.setHidden(True))
            
        # ============= Eventos con la otra función pasada =============
        
        if event.key() == Qt.Key_Escape:
            self.close()
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmRegistrarColoresJabas == True and frmRegistrarCantidad == False and frmInicioProceso == True and self.ui.frmColores.isVisible():     
            
            cantidadTotalJabas = 0
            registroCantidadPrimerColor = int(self.ui.txtCantidadPrimerColor.text().strip()) if self.ui.txtCantidadPrimerColor.text().strip() else 0
            registroCantidadSegundoColor = int(self.ui.txtCantidadSegundoColor.text().strip()) if self.ui.txtCantidadSegundoColor.text().strip() else 0
            registroCantidadTercerColor = int(self.ui.txtCantidadTercerColor.text().strip()) if self.ui.txtCantidadTercerColor.text().strip() else 0
            registroCantidadCuartaColor = int(self.ui.txtCantidadCuartoColor.text().strip()) if self.ui.txtCantidadCuartoColor.text().strip() else 0
            registroCantidadQuintoColor = int(self.ui.txtCantidadQuintoColor.text().strip()) if self.ui.txtCantidadQuintoColor.text().strip() else 0
            registroCantidadSextoColor = int(self.ui.txtCantidadSextoColor.text().strip()) if self.ui.txtCantidadSextoColor.text().strip() else 0
            registroCantidadSeptimoColor = int(self.ui.txtCantidadSeptimoColor.text().strip()) if self.ui.txtCantidadSeptimoColor.text().strip() else 0
            
            cantidadTotalJabas = registroCantidadPrimerColor + registroCantidadSegundoColor + registroCantidadTercerColor + registroCantidadCuartaColor + registroCantidadQuintoColor + registroCantidadSextoColor + registroCantidadSeptimoColor
                    
            # if cantidadTotalJabas != 0:
            self.ui.frmColores.setHidden(True)
            frmRegistrarColoresJabas = False
            self.ui.txtCantidadParaIngresar.setText("")
            self.fn_alertaCantidad("Ingresar cantidad de Pollos")
            frmRegistrarCantidad = True
            self.ui.txtCantidadParaIngresar.setFocus(True)
            # else:
            #     self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de jabas no puede ser 0.")
    
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and self.condiciones_base() and frmInicioProceso == True and self.condiciones_alertas():
            try:
                peso_indicador = float(self.ui.lblPesoIndicador.text())
                self.ui.txtCantidadPrimerColor.setText("")
                self.ui.txtCantidadSegundoColor.setText("")
                self.ui.txtCantidadTercerColor.setText("")
                self.ui.txtCantidadCuartoColor.setText("")
                self.ui.txtCantidadQuintoColor.setText("")
                self.ui.txtCantidadSextoColor.setText("")
                self.ui.txtCantidadSeptimoColor.setText("")
                self.ui.txtCantidadParaIngresar.setText("")
                # self.ui.frmColores.setHidden(False)  
                # frmRegistrarColoresJabas = True
                
                self.ui.frmColores.setHidden(True)
                frmRegistrarColoresJabas = False
                self.ui.txtCantidadParaIngresar.setText("")
                self.fn_alertaCantidad("Ingresar cantidad de Pollos")
                frmRegistrarCantidad = True
                self.ui.txtCantidadParaIngresar.setFocus(True)
                self.ui.frmSombra.setHidden(False)
            except ValueError:
                # Manejar el caso en que el valor no se pueda convertir a float
                # Por ejemplo:
                print("El valor del peso no es válido")
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and self.ui.lwListaClientes.isVisible():
            if (len(listCodCliente)):
                indice = self.ui.lwListaClientes.currentIndex().row()
                estadoDelCliente = listEstadoCliente[indice]
                if (estadoDelCliente == 1):
                    self.fn_seleccionarCliente()
                    if balanzaSeleccionada == 1:
                        self.fn_traerPreciosCliente(codCliente1)
                        self.fn_seleccionarEspecie(idEspecie)
                        self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                    elif balanzaSeleccionada == 2:
                        self.fn_traerPreciosCliente(codCliente2)
                        self.fn_seleccionarEspecie(idEspecie)
                        self.fn_seleccionarEspecieDescuento(idEspecieDesc)
                        
                    self.fn_verificarProceso()
                    self.fn_listarVenta()
                    self.fn_listarPedidos()
                else:
                    self.fn_cambiarCliente()
                    self.ui.btnCerrarFrmAlerta.setHidden(False)
                    self.ui.lblAlertaTitulo.setStyleSheet("color: #EA1D31")
                    self.ui.lblAlertaTexto.setStyleSheet("font-size:16pt;")
                    self.ui.frmAlerta.setHidden(False)
                    self.ui.lblAlertaTitulo.setText("¡ADVERTENCIA!")
                    self.ui.imgIconAlerta.setPixmap(QPixmap(error))
                    self.ui.lblAlertaTexto.setText("El cliente se encuentra INHABILITADO. Seleccione otro cliente por favor.")
                    
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and self.ui.lwListaClientesCambiarPesada.isVisible():
            if (len(listCodClienteCambiarPesada)):
                indice = self.ui.lwListaClientesCambiarPesada.currentIndex().row()
                estadoDelCliente = listEstadoClienteCambiarPesada[indice]
                if (estadoDelCliente == 1):
                    self.fn_seleccionarClienteCambiarPesada()
                else:
                    self.fn_cambiarClienteCambiarPesada()
                    self.ui.btnCerrarFrmAlerta.setHidden(False)
                    self.ui.lblAlertaTitulo.setStyleSheet("color: #EA1D31")
                    self.ui.lblAlertaTexto.setStyleSheet("font-size:16pt;")
                    self.ui.frmAlerta.setHidden(False)
                    self.ui.lblAlertaTitulo.setText("¡ADVERTENCIA!")
                    self.ui.imgIconAlerta.setPixmap(QPixmap(error))
                    self.ui.lblAlertaTexto.setText("El cliente se encuentra INHABILITADO. Seleccione otro cliente por favor.")
                    
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmIngresarPrecioVenta == True and frmInicioProceso == True and self.ui.frmIngresarPrecioVenta.isVisible():
            self.ui.frmIngresarPrecioVenta.setHidden(True)
            frmIngresarPrecioVenta = False   
            self.fn_registrarPesada()
            self.fn_alerta("¡REGISTRO EXITOSO!",correcto,"El registro se realizo correctamente.")
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmAlertaIngresaNombreVenta == True and frmInicioProceso == True and self.ui.frmAlertaIngresaNombreVenta.isVisible():
            self.ui.frmAlertaIngresaNombreVenta.setHidden(True)
            # self.ui.frmIngresarPrecioVenta.setHidden(False)
            frmAlertaIngresaNombreVenta = False
            # frmIngresarPrecioVenta = True
            # self.ui.txtIngresarPrecioVenta.setFocus(True)        
            self.fn_registrarPesada()
            self.fn_alerta("¡REGISTRO EXITOSO!",correcto,"El registro se realizo correctamente.")
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmRegistrarCantidad == True and frmInicioProceso == True and self.ui.frmIngresarCantidad.isVisible() and self.ui.txtCantidadParaIngresar.text() != "":
                self.ui.txtIngresaNombreVenta.setText("")
                self.ui.txtIngresarPrecioVenta.setText("")
                if codCliente != 24 and codCliente != 69:
                    self.fn_registrarPesada()
                    self.ui.frmIngresarCantidad.setHidden(True)
                    self.fn_alerta("¡REGISTRO EXITOSO!",correcto,"El registro se realizo correctamente.")
                    frmRegistrarCantidad = False
                elif codCliente == 24 or codCliente == 69:
                    self.ui.frmIngresarCantidad.setHidden(True)
                    frmRegistrarCantidad = False
                    self.ui.frmAlertaIngresaNombreVenta.setHidden(False)
                    frmAlertaIngresaNombreVenta = True   
                    self.ui.txtIngresaNombreVenta.setFocus(True)
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmEditarCantidad == True and frmInicioProceso == True and self.ui.frmIngresarCantidad.isVisible() and self.ui.txtCantidadParaIngresar.text() != "":
            self.ui.frmIngresarCantidad.setHidden(True)
            self.fn_editarCantidad()
            frmEditarCantidad = False
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmEditarCantidadTara == True and frmInicioProceso == True and self.ui.frmIngresarCantidad.isVisible() and self.ui.txtCantidadParaIngresar.text() != "":
            self.ui.frmIngresarCantidad.setHidden(True)
            self.fn_editarCantidadTara()
            frmEditarCantidadTara = False
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmEditarCantidadDescuento == True and frmInicioProceso == True and self.ui.frmIngresarCantidad.isVisible() and self.ui.txtCantidadParaIngresar.text() != "":
            self.ui.frmIngresarCantidad.setHidden(True)
            self.fn_editarCantidadDescuento()
            frmEditarCantidadDescuento = False
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmRegistrarJabas == True and frmIngresarNumeroPesoJabaEditar == False and frmInicioProceso == True and self.ui.frmIngresarCantidadJabas.isVisible() and self.ui.txtPesoParaIngresarJabas.text() != "":
            self.ui.frmIngresarCantidadJabas.setHidden(True)
            frmRegistrarJabas = False
            self.fn_registrarTara()
            self.fn_alerta("¡REGISTRO EXITOSO!",correcto,"El registro se realizo correctamente.")
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmInicioProceso == True and frmIngresarNumeroPesoJabaEditar == True and frmRegistrarJabas == False and not self.ui.lwListaClientes.isVisible() and self.ui.txtNumeroDePesada.text()  != "" and int(self.ui.txtNumeroDePesada.text()) > 0 :
            numeroDePesada = int(self.ui.txtNumeroDePesada.text())
            tablaDePesos = self.ui.tblDetallePesadas
            totalFilas = tablaDePesos.rowCount()

            if numeroDePesada <= totalFilas:
                # Obtener el índice ajustado según la cantidad total de filas
                txtNumeroDePesada = totalFilas - numeroDePesada
                idPesadaEditarOEliminar = tablaDePesos.item(txtNumeroDePesada, 12).text()
                identificador = tablaDePesos.item(txtNumeroDePesada, 13).text()
                
                self.ui.txtPesoParaIngresarJabas.setText("")
                self.ui.frmIngresarNumeroPesada.setHidden(True)
                self.ui.frmIngresarCantidadJabas.setHidden(False)
                self.ui.txtPesoParaIngresarJabas.setFocus(True)
                frmRegistrarJabas = True
                frmIngresarNumeroPesoJabaEditar = False
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"El registro no existe, intente de nuevo.",1000)
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmRegistrarDescuento == True and frmInicioProceso == True and self.ui.frmAplicarDescuento.isVisible() and idEspecieDesc != 0 and frmSeleccionarTipoTrozadoDesc == False:
            self.ui.txtCantidadDescuento.setEnabled(True)
            self.ui.imgIconDesc.setPixmap(QPixmap(descuento))
            frmRegistrarDescuento = False
            frmRegistrarDescuentoCan = True
            self.ui.txtCantidadDescuento.setFocus(True)
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmRegistrarDescuento == False and frmRegistrarDescuentoCan == True and frmInicioProceso == True and self.ui.frmAplicarDescuento.isVisible() and self.ui.txtCantidadDescuento.text() != "":
            if idEspecieDesc == primerEspecie and int(self.ui.txtCantYugoVivo.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            elif idEspecieDesc == terceraEspecie and int(self.ui.txtCantTecnicoVivo.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            elif idEspecieDesc == quintaEspecie and int(self.ui.txtCantGallinaDoble.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            elif idEspecieDesc == sextaEspecie and int(self.ui.txtCantAhogados.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            elif idEspecieDesc == septimaEspecie and int(self.ui.txtCantGallo.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            elif idEspecieDesc == octavaEspecie and int(self.ui.txtCantPolloMaltratado.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            elif idEspecieDesc == decimaSextaEspecie and int(self.ui.txtCantPolloXx.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            elif idEspecieDesc == decimaSeptimaEspecie and int(self.ui.txtCantBrasaYugo.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            elif idEspecieDesc == decimaOctavaEspecie and int(self.ui.txtCantBrasaTecnico.text().split()[0].strip()) < int(self.ui.txtCantidadDescuento.text()):
                self.fn_alerta("¡ADVERTENCIA!",error,"La cantidad de descuento no puede ser mayor a la registrada.",2000)
            else:
                self.ui.frmAplicarDescuento.setHidden(True)
                self.fn_registrarDescuento()
                self.fn_alerta("¡REGISTRO EXITOSO!",correcto,"El descuento se realizo correctamente.")
                frmRegistrarDescuentoCan = False
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmIngresarNumeroPesadaEliminar == False and frmAlertaEliminarPeso == True and frmInicioProceso == True and self.ui.frmAlertaEliminar.isVisible():
            self.ui.txtPasswordEliminar.setFocus(True)
            self.ui.frmAlertaEliminar.setHidden(True)
            self.ui.frmIngresarPassword.setHidden(False)
            frmAlertaEliminarPeso = False
            frmEliminarPeso = True
            
        if event.key() == Qt.Key_1 and frmDecidirReporte == True and frmInicioProceso == True and self.ui.frmDecidirReporte.isVisible():
            self.ui.frmDecidirReporte.setHidden(True)
            frmDecidirReporte = False
            imprimePrecio = True
            # self.fn_imprimirReporte()
            frmSeleccionaPesadasReporte = True
            self.ui.txtIngresarValorImprimir.setText("")
            self.ui.frmIntervaloDePesadas.setHidden(False)
            self.ui.txtIngresarValorImprimir.setFocus(True)
            enviaTodoReporteImprimir = False
            incluyeResponsable = False
            incluyeEnvio = False
        
        if event.key() == Qt.Key_2 and frmDecidirReporte == True and frmInicioProceso == True and self.ui.frmDecidirReporte.isVisible():
            self.ui.frmDecidirReporte.setHidden(True)
            frmDecidirReporte = False
            imprimePrecio = False
            # self.fn_imprimirReporte()
            frmSeleccionaPesadasReporte = True
            self.ui.txtIngresarValorImprimir.setText("")
            self.ui.frmIntervaloDePesadas.setHidden(False)
            self.ui.txtIngresarValorImprimir.setFocus(True)
            enviaTodoReporteImprimir = False
            incluyeResponsable = False
            incluyeEnvio = False
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmDecidirReporte == False and frmInicioProceso == True and frmSeleccionaPesadasReporte == True and self.ui.frmIntervaloDePesadas.isVisible() and self.ui.txtIngresarValorImprimir.text() != "":
            frmDecidirReporte = False
            frmSeleccionaPesadasReporte = False
            self.ui.frmIntervaloDePesadas.setHidden(True)
            self.ui.frmAlertaDesicionEnvio.setHidden(False)
            frmAlertaDesicionEnvio = True
            incluyeEnvio = False
            incluyeResponsable = False
            numeroEnvio = 0
            enviaTodoReporteImprimir = False
            # self.fn_alerta("¡REPORTE ENVIADO!",correcto,"El reporte sera impreso en estos momentos.")
            # threadAlerta = threading.Thread(target=self.fn_seleccionaPesadasReporte)
            # threadAlerta.start()
            
        if event.key() == Qt.Key_F1 and frmDecidirReporte == False and frmInicioProceso == True and frmSeleccionaPesadasReporte == True and self.ui.frmIntervaloDePesadas.isVisible():
            frmDecidirReporte = False
            frmSeleccionaPesadasReporte = False
            self.ui.frmIntervaloDePesadas.setHidden(True)
            self.ui.frmAlertaDesicionEnvio.setHidden(False)
            frmAlertaDesicionEnvio = True
            incluyeEnvio = False
            incluyeResponsable = False
            numeroEnvio = 0
            enviaTodoReporteImprimir = True
            # self.fn_alerta("¡REPORTE ENVIADO!",correcto,"El reporte sera impreso en estos momentos.")
            # threadAlerta = threading.Thread(target=self.fn_seleccionaPesadasReporteTotal)
            # threadAlerta.start()
            
        if event.key() == Qt.Key_1 and frmAlertaDesicionEnvio == True and frmInicioProceso == True and self.ui.frmAlertaDesicionEnvio.isVisible():
            self.ui.frmAlertaDesicionEnvio.setHidden(True)
            frmAlertaDesicionEnvio = False
            incluyeEnvio = True
            numeroEnvio = 0
            self.ui.frmAlertaIngresaNumeroEnvio.setHidden(False)
            frmAlertaIngresaNumeroEnvio = True
            self.ui.txtNumeroDeEnvio.setText("")           
            self.ui.txtNumeroDeEnvio.setFocus(True)           
        
        if event.key() == Qt.Key_2 and frmAlertaDesicionEnvio == True and frmInicioProceso == True and self.ui.frmAlertaDesicionEnvio.isVisible():
            self.ui.frmAlertaDesicionEnvio.setHidden(True)
            frmAlertaDesicionEnvio = False
            incluyeEnvio = False
            numeroEnvio = 0
            
            if (enviaTodoReporteImprimir == False):
                self.fn_alerta("¡REPORTE ENVIADO!",correcto,"El reporte sera impreso en estos momentos.")
                threadAlerta = threading.Thread(target=self.fn_seleccionaPesadasReporte)
                threadAlerta.start()
            elif (enviaTodoReporteImprimir == True):
                self.fn_alerta("¡REPORTE ENVIADO!",correcto,"El reporte sera impreso en estos momentos.")
                threadAlerta = threading.Thread(target=self.fn_seleccionaPesadasReporteTotal)
                threadAlerta.start()
                
        if event.key() == Qt.Key_1 and frmAlertaDesicionResponsable == True and frmInicioProceso == True and self.ui.frmAlertaDesicionResponsable.isVisible():
            self.ui.frmAlertaDesicionResponsable.setHidden(True)
            frmAlertaDesicionResponsable = False
            incluyeResponsable = True
            
            if (enviaTodoReporteImprimir == False):
                self.fn_seleccionaPesadasReporteConResponsables()
            elif (enviaTodoReporteImprimir == True):
                self.fn_seleccionaPesadasReporteTotalConResponsables()
            
            largo_arreglo = len(arreglo_id_reporte)
            
            self.ui.txtResponsablesDeEnvio.setText("")
            self.ui.txtResponsablesDeEnvio.setFocus(True)
            self.ui.frmAlertaIngresaResponsablesDeEnvio.setHidden(False)
            self.ui.lblPesadasDisponiblesParaEnvio.setText("TENEMOS {} PESADAS EN TOTAL".format(largo_arreglo))
            frmAlertaIngresaResponsablesDeEnvio = True 
        
        if event.key() == Qt.Key_2 and frmAlertaDesicionResponsable == True and frmInicioProceso == True and self.ui.frmAlertaDesicionResponsable.isVisible():
            self.ui.frmAlertaDesicionResponsable.setHidden(True)
            frmAlertaDesicionResponsable = False
            incluyeResponsable = False
            
            if (enviaTodoReporteImprimir == False):
                self.fn_alerta("¡REPORTE ENVIADO!",correcto,"El reporte sera impreso en estos momentos.")
                threadAlerta = threading.Thread(target=self.fn_seleccionaPesadasReporte)
                threadAlerta.start()
            elif (enviaTodoReporteImprimir == True):
                self.fn_alerta("¡REPORTE ENVIADO!",correcto,"El reporte sera impreso en estos momentos.")
                threadAlerta = threading.Thread(target=self.fn_seleccionaPesadasReporteTotal)
                threadAlerta.start()
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmAlertaEliminarPeso == False and frmEliminarPeso == True and frmInicioProceso == True and self.ui.frmIngresarPassword.isVisible() and self.ui.txtPasswordEliminar.text() != "":
            passwordExtraido = self.ui.txtPasswordEliminar.text()
            if str(passwordEliminar) == str(passwordExtraido):
                self.ui.frmIngresarPassword.setHidden(True)
                self.fn_eliminarUltimaCantidad()
                frmEliminarPeso = False
            else:
                self.fn_alerta("¡CONTRASEÑA INCORRECTA!",error,"La contraseña no coincide con la contraseña declara para eliminar.")
        
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmInicioProceso == True and frmIngresarNumeroPesadaEditar == True and not self.ui.lwListaClientes.isVisible() and self.ui.txtNumeroDePesada.text()  != "" and int(self.ui.txtNumeroDePesada.text()) > 0 :                
                numeroDePesada = int(self.ui.txtNumeroDePesada.text())
                tablaDePesos = self.ui.tblDetallePesadas
                totalFilas = tablaDePesos.rowCount()

                if numeroDePesada <= totalFilas:
                    # Obtener el índice ajustado según la cantidad total de filas
                    txtNumeroDePesada = totalFilas - numeroDePesada
                    idPesadaEditarOEliminar = tablaDePesos.item(txtNumeroDePesada, 12).text()
                    identificador = tablaDePesos.item(txtNumeroDePesada, 13).text()
                
                    item = self.ui.tblDetallePesadas.item(txtNumeroDePesada, 6)  # Obtener el item de la primera fila y columna 5
                    valor = item.text()
                    
                    if valor.endswith('T'):
                        self.ui.txtCantidadParaIngresar.setText("")
                        self.fn_alertaCantidad("Ingresar cantidad nueva de Tara")
                        frmEditarCantidadTara = True
                        self.ui.txtCantidadParaIngresar.setFocus(True)
                    elif valor.startswith("-"):
                        self.ui.txtCantidadParaIngresar.setText("")
                        self.fn_alertaCantidad("Ingresar cantidad nueva de Descuento")
                        frmEditarCantidadDescuento = True
                        self.ui.txtCantidadParaIngresar.setFocus(True)
                    else:
                        self.ui.txtCantidadParaIngresar.setText("")
                        self.fn_alertaCantidad("Ingresar cantidad nueva de Pollos")
                        frmEditarCantidad = True
                        self.ui.txtCantidadParaIngresar.setFocus(True)
                        
                    frmIngresarNumeroPesadaEditar = False
                    self.ui.frmIngresarNumeroPesada.setHidden(True)
                else:
                    self.fn_alerta("¡ADVERTENCIA!",error,"El registro no existe, intente de nuevo.",1000)
                    
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmInicioProceso == True and frmIngresarNumeroPesadaEliminar == True and not self.ui.lwListaClientes.isVisible() and self.ui.txtNumeroDePesada.text()  != "" and int(self.ui.txtNumeroDePesada.text()) > 0 :
            numeroDePesada = int(self.ui.txtNumeroDePesada.text())
            tablaDePesos = self.ui.tblDetallePesadas
            totalFilas = tablaDePesos.rowCount()

            if numeroDePesada <= totalFilas:
                # Obtener el índice ajustado según la cantidad total de filas
                txtNumeroDePesada = totalFilas - numeroDePesada
                idPesadaEditarOEliminar = tablaDePesos.item(txtNumeroDePesada, 12).text()
                identificador = tablaDePesos.item(txtNumeroDePesada, 13).text()
                
                self.ui.txtPasswordEliminar.setText("")
                self.ui.frmIngresarNumeroPesada.setHidden(True)
                self.ui.frmAlertaEliminar.setHidden(False)
                frmAlertaEliminarPeso = True
                frmIngresarNumeroPesadaEliminar = False
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"El registro no existe, intente de nuevo.",1000)
        
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and not self.ui.lwListaClientes.isVisible() and self.ui.frmColores.isVisible() and frmRegistrarColoresJabasEditar == True and frmIngresarNumeroColoresEditar == False:
            self.ui.frmColores.setHidden(True)
            self.fn_actualizarPesadaColores()
            frmRegistrarColoresJabasEditar = False
                
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmInicioProceso == True and frmIngresarNumeroColoresEditar == True and not self.ui.lwListaClientes.isVisible() and self.ui.txtNumeroDePesada.text()  != "" and int(self.ui.txtNumeroDePesada.text()) > 0 :
            numeroDePesada = int(self.ui.txtNumeroDePesada.text())
            tablaDePesos = self.ui.tblDetallePesadas
            totalFilas = tablaDePesos.rowCount()

            if numeroDePesada <= totalFilas:
                # Obtener el índice ajustado según la cantidad total de filas
                txtNumeroDePesada = totalFilas - numeroDePesada
                idPesadaEditarOEliminar = tablaDePesos.item(txtNumeroDePesada, 12).text()
                identificador = tablaDePesos.item(txtNumeroDePesada, 13).text()
                
                datosColoresEditar = ""
                if identificador == "tb_pesadas":
                    datosColoresEditar = self.conexion.db_consultarColoresEditar(idPesadaEditarOEliminar)
                elif identificador == "tb_pesadas2":
                    datosColoresEditar = self.conexion.db_consultarColoresEditar2(idPesadaEditarOEliminar)
                
                if datosColoresEditar != "":
                
                    datosColoresEditarDesestruturado = datosColoresEditar.split(' | ')
                    
                    arregloEditar = []
                    
                    for letra in datosColoresEditarDesestruturado:
                        numero = letra[1:]
                        if int(numero) == 0 :
                            numero = ""
                        arregloEditar.append(numero)
                    
                    self.ui.txtCantidadPrimerColor.setText(arregloEditar[0])
                    self.ui.txtCantidadSegundoColor.setText(arregloEditar[1])
                    self.ui.txtCantidadTercerColor.setText(arregloEditar[2])
                    self.ui.txtCantidadCuartoColor.setText(arregloEditar[3])
                    self.ui.txtCantidadQuintoColor.setText(arregloEditar[4])
                    self.ui.txtCantidadSextoColor.setText(arregloEditar[5])
                    self.ui.txtCantidadSeptimoColor.setText(arregloEditar[6])
                    
                    self.ui.txtNumeroDePesada.setText("")
                    self.ui.frmIngresarNumeroPesada.setHidden(True)
                    self.ui.frmColores.setHidden(False)
                    frmRegistrarColoresJabasEditar = True
                    frmIngresarNumeroColoresEditar = False
                else:
                    self.fn_alerta("¡ADVERTENCIA!",error,"Diríjase al otro modulo para poder editar esta pesada.",2000)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"El registro no existe, intente de nuevo.",1000)
                
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmInicioProceso == True and frmIngresarNumeroPesadaEditarEspecie == True and not self.ui.lwListaClientes.isVisible() and self.ui.txtNumeroDePesada.text()  != "" and int(self.ui.txtNumeroDePesada.text()) > 0 :
            numeroDePesada = int(self.ui.txtNumeroDePesada.text())
            tablaDePesos = self.ui.tblDetallePesadas
            totalFilas = tablaDePesos.rowCount()

            if numeroDePesada <= totalFilas:
                # Obtener el índice ajustado según la cantidad total de filas
                txtNumeroDePesada = totalFilas - numeroDePesada
                idPesadaEditarOEliminar = tablaDePesos.item(txtNumeroDePesada, 12).text()
                identificador = tablaDePesos.item(txtNumeroDePesada, 13).text()
                self.ui.lblTextAvisaCambioEspeciePesada.setText("SE CAMBIARA LA ESPECIE DE LA PESADA : {}".format(numeroDePesada))
                
                self.ui.frmIngresarNumeroPesada.setHidden(True)
                self.ui.frmCambiarEspecie.setHidden(False)
                frmSeleccionarEspecieEditarPesada = True
                frmIngresarNumeroPesadaEditarEspecie = False
                precioCambiarEspecie = 0
                idEspecieCambiarEspecie = 0
                self.fn_seleccionarEspecieCambiar(0)
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"El registro no existe, intente de nuevo.",1000)
                
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmSeleccionarEspecieEditarPesada == True and frmIngresarNumeroPesadaEditarEspecie == False and frmInicioProceso == True and self.ui.frmCambiarEspecie.isVisible() and idEspecieCambiarEspecie != 0:
            self.ui.frmCambiarEspecie.setHidden(True)
            self.fn_editarEspeciePesada()
            frmSeleccionarEspecieEditarPesada = False
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmInicioProceso == True and frmIngresarNumeroCambiarPesada == True and not self.ui.lwListaClientes.isVisible() and self.ui.txtNumeroDePesada.text()  != "" and int(self.ui.txtNumeroDePesada.text()) > 0 :
            numeroDePesada = int(self.ui.txtNumeroDePesada.text())
            tablaDePesos = self.ui.tblDetallePesadas
            totalFilas = tablaDePesos.rowCount()

            if numeroDePesada <= totalFilas:
                # Obtener el índice ajustado según la cantidad total de filas
                txtNumeroDePesada = totalFilas - numeroDePesada
                idPesadaEditarOEliminar = tablaDePesos.item(txtNumeroDePesada, 12).text()
                identificador = tablaDePesos.item(txtNumeroDePesada, 13).text()
                nombreClienteAnterior = tablaDePesos.item(txtNumeroDePesada, 1).text()
                pesoClienteAnterior = tablaDePesos.item(txtNumeroDePesada, 5).text()
                cantidadClienteAnterior = tablaDePesos.item(txtNumeroDePesada, 4).text()
                self.ui.lblTextoCambiarPesadaCliente.setText("Cliente : {} \nPeso Bruto : {} Kg. \nCantidad : {}".format(nombreClienteAnterior, pesoClienteAnterior, cantidadClienteAnterior))
                
                codigoClienteCambiarPesada = 0
                self.ui.txtCodigoClienteCambiarPesada.setHidden(False)
                self.ui.txtCodigoClienteCambiarPesada.setText("")
                self.ui.txtCodigoClienteCambiarPesada.setFocus(True)
                self.ui.lwListaClientesCambiarPesada.setHidden(False)
                
                self.ui.frmIngresarNumeroPesada.setHidden(True)
                self.ui.frmCambiarPesadaCliente.setHidden(False)
                frmCambiarPesadaCliente = True
                frmIngresarNumeroCambiarPesada = False
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"El registro no existe, intente de nuevo.",1000)
                
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmInicioProceso == True and frmAlertaIngresaNumeroEnvio == True and not self.ui.lwListaClientes.isVisible() and self.ui.txtNumeroDeEnvio.text()  != "" and int(self.ui.txtNumeroDeEnvio.text()) > 0 :
            self.ui.frmAlertaIngresaNumeroEnvio.setHidden(True)
            frmAlertaIngresaNumeroEnvio = False
            numeroEnvio = int(self.ui.txtNumeroDeEnvio.text())
            self.ui.frmAlertaDesicionResponsable.setHidden(False)
            frmAlertaDesicionResponsable = True
            
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and frmInicioProceso == True and frmAlertaIngresaResponsablesDeEnvio == True and not self.ui.lwListaClientes.isVisible() and self.ui.txtResponsablesDeEnvio.text()  != "" and self.ui.frmAlertaIngresaResponsablesDeEnvio.isVisible():
            responsablesDeEnvio = self.ui.txtResponsablesDeEnvio.text()
            resultado = self.convertir_a_lista_de_diccionarios(responsablesDeEnvio)
            
            if (resultado):
                self.ui.frmAlertaIngresaResponsablesDeEnvio.setHidden(True)
                frmAlertaIngresaResponsablesDeEnvio = False
                self.fn_alerta("¡REPORTE ENVIADO!",correcto,"El reporte sera impreso en estos momentos.")
                # Llamar a la función para imprimir el reporte
                threadAlerta = threading.Thread(target=self.fn_imprimirReporte())
                threadAlerta.start()
            else:
                self.fn_alerta("¡ADVERTENCIA!",error,"El valor ingresado no es correcto, intente de nuevo.",1000)
            
    # ======================== Termina eventos con el Teclado ========================
    
    def fn_temporizadorBtn(self):
        global btnActualizar
        global contadorActualizar

        # Contar desde 30 hasta 0 segundos
        for i in range(30, -1, -1):
            contadorActualizar = i
            time.sleep(1)

        btnActualizar = False
    
    def fn_abrirAnimacion(self):
        self.ui.btnCerrarFrmAlerta.setHidden(True)
        self.ui.lblAlertaTitulo.setStyleSheet("color: #3A93B3")
        self.ui.frmAlerta.setHidden(False)
        self.ui.lblAlertaTitulo.setText("Actualizando Datos")
        
        movie = QMovie(loading)  # Crea una instancia de QMovie
        self.ui.imgIconAlerta.setMovie(movie)  # Asocia la QMovie con el QLabel
        movie.start()  # Inicia la animación
        self.ui.lblAlertaTexto.setStyleSheet("font-size:14pt;")
        self.ui.lblAlertaTexto.setText("Espere por favor los datos se están actualizando. Recuerda que debes esperar 30 segundos para volver a actualizar.")
        
        # Llama a fn_traerDatosServidor en un hilo para evitar bloquear la interfaz de usuario
        thread = threading.Thread(target=self.fn_traerDatosServidor)
        thread.start()
    
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
                print("Exito al interactuar con la base de datos")
            except Exception as e:
                print(f"Error al interactuar con la base de datos: {e}")
            else:
                s2.close()
                
            self.ui.frmAlerta.setHidden(True)
            self.ui.frmSombra.setHidden(True)
    
    def fn_declaraEspecie(self):
        global primerEspecie
        global segundaEspecie
        global terceraEspecie
        global cuartaEspecie
        global quintaEspecie
        global sextaEspecie
        global septimaEspecie
        global octavaEspecie
        global novenaEspecie
        global decimaEspecie
        global decimaPrimeraEspecie
        global decimaSegundaEspecie
        global decimaTerceraEspecie
        global decimaCuartaEspecie
        global decimaQuintaOtrasEspecies
        global decimaSextaEspecie
        global decimaSeptimaEspecie
        global decimaOctavaEspecie
        global nombrePrimerEspecie
        global nombreSegundaEspecie
        global nombreTerceraEspecie
        global nombreCuartaEspecie
        global nombreQuintaEspecie
        global nombreSextaEspecie
        global nombreSeptimaEspecie
        global nombreOctavaEspecie
        global nombreNovenaEspecie
        global nombreDecimaEspecie
        global nombreDecimaPrimeraEspecie
        global nombreDecimaSegundaEspecie
        global nombreDecimaTerceraEspecie
        global nombreDecimaCuartaEspecie
        global nombreDecimaQuintaOtrasEspecies
        global nombreDecimaSextaEspecie
        global nombreDecimaSeptimaEspecie
        global nombreDecimaOctavaEspecie
        global decimaNovenaEspecie
        global vigesimaEspecie
        global vigesimaPrimeraEspecie
        global vigesimaSegundaEspecie
        global nombreDecimaNovenaEspecie 
        global nombreVigesimaEspecie 
        global nombreVigesimaPrimeraEspecie 
        global nombreVigesimaSegundaEspecie 
        global vigesimaTerceraEspecie
        global nombreVigesimaTerceraEspecie
        
        nombresEspecies = self.conexion.db_buscaEspecies()
        
        primerEspecie = nombresEspecies[0][0]
        nombrePrimerEspecie = nombresEspecies[0][1]
        
        segundaEspecie = nombresEspecies[1][0]
        nombreSegundaEspecie = nombresEspecies[1][1]
        
        terceraEspecie = nombresEspecies[2][0]
        nombreTerceraEspecie = nombresEspecies[2][1]
        
        cuartaEspecie = nombresEspecies[3][0]
        nombreCuartaEspecie = nombresEspecies[3][1]
        
        quintaEspecie = nombresEspecies[4][0]
        nombreQuintaEspecie = nombresEspecies[4][1]
        
        sextaEspecie = nombresEspecies[5][0]
        nombreSextaEspecie = nombresEspecies[5][1]
        
        septimaEspecie = nombresEspecies[6][0]
        nombreSeptimaEspecie = nombresEspecies[6][1]
        
        octavaEspecie = nombresEspecies[7][0]
        nombreOctavaEspecie = nombresEspecies[7][1]

        novenaEspecie = nombresEspecies[8][0]
        nombreNovenaEspecie = nombresEspecies[8][1]
        
        decimaEspecie = nombresEspecies[9][0]
        nombreDecimaEspecie = nombresEspecies[9][1]
        
        decimaPrimeraEspecie = nombresEspecies[10][0]
        nombreDecimaPrimeraEspecie = nombresEspecies[10][1]
        
        decimaSegundaEspecie = nombresEspecies[11][0]
        nombreDecimaSegundaEspecie = nombresEspecies[11][1]
        
        decimaTerceraEspecie = nombresEspecies[12][0]
        nombreDecimaTerceraEspecie = nombresEspecies[12][1]
        
        decimaCuartaEspecie = nombresEspecies[13][0]
        nombreDecimaCuartaEspecie = nombresEspecies[13][1]
        
        decimaQuintaOtrasEspecies = nombresEspecies[14][0]
        nombreDecimaQuintaOtrasEspecies = nombresEspecies[14][1]
        
        decimaSextaEspecie = nombresEspecies[15][0]
        nombreDecimaSextaEspecie = nombresEspecies[15][1]
        
        decimaSeptimaEspecie = nombresEspecies[16][0]
        nombreDecimaSeptimaEspecie = nombresEspecies[16][1]
        
        decimaOctavaEspecie = nombresEspecies[17][0]
        nombreDecimaOctavaEspecie = nombresEspecies[17][1]
        
        decimaNovenaEspecie = nombresEspecies[18][0]
        nombreDecimaNovenaEspecie = nombresEspecies[18][1]
        
        vigesimaEspecie = nombresEspecies[19][0]
        nombreVigesimaEspecie = nombresEspecies[19][1]
        
        vigesimaPrimeraEspecie = nombresEspecies[20][0]
        nombreVigesimaPrimeraEspecie = nombresEspecies[20][1]
        
        vigesimaSegundaEspecie = nombresEspecies[21][0]
        nombreVigesimaSegundaEspecie = nombresEspecies[21][1]
        
        vigesimaTerceraEspecie = nombresEspecies[22][0]
        nombreVigesimaTerceraEspecie = nombresEspecies[22][1]
        
        self.ui.btnYugoVivo.setText("{} (1)".format(nombrePrimerEspecie))
        self.ui.btnBrasaYugo.setText("{} (2)".format(nombreDecimaSeptimaEspecie))
        self.ui.btnTecnicoVivo.setText("{} (3)".format(nombreTerceraEspecie))
        self.ui.btnBrasaTecnico.setText("{} (4)".format(nombreDecimaOctavaEspecie))
        txtnombreVigesimaEspecie= self.format_species_name(nombreVigesimaEspecie)
        self.ui.btnGallinaDoble.setText("{} (5)".format(txtnombreVigesimaEspecie))
        self.ui.btnGallo.setText("{} (6)".format(nombreVigesimaSegundaEspecie))
        self.ui.btnPolloMaltratado.setText("{} (7)".format(nombreVigesimaTerceraEspecie))
        self.ui.btnPolloXx.setText("{} (8)".format(nombreDecimaNovenaEspecie))
        self.ui.btnAhogados.setText("{} (9)".format(nombreSextaEspecie))
        self.ui.btnSecos.setText("{} (F1)".format(nombreVigesimaPrimeraEspecie))
        
        self.ui.btnDescYugoVivo.setText("{} (1)".format(nombrePrimerEspecie))
        self.ui.btnDescBrasaYugo.setText("{} (2)".format(nombreDecimaSeptimaEspecie))
        self.ui.btnDescTecnicoVivo.setText("{} (3)".format(nombreTerceraEspecie))
        self.ui.btnDescPolloBrasaTecnico.setText("{} (4)".format(nombreDecimaOctavaEspecie))
        txtnombreVigesimaEspecie= self.format_species_name(nombreVigesimaEspecie)
        self.ui.btnDescGallinaDoble.setText("{} (5)".format(txtnombreVigesimaEspecie))
        self.ui.btnDescGallinaChica.setText("{} (6)".format(nombreVigesimaPrimeraEspecie))
        self.ui.btnDescGallo.setText("{} (7)".format(nombreVigesimaSegundaEspecie))
        txtnombreVigesimaTerceraEspecie = self.format_species_name1(nombreVigesimaTerceraEspecie)
        self.ui.btnDescPolloMaltratado.setText("{} (8)".format(txtnombreVigesimaTerceraEspecie))
        self.ui.btnDescPolloXx.setText("{} (9)".format(nombreDecimaNovenaEspecie))
        
    def format_species_name(self,name):
        parts = name.split()
        if len(parts) > 2:
            # Insertamos el salto de línea a partir del segundo espacio
            formatted_name = ' '.join(parts[:2]) + '\n' + ' '.join(parts[2:])
        else:
            formatted_name = name
        return formatted_name

    def format_species_name1(self,name):
        parts = name.split()
        if len(parts) > 1:
            # Insertamos el salto de línea a partir del segundo espacio
            formatted_name = ' '.join(parts[:1]) + '\n' + ' '.join(parts[1:])
        else:
            formatted_name = name
        return formatted_name
        
    def fn_declaraPassword(self):
        global passwordEliminar
        
        passwordBase = self.conexion.db_declaraPassword()
        passwordEliminar = str(passwordBase[0])
        
        
    def fn_alerta(self,titulo,imagen,mensaje,tiempo = 500):
        self.ui.btnCerrarFrmAlerta.setHidden(True)
        if imagen == correcto:
            self.ui.lblAlertaTitulo.setStyleSheet("color: #24D315")
            self.ui.lblAlertaTexto.setStyleSheet("font-size:16pt;")
        elif imagen == error:
            self.ui.lblAlertaTitulo.setStyleSheet("color: #EA1D31")
            self.ui.lblAlertaTexto.setStyleSheet("font-size:16pt;")
        self.ui.frmAlerta.setHidden(False)
        self.ui.frmSombra.setHidden(False)
        self.ui.lblAlertaTitulo.setText(titulo)
        self.ui.imgIconAlerta.setPixmap(QPixmap(imagen))
        self.ui.lblAlertaTexto.setText(mensaje)

        timer = QtCore.QTimer()
        timer.singleShot(tiempo, lambda: self.ui.frmAlerta.setHidden(True))
        
        if self.condiciones_alertas_sombra():
            timer2 = QtCore.QTimer()
            timer2.singleShot(tiempo, lambda: self.ui.frmSombra.setHidden(True))
        
    def fn_alertaCantidad(self,titulo):
        self.ui.frmIngresarCantidad.setHidden(False)
        self.ui.lblTextoIngresarCantidad.setText(titulo)
        
    def fn_validarEntradaNumerica(self):
        sender = self.sender()

        if sender is not None and isinstance(sender, QLineEdit):
            texto = sender.text()

            texto_valido = ''.join(filter(str.isdigit, texto))

            sender.setText(texto_valido)
    
    def fn_recepcionaCodigoTrabajador(self):
        global listCodCliente
        global listEstadoCliente
        
        self.ui.lwListaClientes.clear()
        listCodCliente.clear()
        listEstadoCliente.clear()
        valor = self.ui.txtCodigoCliente.text()

        if (valor != "" and len(valor) >= 1):

            nombreClienteSeleccionar = self.conexion.db_buscaCliente(valor)
            
            if nombreClienteSeleccionar is not None:
                if (len(nombreClienteSeleccionar) > 0):
                    self.ui.lwListaClientes.setHidden(False)
                    for item in nombreClienteSeleccionar:
                        self.ui.lwListaClientes.addItem(item[0])
                        listCodCliente.append(item[1])
                        listEstadoCliente.append(item[2])
                    self.ui.lwListaClientes.setCurrentRow(0)
            else:
                # Manejar el caso de que db_buscaCliente devolvió None
                print("Error al buscar clientes. La función db_buscaCliente devolvió None.")
                               
    def fn_ArribaLista(self):
        global indexLista
        
        if (indexLista != 0):
            indexLista -= 1
            self.ui.lwListaClientes.setCurrentRow(indexLista)

    def fn_AbajoLista(self):
        global indexLista
        
        numClientes = self.ui.lwListaClientes.count()
        if (indexLista < numClientes-1):
            indexLista += 1
            self.ui.lwListaClientes.setCurrentRow(indexLista)
            
    def fn_seleccionarCliente(self):
        global codCliente
        global codCliente1
        global codCliente2
        global nombresCliBalanza1
        global nombresCliBalanza2
        global precioCliente
        global idEspecie
        global idEspecieDesc
        global especieCli1
        global especieCli2
        global nombresCliBalanza
        global especieDesCli1
        global especieDesCli2
        global indexLista
        
        if (balanzaSeleccionada == 1):
            indice = self.ui.lwListaClientes.currentIndex().row()
            codCliente1 = listCodCliente[indice]

            item = QListWidgetItem(self.ui.lwListaClientes.currentItem())
            self.ui.txtNombreCliente.setText(str(item.text()))
            self.ui.lwListaClientes.setHidden(True)
            self.ui.txtCodigoCliente.setHidden(True)
            nombresCliBalanza1 = str(item.text())
            codCliente = codCliente1
            especieCli1 = primerEspecie
            especieDesCli1 = 0
            idEspecie = especieCli1
            idEspecieDesc = especieDesCli1
            nombresCliBalanza = nombresCliBalanza1
            
        elif (balanzaSeleccionada == 2):
            indice = self.ui.lwListaClientes.currentIndex().row()
            codCliente2 = listCodCliente[indice]

            item = QListWidgetItem(self.ui.lwListaClientes.currentItem())
            self.ui.txtNombreCliente.setText(str(item.text()))
            self.ui.lwListaClientes.setHidden(True)
            self.ui.txtCodigoCliente.setHidden(True)
            nombresCliBalanza2 = str(item.text())
            codCliente = codCliente2
            especieCli2 = primerEspecie
            especieDesCli2 = 0
            idEspecie = especieCli2
            idEspecieDesc = especieDesCli2
            nombresCliBalanza = nombresCliBalanza2
            
        indexLista = 0
            
    def fn_btnCerrarFrmAlerta(self):
        self.ui.frmAlerta.setHidden(True)
        self.ui.txtCodigoCliente.setFocus(True)
            
    def fn_seleccionaBalanza(self):
        global codCliente
        global balanzaSeleccionada
        global nombresCliBalanza
        global idEspecie
        global precioCliente
        global frmInicioProceso
        global idEspecieDesc
        global precioClienteDesc
        
        codCliente = 0
        nombresCliBalanza = ""
        precioCliente = 0
        precioClienteDesc = 0
        idEspecie = 0
        idEspecieDesc = 0
        self.ui.lblCodigoCliente.setText(str(0))
        
        # self.ui.lblEstadoBalanzas.setText("FUERA DE LINEA")
        # self.ui.lblEstadoBalanzas.setStyleSheet("background-color: rgb(234, 29, 49);color: rgb(255, 255, 255);")
        
        if (balanzaSeleccionada == 1):
            self.ui.lblNumBalanza.setText("Cliente N° 1")
            if codCliente1 != 0:
                frmInicioProceso = True
                codCliente = codCliente1
                nombresCliBalanza = nombresCliBalanza1
                idEspecie = especieCli1
                idEspecieDesc = especieDesCli1
                self.fn_traerPreciosCliente(codCliente)
                self.ui.txtNombreCliente.setText(nombresCliBalanza1)
                self.ui.txtCodigoCliente.setHidden(True)
                self.ui.lwListaClientes.setHidden(True)
            else:
                self.ui.txtCodigoCliente.setHidden(False)
                self.ui.txtCodigoCliente.setText("")
                self.ui.txtCodigoCliente.setFocus(True)
                self.ui.lwListaClientes.setHidden(False)
                
        elif (balanzaSeleccionada == 2):
            self.ui.lblNumBalanza.setText("Cliente N° 2")
            if codCliente2 != 0:
                frmInicioProceso = True
                codCliente = codCliente2
                nombresCliBalanza = nombresCliBalanza2
                idEspecie = especieCli2
                idEspecieDesc = especieDesCli2
                self.fn_traerPreciosCliente(codCliente)
                self.ui.txtNombreCliente.setText(nombresCliBalanza2)
                self.ui.txtCodigoCliente.setHidden(True)
                self.ui.lwListaClientes.setHidden(True)
            else:
                self.ui.txtCodigoCliente.setHidden(False)
                self.ui.txtCodigoCliente.setText("")
                self.ui.txtCodigoCliente.setFocus(True)
                self.ui.lwListaClientes.setHidden(False)
            
    def fn_traerPreciosCliente(self, codCliente):
        global precioPrimerEspecie
        global precioSegundaEspecie
        global precioTerceraEspecie
        global precioCuartaEspecie
        global precioQuintaEspecie
        global precioSextaEspecie
        global precioSeptimaEspecie
        global precioOctavaEspecie
        global precioNovenaEspecie
        global precioDecimaEspecie
        global precioDecimaPrimeraEspecie
        global precioDecimaSegundaEspecie
        global precioDecimaTerceraEspecie
        global precioDecimaCuartaEspecie
        global precioDecimaQuintaOtrasEspecies
        global precioDecimaSextaEspecie
        global precioDecimaSeptimaEspecie
        global precioDecimaOctavaEspecie
        global precioDecimaNovenaEspecie
        global precioVigesimaEspecie
        global precioVigesimaPrimeraEspecie
        global precioVigesimaSegundaEspecie
        global precioVigesimaTerceraEspecie
        
        global precioPrimerEspecie_ant
        global precioSegundaEspecie_ant
        global precioTerceraEspecie_ant
        global precioCuartaEspecie_ant
        global precioQuintaEspecie_ant
        global precioSextaEspecie_ant
        global precioSeptimaEspecie_ant
        global precioOctavaEspecie_ant
        global precioNovenaEspecie_ant
        global precioDecimaEspecie_ant
        global precioDecimaPrimeraEspecie_ant
        global precioDecimaSegundaEspecie_ant
        global precioDecimaTerceraEspecie_ant
        global precioDecimaCuartaEspecie_ant
        global precioDecimaQuintaOtrasEspecies_ant
        global precioDecimaSextaEspecie_ant
        global precioDecimaSeptimaEspecie_ant
        global precioDecimaOctavaEspecie_ant
        global precioDecimaNovenaEspecie_ant
        global precioVigesimaEspecie_ant
        global precioVigesimaPrimeraEspecie_ant
        global precioVigesimaSegundaEspecie_ant
        global precioVigesimaTerceraEspecie_ant
        
        try:
            self.preciosCliente = self.conexion.db_traerPreciosCliente(codCliente)
            self.preciosCliente_ant = self.conexion.db_traerPreciosCliente_ant(codCliente)
            
            (precioPrimerEspecie, precioSegundaEspecie, precioTerceraEspecie, precioCuartaEspecie, precioQuintaEspecie,precioSextaEspecie,precioSeptimaEspecie,precioOctavaEspecie,precioNovenaEspecie,precioDecimaEspecie,precioDecimaPrimeraEspecie,precioDecimaSegundaEspecie,precioDecimaTerceraEspecie,precioDecimaCuartaEspecie,precioDecimaQuintaOtrasEspecies,precioDecimaSextaEspecie,precioDecimaSeptimaEspecie,precioDecimaOctavaEspecie, precioDecimaNovenaEspecie, precioVigesimaEspecie, precioVigesimaPrimeraEspecie, precioVigesimaSegundaEspecie, precioVigesimaTerceraEspecie) = self.preciosCliente[0]
            
            (precioPrimerEspecie_ant, precioSegundaEspecie_ant, precioTerceraEspecie_ant, precioCuartaEspecie_ant, precioQuintaEspecie_ant,precioSextaEspecie_ant,precioSeptimaEspecie_ant,precioOctavaEspecie_ant,precioNovenaEspecie_ant,precioDecimaEspecie_ant,precioDecimaPrimeraEspecie_ant,precioDecimaSegundaEspecie_ant,precioDecimaTerceraEspecie_ant,precioDecimaCuartaEspecie_ant,precioDecimaQuintaOtrasEspecies_ant,precioDecimaSextaEspecie_ant,precioDecimaSeptimaEspecie_ant,precioDecimaOctavaEspecie_ant, precioDecimaNovenaEspecie_ant, precioVigesimaEspecie_ant, precioVigesimaPrimeraEspecie_ant, precioVigesimaSegundaEspecie_ant, precioVigesimaTerceraEspecie_ant) = self.preciosCliente_ant[0]
        except Exception as e:
            self.fn_alerta("¡ERROR!",error,"No se pudieron obtener los precios del cliente.", 2000)
            self.fn_cambiarCliente()
        
    def fn_cambiarCliente(self):
        global precioPrimerEspecie
        global precioSegundaEspecie
        global precioTerceraEspecie
        global precioCuartaEspecie
        global precioQuintaEspecie
        global precioSextaEspecie
        global precioSeptimaEspecie
        global precioOctavaEspecie
        global precioNovenaEspecie
        global precioDecimaEspecie
        global precioDecimaPrimeraEspecie
        global precioDecimaSegundaEspecie
        global precioDecimaTerceraEspecie
        global precioDecimaCuartaEspecie
        global precioDecimaQuintaOtrasEspecies
        global precioDecimaSextaEspecie
        global precioDecimaSeptimaEspecie
        global precioDecimaOctavaEspecie
        global precioDecimaNovenaEspecie
        global precioVigesimaEspecie
        global precioVigesimaPrimeraEspecie
        global precioVigesimaSegundaEspecie
        global precioVigesimaTerceraEspecie
        global codCliente1
        global codCliente2
        global nombresCliBalanza1
        global nombresCliBalanza2
        global codCliente
        global frmInicioProceso
        global indexLista
        
        precioPrimerEspecie = 0
        precioSegundaEspecie = 0
        precioTerceraEspecie = 0
        precioCuartaEspecie = 0
        precioQuintaEspecie = 0
        precioSextaEspecie = 0
        precioSeptimaEspecie = 0
        precioOctavaEspecie = 0
        precioNovenaEspecie = 0
        precioDecimaEspecie = 0
        precioDecimaPrimeraEspecie = 0
        precioDecimaSegundaEspecie = 0
        precioDecimaTerceraEspecie = 0
        precioDecimaCuartaEspecie = 0
        precioDecimaQuintaOtrasEspecies = 0
        precioDecimaSextaEspecie = 0
        precioDecimaSeptimaEspecie = 0
        precioDecimaOctavaEspecie = 0
        precioDecimaNovenaEspecie = 0
        precioVigesimaEspecie = 0
        precioVigesimaPrimeraEspecie = 0
        precioVigesimaSegundaEspecie = 0
        precioVigesimaTerceraEspecie = 0
        
        codCliente = 0
        indexLista = 0
        
        self.ui.txtCantJabasTotales.setText("{} Uds.".format(0))
                            
        self.ui.lblKgYugoVivo.setText("{:.2f} Kg".format(0))
        self.ui.lblKgTecnicoVivo.setText("{:.2f} Kg".format(0))
        self.ui.lblKgGallinaDoble.setText("{:.2f} Kg".format(0))
        self.ui.lblKgAhogados.setText("{:.2f} Kg".format(0))
        self.ui.lblKgGallo.setText("{:.2f} Kg".format(0))
        self.ui.lblKgPolloMaltratado.setText("{:.2f} Kg".format(0))
        self.ui.lblKgPolloXx.setText("{:.2f} Kg".format(0))
        self.ui.lblKgBrasaYugo.setText("{:.2f} Kg".format(0))
        self.ui.lblKgBrasaTecnico.setText("{:.2f} Kg".format(0))
        
        self.ui.txtCantPolloTotales.setText("{} Uds.".format(0))
        
        self.ui.txtCantYugoVivo.setText("{} Uds.".format(0))
        self.ui.txtCantTecnicoVivo.setText("{} Uds.".format(0))
        self.ui.txtCantGallinaDoble.setText("{} Uds.".format(0))
        self.ui.txtCantAhogados.setText("{} Uds.".format(0))
        self.ui.txtCantGallo.setText("{} Uds.".format(0))
        self.ui.txtCantPolloMaltratado.setText("{} Uds.".format(0))
        self.ui.txtCantPolloXx.setText("{} Uds.".format(0))
        self.ui.txtCantBrasaYugo.setText("{} Uds.".format(0))
        self.ui.txtCantBrasaTecnico.setText("{} Uds.".format(0))
        
        tablaDePesos = self.ui.tblDetallePesadas
        tablaDePesos.clearContents()
        tablaDePesos.setRowCount(0)
        
        tablaDePedidos = self.ui.tblDetallePedidos
        tablaDePedidos.clearContents()
        tablaDePedidos.setRowCount(0)
        
        frmInicioProceso = False
        
        self.ui.lblCodigoCliente.setText(str(0))
        
        if balanzaSeleccionada == 1:
            codCliente1 = 0
            nombresCliBalanza1 = ""
        elif balanzaSeleccionada == 2:
            codCliente2 = 0
            nombresCliBalanza2 = ""
            
        self.ui.txtCodigoCliente.setHidden(False)
        self.ui.txtCodigoCliente.setText("")
        self.ui.txtCodigoCliente.setFocus(True)
        self.ui.lwListaClientes.setHidden(False)
        
    def fn_seleccionarEspecie(self,especie):
        global idEspecie
        global precioCliente
        global especieCli1
        global especieCli2
        global frmSeleccionarTipoTrozado
        
        self.ui.btnYugoVivo.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnTecnicoVivo.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnGallinaDoble.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnAhogados.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnGallo.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnPolloMaltratado.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnPolloXx.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnBrasaYugo.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnBrasaTecnico.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        self.ui.btnSecos.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        
        if especie == 1:
            self.ui.btnYugoVivo.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioPrimerEspecie
            idEspecie = primerEspecie
        elif especie == 3:
            self.ui.btnTecnicoVivo.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioTerceraEspecie
            idEspecie = terceraEspecie
        elif especie == 20:
            self.ui.btnGallinaDoble.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioVigesimaEspecie
            idEspecie = vigesimaEspecie
        elif especie == 21:
            self.ui.btnSecos.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioVigesimaPrimeraEspecie
            idEspecie = vigesimaPrimeraEspecie
        elif especie == 22:
            self.ui.btnGallo.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioVigesimaSegundaEspecie
            idEspecie = vigesimaSegundaEspecie
        elif especie == 23:
            self.ui.btnPolloMaltratado.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioVigesimaTerceraEspecie
            idEspecie = vigesimaTerceraEspecie
        elif especie == 19:
            self.ui.btnPolloXx.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioDecimaNovenaEspecie
            idEspecie = decimaNovenaEspecie
        elif especie == 17:
            self.ui.btnBrasaYugo.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioDecimaSeptimaEspecie
            idEspecie = decimaSeptimaEspecie
        elif especie == 18:
            self.ui.btnBrasaTecnico.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioDecimaOctavaEspecie
            idEspecie = decimaOctavaEspecie
        elif especie == 6:
            self.ui.btnAhogados.setStyleSheet("background-color: #2ABF4E; color: #fff")
            precioCliente = precioSextaEspecie
            idEspecie = sextaEspecie
            
        if balanzaSeleccionada == 1:
            especieCli1 = idEspecie
        elif balanzaSeleccionada == 2:
            especieCli2 = idEspecie
            
    def fn_seleccionarEspecieDescuento(self,especieDesc):
        global idEspecieDesc
        global precioClienteDesc
        global especieDesCli1
        global especieDesCli2
        global frmSeleccionarTipoTrozadoDesc
        
        self.ui.btnDescYugoVivo.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnDescTecnicoVivo.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnDescGallinaDoble.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnDescGallinaChica.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnDescGallo.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnDescPolloMaltratado.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        
        self.ui.btnDescPolloXx.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnDescBrasaYugo.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnDescPolloBrasaTecnico.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        
        if especieDesc == 1:
            self.ui.btnDescYugoVivo.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioPrimerEspecie
            idEspecieDesc = primerEspecie
        elif especieDesc == 3:
            self.ui.btnDescTecnicoVivo.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioTerceraEspecie
            idEspecieDesc = terceraEspecie
        elif especieDesc == 20:
            self.ui.btnDescGallinaDoble.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioVigesimaEspecie
            idEspecieDesc = vigesimaEspecie
        elif especieDesc == 21:
            self.ui.btnDescGallinaChica.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioVigesimaPrimeraEspecie
            idEspecieDesc = vigesimaPrimeraEspecie
        elif especieDesc == 22:
            self.ui.btnDescGallo.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioVigesimaSegundaEspecie
            idEspecieDesc = vigesimaSegundaEspecie
        elif especieDesc == 23:
            self.ui.btnDescPolloMaltratado.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioVigesimaTerceraEspecie
            idEspecieDesc = vigesimaTerceraEspecie
        elif especieDesc == 19:
            self.ui.btnDescPolloXx.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioDecimaNovenaEspecie
            idEspecieDesc = decimaNovenaEspecie
        elif especieDesc == 17:
            self.ui.btnDescBrasaYugo.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioDecimaSeptimaEspecie
            idEspecieDesc = decimaSeptimaEspecie
        elif especieDesc == 18:
            self.ui.btnDescPolloBrasaTecnico.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioClienteDesc = precioDecimaOctavaEspecie
            idEspecieDesc = decimaOctavaEspecie
            
        if balanzaSeleccionada == 1:
            especieDesCli1 = idEspecieDesc
        elif balanzaSeleccionada == 2:
            especieDesCli2 = idEspecieDesc
        
    def fn_verificarProceso(self):
        global numProceso
        
        numProceso = 0
        
        procesoActual = self.conexion.db_verificarProceso(codCliente)
            
        if(len(procesoActual) > 0 and codCliente != 0):
            numProceso = procesoActual[0][0]
        else:          
            if codCliente != 0 :  
                self.conexion.db_registrarProceso(codCliente)
                numVentaBase = self.conexion.db_obtieneUltimoIdProcesoRegistrado()
                numProceso = numVentaBase[0]
            
        self.ui.lblCodigoCliente.setText(str(codCliente))
        
    def fn_registrarPesada(self):
        global pesoNeto
        global cantidadRegistro
        global horaPeso
        global fechaPeso
        global cantidadPrimerColor
        global cantidadSegundoColor
        global cantidadTercerColor
        global cantidadCuartaColor
        global cantidadQuintoColor
        global cantidadSextoColor
        global cantidadSeptimoColor
        global pesoNetoJabas
        global observacionPes
        global precioCliente
        
        horaPeso = datetime.now().strftime('%H:%M:%S')
        fechaPeso = datetime.now().strftime('%Y-%m-%d')
        
        pesoNeto = float(self.ui.lblPesoIndicador.text())
        cantidadRegistro = int(self.ui.txtCantidadParaIngresar.text())
        
        observacionPes = ""

        if codCliente == 24 or codCliente == 69:
            observacionPes = self.ui.txtIngresaNombreVenta.text()
            precioClienteAnt = self.ui.txtIngresarPrecioVenta.text()
            if precioClienteAnt != "":
                precioCliente = self.ui.txtIngresarPrecioVenta.text()
        
        pesoExtrasPorGramos = cantidadRegistro * gramosExtras
        
        pesoNeto = pesoNeto + pesoExtrasPorGramos
        
        cantidadPrimerColor = 0
        cantidadSegundoColor = 0
        cantidadTercerColor = 0
        cantidadCuartaColor = 0
        cantidadQuintoColor = 0
        cantidadSextoColor = 0
        cantidadSeptimoColor = 0
        numeroJabasPes = 0
        pesoNetoJabas = 0
        
        colores = ['PrimerColor', 'SegundoColor', 'TercerColor', 'CuartoColor', 'QuintoColor', 'SextoColor', 'SeptimoColor']
        
        if (idEspecie == primerEspecie or idEspecie == decimaSextaEspecie) and pesoNeto > 110:
            self.ui.txtCantidadSegundoColor.setText("5")

        for color in colores:
            cantidad_color = getattr(self.ui, f"txtCantidad{color}").text()
            
            # Verificar si el campo está vacío y asignar 0 en ese caso
            if cantidad_color == "":
                cantidad_color = 0
            else:
                cantidad_color = int(cantidad_color)

            numeroJabasPes += cantidad_color
            
            if color == 'PrimerColor':
                pesoNetoJabas += (cantidad_color * pesoPrimerColor)
            elif color == 'SegundoColor':
                pesoNetoJabas += (cantidad_color * pesoSegundoColor)
            elif color == 'TercerColor':
                pesoNetoJabas += (cantidad_color * pesoTercerColor)
            elif color == 'CuartoColor':
                pesoNetoJabas += (cantidad_color * pesoCuartaColor)
            elif color == 'QuintoColor':
                pesoNetoJabas += (cantidad_color * pesoQuintoColor)
            elif color == 'SextoColor':
                pesoNetoJabas += (cantidad_color * pesoSextoColor)
            elif color == 'SeptimoColor':
                pesoNetoJabas += (cantidad_color * pesoSeptimoColor)
        
        if (idEspecie == primerEspecie or idEspecie == decimaSextaEspecie) and pesoNeto > 110:
            pesoNetoJabas += 39.5

        coloresJabas = " | ".join(f"{letra}{getattr(self.ui, f'txtCantidad{color}').text()}" if getattr(self.ui, f'txtCantidad{color}').text() != "" else f"{letra}0" for letra, color in zip("RCAVNDO", colores))
        
        self.conexion.db_registrarPesadas(numProceso,idEspecie,pesoNeto,horaPeso,codCliente,fechaPeso,cantidadRegistro,precioCliente,pesoNetoJabas,numeroJabasPes,numeroCubetasPes,estadoPeso,estadoWebPeso,tipoCubetas,coloresJabas,observacionPes)
        
        thread = threading.Thread(target=self.fn_pulsoLuzVerdeBuzzer)
        thread.start()
        inicioSistema.pesoBalanza1 = True
            
        observacionPes = ""  
        self.fn_desactivarGramosExtrasPorCantidad() 
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_actualizarPesadaColores(self):
        global cantidadPrimerColor
        global cantidadSegundoColor
        global cantidadTercerColor
        global cantidadCuartaColor
        global cantidadQuintoColor
        global cantidadSextoColor
        global cantidadSeptimoColor
        global pesoNetoJabas
        
        cantidadPrimerColor = 0
        cantidadSegundoColor = 0
        cantidadTercerColor = 0
        cantidadCuartaColor = 0
        cantidadQuintoColor = 0
        cantidadSextoColor = 0
        cantidadSeptimoColor = 0
        numeroJabasPes = 0
        pesoNetoJabas = 0
        
        colores = ['PrimerColor', 'SegundoColor', 'TercerColor', 'CuartoColor', 'QuintoColor', 'SextoColor', 'SeptimoColor']

        for color in colores:
            cantidad_color = getattr(self.ui, f"txtCantidad{color}").text()
            
            # Verificar si el campo está vacío y asignar 0 en ese caso
            if cantidad_color == "":
                cantidad_color = 0
            else:
                cantidad_color = int(cantidad_color)

            numeroJabasPes += cantidad_color
            
            if color == 'PrimerColor':
                pesoNetoJabas += (cantidad_color * pesoPrimerColor)
            elif color == 'SegundoColor':
                pesoNetoJabas += (cantidad_color * pesoSegundoColor)
            elif color == 'TercerColor':
                pesoNetoJabas += (cantidad_color * pesoTercerColor)
            elif color == 'CuartoColor':
                pesoNetoJabas += (cantidad_color * pesoCuartaColor)
            elif color == 'QuintoColor':
                pesoNetoJabas += (cantidad_color * pesoQuintoColor)
            elif color == 'SextoColor':
                pesoNetoJabas += (cantidad_color * pesoSextoColor)
            elif color == 'SeptimoColor':
                pesoNetoJabas += (cantidad_color * pesoSeptimoColor)

        coloresJabas = " | ".join(f"{letra}{getattr(self.ui, f'txtCantidad{color}').text()}" if getattr(self.ui, f'txtCantidad{color}').text() != "" else f"{letra}0" for letra, color in zip("RCAVNDO", colores))
        
        if (identificador == 'tb_pesadas'):
            respuesta = self.conexion.db_actualizarPesadaColores(idPesadaEditarOEliminar,numeroJabasPes,coloresJabas,pesoNetoJabas)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        elif (identificador == 'tb_pesadas2'):
            respuesta = self.conexion.db_actualizarPesadaColores2(idPesadaEditarOEliminar,numeroJabasPes,coloresJabas,pesoNetoJabas)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_registrarDescuento(self):
        global pesoNeto
        global cantidadRegistro
        global horaPeso
        global fechaPeso
        global coloresJabas
        
        horaPeso = datetime.now().strftime('%H:%M:%S')
        fechaPeso = datetime.now().strftime('%Y-%m-%d')
        
        pesoNeto = float(self.ui.lblPesoIndicador.text())*-1
        cantidadRegistro = int(self.ui.txtCantidadDescuento.text())*-1
        
        pesoExtrasPorGramos = cantidadRegistro * gramosExtras
        
        pesoNeto = pesoNeto + pesoExtrasPorGramos
        
        coloresJabas = "R0 | C0 | A0 | V0 | N0 | D0 | O0"
        self.conexion.db_registrarPesadas(numProceso,idEspecieDesc,pesoNeto,horaPeso,codCliente,fechaPeso,cantidadRegistro,precioClienteDesc,pesoNetoJabas,numeroJabasPes,numeroCubetasPes,estadoPeso,estadoWebPeso,tipoCubetas,coloresJabas,observacionPes)
        coloresJabas = ""
        
        thread = threading.Thread(target=self.fn_pulsoLuzVerdeBuzzer)
        thread.start()
        inicioSistema.pesoBalanza1 = True
            
        self.fn_desactivarGramosExtrasPorCantidad()        
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_registrarTara(self):        
        pesoNetoJabas = float(self.ui.txtPesoParaIngresarJabas.text())
        if (identificador == 'tb_pesadas'):
            respuesta = self.conexion.db_actualizarPesoJabas(pesoNetoJabas,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        elif (identificador == 'tb_pesadas2'):
            respuesta = self.conexion.db_actualizarPesoJabas2(pesoNetoJabas,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_editarCantidad(self):
        cantidadNueva = int(self.ui.txtCantidadParaIngresar.text())
        if (identificador == 'tb_pesadas'):
            respuesta = self.conexion.db_editarCantidadNueva(cantidadNueva,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        elif (identificador == 'tb_pesadas2'):
            respuesta = self.conexion.db_editarCantidadNueva2(cantidadNueva,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
            
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_editarCantidadTara(self):
        cantidadNueva = int(self.ui.txtCantidadParaIngresar.text())
        if (identificador == 'tb_pesadas'):
            respuesta = self.conexion.db_editarCantidadTaraNueva(cantidadNueva,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        elif (identificador == 'tb_pesadas2'):   
            respuesta = self.conexion.db_editarCantidadTaraNueva2(cantidadNueva,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_editarCantidadDescuento(self):
        cantidadNueva = int(self.ui.txtCantidadParaIngresar.text())*-1
        if (identificador == 'tb_pesadas'):
            respuesta = self.conexion.db_editarCantidadDescuentoNueva(cantidadNueva,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        elif (identificador == 'tb_pesadas2'):   
            respuesta = self.conexion.db_editarCantidadDescuentoNueva2(cantidadNueva,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_eliminarUltimaCantidad(self):
        if (identificador == 'tb_pesadas'):
            respuesta = self.conexion.db_eliminarUltimaCantidad(idPesadaEditarOEliminar)    
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL ELIMINAR!",error,"Error al eliminar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡ELIMINADO EXITOSO!",correcto,"El registro se elimino correctamente.",2000)
        elif (identificador == 'tb_pesadas2'):
            respuesta = self.conexion.db_eliminarUltimaCantidad2(idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL ELIMINAR!",error,"Error al eliminar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡ELIMINADO EXITOSO!",correcto,"El registro se elimino correctamente.",2000)
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_listarVenta(self):
        global frmInicioProceso
        global listoParaAccionar
        global pesoKgPechuga
        global pesoKgPierna
        global pesoKgAlas
        global pesoKgMenudencia
        global pesoKgDorso
        global pesoKgOtros
        
        tablaDePesos = self.ui.tblDetallePesadas
        tablaDePesos.clearContents()
        tablaDePesos.setRowCount(0)
        
        totalPesoPrimerEspecie = 0
        totalPesoSegundaEspecie = 0
        totalPesoTerceraEspecie = 0
        totalPesoCuartaEspecie = 0
        totalPesoQuintaEspecie = 0
        totalPesoSextaEspecie = 0
        totalPesoSeptimaEspecie = 0
        totalPesoOctavaEspecie = 0
        totalPesoDecimaSextaEspecie = 0
        totalPesoDecimaSeptimaEspecie = 0
        totalPesoDecimaOctavaEspecie = 0
        totalPesoDecimaNovenaEspecie = 0
        
        pesoKgPechugaSecun = 0.00
        pesoKgPiernaSecun = 0.00
        pesoKgAlasSecun = 0.00
        pesoKgMenudenciaSecun = 0.00
        pesoKgDorsoSecun = 0.00
        pesoKgOtrosSecun = 0.00
        
        totalCantidadTotalEspecies = 0
        
        totalCantidadPrimerEspecie = 0
        totalCantidadSegundaEspecie = 0
        totalCantidadTerceraEspecie = 0
        totalCantidadCuartaEspecie = 0
        totalCantidadQuintaEspecie = 0
        totalCantidadSextaEspecie = 0
        totalCantidadSeptimaEspecie = 0
        totalCantidadOctavaEspecie = 0
        totalCantidadNovenaEspecie = 0
        totalCantidadDecimaSextaEspecie = 0
        totalCantidadDecimaSeptimaEspecie = 0
        totalCantidadDecimaOctavaEspecie = 0
        totalCantidadDecimaNovenaEspecie = 0
        
        totalDeJabas = 0
        
        frmInicioProceso = False
        listoParaAccionar = False
        
        if codCliente != 0:
            pesosListarTabla = self.conexion.db_listarPesosTabla(numProceso,codCliente)
            
            frmInicioProceso = True
            
            if pesosListarTabla != "" and pesosListarTabla != None:
            
                if len(pesosListarTabla) > 0:
                    
                    listoParaAccionar = True
                
                    for row_number, row_data in enumerate(pesosListarTabla):
                        
                            tablaDePesos.insertRow(row_number)
                            
                            for column_number, data in enumerate(row_data):
                                
                                if column_number == 1:
                                    if row_data[15] != "":
                                        data = row_data[1] +" ( "+ row_data[15].upper() +" )"
                                
                                if column_number == 0:  # Columna de "correlativo"
                                    data = (row_number - len(pesosListarTabla))*-1
                                # if column_number == 4:  # Columna de "pesoNetoPesBruto"
                                #     data = "{:.2f} Kg".format(data)
                                if column_number == 7:  # Columna de "pesoNetoPes"
                                    data = "{:.2f}".format(data)
                                if column_number == 6:  # Columna de "pesoNetoJabas"
                                    data = "{:.2f}".format(data)
                                if column_number == 10 :  # Columna de "horaPes"
                                    hours, remainder = divmod(data.seconds, 3600)
                                    minutes, seconds = divmod(remainder, 60)
                                    data = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
                                    
                                if column_number == 7 : # Columna de "peso"
                                    if row_data[7] > 0 :
                                        data = row_data[7] - row_data[14]
                                    else:
                                        data = row_data[7] + row_data[14]
                                
                                # if column_number == 2 and row_data[2] is None and row_data[6] > 0: # Columna de "Promedio"
                                #     data = (row_data[5] / row_data[9])*-1
                                    
                                if column_number == 3 and row_data[11] == 1: # Columna de "idEspecie" y columna de "estadoPes"
                                    if data == nombrePrimerEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoPrimerEspecie += (row_data[5]-row_data[14]) # Columna de "pesoNetoPes"
                                        else:
                                            totalPesoPrimerEspecie += (row_data[5]+row_data[14]) # Columna de "pesoNetoPes"
                                        
                                        totalCantidadPrimerEspecie += row_data[4] # Columna de "cantidadPes"  
                                    elif data == nombreSegundaEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoSegundaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoSegundaEspecie += (row_data[5]+row_data[14])
                                        
                                        totalCantidadSegundaEspecie += row_data[4]
                                    elif data == nombreTerceraEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoTerceraEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoTerceraEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadTerceraEspecie += row_data[4]
                                    elif data == nombreCuartaEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoCuartaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoCuartaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadCuartaEspecie += row_data[4]
                                    elif data == nombreVigesimaEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoQuintaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoQuintaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadQuintaEspecie += row_data[4]
                                    elif data == nombreSextaEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoSextaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoSextaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadSextaEspecie += row_data[4]
                                    elif data == nombreVigesimaPrimeraEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoDecimaNovenaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoDecimaNovenaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadDecimaNovenaEspecie += row_data[4]
                                    elif data == nombreVigesimaSegundaEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoSeptimaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoSeptimaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadSeptimaEspecie += row_data[4]
                                    elif data == nombreVigesimaTerceraEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoOctavaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoOctavaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadOctavaEspecie += row_data[4]
                                    elif data == nombreDecimaNovenaEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoDecimaSextaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoDecimaSextaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadDecimaSextaEspecie += row_data[4]
                                    elif data == nombreDecimaSeptimaEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoDecimaSeptimaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoDecimaSeptimaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadDecimaSeptimaEspecie += row_data[4]
                                    elif data == nombreDecimaOctavaEspecie:
                                        if row_data[5] > 0 :
                                            totalPesoDecimaOctavaEspecie += (row_data[5]-row_data[14])
                                        else:
                                            totalPesoDecimaOctavaEspecie += (row_data[5]+row_data[14])
                                            
                                        totalCantidadDecimaOctavaEspecie += row_data[4]
                                        
                                    if data == nombreDecimaEspecie or data == nombreDecimaPrimeraEspecie or data == nombreDecimaSegundaEspecie or data == nombreDecimaTerceraEspecie or data == nombreDecimaCuartaEspecie or data == nombreDecimaQuintaOtrasEspecies:
                                        totalCantidadNovenaEspecie += row_data[4]
                                        
                                    if data == nombreDecimaEspecie:
                                        if row_data[5] > 0 :
                                            pesoKgPechugaSecun += float(row_data[5] - row_data[14])
                                        else:
                                            pesoKgPechugaSecun += float(row_data[5] + row_data[14])
                                    elif data == nombreDecimaPrimeraEspecie:
                                        if row_data[5] > 0 :
                                            pesoKgPiernaSecun += float(row_data[5] - row_data[14])
                                        else:
                                            pesoKgPiernaSecun += float(row_data[5] + row_data[14])
                                    elif data == nombreDecimaSegundaEspecie:
                                        if row_data[5] > 0 :
                                            pesoKgAlasSecun += float(row_data[5] - row_data[14])
                                        else:
                                            pesoKgAlasSecun += float(row_data[5] + row_data[14])
                                    elif data == nombreDecimaTerceraEspecie:
                                        if row_data[5] > 0 :
                                            pesoKgMenudenciaSecun += float(row_data[5] - row_data[14])
                                        else:
                                            pesoKgMenudenciaSecun += float(row_data[5] + row_data[14])
                                    elif data == nombreDecimaCuartaEspecie:
                                        if row_data[5] > 0 :
                                            pesoKgDorsoSecun += float(row_data[5] - row_data[14])
                                        else:
                                            pesoKgDorsoSecun += float(row_data[5] + row_data[14])
                                    elif data == nombreDecimaQuintaOtrasEspecies:
                                        if row_data[5] > 0 :
                                            pesoKgOtrosSecun += float(row_data[5] - row_data[14])
                                        else:
                                            pesoKgOtrosSecun += float(row_data[5] + row_data[14])
                                    
                                    totalCantidadTotalEspecies += row_data[4]
                                    
                                item = QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                tablaDePesos.setItem(row_number, column_number, item)

                                if column_number == 9:  # Columna de "letras"
                                    if data == "":
                                        data = "R0 | C0 | A0 | V0 | N0 | D0 | O0"
                                        letras = data.split(' | ')
                                        color_column = column_number

                                        letras_widget = LetrasWidget(letras)

                                        item = QTableWidgetItem()
                                        tablaDePesos.setItem(row_number, color_column, item)
                                        tablaDePesos.setCellWidget(row_number, color_column, letras_widget)
                                
                                        # Después de insertar filas y configurar elementos
                                        tablaDePesos.resizeRowsToContents()
                                    else:
                                        letras = data.split(' | ')
                                        color_column = column_number

                                        letras_widget = LetrasWidget(letras)

                                        item = QTableWidgetItem()
                                        tablaDePesos.setItem(row_number, color_column, item)
                                        tablaDePesos.setCellWidget(row_number, color_column, letras_widget)
                                
                                        # Después de insertar filas y configurar elementos
                                        tablaDePesos.resizeRowsToContents()
                            
                                if column_number == 8:
                                    if row_data[8] > 0:
                                        totalDeJabas += row_data[8]
                                
                            if (row_data[11] == 0):
                                self.fn_pintarCeldasRegistrosEliminados(row_number)
                            
        pesoKgPechuga = pesoKgPechugaSecun
        pesoKgPierna = pesoKgPiernaSecun
        pesoKgAlas = pesoKgAlasSecun
        pesoKgMenudencia = pesoKgMenudenciaSecun
        pesoKgDorso = pesoKgDorsoSecun
        pesoKgOtros = pesoKgOtrosSecun
        
        self.ui.txtCantJabasTotales.setText("{} {}".format(totalDeJabas, "Ud." if totalDeJabas == 1 else "Uds."))
                            
        self.ui.lblKgYugoVivo.setText("{:.2f} Kg".format(totalPesoPrimerEspecie))
        self.ui.lblKgTecnicoVivo.setText("{:.2f} Kg".format(totalPesoTerceraEspecie))
        self.ui.lblKgGallinaDoble.setText("{:.2f} Kg".format(totalPesoQuintaEspecie))
        self.ui.lblKgAhogados.setText("{:.2f} Kg".format(totalPesoSextaEspecie))
        self.ui.lblKgGallo.setText("{:.2f} Kg".format(totalPesoSeptimaEspecie))
        self.ui.lblKgPolloMaltratado.setText("{:.2f} Kg".format(totalPesoOctavaEspecie))
        self.ui.lblKgPolloXx.setText("{:.2f} Kg".format(totalPesoDecimaSextaEspecie))
        self.ui.lblKgBrasaYugo.setText("{:.2f} Kg".format(totalPesoDecimaSeptimaEspecie))
        self.ui.lblKgBrasaTecnico.setText("{:.2f} Kg".format(totalPesoDecimaOctavaEspecie))
        self.ui.lblKgSecos.setText("{:.2f} Kg".format(totalPesoDecimaNovenaEspecie))
        
        self.ui.txtCantPolloTotales.setText("{} {}".format(totalCantidadTotalEspecies, "Ud." if totalCantidadTotalEspecies == 1 else "Uds."))
        
        self.ui.txtCantYugoVivo.setText("{} {}".format(totalCantidadPrimerEspecie, "Ud." if totalCantidadPrimerEspecie == 1 else "Uds."))
        self.ui.txtCantTecnicoVivo.setText("{} {}".format(totalCantidadTerceraEspecie, "Ud." if totalCantidadTerceraEspecie == 1 else "Uds."))
        self.ui.txtCantGallinaDoble.setText("{} {}".format(totalCantidadQuintaEspecie, "Ud." if totalCantidadQuintaEspecie == 1 else "Uds."))
        self.ui.txtCantAhogados.setText("{} {}".format(totalCantidadSextaEspecie, "Ud." if totalCantidadSextaEspecie == 1 else "Uds."))
        self.ui.txtCantGallo.setText("{} {}".format(totalCantidadSeptimaEspecie, "Ud." if totalCantidadSeptimaEspecie == 1 else "Uds."))
        self.ui.txtCantPolloMaltratado.setText("{} {}".format(totalCantidadOctavaEspecie, "Ud." if totalCantidadOctavaEspecie == 1 else "Uds."))
        self.ui.txtCantPolloXx.setText("{} {}".format(totalCantidadDecimaSextaEspecie, "Ud." if totalCantidadDecimaSextaEspecie == 1 else "Uds."))
        self.ui.txtCantBrasaYugo.setText("{} {}".format(totalCantidadDecimaSeptimaEspecie, "Ud." if totalCantidadDecimaSeptimaEspecie == 1 else "Uds."))
        self.ui.txtCantBrasaTecnico.setText("{} {}".format(totalCantidadDecimaOctavaEspecie, "Ud." if totalCantidadDecimaOctavaEspecie == 1 else "Uds."))
        self.ui.txtCantSecos.setText("{} {}".format(totalCantidadDecimaNovenaEspecie, "Ud." if totalCantidadDecimaNovenaEspecie == 1 else "Uds."))
                            
    def fn_pintarCeldasRegistrosEliminados(self, row):
        tablaDePesos = self.ui.tblDetallePesadas
        for e in range(tablaDePesos.columnCount()):
            item = tablaDePesos.item(row, e)
            item.setBackground(QColor(255, 51, 51))
            item.setForeground(QColor(255, 255, 255))
            
    def fn_imprimirReporte(self):
        global arreglo_id_reporte
        global imprimePrecio
        global diccionarioResponsablesDeEnvio

        datosTicket = self.conexion.db_traerDatosReporte(numProceso,codCliente)
        
        reporteTotalCantidadPrimerEspecie = 0
        reporteTotalCantidadSegundaEspecie = 0
        reporteTotalCantidadTerceraEspecie = 0
        reporteTotalCantidadCuartaEspecie = 0
        reporteTotalCantidadQuintaEspecie = 0
        reporteTotalCantidadSextaEspecie = 0
        reporteTotalCantidadSeptimaEspecie = 0
        reporteTotalCantidadOctavaEspecie = 0
        reporteTotalCantidadDecimaEspecie = 0
        reporteTotalCantidadDecimaPrimeraEspecie = 0
        reporteTotalCantidadDecimaSegundaEspecie = 0
        reporteTotalCantidadDecimaTerceraEspecie = 0
        reporteTotalCantidadDecimaCuartaEspecie = 0
        reporteTotalCantidadDecimaQuintaEspecie = 0
        reporteTotalCantidadDecimaSextaEspecie = 0
        reporteTotalCantidadDecimaSeptimaEspecie = 0
        reporteTotalCantidadDecimaOctavaEspecie = 0
        reporteTotalCantidadDecimaNovenaEspecie = 0
        reporteTotalCantidadVigesimaEspecie = 0
        reporteTotalCantidadVigesimaPrimeraEspecie = 0
        reporteTotalCantidadVigesimaSegundaEspecie = 0
        reporteTotalCantidadVigesimaTerceraEspecie = 0
        
        reporteTotalPesoPrimerEspecie = 0
        reporteTotalPesoSegundaEspecie = 0
        reporteTotalPesoTerceraEspecie = 0
        reporteTotalPesoCuartaEspecie = 0
        reporteTotalPesoQuintaEspecie = 0
        reporteTotalPesoSextaEspecie = 0
        reporteTotalPesoSeptimaEspecie = 0
        reporteTotalPesoOctavaEspecie = 0
        reporteTotalPesoDecimaEspecie = 0
        reporteTotalPesoDecimaPrimeraEspecie = 0
        reporteTotalPesoDecimaSegundaEspecie = 0
        reporteTotalPesoDecimaTerceraEspecie = 0
        reporteTotalPesoDecimaCuartaEspecie = 0
        reporteTotalPesoDecimaQuintaEspecie = 0
        reporteTotalPesoDecimaSextaEspecie = 0
        reporteTotalPesoDecimaSeptimaEspecie = 0
        reporteTotalPesoDecimaOctavaEspecie = 0
        reporteTotalPesoDecimaNovenaEspecie = 0
        reporteTotalPesoVigesimaEspecie = 0
        reporteTotalPesoVigesimaPrimeraEspecie = 0
        reporteTotalPesoVigesimaSegundaEspecie = 0
        reporteTotalPesoVigesimaTerceraEspecie = 0
        
        reporteTotalPesoPrimerEspecieBruto = 0
        reporteTotalPesoSegundaEspecieBruto = 0
        reporteTotalPesoTerceraEspecieBruto = 0
        reporteTotalPesoCuartaEspecieBruto = 0
        reporteTotalPesoQuintaEspecieBruto = 0
        reporteTotalPesoSextaEspecieBruto = 0
        reporteTotalPesoSeptimaEspecieBruto = 0
        reporteTotalPesoOctavaEspecieBruto = 0
        reporteTotalPesoDecimaEspecieBruto = 0
        reporteTotalPesoDecimaPrimeraEspecieBruto = 0
        reporteTotalPesoDecimaSegundaEspecieBruto = 0
        reporteTotalPesoDecimaTerceraEspecieBruto = 0
        reporteTotalPesoDecimaCuartaEspecieBruto = 0
        reporteTotalPesoDecimaQuintaEspecieBruto = 0
        reporteTotalPesoDecimaSextaEspecieBruto = 0
        reporteTotalPesoDecimaSeptimaEspecieBruto = 0
        reporteTotalPesoDecimaOctavaEspecieBruto = 0
        reporteTotalPesoDecimaNovenaEspecieBruto = 0
        reporteTotalPesoVigesimaEspecieBruto = 0
        reporteTotalPesoVigesimaPrimeraEspecieBruto = 0
        reporteTotalPesoVigesimaSegundaEspecieBruto = 0
        reporteTotalPesoVigesimaTerceraEspecieBruto = 0
        
        reporteTotalPesoTaraPrimerEspecie = 0
        reporteTotalPesoTaraSegundaEspecie = 0
        reporteTotalPesoTaraTerceraEspecie = 0
        reporteTotalPesoTaraCuartaEspecie = 0
        reporteTotalPesoTaraQuintaEspecie = 0
        reporteTotalPesoTaraSextaEspecie = 0
        reporteTotalPesoTaraSeptimaEspecie = 0
        reporteTotalPesoTaraOctavaEspecie = 0
        reporteTotalPesoTaraDecimaEspecie = 0
        reporteTotalPesoTaraDecimaPrimeraEspecie = 0
        reporteTotalPesoTaraDecimaSegundaEspecie = 0
        reporteTotalPesoTaraDecimaTerceraEspecie = 0
        reporteTotalPesoTaraDecimaCuartaEspecie = 0
        reporteTotalPesoTaraDecimaQuintaEspecie = 0
        reporteTotalPesoTaraDecimaSextaEspecie = 0
        reporteTotalPesoTaraDecimaSeptimaEspecie = 0
        reporteTotalPesoTaraDecimaOctavaEspecie = 0
        reporteTotalPesoTaraDecimaNovenaEspecie = 0
        reporteTotalPesoTaraVigesimaEspecie = 0
        reporteTotalPesoTaraVigesimaPrimeraEspecie = 0
        reporteTotalPesoTaraVigesimaSegundaEspecie = 0
        reporteTotalPesoTaraVigesimaTerceraEspecie = 0
        
        reporteTotalPrecioPrimerEspecie = 0
        reporteTotalPrecioSegundaEspecie = 0
        reporteTotalPrecioTerceraEspecie = 0
        reporteTotalPrecioCuartaEspecie = 0
        reporteTotalPrecioQuintaEspecie = 0
        reporteTotalPrecioSextaEspecie = 0
        reporteTotalPrecioSeptimaEspecie = 0
        reporteTotalPrecioOctavaEspecie = 0
        reporteTotalPrecioDecimaEspecie = 0
        reporteTotalPrecioDecimaPrimeraEspecie = 0
        reporteTotalPrecioDecimaSegundaEspecie = 0
        reporteTotalPrecioDecimaTerceraEspecie = 0
        reporteTotalPrecioDecimaCuartaEspecie = 0
        reporteTotalPrecioDecimaQuintaEspecie = 0
        reporteTotalPrecioDecimaSextaEspecie = 0
        reporteTotalPrecioDecimaSeptimaEspecie = 0
        reporteTotalPrecioDecimaOctavaEspecie = 0
        reporteTotalPrecioDecimaNovenaEspecie = 0
        reporteTotalPrecioVigesimaEspecie = 0
        reporteTotalPrecioVigesimaPrimeraEspecie = 0
        reporteTotalPrecioVigesimaSegundaEspecie = 0
        reporteTotalPrecioVigesimaTerceraEspecie = 0
        
        contarDescuentos = 0
        contarJabas = 0
            
        try:
            # p = Network(ipImpresora)
            file = open("ArchivosDeTexto/reporte.txt", "w") 

            # Enviar comandos ESC/POS para configurar el tamaño de la fuente
            # p.set(align='left', font='b')
            
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            
            if (incluyeEnvio == True):
                # p.set(align='center', font='b')
                file.write("ENVIO NUMERO : "+str(numeroEnvio)+" \n")
                file.write("\n")
                file.write("\n")
                # p.set(align='left', font='b')
            
            file.write("FECHA : "+fechaPeso+"   HORA : "+horaPeso+"\n")
            if (codCliente == 24):
                valor_extra = valores_individuales_pesadas[0]
                tablaDePesos = self.ui.tblDetallePesadas
                totalFilas = tablaDePesos.rowCount()
                valor_extra = totalFilas - valor_extra
                nombre_valor_extra = tablaDePesos.item(valor_extra, 1).text()
                if(len(arreglo_id_reporte)> 1):
                    file.write("CLIENTE :  "+str(self.ui.txtNombreCliente.text())+" \n")
                else:
                    file.write("CLIENTE :  "+str(nombre_valor_extra)+" \n")
            else:
                file.write("CLIENTE :  "+str(self.ui.txtNombreCliente.text())+" \n")
            file.write("\n")
            file.write("{:<15}{:<9}{:<10}{:<6}\n".format("PRODUCTO", "CANT", "KG.", "TARA."))
            file.write("========================================\n")
            
            last_responsable = None 
            
            for idx, item in enumerate(datosTicket, start=1):
                reporteEspecie = item[0]
                reportePeso = item[1]
                reporteCantidad = item[2]
                reportePrecio = item[3]
                reporteJabas = item[4]
                reporteJabasPeso = item[5]
                numeroCubetasPes = item[6]
                
                idPesada = item[8]
                idIdentificadorTabla = item[9]
                
                for dato in arreglo_id_reporte:
                    
                    variable = f"{{'{idIdentificadorTabla}': '{idPesada}'}}"
                    variable = ast.literal_eval(variable)
                    
                    if dato == variable:
                        
                        if incluyeResponsable:
                            for responsable in diccionarioResponsablesDeEnvio:
                                rango_inicio, rango_fin = map(int, responsable['rango'].split('-'))
                                if rango_inicio <= idx <= rango_fin:
                                    if responsable['responsable'] != last_responsable:
                                        file.write("Responsable: {}\n".format(responsable['responsable']))
                                        last_responsable = responsable['responsable']
                                    break
                    
                        if reportePeso < 0:
                            contarDescuentos += 1
                            
                        if reporteJabas > 0 or numeroCubetasPes > 0:
                            contarJabas += 1
                        
                        if (reporteEspecie == nombrePrimerEspecie) and reportePeso > 0 :
                            reporteTotalCantidadPrimerEspecie += reporteCantidad
                            reporteTotalPesoPrimerEspecieBruto += reportePeso
                            reporteTotalPesoTaraPrimerEspecie += reporteJabasPeso
                            reporteTotalPrecioPrimerEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("YUGO VIVO", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreSegundaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadSegundaEspecie += reporteCantidad
                            reporteTotalPesoSegundaEspecieBruto += reportePeso
                            reporteTotalPesoTaraSegundaEspecie += reporteJabasPeso
                            reporteTotalPrecioSegundaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("YUGO PELADO", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreTerceraEspecie) and reportePeso > 0 :
                            reporteTotalCantidadTerceraEspecie += reporteCantidad
                            reporteTotalPesoTerceraEspecieBruto += reportePeso
                            reporteTotalPesoTaraTerceraEspecie += reporteJabasPeso
                            reporteTotalPrecioTerceraEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("TEC. VIVO", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreCuartaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadCuartaEspecie += reporteCantidad
                            reporteTotalPesoCuartaEspecieBruto += reportePeso
                            reporteTotalPesoTaraCuartaEspecie += reporteJabasPeso
                            reporteTotalPrecioCuartaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("TEC. PELADO", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreQuintaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadQuintaEspecie += reporteCantidad
                            reporteTotalPesoQuintaEspecieBruto += reportePeso
                            reporteTotalPesoTaraQuintaEspecie += reporteJabasPeso
                            reporteTotalPrecioQuintaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLINA DB", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreSextaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadSextaEspecie += reporteCantidad
                            reporteTotalPesoSextaEspecieBruto += reportePeso
                            reporteTotalPesoTaraSextaEspecie += reporteJabasPeso
                            reporteTotalPrecioSextaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("AHOGADOS", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreSeptimaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadSeptimaEspecie += reporteCantidad
                            reporteTotalPesoSeptimaEspecieBruto += reportePeso
                            reporteTotalPesoTaraSeptimaEspecie += reporteJabasPeso
                            reporteTotalPrecioSeptimaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLO", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreOctavaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadOctavaEspecie += reporteCantidad
                            reporteTotalPesoOctavaEspecieBruto += reportePeso
                            reporteTotalPesoTaraOctavaEspecie += reporteJabasPeso
                            reporteTotalPrecioOctavaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("MALTRATADO", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaEspecie += reporteCantidad
                            reporteTotalPesoDecimaEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("PECHUGA", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaPrimeraEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaPrimeraEspecie += reporteCantidad
                            reporteTotalPesoDecimaPrimeraEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaPrimeraEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaPrimeraEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("PIERNA", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaSegundaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaSegundaEspecie += reporteCantidad
                            reporteTotalPesoDecimaSegundaEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaSegundaEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaSegundaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("ALAS", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaTerceraEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaTerceraEspecie += reporteCantidad
                            reporteTotalPesoDecimaTerceraEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaTerceraEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaTerceraEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("MENUDENCIA", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaCuartaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaCuartaEspecie += reporteCantidad
                            reporteTotalPesoDecimaCuartaEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaCuartaEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaCuartaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLINA CH", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaQuintaOtrasEspecies) and reportePeso > 0 :
                            reporteTotalCantidadDecimaQuintaEspecie += reporteCantidad
                            reporteTotalPesoDecimaQuintaEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaQuintaEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaQuintaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("OTROS", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaSextaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaSextaEspecie += reporteCantidad
                            reporteTotalPesoDecimaSextaEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaSextaEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaSextaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("POLLO XX", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaSeptimaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaSeptimaEspecie += reporteCantidad
                            reporteTotalPesoDecimaSeptimaEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaSeptimaEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaSeptimaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("BRASA YUGO", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaOctavaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaOctavaEspecie += reporteCantidad
                            reporteTotalPesoDecimaOctavaEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaOctavaEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaOctavaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("BRASA TEC.", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreDecimaNovenaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadDecimaNovenaEspecie += reporteCantidad
                            reporteTotalPesoDecimaNovenaEspecieBruto += reportePeso
                            reporteTotalPesoTaraDecimaNovenaEspecie += reporteJabasPeso
                            reporteTotalPrecioDecimaNovenaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("POLLO XX V", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreVigesimaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadVigesimaEspecie += reporteCantidad
                            reporteTotalPesoVigesimaEspecieBruto += reportePeso
                            reporteTotalPesoTaraVigesimaEspecie += reporteJabasPeso
                            reporteTotalPrecioVigesimaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLINA DB V", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreVigesimaPrimeraEspecie) and reportePeso > 0 :
                            reporteTotalCantidadVigesimaPrimeraEspecie += reporteCantidad
                            reporteTotalPesoVigesimaPrimeraEspecieBruto += reportePeso
                            reporteTotalPesoTaraVigesimaPrimeraEspecie += reporteJabasPeso
                            reporteTotalPrecioVigesimaPrimeraEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("SECOS", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreVigesimaSegundaEspecie) and reportePeso > 0 :
                            reporteTotalCantidadVigesimaSegundaEspecie += reporteCantidad
                            reporteTotalPesoVigesimaSegundaEspecieBruto += reportePeso
                            reporteTotalPesoTaraVigesimaSegundaEspecie += reporteJabasPeso
                            reporteTotalPrecioVigesimaSegundaEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLO VIVO", reporteCantidad, reportePeso, reporteJabasPeso))
                        elif (reporteEspecie == nombreVigesimaTerceraEspecie) and reportePeso > 0 :
                            reporteTotalCantidadVigesimaTerceraEspecie += reporteCantidad
                            reporteTotalPesoVigesimaTerceraEspecieBruto += reportePeso
                            reporteTotalPesoTaraVigesimaTerceraEspecie += reporteJabasPeso
                            reporteTotalPrecioVigesimaTerceraEspecie += reportePrecio * (reportePeso - reporteJabasPeso)
                            file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLINA CH", reporteCantidad, reportePeso, reporteJabasPeso))
                    
            if contarDescuentos > 0 :
                
                file.write("\n")
                file.write("DESCUENTOS :\n")
                file.write("========================================\n")
                
                for item in datosTicket:
                    reporteEspecie = item[0]
                    reportePeso = item[1]
                    reporteCantidad = item[2]
                    reportePrecio = item[3]
                    reporteJabas = item[4]
                    reporteJabasPeso = item[5]
                    numeroCubetasPes = item[6]
                    
                    idPesada = item[8]
                    idIdentificadorTabla = item[9]
                    
                    for dato in arreglo_id_reporte:
                        
                        variable = f"{{'{idIdentificadorTabla}': '{idPesada}'}}"
                        variable = ast.literal_eval(variable)
                        
                        if dato == variable:
                            
                            if (reporteEspecie == nombrePrimerEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadPrimerEspecie += reporteCantidad
                                reporteTotalPesoPrimerEspecieBruto += reportePeso
                                reporteTotalPesoTaraPrimerEspecie -= reporteJabasPeso
                                reporteTotalPrecioPrimerEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("YUGO VIVO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreSegundaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadSegundaEspecie += reporteCantidad
                                reporteTotalPesoSegundaEspecieBruto += reportePeso
                                reporteTotalPesoTaraSegundaEspecie -= reporteJabasPeso
                                reporteTotalPrecioSegundaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("YUGO PELADO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreTerceraEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadTerceraEspecie += reporteCantidad
                                reporteTotalPesoTerceraEspecieBruto += reportePeso
                                reporteTotalPesoTaraTerceraEspecie -= reporteJabasPeso
                                reporteTotalPrecioTerceraEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("TEC. VIVO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreCuartaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadCuartaEspecie += reporteCantidad
                                reporteTotalPesoCuartaEspecieBruto += reportePeso
                                reporteTotalPesoTaraCuartaEspecie -= reporteJabasPeso
                                reporteTotalPrecioCuartaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("TEC. PELADO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreQuintaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadQuintaEspecie += reporteCantidad
                                reporteTotalPesoQuintaEspecieBruto += reportePeso
                                reporteTotalPesoTaraQuintaEspecie -= reporteJabasPeso
                                reporteTotalPrecioQuintaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLINA DB", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreSextaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadSextaEspecie += reporteCantidad
                                reporteTotalPesoSextaEspecieBruto += reportePeso
                                reporteTotalPesoTaraSextaEspecie -= reporteJabasPeso
                                reporteTotalPrecioSextaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("AHOGADOS", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreSeptimaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadSeptimaEspecie += reporteCantidad
                                reporteTotalPesoSeptimaEspecieBruto += reportePeso
                                reporteTotalPesoTaraSeptimaEspecie -= reporteJabasPeso
                                reporteTotalPrecioSeptimaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreOctavaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadOctavaEspecie += reporteCantidad
                                reporteTotalPesoOctavaEspecieBruto += reportePeso
                                reporteTotalPesoTaraOctavaEspecie -= reporteJabasPeso
                                reporteTotalPrecioOctavaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("MALTRATADO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaEspecie += reporteCantidad
                                reporteTotalPesoDecimaEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("PECHUGA", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaPrimeraEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaPrimeraEspecie += reporteCantidad
                                reporteTotalPesoDecimaPrimeraEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaPrimeraEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaPrimeraEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("PIERNA", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaSegundaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaSegundaEspecie += reporteCantidad
                                reporteTotalPesoDecimaSegundaEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaSegundaEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaSegundaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("ALAS", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaTerceraEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaTerceraEspecie += reporteCantidad
                                reporteTotalPesoDecimaTerceraEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaTerceraEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaTerceraEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("MENUDENCIA", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaCuartaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaCuartaEspecie += reporteCantidad
                                reporteTotalPesoDecimaCuartaEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaCuartaEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaCuartaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLINA CH", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaQuintaOtrasEspecies) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaQuintaEspecie += reporteCantidad
                                reporteTotalPesoDecimaQuintaEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaQuintaEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaQuintaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("OTROS", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaSextaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaSextaEspecie += reporteCantidad
                                reporteTotalPesoDecimaSextaEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaSextaEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaSextaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("POLLO XX", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaSeptimaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaSeptimaEspecie += reporteCantidad
                                reporteTotalPesoDecimaSeptimaEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaSeptimaEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaSeptimaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("BRASA YUGO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreDecimaOctavaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaOctavaEspecie += reporteCantidad
                                reporteTotalPesoDecimaOctavaEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaOctavaEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaOctavaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("BRASA TEC.", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))  
                            elif (reporteEspecie == nombreDecimaNovenaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadDecimaNovenaEspecie += reporteCantidad
                                reporteTotalPesoDecimaNovenaEspecieBruto += reportePeso
                                reporteTotalPesoTaraDecimaNovenaEspecie -= reporteJabasPeso
                                reporteTotalPrecioDecimaNovenaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("POLLO XX V", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreVigesimaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadVigesimaEspecie += reporteCantidad
                                reporteTotalPesoVigesimaEspecieBruto += reportePeso
                                reporteTotalPesoTaraVigesimaEspecie -= reporteJabasPeso
                                reporteTotalPrecioVigesimaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLINA DB V", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreVigesimaPrimeraEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadVigesimaPrimeraEspecie += reporteCantidad
                                reporteTotalPesoVigesimaPrimeraEspecieBruto += reportePeso
                                reporteTotalPesoTaraVigesimaPrimeraEspecie -= reporteJabasPeso
                                reporteTotalPrecioVigesimaPrimeraEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("SECOS", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))
                            elif (reporteEspecie == nombreVigesimaSegundaEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadVigesimaSegundaEspecie += reporteCantidad
                                reporteTotalPesoVigesimaSegundaEspecieBruto += reportePeso
                                reporteTotalPesoTaraVigesimaSegundaEspecie -= reporteJabasPeso
                                reporteTotalPrecioVigesimaSegundaEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLO VIVO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))                      
                            elif (reporteEspecie == nombreVigesimaTerceraEspecie) and reportePeso < 0 and reporteJabas == 0:
                                reporteTotalCantidadVigesimaTerceraEspecie += reporteCantidad
                                reporteTotalPesoVigesimaTerceraEspecieBruto += reportePeso
                                reporteTotalPesoTaraVigesimaTerceraEspecie -= reporteJabasPeso
                                reporteTotalPrecioVigesimaTerceraEspecie += reportePrecio * (reportePeso + reporteJabasPeso)
                                file.write("{:<15}{:<7}{:<12}{:<6}\n".format("GALLO VIVO", reporteCantidad, reportePeso+reporteJabasPeso, reporteJabasPeso))                      
                    
            file.write("\n")
            file.write("\n")
            file.write("TOTALES BRUTO :           \n")
            file.write("========================================\n")
            file.write("{:<15}{:<9}{:<10}{:<6}\n".format("PRODUCTO", "CANT.", "KG.", "TARA"))
            file.write("========================================\n")
            
            especies_info = [
                ("YUGO VIVO", reporteTotalCantidadPrimerEspecie, reporteTotalPesoPrimerEspecieBruto, reporteTotalPesoTaraPrimerEspecie),
                ("YUGO PELADO", reporteTotalCantidadSegundaEspecie, reporteTotalPesoSegundaEspecieBruto, reporteTotalPesoTaraSegundaEspecie),
                ("TEC. VIVO", reporteTotalCantidadTerceraEspecie, reporteTotalPesoTerceraEspecieBruto, reporteTotalPesoTaraTerceraEspecie),
                ("TEC. PELADO", reporteTotalCantidadCuartaEspecie, reporteTotalPesoCuartaEspecieBruto, reporteTotalPesoTaraCuartaEspecie),
                ("GALLINA DB", reporteTotalCantidadQuintaEspecie, reporteTotalPesoQuintaEspecieBruto, reporteTotalPesoTaraQuintaEspecie),
                ("AHOGADOS", reporteTotalCantidadSextaEspecie, reporteTotalPesoSextaEspecieBruto, reporteTotalPesoTaraSextaEspecie),
                ("GALLO", reporteTotalCantidadSeptimaEspecie, reporteTotalPesoSeptimaEspecieBruto, reporteTotalPesoTaraSeptimaEspecie),
                ("MALTRATADO", reporteTotalCantidadOctavaEspecie, reporteTotalPesoOctavaEspecieBruto, reporteTotalPesoTaraOctavaEspecie),
                ("PECHUGA", reporteTotalCantidadDecimaEspecie, reporteTotalPesoDecimaEspecieBruto, reporteTotalPesoTaraDecimaEspecie),
                ("PIERNA", reporteTotalCantidadDecimaPrimeraEspecie, reporteTotalPesoDecimaPrimeraEspecieBruto, reporteTotalPesoTaraDecimaPrimeraEspecie),
                ("ALAS", reporteTotalCantidadDecimaSegundaEspecie, reporteTotalPesoDecimaSegundaEspecieBruto, reporteTotalPesoTaraDecimaSegundaEspecie),
                ("MENUDENCIA", reporteTotalCantidadDecimaTerceraEspecie, reporteTotalPesoDecimaTerceraEspecieBruto, reporteTotalPesoTaraDecimaTerceraEspecie),
                ("GALLINA CH", reporteTotalCantidadDecimaCuartaEspecie, reporteTotalPesoDecimaCuartaEspecieBruto, reporteTotalPesoTaraDecimaCuartaEspecie),
                ("OTROS", reporteTotalCantidadDecimaQuintaEspecie, reporteTotalPesoDecimaQuintaEspecieBruto, reporteTotalPesoTaraDecimaQuintaEspecie),
                ("POLLO XX", reporteTotalCantidadDecimaSextaEspecie, reporteTotalPesoDecimaSextaEspecieBruto, reporteTotalPesoTaraDecimaSextaEspecie),
                ("BRASA YUGO", reporteTotalCantidadDecimaSeptimaEspecie, reporteTotalPesoDecimaSeptimaEspecieBruto, reporteTotalPesoTaraDecimaSeptimaEspecie),
                ("BRASA TEC.", reporteTotalCantidadDecimaOctavaEspecie, reporteTotalPesoDecimaOctavaEspecieBruto, reporteTotalPesoTaraDecimaOctavaEspecie),
                ("POLLO XX V", reporteTotalCantidadDecimaNovenaEspecie, reporteTotalPesoDecimaNovenaEspecieBruto, reporteTotalPesoTaraDecimaNovenaEspecie),
                ("GALLINA DB V", reporteTotalCantidadVigesimaEspecie, reporteTotalPesoVigesimaEspecieBruto, reporteTotalPesoTaraVigesimaEspecie),
                ("SECOS", reporteTotalCantidadVigesimaPrimeraEspecie, reporteTotalPesoVigesimaPrimeraEspecieBruto, reporteTotalPesoTaraVigesimaPrimeraEspecie),
                ("GALLO VIVO", reporteTotalCantidadVigesimaSegundaEspecie, reporteTotalPesoVigesimaSegundaEspecieBruto, reporteTotalPesoTaraVigesimaSegundaEspecie),
                ("GALLINA CH", reporteTotalCantidadVigesimaTerceraEspecie, reporteTotalPesoVigesimaTerceraEspecieBruto, reporteTotalPesoTaraVigesimaTerceraEspecie),
            ]

            for especie_info in especies_info:
                nombre_especie, cantidad_especie, peso_especie, peso_tara = especie_info
                if peso_especie != 0 or cantidad_especie != 0:
                    file.write("{:<15}{:<6}{:<10.2f}{:<8}\n".format(nombre_especie, cantidad_especie, peso_especie, peso_tara))
                    
            file.write("\n")
            file.write("\n")
            file.write("TOTALES NETO :   \n")
            file.write("========================================\n")
            file.write("{:<15}{:<10}{:<15}\n".format("PRODUCTO", "CANT.", "KG."))
            file.write("========================================\n")
            
            reporteTotalPesoPrimerEspecie = reporteTotalPesoPrimerEspecieBruto-reporteTotalPesoTaraPrimerEspecie
            reporteTotalPesoSegundaEspecie = reporteTotalPesoSegundaEspecieBruto-reporteTotalPesoTaraSegundaEspecie
            reporteTotalPesoTerceraEspecie = reporteTotalPesoTerceraEspecieBruto-reporteTotalPesoTaraTerceraEspecie
            reporteTotalPesoCuartaEspecie = reporteTotalPesoCuartaEspecieBruto-reporteTotalPesoTaraCuartaEspecie
            reporteTotalPesoQuintaEspecie = reporteTotalPesoQuintaEspecieBruto-reporteTotalPesoTaraQuintaEspecie
            reporteTotalPesoSextaEspecie = reporteTotalPesoSextaEspecieBruto-reporteTotalPesoTaraSextaEspecie
            reporteTotalPesoSeptimaEspecie = reporteTotalPesoSeptimaEspecieBruto-reporteTotalPesoTaraSeptimaEspecie
            reporteTotalPesoOctavaEspecie = reporteTotalPesoOctavaEspecieBruto-reporteTotalPesoTaraOctavaEspecie
            reporteTotalPesoDecimaEspecie = reporteTotalPesoDecimaEspecieBruto-reporteTotalPesoTaraDecimaEspecie
            reporteTotalPesoDecimaPrimeraEspecie = reporteTotalPesoDecimaPrimeraEspecieBruto-reporteTotalPesoTaraDecimaPrimeraEspecie
            reporteTotalPesoDecimaSegundaEspecie = reporteTotalPesoDecimaSegundaEspecieBruto-reporteTotalPesoTaraDecimaSegundaEspecie
            reporteTotalPesoDecimaTerceraEspecie = reporteTotalPesoDecimaTerceraEspecieBruto-reporteTotalPesoTaraDecimaTerceraEspecie
            reporteTotalPesoDecimaCuartaEspecie = reporteTotalPesoDecimaCuartaEspecieBruto-reporteTotalPesoTaraDecimaCuartaEspecie
            reporteTotalPesoDecimaQuintaEspecie = reporteTotalPesoDecimaQuintaEspecieBruto-reporteTotalPesoTaraDecimaQuintaEspecie
            reporteTotalPesoDecimaSextaEspecie = reporteTotalPesoDecimaSextaEspecieBruto-reporteTotalPesoTaraDecimaSextaEspecie
            reporteTotalPesoDecimaSeptimaEspecie = reporteTotalPesoDecimaSeptimaEspecieBruto-reporteTotalPesoTaraDecimaSeptimaEspecie
            reporteTotalPesoDecimaOctavaEspecie = reporteTotalPesoDecimaOctavaEspecieBruto-reporteTotalPesoTaraDecimaOctavaEspecie    
            reporteTotalPesoDecimaNovenaEspecie = reporteTotalPesoDecimaNovenaEspecieBruto-reporteTotalPesoTaraDecimaNovenaEspecie     
            reporteTotalPesoVigesimaEspecie = reporteTotalPesoVigesimaEspecieBruto-reporteTotalPesoTaraVigesimaEspecie     
            reporteTotalPesoVigesimaPrimeraEspecie = reporteTotalPesoVigesimaPrimeraEspecieBruto-reporteTotalPesoTaraVigesimaPrimeraEspecie     
            reporteTotalPesoVigesimaSegundaEspecie = reporteTotalPesoVigesimaSegundaEspecieBruto-reporteTotalPesoTaraVigesimaSegundaEspecie     
            reporteTotalPesoVigesimaTerceraEspecie = reporteTotalPesoVigesimaTerceraEspecieBruto-reporteTotalPesoTaraVigesimaTerceraEspecie     
            
            especies_info2 = [
                ("YUGO VIVO", reporteTotalCantidadPrimerEspecie, reporteTotalPesoPrimerEspecie),
                ("YUGO PELADO", reporteTotalCantidadSegundaEspecie, reporteTotalPesoSegundaEspecie),
                ("TEC. VIVO", reporteTotalCantidadTerceraEspecie, reporteTotalPesoTerceraEspecie),
                ("TEC. PELADO", reporteTotalCantidadCuartaEspecie, reporteTotalPesoCuartaEspecie),
                ("GALLINA DB", reporteTotalCantidadQuintaEspecie, reporteTotalPesoQuintaEspecie),
                ("AHOGADOS", reporteTotalCantidadSextaEspecie, reporteTotalPesoSextaEspecie),
                ("GALLO", reporteTotalCantidadSeptimaEspecie, reporteTotalPesoSeptimaEspecie),
                ("MALTRATADO", reporteTotalCantidadOctavaEspecie, reporteTotalPesoOctavaEspecie),
                ("PECHUGA", reporteTotalCantidadDecimaEspecie, reporteTotalPesoDecimaEspecie),
                ("PIERNA", reporteTotalCantidadDecimaPrimeraEspecie, reporteTotalPesoDecimaPrimeraEspecie),
                ("ALAS", reporteTotalCantidadDecimaSegundaEspecie, reporteTotalPesoDecimaSegundaEspecie),
                ("MENUDENCIA", reporteTotalCantidadDecimaTerceraEspecie, reporteTotalPesoDecimaTerceraEspecie),
                ("GALLINA CH", reporteTotalCantidadDecimaCuartaEspecie, reporteTotalPesoDecimaCuartaEspecie),
                ("OTROS", reporteTotalCantidadDecimaQuintaEspecie, reporteTotalPesoDecimaQuintaEspecie),
                ("POLLO XX", reporteTotalCantidadDecimaSextaEspecie, reporteTotalPesoDecimaSextaEspecie),
                ("BRASA YUGO", reporteTotalCantidadDecimaSeptimaEspecie, reporteTotalPesoDecimaSeptimaEspecie),
                ("BRASA TEC.", reporteTotalCantidadDecimaOctavaEspecie, reporteTotalPesoDecimaOctavaEspecie),
                ("POLLO XX V", reporteTotalCantidadDecimaNovenaEspecie, reporteTotalPesoDecimaNovenaEspecie),
                ("GALLINA DB V", reporteTotalCantidadVigesimaEspecie, reporteTotalPesoVigesimaEspecie),
                ("SECOS", reporteTotalCantidadVigesimaPrimeraEspecie, reporteTotalPesoVigesimaPrimeraEspecie),
                ("GALLO VIVO", reporteTotalCantidadVigesimaSegundaEspecie, reporteTotalPesoVigesimaSegundaEspecie),
                ("GALLINA CH", reporteTotalCantidadVigesimaTerceraEspecie, reporteTotalPesoVigesimaTerceraEspecie),
            ]
            
            totalReporteCantidad = 0
            totalReportePeso = 0

            for especie_info2 in especies_info2:
                nombre_especie2, cantidad_especie2, peso_especie2 = especie_info2
                if peso_especie2 != 0 or cantidad_especie2 != 0:
                    totalReporteCantidad += int(cantidad_especie2)
                    totalReportePeso += float(peso_especie2)
                    file.write("{:<15}{:<10}{:<15.2f}\n".format(nombre_especie2, cantidad_especie2, peso_especie2))

            # file.write("========================================\n")
            # file.write("{:<15}{:<10}{:<15.2f}\n".format("TOTAL :", totalReporteCantidad, totalReportePeso))
            # file.write("========================================\n")
            
            if imprimePrecio == True :
                
                file.write("\n")
                file.write("\n")
                file.write("TOTALES A PAGAR :   \n")
                file.write("========================================\n")
                file.write("{:<14}{:<8}{:<10}{:<8}\n".format("PRODUCTO", "KG.", "PRE.", "TOTAL"))
                file.write("========================================\n")
                
                especies_info3 = [
                    ("YUGO VIVO",reporteTotalPesoPrimerEspecie,precioPrimerEspecie, reporteTotalPrecioPrimerEspecie),
                    ("YUGO PELADO",reporteTotalPesoSegundaEspecie,precioSegundaEspecie, reporteTotalPrecioSegundaEspecie),
                    ("TEC. VIVO",reporteTotalPesoTerceraEspecie,precioTerceraEspecie, reporteTotalPrecioTerceraEspecie),
                    ("TEC. PELADO",reporteTotalPesoCuartaEspecie,precioCuartaEspecie, reporteTotalPrecioCuartaEspecie),
                    ("GALLINA DB",reporteTotalPesoQuintaEspecie,precioQuintaEspecie, reporteTotalPrecioQuintaEspecie),
                    ("AHOGADOS",reporteTotalPesoSextaEspecie,precioSextaEspecie, reporteTotalPrecioSextaEspecie),
                    ("GALLO",reporteTotalPesoSeptimaEspecie,precioSeptimaEspecie, reporteTotalPrecioSeptimaEspecie),
                    ("MALTRATADO",reporteTotalPesoOctavaEspecie,precioOctavaEspecie, reporteTotalPrecioOctavaEspecie),
                    ("PECHUGA",reporteTotalPesoDecimaEspecie,precioDecimaEspecie, reporteTotalPrecioDecimaEspecie),
                    ("PIERNA",reporteTotalPesoDecimaPrimeraEspecie,precioDecimaPrimeraEspecie, reporteTotalPrecioDecimaPrimeraEspecie),
                    ("ALAS",reporteTotalPesoDecimaSegundaEspecie,precioDecimaSegundaEspecie, reporteTotalPrecioDecimaSegundaEspecie),
                    ("MENUDENCIA",reporteTotalPesoDecimaTerceraEspecie,precioDecimaTerceraEspecie, reporteTotalPrecioDecimaTerceraEspecie),
                    ("GALLINA CH",reporteTotalPesoDecimaCuartaEspecie,precioDecimaCuartaEspecie, reporteTotalPrecioDecimaCuartaEspecie),
                    ("OTROS",reporteTotalPesoDecimaQuintaEspecie,precioDecimaQuintaOtrasEspecies, reporteTotalPrecioDecimaQuintaEspecie),
                    ("POLLO XX",reporteTotalPesoDecimaSextaEspecie,precioDecimaSextaEspecie, reporteTotalPrecioDecimaSextaEspecie),
                    ("BRASA YUGO",reporteTotalPesoDecimaSeptimaEspecie,precioDecimaSeptimaEspecie, reporteTotalPrecioDecimaSeptimaEspecie),
                    ("BRASA TEC.",reporteTotalPesoDecimaOctavaEspecie,precioDecimaOctavaEspecie, reporteTotalPrecioDecimaOctavaEspecie),
                    ("POLLO XX V",reporteTotalPesoDecimaNovenaEspecie,precioDecimaNovenaEspecie, reporteTotalPrecioDecimaNovenaEspecie),
                    ("GALLINA DB V",reporteTotalPesoVigesimaEspecie,precioVigesimaEspecie, reporteTotalPrecioVigesimaEspecie),
                    ("SECOS",reporteTotalPesoVigesimaPrimeraEspecie,precioVigesimaPrimeraEspecie, reporteTotalPrecioVigesimaPrimeraEspecie),
                    ("GALLO VIVO",reporteTotalPesoVigesimaSegundaEspecie,precioVigesimaSegundaEspecie, reporteTotalPrecioVigesimaSegundaEspecie),
                    ("GALLINA CH V",reporteTotalPesoVigesimaTerceraEspecie,precioVigesimaTerceraEspecie, reporteTotalPrecioVigesimaTerceraEspecie),
                ]
                
                totalAPagar = 0

                for especie_info3 in especies_info3:
                    nombre_especie3, peso_especie3, precio_unitario, precio_especie = especie_info3
                    if peso_especie3 != 0 and precio_especie != 0:
                        totalAPagar += precio_especie
                        precio_unitario = precio_especie / peso_especie3
                        file.write("{:<14}{:<8.2f}{:<6.2f} S/ {:>8.2f}\n".format(nombre_especie3, peso_especie3, precio_unitario, precio_especie))
                        
                file.write("========================================\n")
                file.write("{:<14}S/ {:<22}\n".format("TOTAL :", "{:,.2f}".format(totalAPagar)))
                file.write("========================================\n")
                
            diferenciaprecioPrimerEspecie =  int((precioPrimerEspecie - precioPrimerEspecie_ant)*10)
            diferenciaprecioSegundaEspecie =  int((precioSegundaEspecie - precioSegundaEspecie_ant)*10)
            diferenciaprecioTerceraEspecie =  int((precioTerceraEspecie - precioTerceraEspecie_ant)*10)
            diferenciaprecioCuartaEspecie =  int((precioCuartaEspecie - precioCuartaEspecie_ant)*10)
            diferenciaprecioQuintaEspecie =  int((precioQuintaEspecie - precioQuintaEspecie_ant)*10)
            diferenciaprecioSextaEspecie =  int((precioSextaEspecie - precioSextaEspecie_ant)*10)
            diferenciaprecioSeptimaEspecie =  int((precioSeptimaEspecie - precioSeptimaEspecie_ant)*10)
            diferenciaprecioOctavaEspecie =  int((precioOctavaEspecie - precioOctavaEspecie_ant)*10)
            diferenciaprecioNovenaEspecie =  int((precioNovenaEspecie - precioNovenaEspecie_ant)*10)
            diferenciaprecioDecimaEspecie =  int((precioDecimaEspecie - precioDecimaEspecie_ant)*10)
            diferenciaprecioDecimaPrimeraEspecie =  int((precioDecimaPrimeraEspecie - precioDecimaPrimeraEspecie_ant)*10)
            diferenciaprecioDecimaSegundaEspecie =  int((precioDecimaSegundaEspecie - precioDecimaSegundaEspecie_ant)*10)
            diferenciaprecioDecimaTerceraEspecie =  int((precioDecimaTerceraEspecie - precioDecimaTerceraEspecie_ant)*10)
            diferenciaprecioDecimaCuartaEspecie =  int((precioDecimaCuartaEspecie - precioDecimaCuartaEspecie_ant)*10)
            diferenciaprecioDecimaQuintaOtrasEspecies =  int((precioDecimaQuintaOtrasEspecies - precioDecimaQuintaOtrasEspecies_ant)*10)
            diferenciaprecioDecimaSextaEspecie =  int((precioDecimaSextaEspecie - precioDecimaSextaEspecie_ant)*10)
            diferenciaprecioDecimaSeptimaEspecie =  int((precioDecimaSeptimaEspecie - precioDecimaSeptimaEspecie_ant)*10)
            diferenciaprecioDecimaOctavaEspecie =  int((precioDecimaOctavaEspecie - precioDecimaOctavaEspecie_ant)*10)
            diferenciaprecioDecimaNovenaEspecie =  int((precioDecimaNovenaEspecie - precioDecimaNovenaEspecie_ant)*10)
            diferenciaprecioVigesimaEspecie =  int((precioVigesimaEspecie - precioVigesimaEspecie_ant)*10)
            diferenciaprecioVigesimaPrimeraEspecie =  int((precioVigesimaPrimeraEspecie - precioVigesimaPrimeraEspecie_ant)*10)
            diferenciaprecioVigesimaSegundaEspecie =  int((precioVigesimaSegundaEspecie - precioVigesimaSegundaEspecie_ant)*10)
            diferenciaprecioVigesimaTerceraEspecie =  int((precioVigesimaTerceraEspecie - precioVigesimaTerceraEspecie_ant)*10)
            
            file.write("\n")
            file.write("\n")
            file.write("\n")
            
            mensaje = ""
            if diferenciaprecioPrimerEspecie > 0:
                mensaje = f"Subio {diferenciaprecioPrimerEspecie} puntos"
            elif diferenciaprecioPrimerEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioPrimerEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoPrimerEspecie) > 0):
                    file.write(f"YUGO VIVO : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioSegundaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioSegundaEspecie} puntos"
            elif diferenciaprecioSegundaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioSegundaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoSegundaEspecie) > 0):
                    file.write(f"YUGO PELADO : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioTerceraEspecie > 0:
                mensaje = f"Subio {diferenciaprecioTerceraEspecie} puntos"
            elif diferenciaprecioTerceraEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioTerceraEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoTerceraEspecie) > 0):
                    file.write(f"TEC. VIVO : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioCuartaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioCuartaEspecie} puntos"
            elif diferenciaprecioCuartaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioCuartaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoCuartaEspecie) > 0):
                    file.write(f"TEC. PELADO : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioQuintaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioQuintaEspecie} puntos"
            elif diferenciaprecioQuintaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioQuintaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoQuintaEspecie) > 0):
                    file.write(f"GALLINA DB : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioSeptimaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioSeptimaEspecie} puntos"
            elif diferenciaprecioSeptimaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioSeptimaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoSeptimaEspecie) > 0):
                    file.write(f"GALLO : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioDecimaCuartaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioDecimaCuartaEspecie} puntos"
            elif diferenciaprecioDecimaCuartaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioDecimaCuartaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoDecimaCuartaEspecie) > 0):
                    file.write(f"GALLINA CH : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioDecimaSextaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioDecimaSextaEspecie} puntos"
            elif diferenciaprecioDecimaSextaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioDecimaSextaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoDecimaSextaEspecie) > 0):
                    file.write(f"POLLO XX : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioDecimaSeptimaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioDecimaSeptimaEspecie} puntos"
            elif diferenciaprecioDecimaSeptimaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioDecimaSeptimaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoDecimaSeptimaEspecie) > 0):
                    file.write(f"BRASA YUGO : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioDecimaOctavaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioDecimaOctavaEspecie} puntos"
            elif diferenciaprecioDecimaOctavaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioDecimaOctavaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoDecimaOctavaEspecie) > 0):
                    file.write(f"BRASA TEC. : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioDecimaNovenaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioDecimaNovenaEspecie} puntos"
            elif diferenciaprecioDecimaNovenaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioDecimaNovenaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoDecimaNovenaEspecie) > 0):
                    file.write(f"POLLO XX V : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioVigesimaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioVigesimaEspecie} puntos"
            elif diferenciaprecioVigesimaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioVigesimaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoVigesimaEspecie) > 0):
                    file.write(f"GALLINA DB V : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioVigesimaSegundaEspecie > 0:
                mensaje = f"Subio {diferenciaprecioVigesimaSegundaEspecie} puntos"
            elif diferenciaprecioVigesimaSegundaEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioVigesimaSegundaEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoVigesimaSegundaEspecie) > 0):
                    file.write(f"GALLO VIVO : {mensaje}\n")
                
            mensaje = ""
            if diferenciaprecioVigesimaTerceraEspecie > 0:
                mensaje = f"Subio {diferenciaprecioVigesimaTerceraEspecie} puntos"
            elif diferenciaprecioVigesimaTerceraEspecie < 0:
                mensaje = f"Bajo {-diferenciaprecioVigesimaTerceraEspecie} puntos"
            if (mensaje != ""):
                if(float(reporteTotalPesoVigesimaTerceraEspecie) > 0):
                    file.write(f"GALLINA CH V : {mensaje}\n")
            
            # file.write("========================================\n")
            # file.write("===       GRACIAS POR SU COMPRA      ===\n")
            # file.write("========================================\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")

            # # Cortar el papel (si es una impresora que admite corte de papel)
            # p.cut()

            # # Cerrar la conexión con la impresora
            # p.close()
            file.close()
        except Exception as e:
            
            print(f"Error al imprimir : {e}")
            # p.close()
            file.close()
        
        imprimePrecio = False
        diccionarioResponsablesDeEnvio = None
        self.ui.frmSombra.setHidden(True)
        self.imprimirTicketWindows()
        
    def imprimirTicketWindows(self):

        # Ruta al archivo que deseas imprimir
        ruta_archivo = r"ArchivosDeTexto/reporte.txt"
        # Abrir el archivo en modo lectura
        with open(ruta_archivo, "r") as f:
            # Leer el contenido del archivo
            contenido = f.read()

        # Imprimir el contenido del archivo en la impresora predeterminada
        hPrinter = win32print.OpenPrinter(ipImpresora)
        try:
            win32print.StartDocPrinter(hPrinter, 1, ("documento", None, "RAW"))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, bytes(contenido, "utf-8"))
                win32print.EndPagePrinter(hPrinter)
            finally:
                win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)
            
    def fn_activarGramosExtrasPorCantidad(self):
        global gramosExtras
        global gramosExtrasActivo
        
        gramosExtras = 0.300 
        gramosExtrasActivo = True
        self.ui.btnAgregarGramosExtras.setStyleSheet("background-color: #2A6BBF; color: #fff")
        
    def fn_desactivarGramosExtrasPorCantidad(self):
        global gramosExtras
        global gramosExtrasActivo
        
        gramosExtras = 0
        gramosExtrasActivo = False
        self.ui.btnAgregarGramosExtras.setStyleSheet("background-color: rgb(192, 192, 192); color: #000")
        
    def fn_seleccionaPesadasReporte(self):
        global frmSeleccionaPesadasReporte
        global arreglo_id_reporte
        global frmDecidirReporte
        global valores_individuales_pesadas
        
        texto_buscar = self.ui.txtIngresarValorImprimir.text()
        
        # Dividir el texto en partes separadas por comas
        valores = texto_buscar.split(',')

        # Inicializar un conjunto para almacenar los valores individuales
        valores_individuales = set()

        # Procesar cada valor obtenido
        for valor in valores:
            # Si el valor contiene un guion '-', considerarlo como un rango
            if '-' in valor:
                # Dividir el valor en un rango y obtener los extremos del rango
                rango = valor.split('-')
                if len(rango) == 2:  # Verificar que haya dos partes después de dividir el valor
                    try:
                        inicio, fin = map(int, rango)
                        
                        # Ordenar los extremos del rango
                        inicio, fin = sorted([inicio, fin])
                        
                        # Generar una lista de valores en el rango y agregarlos al conjunto de valores individuales
                        valores_individuales.update(range(inicio, fin + 1))
                    except ValueError:
                        # Si el valor no es un rango válido, intentar agregar el número directamente
                        try:
                            valores_individuales.add(int(valor.replace('-', '')))
                        except ValueError:
                            print(f"Error: Valor no válido: {valor}")
                else:
                    # Si el valor no es un rango válido, intentar agregar el número directamente
                    try:
                        valores_individuales.add(int(valor.replace('-', '')))
                    except ValueError:
                        print(f"Error: Valor no válido: {valor}")
            else:
                # Si no contiene un guion '-', simplemente agregar el valor al conjunto de valores individuales
                try:
                    valores_individuales.add(int(valor))
                except ValueError:
                    print(f"Error: Valor no válido: {valor}")

        # Convertir el conjunto a una lista para mantener el orden si es necesario
        valores_individuales = list(valores_individuales)
        
        valores_individuales_pesadas = valores_individuales
        
        tablaDePesos = self.ui.tblDetallePesadas
        totalFilas = tablaDePesos.rowCount()
        
        valores_individuales = [x for x in valores_individuales if x != 0]
        
        arreglo_id_reporte = []
        
        for numeroDePesada in valores_individuales:
            if numeroDePesada <= totalFilas:
                # Obtener el índice ajustado según la cantidad total de filas
                indice_fila = totalFilas - numeroDePesada
                # Obtener idPesada e idIdentificadorTabla de la tabla de pesadas
                idPesada = tablaDePesos.item(indice_fila, 12).text()
                idIdentificadorTabla = tablaDePesos.item(indice_fila, 13).text()
                # Construir el diccionario y agregarlo a la lista
                arreglo_id_reporte.append({idIdentificadorTabla: idPesada})
    
        threadAlerta = threading.Thread(target=self.fn_imprimirReporte())
        threadAlerta.start()
        
    def fn_seleccionaPesadasReporteTotal(self):
        global arreglo_id_reporte
        global frmSeleccionaPesadasReporte
        global frmDecidirReporte
        global valores_individuales_pesadas
        
        tablaDePesos = self.ui.tblDetallePesadas
        totalFilas = tablaDePesos.rowCount()
        
        arreglo_id_reporte = []
        
        # Recorrer todas las filas de la tabla
        for fila in range(totalFilas):
            # Obtener idPesada e idIdentificadorTabla de la tabla de pesadas
            idPesada = tablaDePesos.item(fila, 12).text()
            idIdentificadorTabla = tablaDePesos.item(fila, 13).text()
            
            # Construir el diccionario y agregarlo a la lista
            arreglo_id_reporte.append({idIdentificadorTabla: idPesada})
            
        valores_individuales_pesadas = [1]

        # Llamar a la función para imprimir el reporte
        threadAlerta = threading.Thread(target=self.fn_imprimirReporte())
        threadAlerta.start()
        
    def fn_validarEntradaNumericaReporte(self):
        sender = self.sender()

        if sender is not None and isinstance(sender, QLineEdit):
            texto = sender.text()
            texto_valido = ''
            last_char = None
            has_digit = False  # Variable para verificar si hay al menos un dígito mayor a 0
            has_hyphen = False  # Variable para verificar si ya se ha ingresado un guion '-'

            for c in texto:
                if c.isdigit():
                    if c != '0':
                        has_digit = True  # Se ha encontrado al menos un dígito mayor a 0
                    texto_valido += c
                    last_char = c
                elif c == '-' or c == ',':
                    if last_char is not None and last_char.isdigit():
                        if c == '-' and not has_hyphen:  # Solo permitir un guion '-' si no se ha ingresado previamente
                            texto_valido += c
                            has_hyphen = True
                        elif c == ',':
                            texto_valido += c
                    last_char = c

            # Si no hay dígitos mayores a 0, se elimina el '0' del texto válido
            if not has_digit and texto_valido.startswith('0'):
                texto_valido = texto_valido.lstrip('0')

            sender.setText(texto_valido)
            
    def fn_seleccionarEspecieCambiar(self,especieCambiar):
        global idEspecieCambiarEspecie
        global precioCambiarEspecie
        
        self.ui.btnCambioYugoVivo.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnCambioTecnicaVivo.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnCambioGallinaDoble.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnCambioGallinaChica.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnCambioGallo.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnCambioPolloMaltratado.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnCambioPolloXx.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnCambioBrasaYugo.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        self.ui.btnCambioBrasaTecnica.setStyleSheet("background-color: #FFF; color: #000; border: 2px solid black; border-radius: 15px;")
        
        if especieCambiar == 1:
            self.ui.btnCambioYugoVivo.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioSegundaEspecie
            idEspecieCambiarEspecie = primerEspecie
        elif especieCambiar == 3:
            self.ui.btnCambioTecnicaVivo.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioCuartaEspecie
            idEspecieCambiarEspecie = terceraEspecie
        elif especieCambiar == 20:
            self.ui.btnCambioGallinaDoble.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioVigesimaEspecie
            idEspecieCambiarEspecie = vigesimaEspecie
        elif especieCambiar == 21:
            self.ui.btnCambioGallinaChica.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioVigesimaPrimeraEspecie
            idEspecieCambiarEspecie = vigesimaPrimeraEspecie
        elif especieCambiar == 22:
            self.ui.btnCambioGallo.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioVigesimaSegundaEspecie
            idEspecieCambiarEspecie = vigesimaSegundaEspecie
        elif especieCambiar == 23:
            self.ui.btnCambioPolloMaltratado.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioVigesimaTerceraEspecie
            idEspecieCambiarEspecie = vigesimaTerceraEspecie
        elif especieCambiar == 19:
            self.ui.btnCambioPolloXx.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioDecimaNovenaEspecie
            idEspecieCambiarEspecie = decimaNovenaEspecie
        elif especieCambiar == 17:
            self.ui.btnCambioBrasaYugo.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioDecimaSeptimaEspecie
            idEspecieCambiarEspecie = decimaSeptimaEspecie
        elif especieCambiar == 18:
            self.ui.btnCambioBrasaTecnica.setStyleSheet("background-color: #2ABF4E; color: #fff; border: 2px solid black; border-radius: 15px;")
            precioCambiarEspecie = precioDecimaOctavaEspecie
            idEspecieCambiarEspecie = decimaOctavaEspecie
            
    def fn_editarEspeciePesada(self):
        if (identificador == 'tb_pesadas'):
            respuesta = self.conexion.db_editarEspeciePesada(idEspecieCambiarEspecie,precioCambiarEspecie,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        elif (identificador == 'tb_pesadas2'):
            respuesta = self.conexion.db_editarEspeciePesada2(idEspecieCambiarEspecie,precioCambiarEspecie,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
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
        global precioClienteCambiarPesada
        global indexListaCambiarPesada
        
        indice = self.ui.lwListaClientesCambiarPesada.currentIndex().row()
        codClienteCambiarPesada = listCodClienteCambiarPesada[indice]

        item = QListWidgetItem(self.ui.lwListaClientesCambiarPesada.currentItem())
        
        self.ui.txtNombreClienteCambiarPesada.setText(str(item.text()))
        self.ui.lwListaClientesCambiarPesada.setHidden(True)
        self.ui.txtCodigoClienteCambiarPesada.setHidden(True)
        
        codigoClienteCambiarPesada = codClienteCambiarPesada
        indexListaCambiarPesada = 0
        
        precioPrimerEspecieCambiarPesada = 0
        precioSegundaEspecieCambiarPesada = 0
        precioTerceraEspecieCambiarPesada = 0
        precioCuartaEspecieCambiarPesada = 0
        precioQuintaEspecieCambiarPesada = 0
        precioSextaEspecieCambiarPesada = 0
        precioSeptimaEspecieCambiarPesada = 0
        precioOctavaEspecieCambiarPesada = 0
        precioNovenaEspecieCambiarPesada = 0
        precioDecimaEspecieCambiarPesada = 0
        precioDecimaPrimeraEspecieCambiarPesada = 0
        precioDecimaSegundaEspecieCambiarPesada = 0
        precioDecimaTerceraEspecieCambiarPesada = 0
        precioDecimaCuartaEspecieCambiarPesada = 0
        precioDecimaQuintaOtrasEspeciesCambiarPesada = 0
        precioDecimaSextaEspecieCambiarPesada = 0
        precioDecimaSeptimaEspecieCambiarPesada = 0
        precioDecimaOctavaEspecieCambiarPesada = 0
        precioDecimaNovenaEspecieCambiarPesada = 0
        precioVigesimaEspecieCambiarPesada = 0
        precioVigesimaPrimeraEspecieCambiarPesada = 0
        precioVigesimaSegundaEspecieCambiarPesada = 0
        precioVigesimaTerceraEspecieCambiarPesada = 0
        
        idEspecieCambiarPesada = 0
        
        try:
            self.preciosClienteCambiarPesada = self.conexion.db_traerPreciosCliente(codigoClienteCambiarPesada)
            
            (precioPrimerEspecieCambiarPesada, precioSegundaEspecieCambiarPesada, precioTerceraEspecieCambiarPesada, precioCuartaEspecieCambiarPesada, precioQuintaEspecieCambiarPesada,precioSextaEspecieCambiarPesada,precioSeptimaEspecieCambiarPesada,precioOctavaEspecieCambiarPesada,precioNovenaEspecieCambiarPesada,precioDecimaEspecieCambiarPesada,precioDecimaPrimeraEspecieCambiarPesada,precioDecimaSegundaEspecieCambiarPesada,precioDecimaTerceraEspecieCambiarPesada,precioDecimaCuartaEspecieCambiarPesada,precioDecimaQuintaOtrasEspeciesCambiarPesada,precioDecimaSextaEspecieCambiarPesada,precioDecimaSeptimaEspecieCambiarPesada,precioDecimaOctavaEspecieCambiarPesada, precioDecimaNovenaEspecieCambiarPesada, precioVigesimaEspecieCambiarPesada, precioVigesimaPrimeraEspecieCambiarPesada, precioVigesimaSegundaEspecieCambiarPesada, precioVigesimaTerceraEspecieCambiarPesada) = self.preciosClienteCambiarPesada[0]

            if (identificador == 'tb_pesadas'):
                idEspecieCambiarPesada = self.conexion.db_traerIdEspecie(idPesadaEditarOEliminar) 
            elif (identificador == 'tb_pesadas2'):
                idEspecieCambiarPesada = self.conexion.db_traerIdEspecie2(idPesadaEditarOEliminar)
            
            idEspecieCambiarPesada = idEspecieCambiarPesada[0]
            
            if (idEspecieCambiarPesada == 1):
                precioClienteCambiarPesada = precioPrimerEspecieCambiarPesada
            if (idEspecieCambiarPesada == 2):
                precioClienteCambiarPesada = precioSegundaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 3):
                precioClienteCambiarPesada = precioTerceraEspecieCambiarPesada
            if (idEspecieCambiarPesada == 4):
                precioClienteCambiarPesada = precioCuartaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 5):
                precioClienteCambiarPesada = precioQuintaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 6):
                precioClienteCambiarPesada = precioSextaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 7):
                precioClienteCambiarPesada = precioSeptimaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 8):
                precioClienteCambiarPesada = precioOctavaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 9):
                precioClienteCambiarPesada = precioNovenaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 10):
                precioClienteCambiarPesada = precioDecimaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 11):
                precioClienteCambiarPesada = precioDecimaPrimeraEspecieCambiarPesada
            if (idEspecieCambiarPesada == 12):
                precioClienteCambiarPesada = precioDecimaSegundaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 13):
                precioClienteCambiarPesada = precioDecimaTerceraEspecieCambiarPesada
            if (idEspecieCambiarPesada == 14):
                precioClienteCambiarPesada = precioDecimaCuartaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 15):
                precioClienteCambiarPesada = precioDecimaQuintaOtrasEspeciesCambiarPesada
            if (idEspecieCambiarPesada == 16):
                precioClienteCambiarPesada = precioDecimaSextaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 17):
                precioClienteCambiarPesada = precioDecimaSeptimaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 18):
                precioClienteCambiarPesada = precioDecimaOctavaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 19):
                precioClienteCambiarPesada = precioDecimaNovenaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 20):
                precioClienteCambiarPesada = precioVigesimaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 21):
                precioClienteCambiarPesada = precioVigesimaPrimeraEspecieCambiarPesada
            if (idEspecieCambiarPesada == 22):
                precioClienteCambiarPesada = precioVigesimaSegundaEspecieCambiarPesada
            if (idEspecieCambiarPesada == 23):
                precioClienteCambiarPesada = precioVigesimaTerceraEspecieCambiarPesada
        
        except Exception as e:
            self.fn_alerta("¡ERROR!",error,"No se pudieron obtener los precios del cliente.", 2000)
            self.fn_cambiarClienteCambiarPesada()
        
    def fn_cambiarClienteCambiarPesada(self):
        global codigoClienteCambiarPesada
        
        codigoClienteCambiarPesada = 0
            
        self.ui.txtCodigoClienteCambiarPesada.setHidden(False)
        self.ui.txtCodigoClienteCambiarPesada.setText("")
        self.ui.txtCodigoClienteCambiarPesada.setFocus(True)
        self.ui.lwListaClientesCambiarPesada.setHidden(False)
        
    def fn_cambiarPesadaCliente(self):
        if (identificador == 'tb_pesadas'):
            respuesta = self.conexion.db_actualizarCambiarPesada(codigoClienteCambiarPesada,precioClienteCambiarPesada,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
        elif (identificador == 'tb_pesadas2'):
            respuesta = self.conexion.db_actualizarCambiarPesada2(codigoClienteCambiarPesada,precioClienteCambiarPesada,idPesadaEditarOEliminar)
            if respuesta == "ERROR" :
                self.fn_alerta("¡ERROR AL EDITAR!",error,"Error al editar la pesada de la otra pc.",2000)
            else:
                self.fn_alerta("¡EDITADO EXITOSO!",correcto,"El registro se edito correctamente.",1500)
            
        self.fn_listarVenta()
        self.fn_listarPedidos()
        
    def fn_seleccionaPesadasReporteConResponsables(self):
        global frmSeleccionaPesadasReporte
        global arreglo_id_reporte
        global frmDecidirReporte
        global valores_individuales_pesadas
        
        texto_buscar = self.ui.txtIngresarValorImprimir.text()
        
        # Dividir el texto en partes separadas por comas
        valores = texto_buscar.split(',')

        # Inicializar un conjunto para almacenar los valores individuales
        valores_individuales = set()

        # Procesar cada valor obtenido
        for valor in valores:
            # Si el valor contiene un guion '-', considerarlo como un rango
            if '-' in valor:
                # Dividir el valor en un rango y obtener los extremos del rango
                rango = valor.split('-')
                if len(rango) == 2:  # Verificar que haya dos partes después de dividir el valor
                    try:
                        inicio, fin = map(int, rango)
                        
                        # Ordenar los extremos del rango
                        inicio, fin = sorted([inicio, fin])
                        
                        # Generar una lista de valores en el rango y agregarlos al conjunto de valores individuales
                        valores_individuales.update(range(inicio, fin + 1))
                    except ValueError:
                        # Si el valor no es un rango válido, intentar agregar el número directamente
                        try:
                            valores_individuales.add(int(valor.replace('-', '')))
                        except ValueError:
                            print(f"Error: Valor no válido: {valor}")
                else:
                    # Si el valor no es un rango válido, intentar agregar el número directamente
                    try:
                        valores_individuales.add(int(valor.replace('-', '')))
                    except ValueError:
                        print(f"Error: Valor no válido: {valor}")
            else:
                # Si no contiene un guion '-', simplemente agregar el valor al conjunto de valores individuales
                try:
                    valores_individuales.add(int(valor))
                except ValueError:
                    print(f"Error: Valor no válido: {valor}")

        # Convertir el conjunto a una lista para mantener el orden si es necesario
        valores_individuales = list(valores_individuales)
        
        valores_individuales_pesadas = valores_individuales
        
        tablaDePesos = self.ui.tblDetallePesadas
        totalFilas = tablaDePesos.rowCount()
        
        valores_individuales = [x for x in valores_individuales if x != 0]
        
        arreglo_id_reporte = []
        
        for numeroDePesada in valores_individuales:
            if numeroDePesada <= totalFilas:
                # Obtener el índice ajustado según la cantidad total de filas
                indice_fila = totalFilas - numeroDePesada
                # Obtener idPesada e idIdentificadorTabla de la tabla de pesadas
                idPesada = tablaDePesos.item(indice_fila, 12).text()
                idIdentificadorTabla = tablaDePesos.item(indice_fila, 13).text()
                # Construir el diccionario y agregarlo a la lista
                arreglo_id_reporte.append({idIdentificadorTabla: idPesada})
        
    def fn_seleccionaPesadasReporteTotalConResponsables(self):
        global arreglo_id_reporte
        global frmSeleccionaPesadasReporte
        global frmDecidirReporte
        global valores_individuales_pesadas
        
        tablaDePesos = self.ui.tblDetallePesadas
        totalFilas = tablaDePesos.rowCount()
        
        arreglo_id_reporte = []
        
        # Recorrer todas las filas de la tabla
        for fila in range(totalFilas):
            # Obtener idPesada e idIdentificadorTabla de la tabla de pesadas
            idPesada = tablaDePesos.item(fila, 12).text()
            idIdentificadorTabla = tablaDePesos.item(fila, 13).text()
            
            # Construir el diccionario y agregarlo a la lista
            arreglo_id_reporte.append({idIdentificadorTabla: idPesada})
            
        valores_individuales_pesadas = [1]
            
    def convertir_a_lista_de_diccionarios(self, responsablesDeEnvio):
        global diccionarioResponsablesDeEnvio 
        
        # Expresión regular para encontrar nombres seguidos de rangos
        regex = r'(\w+)\s+(\d+-\d+)'

        # Buscar todas las coincidencias en la cadena
        matches = re.findall(regex, responsablesDeEnvio)

        # Lista para almacenar los resultados
        resultados = []

        # Iterar sobre las coincidencias y construir los diccionarios
        for match in matches:
            nombre = match[0]
            rango = match[1]
            resultados.append({'responsable': nombre, 'rango': rango})
            
        diccionarioResponsablesDeEnvio  = resultados

        if resultados:
            return True
        else:
            return False
        
    def fn_encender_apagar_indicador(self):
        inicioSistema.workerAR.user_input_arduino = "x"
        if inicioSistema.workerAR.serialArduino.is_open:
            inicioSistema.workerAR.serialArduino.write(str("x").encode('utf8'))
    
    def fn_pulso_zero_indicador(self):
        inicioSistema.workerAR.user_input_arduino = "z"
        if inicioSistema.workerAR.serialArduino.is_open:
            inicioSistema.workerAR.serialArduino.write(str("z").encode('utf8'))
            
    def fn_traer_agregar_comentario(self):
        self.ui.frmSombra.setHidden(False)
        self.ui.frmIngresaComentario.setHidden(False)
        self.ui.textTareaComentario.clear()
        comentarioObtenido = self.conexion.db_consultarComentario(codCliente)
        
        if(comentarioObtenido):
            comentarioObtenido = comentarioObtenido[0][1]
            self.ui.textTareaComentario.setPlainText(comentarioObtenido)
            
        self.ui.textTareaComentario.setFocus(True)

    def fn_cerrar_comentario(self):
        self.ui.frmSombra.setHidden(True)
        self.ui.frmIngresaComentario.setHidden(True)
        
    def fn_guardarActualizar_comentario(self):
        comentarioObtenido = self.conexion.db_consultarComentario(codCliente)
        comentarioGuardar = self.ui.textTareaComentario.toPlainText()
        
        self.ui.frmSombra.setHidden(True)
        self.ui.frmIngresaComentario.setHidden(True)

        if(comentarioObtenido):
            idComentario = comentarioObtenido[0][0]
            self.conexion.db_actualizarComentario(idComentario, comentarioGuardar)
            self.fn_alerta("¡ACTUALIZADO EXITOSO!",correcto,"El comentario se actualizo correctamente.")
        else:
            self.conexion.db_guardarComentario(codCliente, comentarioGuardar)
            self.fn_alerta("¡REGISTRO EXITOSO!",correcto,"El comentario se registro correctamente.")
            
    def fn_agregar_fila_a_tabla(self, tabla, datos):
        dato1 = int(datos[1])
        dato2 = int(datos[2])
        if dato1 != 0 or dato2 != 0:
            fila = tabla.rowCount()
            tabla.insertRow(fila)
            for columna, dato in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(dato)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                tabla.setItem(fila, columna, item)
            if dato1 != 0 and dato2 == 0 :
                self.fn_pintarCeldasCompleta(fila)
            elif dato1 != 0 and dato2 > 0:
                self.fn_pintarCeldasFaltante(fila)
            else:
                self.fn_pintarCeldasPasados(fila)
            
    def fn_listarPedidos(self):
        tablaDePedidos = self.ui.tblDetallePedidos
        tablaDePedidos.clearContents()
        tablaDePedidos.setRowCount(0)
        
        pedidosArreglo = []
        totalDeTotales = 0
        
        totalCantidadYugoVivo = 0
        totalCantidadYugoPelado = 0
        totalCantidadTecnicaVivo = 0
        totalCantidadTecnicaPelado = 0
        totalCantidadGallinaDoblePelado = 0
        totalCantidadGallinaDobleVivo = 0
        totalCantidadGalloPelado = 0
        totalCantidadGalloVivo = 0
        totalCantidadGallinaChicaPelado = 0
        totalCantidadGallinaChicaVivo = 0
        totalCantidadPolloXXPelado = 0
        totalCantidadBrasaYugo = 0
        totalCantidadBrasaTecnica = 0
        totalCantidadPolloXXVivo = 0
        
        if codCliente != 0:
            pesosListarTabla = self.conexion.db_listarPesosTabla(numProceso,codCliente)
            
            if pesosListarTabla != "" and pesosListarTabla != None:
                if len(pesosListarTabla) > 0:
                
                    for row_number, row_data in enumerate(pesosListarTabla):
                            
                            for column_number, data in enumerate(row_data):
                                    
                                if column_number == 3 and row_data[11] == 1:
                                    if data == nombrePrimerEspecie:
                                        totalCantidadYugoVivo += row_data[4]
                                    elif data == nombreSegundaEspecie:
                                        totalCantidadYugoPelado += row_data[4]
                                    elif data == nombreTerceraEspecie:
                                        totalCantidadTecnicaVivo += row_data[4]
                                    elif data == nombreCuartaEspecie:
                                        totalCantidadTecnicaPelado += row_data[4]
                                    elif data == nombreQuintaEspecie:
                                        totalCantidadGallinaDoblePelado += row_data[4]
                                    elif data == nombreSeptimaEspecie:
                                        totalCantidadGalloPelado += row_data[4]
                                    elif data == nombreDecimaCuartaEspecie:
                                        totalCantidadGallinaChicaPelado += row_data[4]
                                    elif data == nombreDecimaSextaEspecie:
                                        totalCantidadPolloXXPelado += row_data[4]
                                    elif data == nombreDecimaSeptimaEspecie:
                                        totalCantidadBrasaYugo += row_data[4]
                                    elif data == nombreDecimaOctavaEspecie:
                                        totalCantidadBrasaTecnica += row_data[4]
                                    elif data == nombreDecimaNovenaEspecie:                                            
                                        totalCantidadPolloXXVivo += row_data[4]
                                    elif data == nombreVigesimaEspecie:                                            
                                        totalCantidadGallinaDobleVivo += row_data[4]
                                    elif data == nombreVigesimaSegundaEspecie:                                            
                                        totalCantidadGalloVivo += row_data[4]
                                    elif data == nombreVigesimaTerceraEspecie:                                            
                                        totalCantidadGallinaChicaVivo += row_data[4]
        
        if codCliente != 0:
            pedidosListarTabla = self.conexion.db_listarPedidosTabla(codCliente)
            
            if pedidosListarTabla and len(pedidosListarTabla) > 0:
                pedidosListarTabla = pedidosListarTabla[0]
                
                totalDeTotales = pedidosListarTabla[0] + pedidosListarTabla[1] + pedidosListarTabla[2] + pedidosListarTabla[3] + pedidosListarTabla[4] + pedidosListarTabla[5] + pedidosListarTabla[6] + pedidosListarTabla[7] + pedidosListarTabla[8] + pedidosListarTabla[9] + pedidosListarTabla[10] + pedidosListarTabla[11] + pedidosListarTabla[12] + pedidosListarTabla[13]
                
                faltanteYugoVivo = int(pedidosListarTabla[0]) - int(totalCantidadYugoVivo)
                faltanteYugoPelado = int(pedidosListarTabla[1]) - int(totalCantidadYugoPelado)
                faltanteBrasaYugo = int(pedidosListarTabla[2]) - int(totalCantidadBrasaYugo)
                faltanteTecnicaVivo = int(pedidosListarTabla[3]) - int(totalCantidadTecnicaVivo)
                faltanteTecnicaPelado = int(pedidosListarTabla[4]) - int(totalCantidadTecnicaPelado)
                faltanteBrasaTecnica = int(pedidosListarTabla[5]) - int(totalCantidadBrasaTecnica)
                faltantePolloXXPelado = int(pedidosListarTabla[6]) - int(totalCantidadPolloXXPelado)
                faltantePolloXXVivo = int(pedidosListarTabla[7]) - int(totalCantidadPolloXXVivo)
                faltanteGallinaDoblePelado = int(pedidosListarTabla[8]) - int(totalCantidadGallinaDoblePelado)
                faltanteGallinaDobleVivo = int(pedidosListarTabla[9]) - int(totalCantidadGallinaDobleVivo)
                faltanteGalloPelado = int(pedidosListarTabla[10]) - int(totalCantidadGalloPelado)
                faltanteGalloVivo = int(pedidosListarTabla[11]) - int(totalCantidadGalloVivo)
                faltanteGallinaChicaPelado = int(pedidosListarTabla[12]) - int(totalCantidadGallinaChicaPelado)
                faltanteGallinaChicaVivo = int(pedidosListarTabla[13]) - int(totalCantidadGallinaChicaVivo)
                
                # Agregar los datos a las listas
                pedidosArreglo.append((f"{'Yugo Vivo'}", f"{pedidosListarTabla[0]}", f"{faltanteYugoVivo}"))
                pedidosArreglo.append((f"{'Yugo Pelado'}", f"{pedidosListarTabla[1]}", f"{faltanteYugoPelado}"))
                pedidosArreglo.append((f"{'Brasa Yugo'}", f"{pedidosListarTabla[2]}", f"{faltanteBrasaYugo}"))
                
                pedidosArreglo.append((f"{'Tecnica Vivo'}", f"{pedidosListarTabla[3]}", f"{faltanteTecnicaVivo}"))
                pedidosArreglo.append((f"{'Tecnica Pelado'}", f"{pedidosListarTabla[4]}", f"{faltanteTecnicaPelado}"))
                pedidosArreglo.append((f"{'Brasa Tecnica'}", f"{pedidosListarTabla[5]}", f"{faltanteBrasaTecnica}"))
                
                pedidosArreglo.append((f"{'Pollo XX Pelado'}", f"{pedidosListarTabla[6]}", f"{faltantePolloXXPelado}"))
                pedidosArreglo.append((f"{'Pollo XX Vivo'}", f"{pedidosListarTabla[7]}", f"{faltantePolloXXVivo}"))
                
                pedidosArreglo.append((f"{'Gallina Doble Pelado'}", f"{pedidosListarTabla[8]}", f"{faltanteGallinaDoblePelado}"))
                pedidosArreglo.append((f"{'Gallina Doble Vivo'}", f"{pedidosListarTabla[9]}", f"{faltanteGallinaDobleVivo}"))
                
                pedidosArreglo.append((f"{'Gallo Pelado'}", f"{pedidosListarTabla[10]}", f"{faltanteGalloPelado}"))
                pedidosArreglo.append((f"{'Gallo Vivo'}", f"{pedidosListarTabla[11]}", f"{faltanteGalloVivo}"))
                
                pedidosArreglo.append((f"{'Gallina Chica Pelado'}", f"{pedidosListarTabla[12]}", f"{faltanteGallinaChicaPelado}"))
                pedidosArreglo.append((f"{'Gallina Chica Vivo'}", f"{pedidosListarTabla[13]}", f"{faltanteGallinaChicaVivo}"))

                pedidosArreglo = sorted(pedidosArreglo, key=lambda x: -int(x[1]))
                
                # Usar la función auxiliar para agregar filas
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[0])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[1])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[2])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[3])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[4])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[5])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[6])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[7])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[8])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[9])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[10])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[11])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[12])
                self.fn_agregar_fila_a_tabla(tablaDePedidos, pedidosArreglo[13])
                
                self.ui.lblProgramacion.setText(f"La Programación es de : {totalDeTotales}")
                
    def fn_pintarCeldasFaltante(self, fila):
        tablaDePedidos = self.ui.tblDetallePedidos
        
        item = tablaDePedidos.item(fila, 2)
        if item:
            item.setBackground(QColor(255, 51, 51))
            item.setForeground(QColor(255, 255, 255))
            font = item.font()
            font.setBold(True)
            item.setFont(font)
        
        item2 = tablaDePedidos.item(fila, 1)
        if item2:
            font2 = item2.font()
            font2.setBold(True)
            item2.setFont(font2)
            
    def fn_pintarCeldasCompleta(self, fila):
        tablaDePedidos = self.ui.tblDetallePedidos
        
        item = tablaDePedidos.item(fila, 2)
        if item:
            item.setBackground(QColor(0, 170, 0))
            item.setForeground(QColor(255, 255, 255))
            font = item.font()
            font.setBold(True)
            item.setFont(font)
        
        item2 = tablaDePedidos.item(fila, 1)
        if item2:
            font2 = item2.font()
            font2.setBold(True)
            item2.setFont(font2)
    
    def fn_pintarCeldasPasados(self, fila):
        tablaDePedidos = self.ui.tblDetallePedidos
        
        item = tablaDePedidos.item(fila, 2)
        if item:
            item.setBackground(QColor(0, 85, 255))
            item.setForeground(QColor(255, 255, 255))
            font = item.font()
            font.setBold(True)
            item.setFont(font)
        
        item2 = tablaDePedidos.item(fila, 1)
        if item2:
            font2 = item2.font()
            font2.setBold(True)
            item2.setFont(font2)
        
# DISEÑADO Y DESARROLLADO POR SANTOS VILCHEZ EDINSON PASCUAL
# LA UNIÓN - PIURA - PERU ; 2024