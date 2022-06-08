import RPi.GPIO as GPIO
import pigpio #Run this command everytime: sudo apt-get install python3-pigpio; sudo pigpiod
import time
import math

#Portas para os PWM de cada Servo
servo_H = 17
servo_V = 18


# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

pwm = pigpio.pi() #Inicia biblioteca

#Define os Servos com Output
pwm.set_mode(servo_H, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo_H, 50 )
pwm.set_mode(servo_V, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo_V, 50 )


def func(x): #Retorna o valor em segundos [para o t_{on} do PWM] da rotacao em graus desejada
    return ((2500-500)/(180-0))*x+500 #Funcao de primeiro grau



def Controle_Manual(angulo_H=0,angulo_V=0,slp=1): # 'angulo_H' [em graus] e 'angulo_V' [em graus] define o angulo de rotação e 'slp' o tempo entre comandos [em segundos]
       
       if (float(angulo_H)<0 or float(angulo_H)>180) or (float(angulo_V)<0 or float(angulo_V)>180):
           #Desliga os Servos
           pwm.set_PWM_dutycycle(servo_H, 0)
           pwm.set_PWM_frequency(servo_H, 0)
           pwm.set_PWM_dutycycle(servo_V, 0)
           pwm.set_PWM_frequency(servo_V, 0)
           return "ERROR: Angulo fora de faixa [0,180]"
       else:
           pwm.set_servo_pulsewidth( servo_H, func(float(angulo_H))) ;
           pwm.set_servo_pulsewidth( servo_V, func(float(angulo_V))) ;
           time.sleep( slp )
           

def Controle_Manual_H(angulo_H,slp=1): # 'angulo_H' [em graus] define o angulo de rotação e 'slp' o tempo entre comandos [em segundos]
       
       if (float(angulo_H)<0 or float(angulo_H)>180):
           #Desliga os Servos
           pwm.set_PWM_dutycycle(servo_H, 0)
           pwm.set_PWM_frequency(servo_H, 0)
           return "ERROR: Angulo fora de faixa [0,180]"
       else:
           pwm.set_servo_pulsewidth( servo_H, func(float(angulo_H))) ;
           time.sleep( slp )

def Controle_Manual_V(angulo_V,slp=1): # 'angulo_V' [em graus] define o angulo de rotação e 'slp' o tempo entre comandos [em segundos]
       
       if (float(angulo_V)<0 or float(angulo_V)>180):
           #Desliga os Servos
           pwm.set_PWM_dutycycle(servo_V, 0)
           pwm.set_PWM_frequency(servo_V, 0)
           return "ERROR: Angulo fora de faixa [0,180]"
       else:
           pwm.set_servo_pulsewidth( servo_V, func(float(angulo_V))) ;
           time.sleep( slp )
           

def Varredura_Servos(x,passo=20): # 'x' equivale a tempo [em segundos] de varredura e 'passo' a quantidade de passos dentro do tempo 'x'
    meio_passo = passo/2
    for i in range(0, 180, 180/meio_passo):
        Controle_Manual_H(i, x/meio_passo)
    
    for i in range(180, 0, -180/meio_passo):
        Controle_Manual_H(i, x/meio_passo)

#https://www.raspberrypi.com/documentation/accessories/camera.html
        
def Center_Object_H(pos_H,Resolucao_H): # 'pos_H' [em pixel] e 'pos_V' [em pixel] definem o local do Objeto no plano da câmera e 'Resolucao_H' [em pixel] e 'Resolucao_V' [em pixel] a resolução da mesma
    f=3.04; #Distancia focal da Câmera [em mm]; Informacao no datasheet
    Sx=(1.12*10^-3); # Constante de transformação entre pixel para mm; Informação no datasheet
    angulo_H=math.degrees(math.atan((math.fabs(pos_H-Resolucao_H/2.0)*Sx)/f))
    
    Controle_Manual_H(angulo_H,1)

    
def Center_Object_V(pos_V,Resolucao_V): # 'pos_H' [em pixel] e 'pos_V' [em pixel] definem o local do Objeto no plano da câmera e 'Resolucao_H' [em pixel] e 'Resolucao_V' [em pixel] a resolução da mesma
    f=3.04; #Distancia focal da Câmera [em mm]; Informacao no datasheet
    Sx=(1.12*10^-3); # Constante de transformação entre pixel para mm; Informação no datasheet
    angulo_V=math.degrees(math.atan((math.fabs(pos_V-Resolucao_V/2.0)*Sx)/f))
    
    Controle_Manual_V(angulo_V,1)
    
    
def Center_Object(pos_H,pos_V,Resolucao_H,Resolucao_V): # 'pos_H' [em pixel] e 'pos_V' [em pixel] definem o local do Objeto no plano da câmera e 'Resolucao_H' [em pixel] e 'Resolucao_V' [em pixel] a resolução da mesma
    f=3.04; #Distancia focal da Câmera [em mm]; Informacao no datasheet
    Sx=(1.12*10^-3); # Constante de transformação entre pixel para mm; Informação no datasheet
    angulo_H=math.degrees(math.atan((1.0*math.fabs(pos_H-Resolucao_H/2.0)*Sx)/f))
    angulo_V=math.degrees(math.atan((1.0*math.fabs(pos_V-Resolucao_V/2.0)*Sx)/f))
    
    Controle_Manual(angulo_H,angulo_V,1)
        
#while True:
#    Controle_Manual_V(input("Rotacao_V: "),0.5)
