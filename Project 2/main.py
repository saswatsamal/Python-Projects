number_of_exams=3 
exam1=int(input('Enter the first exam Result: '))
exam2=int(input('Enter the second exam Result: '))
exam3=int(input('Enter the third exam Result: '))

average_score=(exam1+exam2+exam3)/number_of_exams

print('The average score: ',format(average_score, '.1f'))
