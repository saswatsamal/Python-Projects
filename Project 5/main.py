#Since this variable is constant
#We going to write it in Capital
NUM_DAYS=7

max_temp=0
min_temp=100

#The for loop will iterate 7 times
#One for each day
for i in range(NUM_DAYS):
    print('Enter the temperature of Day (in Celcius):',i+1)
    temp=int(input())
    if temp>max_temp:
        max_temp=temp
        hottest=i+1
    if temp<min_temp:
        min_temp=temp
        coldest=i+1
    
print('The Hottest Day is: day',hottest)
print()
print('The Coldest Day is: day',coldest)
