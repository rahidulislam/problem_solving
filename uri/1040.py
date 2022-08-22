"""Average 3
Read four numbers (N1, N2, N3, N4), which one with 1 digit after the decimal point, corresponding to 4
scores obtained by a student. Calculate the average with weights 2, 3, 4 e 1 respectively, for these 4 scores and
print the message "Media: " (Average), followed by the calculated result. If the average was 7.0 or more,
print the message "Aluno aprovado." (Approved Student). If the average was less than 5.0, print the message: "Aluno
reprovado." (Reproved Student). If the average was between 5.0 and 6.9, including these, the program must print the
message "Aluno em exame." (In exam student).

In case of exam, read one more score. Print the message "Nota do exame: " (Exam score) followed by the typed score.
Recalculate the average (sum the exam score with the previous calculated average and divide by 2) and print the
message “Aluno aprovado.” (Approved student) in case of average 5.0 or more) or "Aluno reprovado." (Reproved student)
in case of average 4.9 or less. For these 2 cases (approved or reproved after the exam) print the message "Media
final: " (Final average) followed by the final average for this student in the last line.

Input
The input contains four floating point numbers that represent the students' grades.

Output
Print all the answers with one digit after the decimal point.
"""
n1, n2, n3, n4 = list(map(float, input().split()))
avg = (n1*2+n2*3+n3*4+n4*1)/(2+3+4+1)
print(f"Media: {avg:.1f}")
if avg>=7:
    print("Aluno aprovado.")
elif avg<5:
    print("Aluno reprovado.")
elif 5.0 <=avg <=6.9:
    print("Aluno em exame.")
    n5 = float(input())
    print(f"Nota do exame: {n5:.1f}")
    avg2 = (avg+n5)/2
    if avg2 >=5:
        print("Aluno aprovado.")
    elif avg2<=4.9:
        print("Aluno reprovado.")
    print(f"Media final: {avg2:.1f}")