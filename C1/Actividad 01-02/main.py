import threading
import time
import random

PRODUCERS = 10
CONSUMERS = 5
ITEMS = 10

restantes = threading.Semaphore(ITEMS) #items que faltan por producir
consumir = threading.Semaphore(0) #Items que se pueden consumir
buffer = threading.Semaphore(1) #Valor binario que bloquea la "bodega"

q = list()

def mostrar_items():
    #Operador ternario: condition_if_true if condition else condition_if_false
    print(f"Items en bodega: {q}") if len(q)>0 and len(q)<=ITEMS else print("\nBodega vacía\nNo se puede consumir items")
    if len(q) == ITEMS:
        print(f"BODEGA LLENA Items en bodega {q}")

class Producer(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
    def producir(self):
        item = random.randint(1,100) #Se crea un item con un identificador aleatorio
        print(f"El PRODUCER {self.id} produjo {item} items")
        q.append(item)
    def run(self):
        while True:
            buffer.acquire()
            restantes.acquire() 
            mostrar_items()
            buffer.release()
            consumir.release()
            time.sleep(5)

class Consumer(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
    def consumir(self):
        pos = random.randint(0,len(q)-1)
        item = q.pop(pos)
        print(f"El CONSUMER {self.id} consumio {item} items")
    def run(self):
        while True:
            consumir.acquire()
            buffer.acquire()
            mostrar_items()
            consumir()
            buffer.release()
            restantes.release()
            time.sleep(5)

if __name__ == '__main__':
    producers = []
    custormers = []
    for i in range(PRODUCERS):
        producers.append(Producer(i+1))
    for i in range(CONSUMERS):
        custormers.append(Consumer(i+1))
    
    for p in producers:
        p.start()
    for c in custormers:
        c.start()