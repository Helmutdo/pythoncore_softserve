
if __name__ == '__main__':
    students=[]
    notas=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student=[]
        
        student.append(name )
        student.append(score)
        
        students.append(student)
    for alumno in students:
        print(alumno)