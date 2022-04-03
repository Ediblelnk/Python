print('Welcome to the Number Guesser Game!\n') #welcome text

playagain = 'yes'
while playagain != 'no' or playagain != 'No':

    difficulty = input('Pick a difficulty: Very Easy, Easy, Medium, Hard, Very Hard, Impossible\n') #prompts for a difficulty and sets the range of numbers accordingly
    numrange = 400
    if difficulty == 'Very Easy' or difficulty == 'very easy':
        numrange = 400
    elif difficulty == 'Easy' or difficulty == 'easy':
        numrange = 800
    elif difficulty == 'medium' or difficulty == 'Medium':
        numrange = 1600
    elif difficulty == 'hard' or difficulty == 'Hard':
        numrange = 3200
    elif difficulty == 'very hard' or difficulty == 'Very Hard':
        numrange = 6400
    elif difficulty == 'impossible' or difficulty == 'Impossible':
        numrange = 12800
    else:
        print('Unknown Difficulty Requested: "'+difficulty+'" . Defaulted to Medium Difficulty') #sets difficulty to medium if requested difficulty does not exist
        
    import random                   #pick the number and tell the user the challenge
    number = random.randint(1,numrange)
    print(f'I have selected a number between 1 and {str(numrange)}. You have 10 tries to guess the number.')

    for trycount in range(10): #cap the number of guesses for 10
        print('Guess '+str(trycount+1)+':')
        guess = input()
        try:
            guess = int(guess)
        
            if guess > number:
                print('That guess is too high!') #prints high if the guess is too high

            if guess < number:
                print('That guess is too low!') #prints low if the number is too low

            if guess == number: #case for when the guess is the number
                break
        except:
            print('Thats not a number!')

            
    if guess == number:
        print('You have guessed the number I was thinking of in '+str(trycount+1)+' tries. Congrats!\n')

    if guess != number:
        print('You have run out of tries to guess the number I was thinking of. The number was '+str(number)+'.\n')
    
    
