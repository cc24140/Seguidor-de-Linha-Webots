#car_control controller

# Mariana Marietti da Costa - 24140

from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep()) # frequência de atualização da simulação (em milissegundos)

# INICIALIZAÇÃO DOS MOTORES
print("Inicando rodas")
motorE = robot.getDevice('motorE') # Motor Esquerdo
motorD = robot.getDevice('motorD') # Motor Direito
motorE.setPosition(float('inf')) # Define rotação contínua (modo velocidade)
motorD.setPosition(float('inf')) # Define rotação contínua (modo velocidade)
motorE.setVelocity(0.0) # Inicia o motor parado
motorD.setVelocity(0.0) # Inicia o motor parado

# OBTENDO E CONFIGURANDO SENSORES
# Sensor de distância frontal (detetor de obstáculo/parede)
ds = robot.getDevice('DS')
ds.enable(timestep)
# Sensor infravermelho de linha
dse = robot.getDevice('distance sensor left')
dse.enable(timestep)
dsd = robot.getDevice('distance sensor right')
dsd.enable(timestep)

# VARIÁVEIS DE ESTADO E MEMÓRIA
print("Iniciando...")
sentido = False # Flag de sentido de marcha: False = Frente, True = Marcha-atrás
vini_e = 0 # Armazena a última leitura válida do sensor
vini_d = 0 # Armazena a última leitura válida do sensor
    
# LOOP PRINCIPAL DA SIMULAÇÃO
while robot.step(timestep) != -1:
    # Lê os valores dos sensores infravermelhos e arredonda a 2 casas decimais
    ve = round(dse.getValue(), 2)
    vd = round(dsd.getValue(), 2)
    
    # Atualiza a memória do sensor esquerdo se houver alteração de valor acima de zero
    if(ve - vini_e) != 0 and ve > 0:
        vini_e = ve
        print("esquerda")
        
    # Atualiza a memória do sensor direito se houver alteração de valor acima de zero
    elif(vd - vini_d) != 0 and vd > 0:
        vini_d = vd
        print("direita")
        
    # LÓGICA DE DIRECIONAMENTO (CURVAS)
    # Se a leitura da esquerda for maior que a da direita, curva para a esquerda
    if(vini_e > vini_d):
        motorE.setVelocity(0.05);
        motorD.setVelocity(0.4);
        
    # Se a leitura da direita for maior que a da esquerda, curva para a direita
    elif(vini_e < vini_d):
        motorE.setVelocity(0.4);
        motorD.setVelocity(0.05);
    
    # SENSOR FRONTAL E INVERSÃO DE SENTIDO
    value = ds.getValue()
    
    if value < 3.0:
       print("mudou")
       sentido = True
   
    # MOVIMENTO RETO / MARCHA-ATRÁS (Quando ambos os sensores leem igual)
    if(vini_e == vini_d):
        if sentido:
           motorE.setVelocity(-1.0)
           motorD.setVelocity(-1.0)
        else:
           motorE.setVelocity(1.0)
           motorD.setVelocity(1.0)    
