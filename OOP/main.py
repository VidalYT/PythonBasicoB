# Se hereda los metodos de las anteriores clases:
from enemigo import *
from zombie import *
from ogro import *

# Se registran los valores en variables para main:
Zombie = zombie(10, 1)
Ogro = ogro(20, 3)

# Se usan los metodos de las clases y hace su correspondiente accion:
print(f"{Zombie.get_tipo_enemigo()} tiene {Zombie.puntos_energia} de enegía y puede hacer {Zombie.ataque} de daño")
print(f"{Zombie.habla()}")
print(f"{Ogro.get_tipo_enemigo()} tiene {Ogro.puntos_energia} de enegía y puede hacer {Ogro.ataque} de daño")
print(f"{Ogro.habla()}")