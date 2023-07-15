from pybricks.hubs import EV3brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, InfraredSensor
from pybricks.parameters import Port

ev3 = EV3brick()

garra = Motor(Port.A)

motor1 = Motor(Port.B)

motor2 = Motor(Port.C)

traseira = Motor(Port.D)

sensor_meio = ColorSensor(Port.S1)

sensor_direita = ColorSensor(Port.S2)

sensor_esquerda = ColorSensor(Port.S3)

infravermelho = InfraredSensor(Port.S4)

kp = 1.2
ki = 0.01
kd = 0.2

ultimo_erro = 0
integral = 0

while true:
    valor_sensor_esquerda = sensor_esquerda.reflection()
    valor_sensor_meio = sensor_meio.reflection()
    valor_sensor_direita = sensor_direita.reflection()
    
    erro = (valor_sensor_esquerda * 0.2 + valor_sensor_meio * 0.5 + valor_sensor_direita * 0.3) - 50
    
    integral = integral + erro
    integral = max(min(integral, 100), -100)
    
    derivativo = erro - ultimo_erro
    
    ultimo_erro = erro
    
    controle = (kp * erro) + (ki*integral) + (kd * derivativo)
    
    motor1_velocidade = max(min(motor1_velocidade, 100), -100)
    motor2_velocidade = max(min(motor2_velocidade, 100), -100)
    
    motor1_anda(motor1_velocidade)
    motor2_anda(motor2_velocidade)
    
    wait(10)
    