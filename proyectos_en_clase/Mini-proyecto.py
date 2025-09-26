def RegistrarEstudiante():
    nombre_mayus = input('Nombre: ').upper() # mayuscula
    n_cursos = int(input('Números de cursos: '))   
    notas_list = []
    # Bucle for
    for i in range(n_cursos): # 0,1,2,3,4 -> 5 iteraciones
        while True:
            nota = float(input('Nota: '))          
            if (0 >= nota >= 20):
                notas_list.append(nota)
                break      
            else:
                print('La nota debe estar entre 0 y 20')                   
    return dict(nombre=nombre_mayus, notas=tuple(notas_list))
                
def CalcularPromedio(estudiante):
    promedio = sum(estudiante['notas']) / len(estudiante['notas'])   
    estudiante['promedio'] = promedio   
    if promedio >= 12.5:
        estado = 'Aprobado'   
    else:
        estado = 'Desaprobado'      
    estudiante['estado'] = estado  
    return estudiante       


def MostrarReporte(estudiante):
    print('Reporte Individual')
    print(f'Nombre: {estudiante['nombre']}')
    print(f'Notas: {estudiante['notas']}')
    print(f'Promedio: {estudiante['promedio']:.2f}')
    print(f'Estado: {estudiante['estado']}')

def main():
    # Lista de diccionarios
    estudiantes = []   
    while True:
        estudiante = RegistrarEstudiante()
        CalcularPromedio(estudiante)
        MostrarReporte(estudiante)
        # Agregar el diccionario
        estudiantes.append(estudiante)
        a = input('Deseas registrar otro estudiante? (s/n) -> ').lower()
        if a != 's':
            break
        # Total
        total = len(estudiantes)
        # Aprobados
        aprobados = [e['nombre'] for e in estudiante if e['estado'] == 'Aprobado']
        desaprobados = [e['nombre'] for e in estudiante if e['estado'] == 'Desaprobado']
        # Porcentaje
        porcentaje_aprob = (len(aprobados) / total) * 100
        porcentaje_desaprob = (len(desaprobados) / total) * 100
        # Promedio
        suma = 0        
        for e in estudiantes:
            suma += e['promedio']
        promedio_general = suma / total
        # mejor promedio y peor promedio
        promedio_max = max(estudiantes, key=lambda e: e['promedio'])
        promedio_min = min(estudiantes, key=lambda e: e['promedio'])      
        