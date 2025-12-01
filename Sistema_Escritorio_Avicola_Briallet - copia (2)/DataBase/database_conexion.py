import mysql.connector
import requests
import json
import subprocess
import os
import time
from datetime import datetime, timedelta

URLSERVIDOR=""
URLLOCAL = ""

hostServidor = "82.197.82.123"
userServidor = "u487773078_Balinsa2024"
contrasenaServidor = "Balinsa1234"
dataBaseServidor = "u487773078_db_sullana"

hostOtraPc = "192.168.1.102"
userOtraPc = "usuario_prueba2"
contrasenaOtraPc = "Balinsa2023"
dataBaseOtraPc = "bd_proyectosullana"

tb_pesadasPrincipal = "tb_pesadas"
tb_pesadasSecundaria = "tb_pesadas2"

hostLocal = "localhost"
userLocal = "root"
contrasenaLocal = ""
dataBaseLocal = "db_proyectosullana"

class Conectar:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Conectar, cls).__new__(cls)
            # Configuración de la conexión a la base de datos
            cls._instancia.conexionsql = mysql.connector.connect(
                host=hostLocal,
                user=userLocal,
                password=contrasenaLocal,
                database=dataBaseLocal,
                port='3306'
            )
        return cls._instancia

    def __init__(self):
        pass

    def cerrar_conexion(self):
        if self.conexionsql.is_connected():
            self.conexionsql.close()
            self._instancia = None
            print("Conexión cerrada.")

    def abrir_conexion(self):
        if not self.conexionsql.is_connected():
            self.conexionsql.reconnect(attempts=3, delay=5)
            print("Conexión abierta.")
        
    def db_seleccionaApiURL(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT puerto_ApiURLSERVIDOR, puerto_ApiURLLOCAL FROM tb_puertos"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
        
    def db_buscaEspecies(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT idEspecie, nombreEspecie FROM tb_especies_venta"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_asignarPesosCubetas(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT pesoColorCubetaUno, pesoColorCubetaDos, pesoColorCubetaTres, pesoColorCubetaCuatro, pesoColorCubetaCinco FROM pesos_de_jabas"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            if result:
                return result[0]  # Devuelve el primer resultado si hay alguno
            else:
                return None  # Retorna None si no hay resultados
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_asignarPesosJabas(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT pesoColorJavaUno, pesoColorJavaDos, pesoColorJavaTres, pesoColorJavaCuatro, pesoColorJavaCinco, pesoColorJavaSeis, pesoColorJavaSiete FROM pesos_de_jabas"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            if result:
                return result[0]  # Devuelve el primer resultado si hay alguno
            else:
                return None  # Retorna None si no hay resultados
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_seleccionaPuertoIndicadores(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT puerto_indicador1, puerto_indicador2 FROM tb_puertos"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_seleccionaPuertoArduino(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT puerto_indicadorArduino FROM tb_puertos"
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_declaraPassword(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT passwordEliminar FROM tb_password"
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
        
    def db_buscaCliente(self, valor):
        try:
            # Primero, asegúrate de cerrar cualquier cursor anterior si es que existe
            if 'cursor' in locals():
                cursor.close()

            cursor = self.conexionsql.cursor()
            sql = "SELECT IFNULL(CONCAT_WS(' ', nombresCli, apellidoPaternoCli), '') AS nombre_completo, codigoCli, idEstadoCli FROM tb_clientes WHERE estadoEliminadoCli = 1 AND (CONCAT_WS(' ', nombresCli, apellidoPaternoCli) LIKE %s OR codigoCli LIKE %s)"
            cursor.execute(sql, ('%' + valor + '%', '%' + valor + '%'))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_traerPreciosCliente(self, codigoCli):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT primerEspecie, segundaEspecie, terceraEspecie, cuartaEspecie, quintaEspecie, sextaEspecie, septimaEspecie, octavaEspecie, novenaEspecie, decimaEspecie, decimaPrimeraEspecie, decimaSegundaEspecie, decimaTerceraEspecie, decimaCuartaEspecie, decimaQuintaOtrasEspecies, decimaSextaEspecie, decimaSeptimaEspecie, decimaOctavaEspecie, decimaNovenaEspecie, vigesimaEspecie, vigesimaPrimeraEspecie, vigesimaSegundaEspecie, vigesimaTerceraEspecie FROM tb_precio_x_presentacion WHERE codigoCli = %s"
            cursor.execute(sql, (codigoCli,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
        
    def db_traerPreciosCliente_ant(self, codigoCli):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT primerEspecie_ant, segundaEspecie_ant, terceraEspecie_ant, cuartaEspecie_ant, quintaEspecie_ant, sextaEspecie_ant, septimaEspecie_ant, octavaEspecie_ant, novenaEspecie_ant, decimaEspecie_ant, decimaPrimeraEspecie_ant, decimaSegundaEspecie_ant, decimaTerceraEspecie_ant, decimaCuartaEspecie_ant, decimaQuintaOtrasEspecies_ant, decimaSextaEspecie_ant, decimaSeptimaEspecie_ant, decimaOctavaEspecie_ant, decimaNovenaEspecie_ant, vigesimaEspecie_ant, vigesimaPrimeraEspecie_ant, vigesimaSegundaEspecie_ant, vigesimaTerceraEspecie_ant FROM tb_precio_x_presentacion WHERE codigoCli = %s"
            cursor.execute(sql, (codigoCli,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_verificarProceso(self, codigoCli):
        try:
            cursor = self.conexionsql.cursor()    
            sql = "SELECT idProceso, codigoCli FROM tb_procesos WHERE codigoCli = %s AND fechaInicioPro = DATE(NOW())"
            cursor.execute(sql, (codigoCli,))        
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_registrarProceso(self, cliente):
        try:
            cursor = self.conexionsql.cursor()
            sql = "INSERT INTO tb_procesos (fechaInicioPro, horaInicioPro, codigoCli) VALUES (DATE(NOW()), TIME(NOW()), %s)"
            cursor.execute(sql, (cliente,))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()

    def db_obtieneUltimoIdProcesoRegistrado(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT MAX(idProceso) AS idProceso FROM tb_procesos"
            cursor.execute(sql)        
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_registrarPesadas(self, numProceso, idEspecie, pesoNeto, horaPeso, codCliente, fechaPeso, cantidadRegistro, precioCliente, pesoNetoJabas, numeroJabasPes, numeroCubetasPes, estadoPeso, estadoWebPeso, tipoCubetas, coloresJabas, observacionPes): # Cambiar tb_pesadas
        try:
            cursor = self.conexionsql.cursor()
            sql = f"""INSERT INTO {tb_pesadasPrincipal}
                        (idProceso, idEspecie, pesoNetoPes, horaPes, codigoCli, fechaRegistroPes, cantidadPes, precioPes, pesoNetoJabas, numeroJabasPes, numeroCubetasPes, estadoPes, estadoWebPes, tipoCubetas, coloresJabas, observacionPes) 
                    VALUES 
                        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (numProceso, idEspecie, pesoNeto, horaPeso, codCliente, fechaPeso, cantidadRegistro, precioCliente, pesoNetoJabas, numeroJabasPes, numeroCubetasPes, estadoPeso, estadoWebPeso, tipoCubetas, coloresJabas, observacionPes))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    
    def db_consultarColoresEditar(self, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = """SELECT coloresJabas FROM tb_pesadas WHERE idPesada = %s"""
            cursor.execute(sql, (idPesadaEditarOEliminar,))
            result = cursor.fetchone()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_consultarVariedadEditar(self, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = """SELECT tipoCubetas FROM tb_pesadas WHERE idPesada = %s"""
            cursor.execute(sql, (idPesadaEditarOEliminar,))
            result = cursor.fetchone()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
        
    def db_consultarColoresEditar2(self, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = """SELECT coloresJabas FROM tb_pesadas2 WHERE idPesada = %s"""
            cursor.execute(sql, (idPesadaEditarOEliminar,))
            result = cursor.fetchone()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_consultarVariedadEditar2(self, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = """SELECT tipoCubetas FROM tb_pesadas2 WHERE idPesada = %s"""
            cursor.execute(sql, (idPesadaEditarOEliminar,))
            result = cursor.fetchone()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None

    ######################################################################################################
    ###################################### CONSULTAS A SERVIDOR WEB ######################################
    ######################################################################################################
                
    def actualizar_datos_servidor_a_local_precios(self):
        try:
            conexionRemotaBalinsa = mysql.connector.connect(
                host=hostServidor,
                user=userServidor,
                password=contrasenaServidor,
                database=dataBaseServidor
            )

            remoto_cursor = conexionRemotaBalinsa.cursor()

            query = "SELECT idPrecio, codigoCli, primerEspecie, segundaEspecie, terceraEspecie, cuartaEspecie, quintaEspecie, sextaEspecie, septimaEspecie, octavaEspecie, novenaEspecie, decimaEspecie, decimaPrimeraEspecie, decimaSegundaEspecie, decimaTerceraEspecie, decimaCuartaEspecie, decimaQuintaOtrasEspecies, decimaSextaEspecie, decimaSeptimaEspecie, decimaOctavaEspecie, decimaNovenaEspecie, vigesimaEspecie, vigesimaPrimeraEspecie, vigesimaSegundaEspecie, vigesimaTerceraEspecie, created_at, updated_at FROM tb_precio_x_presentacion"
            remoto_cursor.execute(query)
            remote_data = remoto_cursor.fetchall()

            with self.conexionsql.cursor() as cursor:
                # Verificar la última actualización local
                cursor.execute("SELECT MAX(updated_at) FROM tb_precio_x_presentacion")
                last_update_local = cursor.fetchone()[0]

                # Verificar la última actualización remota
                remoto_cursor.execute("SELECT MAX(updated_at) FROM tb_precio_x_presentacion")
                last_update_remote = remoto_cursor.fetchone()[0]

                if last_update_local is not None and (last_update_remote - last_update_local) >= timedelta(hours=16):
                    # Actualizar campos _ant
                    update_ant_query = """
                    UPDATE tb_precio_x_presentacion SET
                    primerEspecie_ant = primerEspecie,
                    segundaEspecie_ant = segundaEspecie,
                    terceraEspecie_ant = terceraEspecie,
                    cuartaEspecie_ant = cuartaEspecie,
                    quintaEspecie_ant = quintaEspecie,
                    sextaEspecie_ant = sextaEspecie,
                    septimaEspecie_ant = septimaEspecie,
                    octavaEspecie_ant = octavaEspecie,
                    novenaEspecie_ant = novenaEspecie,
                    decimaEspecie_ant = decimaEspecie,
                    decimaPrimeraEspecie_ant = decimaPrimeraEspecie,
                    decimaSegundaEspecie_ant = decimaSegundaEspecie,
                    decimaTerceraEspecie_ant = decimaTerceraEspecie,
                    decimaCuartaEspecie_ant = decimaCuartaEspecie,
                    decimaQuintaOtrasEspecies_ant = decimaQuintaOtrasEspecies,
                    decimaSextaEspecie_ant = decimaSextaEspecie,
                    decimaSeptimaEspecie_ant = decimaSeptimaEspecie,
                    decimaOctavaEspecie_ant = decimaOctavaEspecie,
                    decimaNovenaEspecie_ant = decimaNovenaEspecie,
                    vigesimaEspecie_ant = vigesimaEspecie,
                    vigesimaPrimeraEspecie_ant = vigesimaPrimeraEspecie,
                    vigesimaSegundaEspecie_ant = vigesimaSegundaEspecie,
                    vigesimaTerceraEspecie_ant = vigesimaTerceraEspecie
                    """
                    cursor.execute(update_ant_query)
                    self.conexionsql.commit()

                # Insertar/actualizar los datos actuales
                insert_query = """
                INSERT INTO tb_precio_x_presentacion 
                (idPrecio, codigoCli, primerEspecie, segundaEspecie, terceraEspecie, cuartaEspecie, quintaEspecie, sextaEspecie, septimaEspecie, octavaEspecie, novenaEspecie, decimaEspecie, decimaPrimeraEspecie, decimaSegundaEspecie, decimaTerceraEspecie, decimaCuartaEspecie, decimaQuintaOtrasEspecies, decimaSextaEspecie, decimaSeptimaEspecie, decimaOctavaEspecie, decimaNovenaEspecie, vigesimaEspecie, vigesimaPrimeraEspecie, vigesimaSegundaEspecie, vigesimaTerceraEspecie, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                codigoCli = VALUES(codigoCli), 
                primerEspecie = VALUES(primerEspecie), 
                segundaEspecie = VALUES(segundaEspecie), 
                terceraEspecie = VALUES(terceraEspecie), 
                cuartaEspecie = VALUES(cuartaEspecie), 
                quintaEspecie = VALUES(quintaEspecie), 
                sextaEspecie = VALUES(sextaEspecie), 
                septimaEspecie = VALUES(septimaEspecie), 
                octavaEspecie = VALUES(octavaEspecie), 
                novenaEspecie = VALUES(novenaEspecie), 
                decimaEspecie = VALUES(decimaEspecie), 
                decimaPrimeraEspecie = VALUES(decimaPrimeraEspecie), 
                decimaSegundaEspecie = VALUES(decimaSegundaEspecie), 
                decimaTerceraEspecie = VALUES(decimaTerceraEspecie), 
                decimaCuartaEspecie = VALUES(decimaCuartaEspecie), 
                decimaQuintaOtrasEspecies = VALUES(decimaQuintaOtrasEspecies), 
                decimaSextaEspecie = VALUES(decimaSextaEspecie), 
                decimaSeptimaEspecie = VALUES(decimaSeptimaEspecie), 
                decimaOctavaEspecie = VALUES(decimaOctavaEspecie),
                decimaNovenaEspecie = VALUES(decimaNovenaEspecie),
                vigesimaEspecie = VALUES(vigesimaEspecie),
                vigesimaPrimeraEspecie = VALUES(vigesimaPrimeraEspecie),
                vigesimaSegundaEspecie = VALUES(vigesimaSegundaEspecie),
                vigesimaTerceraEspecie = VALUES(vigesimaTerceraEspecie),
                created_at = VALUES(created_at),
                updated_at = VALUES(updated_at)"""
                cursor.executemany(insert_query, remote_data)
                self.conexionsql.commit()

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos remota o ejecutar consulta:", error)
        finally:
            if conexionRemotaBalinsa.is_connected():
                remoto_cursor.close()
                conexionRemotaBalinsa.close()
                print("Conexión remota cerrada")
                
    def actualizar_datos_servidor_a_local_clientes(self):
        try:
            conexionRemotaBalinsa = mysql.connector.connect(
                host=hostServidor,
                user=userServidor,
                password=contrasenaServidor,
                database=dataBaseServidor
            )

            remoto_cursor = conexionRemotaBalinsa.cursor()

            query = "SELECT idCliente, apellidoPaternoCli, apellidoMaternoCli, nombresCli, tipoDocumentoCli, numDocumentoCli, contactoCli, direccionCli, idEstadoCli, fechaRegistroCli, horaRegistroCli, usuarioRegistroCli, codigoCli, comentarioCli, estadoEliminadoCli, created_at, updated_at, limitEndeudamiento FROM tb_clientes"
            remoto_cursor.execute(query)
            remote_data = remoto_cursor.fetchall()

            for data in remote_data:
                try:
                    cursor = self.conexionsql.cursor()
                    query = """INSERT INTO tb_clientes 
                                        (idCliente, apellidoPaternoCli, apellidoMaternoCli, nombresCli, tipoDocumentoCli, numDocumentoCli, contactoCli, direccionCli, idEstadoCli, fechaRegistroCli, horaRegistroCli, usuarioRegistroCli, codigoCli, comentarioCli, estadoEliminadoCli, created_at, updated_at, limitEndeudamiento) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        ON DUPLICATE KEY UPDATE
                                        apellidoPaternoCli = VALUES(apellidoPaternoCli),
                                        apellidoMaternoCli = VALUES(apellidoMaternoCli),
                                        nombresCli = VALUES(nombresCli),
                                        tipoDocumentoCli = VALUES(tipoDocumentoCli),
                                        numDocumentoCli = VALUES(numDocumentoCli),
                                        contactoCli = VALUES(contactoCli),
                                        direccionCli = VALUES(direccionCli),
                                        idEstadoCli = VALUES(idEstadoCli),
                                        fechaRegistroCli = VALUES(fechaRegistroCli),
                                        horaRegistroCli = VALUES(horaRegistroCli),
                                        usuarioRegistroCli = VALUES(usuarioRegistroCli),
                                        codigoCli = VALUES(codigoCli),
                                        comentarioCli = VALUES(comentarioCli),
                                        estadoEliminadoCli = VALUES(estadoEliminadoCli),
                                        created_at = VALUES(created_at),
                                        updated_at = VALUES(updated_at),
                                        limitEndeudamiento = VALUES(limitEndeudamiento)"""
                    cursor.execute(query, data)
                    self.conexionsql.commit()
                except mysql.connector.Error as e:
                    print("Error al ejecutar consulta local:", e)
                finally:
                    cursor.close()

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos remota:", error)
        finally:
            if 'conexionRemotaBalinsa' in locals() and conexionRemotaBalinsa.is_connected():
                conexionRemotaBalinsa.close()
                print("Conexión remota cerrada")
                
    def actualizar_datos_servidor_a_local_password(self):
        try:
            conexionRemotaBalinsa = mysql.connector.connect(
                host=hostServidor,
                user=userServidor,
                password=contrasenaServidor,
                database=dataBaseServidor
            )

            remoto_cursor = conexionRemotaBalinsa.cursor()
            query = "SELECT * FROM tb_password"
            remoto_cursor.execute(query)
            remote_data = remoto_cursor.fetchall()

            for data in remote_data:
                try:
                    cursor = self.conexionsql.cursor()
                    query = """INSERT INTO tb_password (idPassword, passwordEliminar, created_at, updated_at)
                                VALUES (%s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE 
                                passwordEliminar = VALUES(passwordEliminar),
                                updated_at = VALUES(updated_at)"""
                    cursor.execute(query, data)
                    self.conexionsql.commit()
                except mysql.connector.Error as e:
                    print("Error al ejecutar consulta local:", e)
                finally:
                    cursor.close()

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos remota:", error)
        finally:
            if 'conexionRemotaBalinsa' in locals() and conexionRemotaBalinsa.is_connected():
                conexionRemotaBalinsa.close()
                print("Conexión remota cerrada")
        
    def actualizar_datos_servidor_pesadas(self): # Cambiar tb_pesadas
        try:
            conexionLocal = mysql.connector.connect(
                host=hostLocal,
                user=userLocal,
                password=contrasenaLocal,
                database=dataBaseLocal
            )
            
            conexionRemotaBalinsa = mysql.connector.connect(
                host=hostServidor,
                user=userServidor,
                password=contrasenaServidor,
                database=dataBaseServidor
            )
            
            cursor_local = conexionLocal.cursor()
            cursor_remoto = conexionRemotaBalinsa.cursor()

            # Obtener datos locales
            query_local = f"SELECT * FROM {tb_pesadasPrincipal} WHERE fechaRegistroPes = DATE(NOW())"
            cursor_local.execute(query_local)
            local_data = cursor_local.fetchall()
            
            for fila in local_data:
                try:
                    # Insertar datos
                    query_insert = f"""INSERT IGNORE INTO {tb_pesadasPrincipal} (idPesada, idProceso, idEspecie, pesoNetoPes, 
                        horaPes, codigoCli, fechaRegistroPes, cantidadPes, precioPes, pesoNetoJabas, 
                        numeroJabasPes, numeroCubetasPes, estadoPes, estadoWebPes, tipoCubetas, coloresJabas, 
                        observacionPes, created_at, updated_at) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor_remoto.execute(query_insert, fila)
                except mysql.connector.Error as e:
                    print("Error al ejecutar consulta de inserción remota:", e)

            for fila in local_data:
                try:
                    # Actualizar datos
                    query_update = f"""UPDATE {tb_pesadasPrincipal} SET idProceso = %s, idEspecie = %s, pesoNetoPes = %s, 
                        horaPes = %s, codigoCli = %s, fechaRegistroPes = %s, cantidadPes = %s, precioPes = %s, pesoNetoJabas = %s, 
                        numeroJabasPes = %s, numeroCubetasPes = %s, estadoPes = %s, estadoWebPes = %s, 
                        tipoCubetas = %s, coloresJabas = %s, observacionPes = %s, created_at = %s, updated_at = %s
                        WHERE idPesada = %s and estadoWebPes = 1"""
                    cursor_remoto.execute(query_update, (fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12], fila[13], fila[14], fila[15], fila[16], fila[17], fila[18], fila[0]))
                except mysql.connector.Error as e:
                    print("Error al ejecutar consulta de actualización remota:", e)
            
            conexionRemotaBalinsa.commit()
            cursor_local.close()
            cursor_remoto.close()
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)
        finally:
            if 'conexion' in locals() and conexionLocal.is_connected():
                conexionLocal.close()
                print("Conexión local cerrada")
            if 'conexionRemotaBalinsa' in locals() and conexionRemotaBalinsa.is_connected():
                conexionRemotaBalinsa.close()
                print("Conexión remota cerrada")
        
    # ===================================================================
    
    def db_listarPesosTabla(self, numProceso, codigoCli):
        try:
            cursor = self.conexionsql.cursor()
            cursor2 = self.conexionsql.cursor()
            sql = """SELECT
                        ROW_NUMBER() OVER (ORDER BY p.idPesada DESC) AS num,
                        IFNULL(CONCAT_WS(' ', nombresCli, apellidoPaternoCli), '') AS cliente,
                        (SELECT TRUNCATE((pesoNetoPes-pesoNetoJabas) / cantidadPes, 2) FROM tb_pesadas WHERE idPesada = p.idPesada) AS promedioPesoNetoCantidad,
                        nombreEspecie, 
                        cantidadPes, 
                        TRUNCATE(pesoNetoPes, 2) as pesoBruto, 
                        pesoNetoJabas, 
                        TRUNCATE(pesoNetoPes, 2), 
                        numeroJabasPes, 
                        coloresJabas, 
                        horaPes, 
                        estadoPes, idPesada, 'tb_pesadas' AS tabla_origen, pesoNetoJabas, observacionPes
                    FROM
                        (SELECT @rownum:=(SELECT COUNT(idPesada) FROM tb_pesadas WHERE fechaRegistroPes = DATE(NOW()) AND tb_pesadas.codigoCli = %s) + 1) r,
                        tb_pesadas p
                        INNER JOIN tb_clientes ON p.codigoCli = tb_clientes.codigoCli
                        INNER JOIN tb_especies_venta ON p.idEspecie = tb_especies_venta.idEspecie
                    WHERE
                        p.fechaRegistroPes = DATE(NOW()) AND p.codigoCli = %s AND p.estadoPes = 1
                    ORDER BY
                        p.idPesada desc"""
            cursor.execute(sql, (codigoCli, codigoCli))
            result = cursor.fetchall()
            
            sql2 = """SELECT
                        ROW_NUMBER() OVER (ORDER BY p.idPesada DESC) AS num,
                        IFNULL(CONCAT_WS(' ', nombresCli, apellidoPaternoCli), '') AS cliente,
                        (SELECT TRUNCATE((pesoNetoPes-pesoNetoJabas) / cantidadPes, 2) FROM tb_pesadas2 WHERE idPesada = p.idPesada) AS promedioPesoNetoCantidad,
                        nombreEspecie, 
                        cantidadPes, 
                        TRUNCATE(pesoNetoPes, 2) as pesoBruto, 
                        pesoNetoJabas, 
                        TRUNCATE(pesoNetoPes, 2), 
                        numeroJabasPes, 
                        coloresJabas, 
                        horaPes, 
                        estadoPes, idPesada, 'tb_pesadas2' AS tabla_origen, pesoNetoJabas, observacionPes
                    FROM
                        (SELECT @rownum:=(SELECT COUNT(idPesada) FROM tb_pesadas2 WHERE fechaRegistroPes = DATE(NOW()) AND tb_pesadas2.codigoCli = %s) + 1) r,
                        tb_pesadas2 p
                        INNER JOIN tb_clientes ON p.codigoCli = tb_clientes.codigoCli
                        INNER JOIN tb_especies_venta ON p.idEspecie = tb_especies_venta.idEspecie
                    WHERE
                        p.fechaRegistroPes = DATE(NOW()) AND p.codigoCli = %s AND p.estadoPes = 1
                    ORDER BY
                        p.idPesada desc"""
            cursor2.execute(sql2, (codigoCli, codigoCli))
            result2 = cursor2.fetchall()
            
            combined_result = sorted(result + result2, key=lambda x: x[10], reverse=True)
            
            cursor.close()
            cursor2.close()
            return combined_result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    def db_listarPesosTablaBeneficiado(self, numProceso, codigoCli):    
        try:
            cursor = self.conexionsql.cursor()
            cursor2 = self.conexionsql.cursor()
            sql = """SELECT
                        ROW_NUMBER() OVER (ORDER BY p.idPesada DESC) AS num,
                        IFNULL(CONCAT_WS(' ', nombresCli, apellidoPaternoCli), '') AS cliente,
                        (SELECT TRUNCATE((pesoNetoPes-pesoNetoJabas) / cantidadPes, 2) FROM tb_pesadas WHERE idPesada = p.idPesada) AS promedioPesoNetoCantidad,
                        nombreEspecie,
                        cantidadPes, 
                        TRUNCATE(pesoNetoPes, 2) as pesoBruto, 
                        pesoNetoJabas, 
                        TRUNCATE(pesoNetoPes, 2), 
                        numeroCubetasPes, 
                        tipoCubetas, 
                        horaPes, 
                        estadoPes, idPesada, 'tb_pesadas' AS tabla_origen, pesoNetoJabas, observacionPes
                    FROM
                        (SELECT @rownum:=(SELECT COUNT(idPesada) FROM tb_pesadas WHERE fechaRegistroPes = DATE(NOW()) AND tb_pesadas.codigoCli = %s) + 1) r,
                        tb_pesadas p
                        INNER JOIN tb_clientes ON p.codigoCli = tb_clientes.codigoCli
                        INNER JOIN tb_especies_venta ON p.idEspecie = tb_especies_venta.idEspecie
                    WHERE
                        p.fechaRegistroPes = DATE(NOW()) AND p.codigoCli = %s AND p.estadoPes = 1
                    ORDER BY
                        p.idPesada desc"""
            cursor.execute(sql, (codigoCli, codigoCli))
            result = cursor.fetchall()
            
            sql2 = """SELECT
                        ROW_NUMBER() OVER (ORDER BY p.idPesada DESC) AS num,
                        IFNULL(CONCAT_WS(' ', nombresCli, apellidoPaternoCli), '') AS cliente,
                        (SELECT TRUNCATE((pesoNetoPes-pesoNetoJabas) / cantidadPes, 2) FROM tb_pesadas2 WHERE idPesada = p.idPesada) AS promedioPesoNetoCantidad,
                        nombreEspecie,
                        cantidadPes, 
                        TRUNCATE(pesoNetoPes, 2) as pesoBruto, 
                        pesoNetoJabas, 
                        TRUNCATE(pesoNetoPes, 2), 
                        numeroCubetasPes, 
                        tipoCubetas, 
                        horaPes, 
                        estadoPes, idPesada, 'tb_pesadas2' AS tabla_origen, pesoNetoJabas, observacionPes
                    FROM
                        (SELECT @rownum:=(SELECT COUNT(idPesada) FROM tb_pesadas2 WHERE fechaRegistroPes = DATE(NOW()) AND tb_pesadas2.codigoCli = %s) + 1) r,
                        tb_pesadas2 p
                        INNER JOIN tb_clientes ON p.codigoCli = tb_clientes.codigoCli
                        INNER JOIN tb_especies_venta ON p.idEspecie = tb_especies_venta.idEspecie
                    WHERE
                        p.fechaRegistroPes = DATE(NOW()) AND p.codigoCli = %s AND p.estadoPes = 1
                    ORDER BY
                        p.idPesada desc"""
            cursor2.execute(sql2, (codigoCli, codigoCli))
            result2 = cursor2.fetchall()
            
            combined_result = sorted(result + result2, key=lambda x: x[10], reverse=True)
            
            cursor.close()
            cursor2.close()
            return combined_result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    
    # ====================================================================
        
    def db_traer_pesadas_desde_otra_pc(self): # Cambiar tb_pesadas
        try:
            # Conectarse a la base de datos en la otra PC
            conexion = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )
            
            conexionLocalSinc = mysql.connector.connect(
                host=hostLocal,
                user=userLocal,
                password=contrasenaLocal,
                database=dataBaseLocal
            )

            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")

                # Aquí puedes ejecutar consultas, por ejemplo:
                cursor = conexion.cursor()
                cursor.execute(f"SELECT * FROM {tb_pesadasSecundaria} WHERE fechaRegistroPes = DATE(NOW())")
                resultados = cursor.fetchall()

                local_cursor = conexionLocalSinc.cursor()

                # Imprimir los resultados
                for fila in resultados:
                    query = f"""INSERT INTO {tb_pesadasSecundaria} (idPesada, idProceso, idEspecie, pesoNetoPes, horaPes, codigoCli, fechaRegistroPes, cantidadPes, precioPes, pesoNetoJabas, numeroJabasPes, numeroCubetasPes, estadoPes, estadoWebPes, tipoCubetas, coloresJabas, observacionPes, created_at, updated_at)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE 
                                idProceso = VALUES(idProceso), 
                                idEspecie = VALUES(idEspecie), 
                                pesoNetoPes = VALUES(pesoNetoPes), 
                                horaPes = VALUES(horaPes), 
                                codigoCli = VALUES(codigoCli), 
                                fechaRegistroPes = VALUES(fechaRegistroPes), 
                                cantidadPes = VALUES(cantidadPes), 
                                precioPes = VALUES(precioPes), 
                                pesoNetoJabas = VALUES(pesoNetoJabas), 
                                numeroJabasPes = VALUES(numeroJabasPes), 
                                numeroCubetasPes = VALUES(numeroCubetasPes), 
                                estadoPes = VALUES(estadoPes), 
                                estadoWebPes = VALUES(estadoWebPes), 
                                tipoCubetas = VALUES(tipoCubetas), 
                                coloresJabas = VALUES(coloresJabas), 
                                observacionPes = VALUES(observacionPes), 
                                created_at = VALUES(created_at), 
                                updated_at = VALUES(updated_at)"""
                    local_cursor.execute(query, fila)

                # Confirmar la inserción y actualización de datos en la base de datos local
                conexionLocalSinc.commit()

                cursor.close()

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)

        finally:
            # Cerrar la conexión
            if 'conexion' in locals() and conexion.is_connected():
                conexion.close()
                print("Conexión cerrada")
                
    def db_traerDatosReporte(self, numProceso, codigoCli):
        try:
            cursor = self.conexionsql.cursor()
            cursor2 = self.conexionsql.cursor()
            sql = """SELECT
                        nombreEspecie, 
                        TRUNCATE(pesoNetoPes, 2), 
                        cantidadPes, 
                        precioPes, 
                        numeroJabasPes, 
                        pesoNetoJabas, 
                        numeroCubetasPes,
                        horaPes,
                        idPesada,
                        'tb_pesadas' AS tabla_origen
                    FROM
                        tb_pesadas p
                        INNER JOIN tb_especies_venta ON p.idEspecie = tb_especies_venta.idEspecie
                    WHERE
                        p.fechaRegistroPes = DATE(NOW()) AND p.codigoCli = %s AND estadoPes = 1
                    ORDER BY
                        p.idPesada desc"""
            cursor.execute(sql, (codigoCli,))
            result = cursor.fetchall()
            
            sql2 = """SELECT
                        nombreEspecie, 
                        TRUNCATE(pesoNetoPes, 2), 
                        cantidadPes, 
                        precioPes, 
                        numeroJabasPes, 
                        pesoNetoJabas, 
                        numeroCubetasPes,
                        horaPes,
                        idPesada,
                        'tb_pesadas2' AS tabla_origen
                    FROM
                        tb_pesadas2 p
                        INNER JOIN tb_especies_venta ON p.idEspecie = tb_especies_venta.idEspecie
                    WHERE
                        p.fechaRegistroPes = DATE(NOW()) AND p.codigoCli = %s AND estadoPes = 1
                    ORDER BY
                        p.idPesada desc"""
            cursor2.execute(sql2, (codigoCli,))
            result2 = cursor2.fetchall()
            
            combined_result = sorted(result + result2, key=lambda x: x[7], reverse=False)
            
            cursor.close()
            cursor2.close()        
            return combined_result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None

    # ################################# BALANZA 1 #################################
    
    def db_actualizarPesadaColores(self, idPesadaEditarOEliminar, numeroJabasPes, coloresJabas, pesoNetoJabas):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET coloresJabas = %s, numeroJabasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
            cursor.execute(sql, (coloresJabas, numeroJabasPes, pesoNetoJabas, idPesadaEditarOEliminar))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_actualizarPesadaColores2(self, idPesadaEditarOEliminar, numeroJabasPes, coloresJabas, pesoNetoJabas):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET coloresJabas = %s, numeroJabasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (coloresJabas, numeroJabasPes, pesoNetoJabas, idPesadaEditarOEliminar))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET coloresJabas = %s, numeroJabasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
                cursor_local.execute(sql_local, (coloresJabas, numeroJabasPes, pesoNetoJabas, idPesadaEditarOEliminar))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
            
    def db_actualizarPesadaVariedad(self, idPesadaEditarOEliminar,numeroCubetasPes,coloresJabas,pesoNetoJabas):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET tipoCubetas = %s, numeroCubetasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
            cursor.execute(sql, (coloresJabas,numeroCubetasPes,pesoNetoJabas,idPesadaEditarOEliminar))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_actualizarPesadaVariedad2(self, idPesadaEditarOEliminar, numeroCubetasPes, coloresJabas, pesoNetoJabas):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET tipoCubetas = %s, numeroCubetasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (coloresJabas, numeroCubetasPes, pesoNetoJabas, idPesadaEditarOEliminar))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET tipoCubetas = %s, numeroCubetasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
                cursor_local.execute(sql_local, (coloresJabas, numeroCubetasPes, pesoNetoJabas, idPesadaEditarOEliminar))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
            
    def db_actualizarPesoJabas(self, pesoNetoJabas,idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET pesoNetoJabas = %s WHERE idPesada = %s"
            cursor.execute(sql, (pesoNetoJabas,idPesadaEditarOEliminar))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_actualizarPesoJabas2(self, pesoNetoJabas,idPesadaEditarOEliminar):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET pesoNetoJabas = %s WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (pesoNetoJabas, idPesadaEditarOEliminar))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET pesoNetoJabas = %s WHERE idPesada = %s"
                cursor_local.execute(sql_local, (pesoNetoJabas, idPesadaEditarOEliminar))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
            
    def db_editarCantidadNueva(self, cantidadNueva, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET cantidadPes = %s WHERE idPesada = %s"
            cursor.execute(sql, (cantidadNueva, idPesadaEditarOEliminar))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_editarCantidadNueva2(self, cantidadNueva, idPesadaEditarOEliminar):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET cantidadPes = %s WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (cantidadNueva, idPesadaEditarOEliminar))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET cantidadPes = %s WHERE idPesada = %s"
                cursor_local.execute(sql_local, (cantidadNueva, idPesadaEditarOEliminar))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
            
    def db_editarCantidadTaraNueva(self, cantidadNueva, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET numeroJabasPes = %s WHERE idPesada = %s"
            cursor.execute(sql, (cantidadNueva, idPesadaEditarOEliminar))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_editarCantidadTaraNueva2(self, cantidadNueva, idPesadaEditarOEliminar):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET numeroJabasPes = %s WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (cantidadNueva, idPesadaEditarOEliminar))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET numeroJabasPes = %s WHERE idPesada = %s"
                cursor_local.execute(sql_local, (cantidadNueva, idPesadaEditarOEliminar))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
        
    def db_editarCantidadDescuentoNueva(self, cantidadNueva, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET cantidadPes = %s WHERE idPesada = %s"
            cursor.execute(sql, (cantidadNueva, idPesadaEditarOEliminar))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_editarCantidadDescuentoNueva2(self, cantidadNueva, idPesadaEditarOEliminar):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET cantidadPes = %s WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (cantidadNueva, idPesadaEditarOEliminar))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET cantidadPes = %s WHERE idPesada = %s"
                cursor_local.execute(sql_local, (cantidadNueva, idPesadaEditarOEliminar))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
        
    def db_eliminarUltimaCantidad(self, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET estadoPes = 0 WHERE idPesada = %s"
            cursor.execute(sql, (idPesadaEditarOEliminar,))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_eliminarUltimaCantidad2(self, idPesadaEditarOEliminar):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET estadoPes = 0 WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (idPesadaEditarOEliminar,))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET estadoPes = 0 WHERE idPesada = %s"
                cursor_local.execute(sql_local, (idPesadaEditarOEliminar,))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
    
    def db_editarEspeciePesada (self,idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET idEspecie = %s, precioPes = %s WHERE idPesada = %s"
            cursor.execute(sql, (idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_editarEspeciePesada2(self, idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET idEspecie = %s, precioPes = %s WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET idEspecie = %s, precioPes = %s WHERE idPesada = %s"
                cursor_local.execute(sql_local, (idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
        
    def db_actualizarCambiarPesada (self,codigoClienteCambiarPesada,precioClienteCambiarPesada,idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_pesadas SET codigoCli = %s, precioPes = %s WHERE idPesada = %s"
            cursor.execute(sql, (codigoClienteCambiarPesada,precioClienteCambiarPesada,idPesadaEditarOEliminar))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
    def db_actualizarCambiarPesada2(self, codigoClienteCambiarPesada, precioClienteCambiarPesada, idPesadaEditarOEliminar):
        try:
            # Establecer conexión a la base de datos remota en la otra PC
            conexion_remota = mysql.connector.connect(
                host=hostOtraPc,
                user=userOtraPc,
                password=contrasenaOtraPc,
                database=dataBaseOtraPc
            )

            if conexion_remota.is_connected():
                print("Conexión exitosa a la base de datos remota")

                # Actualizar los datos en la base de datos remota
                cursor_remoto = conexion_remota.cursor()
                sql_remoto = "UPDATE tb_pesadas2 SET codigoCli = %s, precioPes = %s WHERE idPesada = %s"
                cursor_remoto.execute(sql_remoto, (codigoClienteCambiarPesada, precioClienteCambiarPesada, idPesadaEditarOEliminar))
                conexion_remota.commit()
                cursor_remoto.close()

                # Cerrar la conexión a la base de datos remota
                conexion_remota.close()
                print("Conexión remota cerrada")
                
                # Actualizar datos en la base de datos local
                cursor_local = self.conexionsql.cursor()
                sql_local = "UPDATE tb_pesadas2 SET codigoCli = %s, precioPes = %s WHERE idPesada = %s"
                cursor_local.execute(sql_local, (codigoClienteCambiarPesada, precioClienteCambiarPesada, idPesadaEditarOEliminar))
                self.conexionsql.commit()
                cursor_local.close()

                return "OK"  # Indicador de éxito
            else:
                return "ERROR: No se pudo conectar a la base de datos remota"

        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            return "ERROR"  # Indicador de error
            
    def db_traerIdEspecie(self, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT idEspecie FROM tb_pesadas WHERE idPesada = %s"
            cursor.execute(sql, (idPesadaEditarOEliminar,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    def db_traerIdEspecie2(self, idPesadaEditarOEliminar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT idEspecie FROM tb_pesadas2 WHERE idPesada = %s"
            cursor.execute(sql, (idPesadaEditarOEliminar,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
    # ################################# TERMINA 1 #################################    
    
    # ################################# BALANZA 2 #################################
    
    # def db_actualizarPesadaColores(self, idPesadaEditarOEliminar, numeroJabasPes, coloresJabas, pesoNetoJabas):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET coloresJabas = %s, numeroJabasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (coloresJabas, numeroJabasPes, pesoNetoJabas, idPesadaEditarOEliminar))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET coloresJabas = %s, numeroJabasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (coloresJabas, numeroJabasPes, pesoNetoJabas, idPesadaEditarOEliminar))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_actualizarPesadaColores2(self, idPesadaEditarOEliminar,numeroJabasPes,coloresJabas,pesoNetoJabas):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET coloresJabas = %s, numeroJabasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
    #         cursor.execute(sql, (coloresJabas,numeroJabasPes,pesoNetoJabas,idPesadaEditarOEliminar))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    
    # def db_actualizarPesadaVariedad(self, idPesadaEditarOEliminar, numeroCubetasPes, coloresJabas, pesoNetoJabas):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET tipoCubetas = %s, numeroCubetasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (coloresJabas, numeroCubetasPes, pesoNetoJabas, idPesadaEditarOEliminar))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET tipoCubetas = %s, numeroCubetasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (coloresJabas, numeroCubetasPes, pesoNetoJabas, idPesadaEditarOEliminar))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_actualizarPesadaVariedad2(self, idPesadaEditarOEliminar,numeroCubetasPes,coloresJabas,pesoNetoJabas):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET tipoCubetas = %s, numeroCubetasPes = %s, pesoNetoJabas = %s WHERE idPesada = %s"
    #         cursor.execute(sql, (coloresJabas,numeroCubetasPes,pesoNetoJabas,idPesadaEditarOEliminar))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
            
    # def db_actualizarPesoJabas(self, pesoNetoJabas, idPesadaEditarOEliminar):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET pesoNetoJabas = %s WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (pesoNetoJabas, idPesadaEditarOEliminar))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET pesoNetoJabas = %s WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (pesoNetoJabas, idPesadaEditarOEliminar))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_actualizarPesoJabas2(self, pesoNetoJabas,idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET pesoNetoJabas = %s WHERE idPesada = %s"
    #         cursor.execute(sql, (pesoNetoJabas,idPesadaEditarOEliminar))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
            
    # def db_editarCantidadNueva(self, cantidadNueva, idPesadaEditarOEliminar):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET cantidadPes = %s WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (cantidadNueva, idPesadaEditarOEliminar))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET cantidadPes = %s WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (cantidadNueva, idPesadaEditarOEliminar))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_editarCantidadNueva2(self, cantidadNueva, idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET cantidadPes = %s WHERE idPesada = %s"
    #         cursor.execute(sql, (cantidadNueva, idPesadaEditarOEliminar))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
            
    # def db_editarCantidadTaraNueva(self, cantidadNueva, idPesadaEditarOEliminar):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET numeroJabasPes = %s WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (cantidadNueva, idPesadaEditarOEliminar))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET numeroJabasPes = %s WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (cantidadNueva, idPesadaEditarOEliminar))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_editarCantidadTaraNueva2(self, cantidadNueva, idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET numeroJabasPes = %s WHERE idPesada = %s"
    #         cursor.execute(sql, (cantidadNueva, idPesadaEditarOEliminar))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
        
    # def db_editarCantidadDescuentoNueva(self, cantidadNueva, idPesadaEditarOEliminar):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET cantidadPes = %s WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (cantidadNueva, idPesadaEditarOEliminar))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET cantidadPes = %s WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (cantidadNueva, idPesadaEditarOEliminar))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_editarCantidadDescuentoNueva2(self, cantidadNueva, idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET cantidadPes = %s WHERE idPesada = %s"
    #         cursor.execute(sql, (cantidadNueva, idPesadaEditarOEliminar))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
        
    # def db_eliminarUltimaCantidad(self, idPesadaEditarOEliminar):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET estadoPes = 0 WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (idPesadaEditarOEliminar,))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET estadoPes = 0 WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (idPesadaEditarOEliminar,))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_eliminarUltimaCantidad2(self, idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET estadoPes = 0 WHERE idPesada = %s"
    #         cursor.execute(sql, (idPesadaEditarOEliminar,))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    
    # def db_editarEspeciePesada(self, idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET idEspecie = %s, precioPes = %s WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET idEspecie = %s, precioPes = %s WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_editarEspeciePesada2 (self,idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET idEspecie = %s, precioPes = %s WHERE idPesada = %s"
    #         cursor.execute(sql, (idEspecieCambiarEspecie, precioCambiarEspecie, idPesadaEditarOEliminar))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
        
    # def db_actualizarCambiarPesada(self, codigoClienteCambiarPesada, precioClienteCambiarPesada, idPesadaEditarOEliminar):
    #     try:
    #         # Establecer conexión a la base de datos remota en la otra PC
    #         conexion_remota = mysql.connector.connect(
    #             host=hostOtraPc,
    #             user=userOtraPc,
    #             password=contrasenaOtraPc,
    #             database=dataBaseOtraPc
    #         )

    #         if conexion_remota.is_connected():
    #             print("Conexión exitosa a la base de datos remota")

    #             # Actualizar los datos en la base de datos remota
    #             cursor_remoto = conexion_remota.cursor()
    #             sql_remoto = "UPDATE tb_pesadas SET codigoCli = %s, precioPes = %s WHERE idPesada = %s"
    #             cursor_remoto.execute(sql_remoto, (codigoClienteCambiarPesada, precioClienteCambiarPesada, idPesadaEditarOEliminar))
    #             conexion_remota.commit()
    #             cursor_remoto.close()

    #             # Cerrar la conexión a la base de datos remota
    #             conexion_remota.close()
    #             print("Conexión remota cerrada")
                
    #             # Actualizar datos en la base de datos local
    #             cursor_local = self.conexionsql.cursor()
    #             sql_local = "UPDATE tb_pesadas SET codigoCli = %s, precioPes = %s WHERE idPesada = %s"
    #             cursor_local.execute(sql_local, (codigoClienteCambiarPesada, precioClienteCambiarPesada, idPesadaEditarOEliminar))
    #             self.conexionsql.commit()
    #             cursor_local.close()

    #             return "OK"  # Indicador de éxito
    #         else:
    #             return "ERROR: No se pudo conectar a la base de datos remota"

    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
    #         return "ERROR"  # Indicador de error
    # def db_actualizarCambiarPesada2 (self,codigoClienteCambiarPesada,precioClienteCambiarPesada,idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "UPDATE tb_pesadas2 SET codigoCli = %s, precioPes = %s WHERE idPesada = %s"
    #         cursor.execute(sql, (codigoClienteCambiarPesada,precioClienteCambiarPesada,idPesadaEditarOEliminar))
    #         self.conexionsql.commit()
    #         cursor.close()
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         self.conexionsql.rollback()
            
    # def db_traerIdEspecie(self, idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "SELECT idEspecie FROM tb_pesadas WHERE idPesada = %s"
    #         cursor.execute(sql, (idPesadaEditarOEliminar,))
    #         result = cursor.fetchone()
    #         cursor.close()
    #         return result
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         return None
    # def db_traerIdEspecie2(self, idPesadaEditarOEliminar):
    #     try:
    #         cursor = self.conexionsql.cursor()
    #         sql = "SELECT idEspecie FROM tb_pesadas2 WHERE idPesada = %s"
    #         cursor.execute(sql, (idPesadaEditarOEliminar,))
    #         result = cursor.fetchone()
    #         cursor.close()
    #         return result
    #     except Exception as e:
    #         print("Error al ejecutar la consulta SQL:", e)
    #         return None
    
    # ################################# TERMINA 2 #################################  
    
    def db_seleccionaPuertoHostIp(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT puerto_HostIP FROM tb_puertos"
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
        
    def db_registrarPrestamo(self, codigoClienteCambiarPesada,tipo,variedad,cantidad,fechaPeso,horaPeso):
        try:
            cursor = self.conexionsql.cursor()
            sql = """INSERT INTO tb_prestamo
                        (codCliente ,tipo_prestamo ,variedad_prestamo ,cantidad_prestamo ,fecha_prestamo ,hora_prestamo ) 
                    VALUES 
                        (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (codigoClienteCambiarPesada,tipo,variedad,cantidad,fechaPeso,horaPeso))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            
    def db_listarDatosPrestamos(self):
        try:
            cursor = self.conexionsql.cursor()
            sql = """SELECT
                        ROW_NUMBER() OVER (ORDER BY p.id_prestamo DESC) AS num,
                        IFNULL(CONCAT_WS(' ', nombresCli, apellidoPaternoCli), '') AS cliente,
                        tipo_prestamo,
                        variedad_prestamo,
                        cantidad_prestamo, 
                        hora_prestamo,
                        id_prestamo
                    FROM
                        (SELECT @rownum:=(SELECT COUNT(id_prestamo) FROM tb_prestamo WHERE fecha_prestamo = DATE(NOW())) + 1) r,
                        tb_prestamo p
                        INNER JOIN tb_clientes ON p.codCliente = tb_clientes.codigoCli
                    WHERE
                        p.fecha_prestamo = DATE(NOW())
                    ORDER BY
                        p.id_prestamo desc"""
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
        
    def db_traerPrestamo(self, codCliente):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT tipo_prestamo, variedad_prestamo, cantidad_prestamo FROM tb_prestamo WHERE tb_prestamo.codCliente = %s AND fecha_prestamo = DATE(NOW())"
            cursor.execute(sql, (codCliente,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None

    def db_consultarComentario(self, codCliente):
        try:
            cursor = self.conexionsql.cursor()    
            sql = "SELECT id_comentario, comentario FROM tb_comentario_x_cliente WHERE codCliente = %s AND fecha_comentario = DATE(NOW())"
            cursor.execute(sql, (codCliente,))  
            result = cursor.fetchall()      
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
        
    def db_actualizarComentario(self, idComentario, comentarioGuardar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "UPDATE tb_comentario_x_cliente SET comentario = %s WHERE id_comentario = %s"
            cursor.execute(sql, (comentarioGuardar, idComentario))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            
    def db_guardarComentario(self, codCliente, comentarioGuardar):
        try:
            cursor = self.conexionsql.cursor()
            sql = "INSERT INTO tb_comentario_x_cliente (codCliente, comentario, fecha_comentario) VALUES (%s, %s, DATE(NOW()))"
            cursor.execute(sql, (codCliente, comentarioGuardar,))
            self.conexionsql.commit()
            cursor.close()
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            self.conexionsql.rollback()
            
    def actualizar_datos_local_a_servidor_comentarios(self):
        try:
            conexionLocal = mysql.connector.connect(
                host=hostLocal,
                user=userLocal,
                password=contrasenaLocal,
                database=dataBaseLocal
            )
            
            conexionRemotaBalinsa = mysql.connector.connect(
                host=hostServidor,
                user=userServidor,
                password=contrasenaServidor,
                database=dataBaseServidor
            )
            
            cursor_local = conexionLocal.cursor()
            cursor_remoto = conexionRemotaBalinsa.cursor()

            # Obtener datos locales
            query_local = f"SELECT * FROM tb_comentario_x_cliente WHERE fecha_comentario = DATE(NOW())"
            cursor_local.execute(query_local)
            local_data = cursor_local.fetchall()
            
            for fila in local_data:
                try:
                    query = """
                    INSERT INTO tb_comentario_x_cliente 
                    (id_comentario, codCliente, comentario, fecha_comentario) 
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    codCliente = VALUES(codCliente),
                    comentario = VALUES(comentario),
                    fecha_comentario = VALUES(fecha_comentario)"""
                    cursor_remoto.execute(query, fila)
                except mysql.connector.Error as e:
                    print("Error al ejecutar consulta de inserción remota:", e)
            
            conexionRemotaBalinsa.commit()
            cursor_local.close()
            cursor_remoto.close()
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)
        finally:
            if 'conexion' in locals() and conexionLocal.is_connected():
                conexionLocal.close()
                print("Conexión local cerrada")
            if 'conexionRemotaBalinsa' in locals() and conexionRemotaBalinsa.is_connected():
                conexionRemotaBalinsa.close()
                print("Conexión remota cerrada")
                
    def actualizar_datos_local_a_servidor_prestamos(self):
        try:
            conexionLocal = mysql.connector.connect(
                host=hostLocal,
                user=userLocal,
                password=contrasenaLocal,
                database=dataBaseLocal
            )
            
            conexionRemotaBalinsa = mysql.connector.connect(
                host=hostServidor,
                user=userServidor,
                password=contrasenaServidor,
                database=dataBaseServidor
            )
            
            cursor_local = conexionLocal.cursor()
            cursor_remoto = conexionRemotaBalinsa.cursor()

            # Obtener datos locales
            query_local = f"SELECT * FROM tb_prestamo WHERE fecha_prestamo = DATE(NOW())"
            cursor_local.execute(query_local)
            local_data = cursor_local.fetchall()
            
            for fila in local_data:
                try:
                    query = """
                    INSERT INTO tb_prestamo 
                    (id_prestamo, codCliente, tipo_prestamo, variedad_prestamo, cantidad_prestamo, fecha_prestamo, hora_prestamo) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    codCliente = VALUES(codCliente),
                    tipo_prestamo = VALUES(tipo_prestamo),
                    variedad_prestamo = VALUES(variedad_prestamo),
                    cantidad_prestamo = VALUES(cantidad_prestamo),
                    fecha_prestamo = VALUES(fecha_prestamo),
                    hora_prestamo = VALUES(hora_prestamo)"""
                    cursor_remoto.execute(query, fila)
                except mysql.connector.Error as e:
                    print("Error al ejecutar consulta de inserción remota:", e)
            
            conexionRemotaBalinsa.commit()
            cursor_local.close()
            cursor_remoto.close()
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)
        finally:
            if 'conexion' in locals() and conexionLocal.is_connected():
                conexionLocal.close()
                print("Conexión local cerrada")
            if 'conexionRemotaBalinsa' in locals() and conexionRemotaBalinsa.is_connected():
                conexionRemotaBalinsa.close()
                print("Conexión remota cerrada")
                
    def actualizar_datos_servidor_a_local_pedidos(self):
        try:
            conexionRemotaBalinsa = mysql.connector.connect(
                host=hostServidor,
                user=userServidor,
                password=contrasenaServidor,
                database=dataBaseServidor
            )

            remoto_cursor = conexionRemotaBalinsa.cursor()

            query = "SELECT * FROM tb_pedidos WHERE fechaRegistroPedido = DATE(NOW())"
            remoto_cursor.execute(query)
            remote_data = remoto_cursor.fetchall()

            for data in remote_data:
                try:
                    cursor = self.conexionsql.cursor()
                    query = """INSERT INTO tb_pedidos 
                                        (idPedido, codigoCliPedidos, fechaRegistroPedido, pedidoPrimerEspecie, pedidoSegundaEspecie, pedidoTercerEspecie, pedidoCuartaEspecie, pedidoQuintaEspecie, pedidoSextaEspecie, pedidoSeptimaEspecie, pedidoOctavaEspecie, pedidoNovenaEspecie, pedidoDecimaEspecie, pedidoDecimaPrimeraEspecie, pedidoDecimaSegundaEspecie, pedidoDecimaTerceraEspecie, pedidoDecimaCuartaEspecie, comentarioPedido, estadoPedido, created_at, updated_at) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        ON DUPLICATE KEY UPDATE
                                        codigoCliPedidos = VALUES(codigoCliPedidos),
                                        fechaRegistroPedido = VALUES(fechaRegistroPedido),
                                        pedidoPrimerEspecie = VALUES(pedidoPrimerEspecie),
                                        pedidoSegundaEspecie = VALUES(pedidoSegundaEspecie),
                                        pedidoTercerEspecie = VALUES(pedidoTercerEspecie),
                                        pedidoCuartaEspecie = VALUES(pedidoCuartaEspecie),
                                        pedidoQuintaEspecie = VALUES(pedidoQuintaEspecie),
                                        pedidoSextaEspecie = VALUES(pedidoSextaEspecie),
                                        pedidoSeptimaEspecie = VALUES(pedidoSeptimaEspecie),
                                        pedidoOctavaEspecie = VALUES(pedidoOctavaEspecie),
                                        pedidoNovenaEspecie = VALUES(pedidoNovenaEspecie),
                                        pedidoDecimaEspecie = VALUES(pedidoDecimaEspecie),
                                        pedidoDecimaPrimeraEspecie = VALUES(pedidoDecimaPrimeraEspecie),
                                        pedidoDecimaSegundaEspecie = VALUES(pedidoDecimaSegundaEspecie),
                                        pedidoDecimaTerceraEspecie = VALUES(pedidoDecimaTerceraEspecie),
                                        pedidoDecimaCuartaEspecie = VALUES(pedidoDecimaCuartaEspecie),
                                        comentarioPedido = VALUES(comentarioPedido),
                                        estadoPedido = VALUES(estadoPedido),
                                        created_at = VALUES(created_at),
                                        updated_at = VALUES(updated_at)"""
                    cursor.execute(query, data)
                    self.conexionsql.commit()
                except mysql.connector.Error as e:
                    print("Error al ejecutar consulta local:", e)
                finally:
                    cursor.close()

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos remota:", error)
        finally:
            if 'conexionRemotaBalinsa' in locals() and conexionRemotaBalinsa.is_connected():
                conexionRemotaBalinsa.close()
                print("Conexión remota cerrada")
                
    def db_listarPedidosTabla(self, codigoCli):
        try:
            cursor = self.conexionsql.cursor()
            sql = "SELECT pedidoPrimerEspecie, pedidoSegundaEspecie, pedidoTercerEspecie, pedidoCuartaEspecie, pedidoQuintaEspecie, pedidoSextaEspecie, pedidoSeptimaEspecie, pedidoOctavaEspecie, pedidoNovenaEspecie, pedidoDecimaEspecie, pedidoDecimaPrimeraEspecie, pedidoDecimaSegundaEspecie, pedidoDecimaTerceraEspecie, pedidoDecimaCuartaEspecie, comentarioPedido FROM tb_pedidos WHERE codigoCliPedidos = %s AND fechaRegistroPedido = DATE(NOW())"
            cursor.execute(sql, (codigoCli,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Error al ejecutar la consulta SQL:", e)
            return None
        
# DISEÑADO Y DESARROLLADO POR SANTOS VILCHEZ EDINSON PASCUAL
# LA UNIÓN - PIURA - PERU ; 2024