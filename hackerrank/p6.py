if __name__ == '__main__':
    students=[]
    notas=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student=[]
    # agrego input a student    
        student.append(name )
        student.append(score)
        
    # agrego input a students    
        students.append(student)
    
    # separo las notas
    for estudiante in students:
        for nota in estudiante:
            if isinstance(nota, float):
                notas.append(nota)
            
    # ahora busco el segundo mayor
    notas_unicas = list(set(notas)).sort()
    print(notas_unicas)
    nota_minima = notas_unicas[-2]
    
    # imprimir estudiantes con esa nota
    student_runnerup = []
    for estudiante in students:
        if nota_minima in estudiante:
            student_runnerup.append(estudiante[0])
            
    student_runnerup.sort()
    for i in student_runnerup:
        print(i)