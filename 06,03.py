n = int(input('Enter number:'))
student_grades = {}
for _ in range(n):
    student, grade = input('Enter name and grade split by space:').split(' ')
    if student_grades.get(student) is None:
        student_grades[student] = [] student_grades[student].append(float(grade))
for student, grades in student_grades.items():
    avg = sum(grades)/len(grades)
    print(f" {student} -> {grades} (avg: {avg:.2f})")