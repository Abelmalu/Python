import random




def new_game():

    choices = ['rock', 'paper', 'scissors']


    computer = random.choice(choices)


    user = input('rock,paper,scissors:  ')
    user = user.lower()


    if computer == 'rock':
        if computer == user:
            print('draw ')
            print('Computer:'+computer)
            print('Player:'+user)
        elif user == 'scissors':
            print('you lost')
            print('Computer:'+computer)
            print('Player:'+user)
        elif user == 'paper':
            print('you won ')
            print('Computer:'+computer)
            print('Player:'+user)
        else:
            print('wrong input')
            print('Computer:'+computer)
            print('Player:'+user)


    if computer == 'scissors':
        if computer == user:
            print('draw ')
            print('Computer:'+computer)
            print('Player:'+user)
        elif user == 'rock':
            print('you won')
            print('Computer:'+computer)
            print('Player:'+user)
        elif user == 'paper':
            print('you lost ')
            print('Computer:'+computer)
            print('Player:'+user)

        else:
            print('wrong input')
            print('Computer:'+computer)
            print('Player:'+user)


    if computer == 'paper':
        if computer == user:
            print('draw ')
            print('Computer:'+computer)
            print('Player:'+user)
        elif user == 'scissors':
            print('you won')
            print('Computer:'+computer)
            print('Player:'+user)
        elif user == 'rock':
            print('you lost ')
            print('Computer:'+computer)
            print('Player:'+user)
        else:
            print('wrong input')
            print('Computer:'+computer)
            print('Player:'+user)


response = 'yes'
new_game()


while response == 'yes':
    response = input('do you wanna play again(yes or no)')
    response = response.lower()
    if response == 'no':
        break
    

    new_game()




