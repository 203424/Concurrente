import threading
import time
import random

CAPACIDAD = 100
MESEROS = round(CAPACIDAD * 0.1)
COCINEROS = round(CAPACIDAD * 0.1)
RESERVACION_MAX = round(CAPACIDAD * 0.2)

'''
RECEPCIÓN
- Los comensales llegan de forma individual o en grupo
- La recepción solo puede atender de forma individual o en grupo

RESERVACIONES
- Se pueden hacer reservaciones de manera aleatoria para un máximo del 20% de la capacidad
- Los hilos con reservación pasan a este proceso, se bloquean, tras cierto tiempo se desbloquean y llegan al restaurante
- Cuando un hilo trate de hacer una reservación y no haya espacio se va a la cola del restaurante

COMENSAL
- Llama a un mesero una vez entra al restaurante
- Cambia la orden a EN PROCESO
- Tardan un tiempo específico comiendo y al terminar se retiran y despiertan a los comensales en espera

MESERO
- Solo puede atender a un comensal simultaneamente
- Genera una ORDEN que tiene 2 estados
    EN PROCESO: el comensal bloquea al mesero y el mesero añade la orden a un buffer de ordenes infinito
    LISTO: el cocinero desbloquea al mesero y añade a un buffer de comidas
- Si no hay comensales todos los meseros descansan

COCINERO
- Esta en reposo si no hay ordenes en el buffer
- Cocina, cambia la orden a LISTO y añade al buffer de comidas
'''
