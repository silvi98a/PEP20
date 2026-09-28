print("Introduce tu edad: ")
n = int(input())

for i in range(n): # 0 a n-1
    if i == 5:
        continue
        # para la ejecución de ese número en concreto (5),
        # pero luego vuelve a ejecutarlo y sigue hasta terminarlo.
    print(i) 