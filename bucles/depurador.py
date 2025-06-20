edades = [30, 7, 10, 13, 16, 18, 20, 22, 23, 25]

for edad in edades:
    if edad >= 20:
        edades.remove(edad)

print(f'Edades menores: {edades}')