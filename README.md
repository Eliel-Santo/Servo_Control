# Servo_Control
Programa para controle dos servo motores da disciplina de "Projetos de Sistemas Digitais". Feito para uso em Raspberry Pi. Funciona numa Raspberry Pi modelo 3B+.

Primeiro instala-se o pacote para o controle do PWM, é necessário permissão de sudo.

`sudo apt-get update`
`sudo apt-get upgrade`
`sudo apt-get install python3-pigpio`
`sudo pigpiod`

Antes de utilizar o código é sempre necessário efetuar o seguinte comando no terminal:

`
sudo pigpiod
`

### Funções

As funções externas disponíveis no código são as seguintes:

- toogle_servo(X)
- --Desliga-se o PWM sendo enviado aos servos. Útil por questões de controle e segurança.
-- Recebe como argumento **X**, para **X**=1 liga-se os servos e para **X**≠1 desliga-se os servos.

- Controle_Manual(angulo_H,angulo_V,slp)
- --Define a posição onde deve-se posicionar o servo motor, tanto na horizontal quanto na vertical.
--Recebe como argumentos **angulo_H, angulo_V, slp**, onde **angulo_H** define a posição em ângulo do servo_H, **angulo_V** define a posição do ângulo do servo_V e **slp** define o tempo de espera após a rotação.
Obs: Valores padrão: angulo_H=0,angulo_V=0,slp=1

- Controle_Manual_H(angulo_H,slp)
- --Define a posição onde deve-se posicionar o servo motor na horizontal.
--Recebe como argumentos **angulo_H, slp**, onde **angulo_H** define a posição em ângulo do servo_H e **slp** define o tempo de espera após a rotação.
Obs: Valores padrão: angulo_H=0,slp=1

- Controle_Manual_V(angulo_V,slp)
- --Define a posição onde deve-se posicionar o servo motor na vertical.
--Recebe como argumentos **angulo_V, slp**, onde **angulo_H** define a posição em ângulo do servo_V e **slp** define o tempo de espera após a rotação.
Obs: Valores padrão: angulo_V=0,slp=1

- Varredura_Servos(x,passo)
- --Recebe como argumentos **x, passo**, onde **x** define o tempo em segundos da varredura e passo define a quantidade de passos a serem realizados durante a varredura, por exemplo, para uma varredura de 10 segundos e 40 passos, serão realizados 20 movimentos do servo motor em 5 segundos, até um extremo e depois 20 movimentos do servo motor em 5 segundos para a posição original.
Obs: Valores padrão: passo=20. Somente movimenta o servo_H.

- Center_Object(pos_H,pos_V,Resolucao_H,Resolucao_V)
- --A função centraliza na tela, tanto na vertical, quanto na horizontal, um objeto em uma posição qualquer (pos_H,pos_V). 
--Recebe como argumentos **pos_H, pos_V, Resolucao_H, Resolucao_V**, onde **pos_H** define a posição atual do objeto na horizontal, **pos_V** a posição atual do objeto na vertical, **Resolucao_H** define a resolução da imagem na horizontal e **Resolucao_V** define a resolução da imagem na vertical (quantidade de pixels).
Obs: Valores padrão: pos_H, pos_V, Resolucao_H=640, Resolucao_V=480

- Center_Object_H(pos_H,Resolucao_H)
- --A função centraliza no eixo horizontal da tela um objeto em uma posição qualquer (pos_H,pos_V). 
--Recebe como argumentos **pos_H, Resolucao_H**, onde **pos_H** define a posição atual do objeto na horizontal e **Resolucao_H** define a resolução da imagem na horizontal (quantidade de pixels).
Obs: Valores padrão: pos_H, Resolucao_H=640

- Center_Object_V(pos_V,Resolucao_V)
- --A função centraliza no eixo vertical da tela um objeto em uma posição qualquer (pos_H,pos_V). 
--Recebe como argumentos **pos_V, Resolucao_V**, onde **pos_V** define a posição atual do objeto na horizontal e **Resolucao_V** define a resolução da imagem na vertical (quantidade de pixels).
Obs: Valores padrão: pos_H, Resolucao_H=480

### Definições dos Servos
Os servo motores sendo utilizados são controlados via Pulse Width Modulation (PWM) e possuem um eixo de rotação de -90º até 90º, onde as larguras dos pulsos respectivos são: 1ms até 2ms. O período do pulso deve ser de 20ms (50 Hz). É utilizado o modelo SG90 e o seu datasheet pode ser encontrado na pasta de anexos ou um link direto esta disponível na referências.

### Definições da Câmera
Utilizou-se uma camêra para a centralização do objeto na imagem. O modelo utilizado foi o "Camera Module v2". Onde utilizou-se o tamanho de pixel de 0.0012 mm (tanto pra largura quanto pro comprimento) e distância focal de 3.04 mm.

---
### Referências
                
1. Datasheet dos Servo Motores (SG90): 
https://www.datasheet4u.com/datasheet-pdf/TowerPro/SG90/pdf.php?id=791970
2. Definições da Câmera (Modelo v2):
https://www.raspberrypi.com/documentation/accessories/camera.html
3. Documentação da Biblioteca pigpio:
http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

                
----

### Links Úteis

+ Edição do Readme.md
	+ https://pandao.github.io/editor.md/en.html
	+ https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

+ Explicação sucinta do Pigpio
	+ https://ben.akrin.com/raspberry-pi-servo-jitter/
                    
