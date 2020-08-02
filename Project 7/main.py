import random
def intro():
    print('I will guess a number  between (1,100)')
    print('and you have 7 chances to find my guess')
    print('I will help you by saying that your guess')
    print('is higher, or lower than my guess ')
    print()

def get_computer_guess():
    print('I\'m guessing a number')
    return random.randint(1,100)
    
def main():
    player_score=0 
    com_score=0 
    intro()
    again='y'
    while again=='y':
        player_won=False
        com_guess=get_computer_guess()
        print('I guessed the number')
        print('your turn')
        
        for i in range(7):
            print('what is your',i+1,'guess')
            guess=int(input())
            if guess==com_guess:
                print('congratulation you won the game')
                player_won=True
                break
                
            elif guess>com_guess:
                print('your guess is higher than mine')
            else:
                print('your guess is lower than mine')
            
        if player_won:
            player_score+=1 
        else:
            com_score+=1
            
        print('Player score: ',player_score)
        print('computer score: ',com_score)
        print()
        print('do want to play again?')
        print('press y for yes')
        print('or any other key to exit')
        again=input().lower()
main()
