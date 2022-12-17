import pyfirmata 
import time 
pin = 8 
port = 'COM10' 
board = pyfirmata.Arduino(port) 
 
numeroBlink = input('Insira o número de vezes que o LED deve piscar:  ') 
print("Piscando " + numeroBlink + " vezes.") 
 
for x in range(int(numeroBlink)):#A cada elemento no escopo da variável numeroBlink, realizar os seguintes comandos:
      board.digital[8].write(1)#Utilizamos a variável board e seu método .Digital para dizer ao pino 13 que ele deve acender
      time.sleep(1)#Colocamos uma pausa de 0.01 segundos
      board.digital[8].write(0)#Utilizamos a variável board e seu método .Digital para dizer ao pino 13 que ele deve apagar
      time.sleep(1)#Colocamos uma pausa de 0.01 segundos
