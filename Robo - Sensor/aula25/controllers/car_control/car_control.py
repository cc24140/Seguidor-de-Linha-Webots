#car_control controller
from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

print("Inicando rodas")
motorE = robot.getDevice('motorE')
motorD = robot.getDevice('motorD')
motorE.setPosition(float('inf'))
motorD.setPosition(float('inf'))
motorE.setVelocity(0.0)
motorD.setVelocity(0.0)

# OBTENDO E CONFIGURANDO SENSORES
ds = robot.getDevice('DS')
ds.enable(timestep)

dse = robot.getDevice('distance sensor left')
dse.enable(timestep)
dsd = robot.getDevice('distance sensor right')
dsd.enable(timestep)


print("Iniciando...")
sentido = False
vini_e = 0
vini_d = 0
    
while robot.step(timestep) != -1:
    ve = round(dse.getValue(), 2)
    vd = round(dsd.getValue(), 2)
    
    if(ve - vini_e) != 0 and ve > 0:
        vini_e = ve
        print("esquerda")
        
    elif(vd - vini_d) != 0 and vd > 0:
        vini_d = vd
        print("direita")
        
    if(vini_e > vini_d):
        motorE.setVelocity(0.05);
        motorD.setVelocity(0.4);
        
    elif(vini_e < vini_d):
        motorE.setVelocity(0.4);
        motorD.setVelocity(0.05);
    
    value = ds.getValue()
    
    if value < 3.0:
       print("mudou")
       sentido = True
   
    if(vini_e == vini_d):
        if sentido:
           motorE.setVelocity(-1.0)
           motorD.setVelocity(-1.0)
        else:
           motorE.setVelocity(1.0)
           motorD.setVelocity(1.0)    
