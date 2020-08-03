score_list=[]
print('How many scores you want to add?')
num_score=int(input())

hi_score=0
for i in range(num_score):
    print('Enter the',i+1,'score') 
    n=int(input())
    if n>hi_score:   #Checking the highest value among all.
        hi_score=n
    score_list.append(n) #Storing all the Scores in List Format
    

print('The scores that you entered:')
print(score_list) #Printing all the Scores in List Format
print()
print('The Highest score is',hi_score)
