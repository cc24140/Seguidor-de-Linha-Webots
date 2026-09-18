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

print("Iniciando...")
sentido = False
    
while robot.step(timestep) != -1:    
    value = ds.getValue()
    
    if value < 3.0:
       print("mudou")
       sentido = True
       
    if sentido:
       motorE.setVelocity(-1.0)
       motorD.setVelocity(-1.0)
    else:
       motorE.setVelocity(1.0)
       motorD.setVelocity(1.0)    

# Enter here exit cleanup code.
