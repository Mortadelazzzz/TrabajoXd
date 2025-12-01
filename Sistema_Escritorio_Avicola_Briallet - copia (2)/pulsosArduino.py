import inicioSistema

def fn_encenderPulsoVerde():
    if inicioSistema.workerAR.serialArduino and inicioSistema.workerAR.serialArduino.is_open:
        inicioSistema.workerAR.serialArduino.write(str("a").encode('utf8'))

def fn_apagarPulsoVerde():
    if inicioSistema.workerAR.serialArduino and inicioSistema.workerAR.serialArduino.is_open:
        inicioSistema.workerAR.serialArduino.write(str("e").encode('utf8'))
        
def fn_encenderPulsoRojo():
    if inicioSistema.workerAR.serialArduino and inicioSistema.workerAR.serialArduino.is_open:
        inicioSistema.workerAR.serialArduino.write(str("c").encode('utf8'))

def fn_apagarPulsoRojo():
    if inicioSistema.workerAR.serialArduino and inicioSistema.workerAR.serialArduino.is_open:
        inicioSistema.workerAR.serialArduino.write(str("g").encode('utf8'))
        
def fn_encenderPulsoBuzzer():
    if inicioSistema.workerAR.serialArduino and inicioSistema.workerAR.serialArduino.is_open:
        inicioSistema.workerAR.serialArduino.write(str("i").encode('utf8'))

def fn_apagarPulsoBuzzer():
    if inicioSistema.workerAR.serialArduino and inicioSistema.workerAR.serialArduino.is_open:
        inicioSistema.workerAR.serialArduino.write(str("k").encode('utf8'))

def fn_activarPulsoEnciendeApagaIndicador():
    if inicioSistema.workerAR.serialArduino and inicioSistema.workerAR.serialArduino.is_open:
        inicioSistema.workerAR.serialArduino.write(str("x").encode('utf8'))
        
def fn_activarPulsoZero():
    if inicioSistema.workerAR.serialArduino and inicioSistema.workerAR.serialArduino.is_open:
        inicioSistema.workerAR.serialArduino.write(str("z").encode('utf8'))