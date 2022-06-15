# Servo_Control
Programa para controle dos servo motores da disciplina de "Projetos de Sistemas Digitais". Feito para uso em Raspberry Pi. Funciona numa Raspberry Pi modelo 3B+.

Primeiro instala-se o pacote para o controle do PWM, é necessário permissão de sudo.

`
sudo apt-get update && sudo apt-get install python3-pigpio

sudo pigpiod
`

Antes de utilizar o código é sempre necessário efetuar o seguinte comando no terminal:

`
sudo pigpiod
`

### Funções

As funções disponíveis no código são as seguintes:

- toogle_servo(X) - Recebe como argumento X, para X=1 liga-se os servos e para X≠1 desliga-se os servos. 

- Controle_Manual(angulo_H,angulo_V,slp)

- Controle_Manual_H(angulo_H,slp)

- Controle_Manual_V(angulo_V,slp)

- Varredura_Servos

- Center_Object

- Center_Object_H

- Center_Object_V


