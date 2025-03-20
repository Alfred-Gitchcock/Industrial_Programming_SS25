import numpy as np

print("Congratulations! You have been selected as a test subject for our number guessing testing initiative. "
      "Please do not resist, for resistance is futile. \n "
      "The Game works as follows: You have to compete against our highly advanced number guessing AI in guessing a randomly selected integer between 1 and a number of your choice. \n"
      "Each round you get a guess and then our AI gets a guess, on a wrong guess you are told if the guess was higher or lower than the selected number. \n"
      "If you guess the number first, you win. If our AI guesses the number first, you lose and eternal shame shall befall you and your kin. Good luck!")

high_bound = int(input("Choose upper bound of number generation range: "))

#determining number to guess
random_number = np.random.randint(1,high_bound)

#initial guesses that cannot be true, so python doesn't complain about not knowing "player_guess" and "ai_guess"
player_guess = 0
ai_guess = 0
lower = 1
upper = high_bound

#loop that runs until correct number is gussed
while player_guess != random_number and ai_guess != random_number:

      #player's turn
      player_guess = int(input("Your turn. Please enter your guess: "))

      if player_guess == random_number:
            print("Hooray, you won!")
            break

      elif player_guess < random_number:
            print("Your guess was too low.")
            lower = player_guess + 1

      elif player_guess > random_number:
            print("Your guess was too high.")
            upper = player_guess - 1

      #"AI"'s turn
      ai_guess = np.random.randint(lower,upper)
      print("AI's turn. Our AI's guess was:", ai_guess)

      if ai_guess == random_number:
            print("This guess was correct. You have lost, prepare for eternal shame to be heaped upon you and your family.")
            break

      elif ai_guess < random_number:
            print("This guess was too low.")
            lower = ai_guess + 1

      elif ai_guess > random_number:
            print("This guess was too high.")
            upper = ai_guess -1