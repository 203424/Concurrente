import threading
import time

mutex = threading.Lock()
class Hilo:
    def __init__(self,id ,palillos):
        self.id = id
        self.palillos = palillos

def comiendo(hilo):
    mutex.acquire()
    print("\n(Palillos: ",hilo.palillos,") Persona ",hilo.id," esta recibiendo el palillo")
    hilo.palillos = 2
    print("Persona ",hilo.id," comiendo (Palillos: ",hilo.palillos,")")
    hilo.palillos = 1
    time.sleep(3)
    print("Persona ",hilo.id," termino de comer, prestó el palillo (Palillos: ",hilo.palillos,")")
    mutex.release()

def iniciar(hilos):
    for hilo in hilos:
        personaComiendo = threading.Thread(target=comiendo, args=[hilo])
        print("Persona ",hilo.id,"esperando palillo")
        personaComiendo.start()

def main():
    hilos = [Hilo(1,1),Hilo(2,1),Hilo(3,1),Hilo(4,1),Hilo(5,1),Hilo(6,1),Hilo(7,1),Hilo(8,1)]
    iniciar(hilos)

if __name__ == "__main__":
    main()