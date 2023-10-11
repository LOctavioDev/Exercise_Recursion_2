# Importamos la función 'print' para mostrar el estado del puzzle.
from __future__ import print_function

# Función para generar todas las posibles jugadas que se pueden realizar para mover el número
# del espacio vacío a una de las ocho casillas adyacentes.
def move_puzzle(n, source, target):
  """
  Args:
    n: El número total de movimientos que se pueden realizar.
    source: La posición actual del espacio vacío.
    target: La posición deseada del espacio vacío.

  Returns:
    Una lista de tuplas que representan las posibles jugadas.
  """

  if n == 1:
    if is_solved(source, target):
      return [(source, target)]
    else:
      return []
  else:
    auxiliary = 3 - source - target
    moves = []
    moves.extend(move_puzzle(n - 1, source, auxiliary))
    moves.append((source, target))
    moves.extend(move_puzzle(n - 1, auxiliary, target))
    return moves


def is_solved(source, target):


  if source == 0 and target == 8:
    return True
  elif source == 8 and target == 0:
    return True
  else:
    return False



initial_state = [[8, 1, 0], [3, 2, 6], [7, 5, 4]]


moves = move_puzzle(9, 0, 2)


print("ESTADO INICIAL:")
for row in initial_state:
    print(row)
    print()

step = 1
for source, target in moves:
    print("MOVIMIENTO", step)
    for row in initial_state:
        print(row)
        print()
    initial_state[source][0], initial_state[target][0] = initial_state[target][0], initial_state[source][0]
    step += 1

print("¡Puzzle resuelto!")
