number_of_exams=4
print("ENTER THE MARKS OF ALL THE SUBJECTS RESPECTIVELY TO KNOW WHETHER YOU HAVE PASSED OR NOT!")
exam1=int(input('Marks of First Exam: '))
exam2=int(input('Marks of Second Exam: '))
exam3=int(input('Marks of Third Exam: '))
exam4=int(input('Marks of Fourth Exam: '))


total=exam1+exam2+exam3+exam4
average_score=total/number_of_exams

if average_score>=50:
    print('Your total score is: ' ,total , ' Hence you have passed the exam!')
else:
    print('Your total score is: ' ,total , 'Sorry, you have failed the exam!r')
