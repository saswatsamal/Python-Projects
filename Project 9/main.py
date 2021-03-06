import pickle
def main():
    again='y'
    while again.lower()=='y':
        choice=0
        
        # ask from the user what to do
        while choice != 1 and choice!= 2:
            try:
                print('Choose the Number.')
                choice=int(input('[1] : To add data to the file\n[2] : To read data from the file \n'))
                if choice!=1 and choice!=2:
                    print('Wrong entry')
            
            except:
                choice=int(input('Enter either [1] or [2] '))
            
     #this will do what user asked for      
        if choice==1:
            my_file=open('student_data.dat', 'wb') #Adding the data of the Student
            add_student(my_file)
            
        elif choice==2:
            my_file=open('student_data.dat', 'rb')
            read_student(my_file)
        again=input('Do you want to continue?: [y] for yes [n] for no: ')
    

def add_student(data):       
    
        student=dict()
        again='y'
        while again.lower()=='y':
            name=input('Enter the student name: ')
            score=int(input('Enter his score out of 100: '))
            student[name]=score
            pickle.dump(student, data)
            print('All data have been saved to the student_data file!')
            print()
            again=input('Do you want to add another student? \n' \
                        'enter [y] for yes and [n] for no.\n')
        
        data.close()
# this will read data from the file to the dictionary        
def read_student(my_file):
    end_of_file=False
    while end_of_file==False:
        try:
            student=pickle.load(my_file)
        except EOFError:
            end_of_file=True
            
    print(student)

    my_file.close()
    
       
main()
