"""
S'imprimeix una piràmide d'altura N de 🧱 centrada
input
5
output
              🧱
             🧱🧱
            🧱🧱🧱
           🧱🧱🧱🧱
          🧱🧱🧱🧱🧱
"""
brick = "🧱"


n = int(input())

for i in range(1, n+1):
    espacio = " " * (n - i)
    bricks = brick * i
    print(espacio + bricks)




