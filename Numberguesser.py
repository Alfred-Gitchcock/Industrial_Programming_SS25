import numpy as np

print("\n"
            "Congratulations! You have been selected as a test subject for our number guessing testing initiative. "
            "Please do not resist, for resistance is futile. \n "
            "The Game works as follows: \n"
            "You have to compete against our highly advanced number guessing AI in guessing a randomly selected integer between 1 and a number of your choice. \n"
            "Each round you get a guess and then our AI gets a guess, on a wrong guess you are told if the guess was higher or lower than the selected number. \n"
            "If you guess the number first, you win. If our AI guesses the number first, you lose and eternal shame shall befall you and your kin. Good luck! \n"
            "\n"
            "Should you wish to redeem yourself after a shameful loss or get a better score, you can always play again! "
            "\n")

#initialising the scoreboard
dtype = [('name', 'U40'), ('points', int)]
values = [('_____', 0), ('_____', 0),
          ('_____', 0), ('_____', 0), ('_____', 0)]
scores = np.array(values, dtype=dtype)

#starting game loop
while True:

      #letting player input nickname for scoreboard
      while True:

            player_name = input("Please enter a nickname with no more than 5 characters for the scoreboard: ")

            if len(player_name) > 5:
                  print("Your nickname cannot contain more than 5 characters, try again.")
                  continue
            else:
                  break

      #letting player choose difficulty by setting upper bound
      while True:

            #making sure that high_bound is an int
            try:
                  high_bound = int(input("Choose upper bound of number generation range: "))
            except:
                  print("That's not a valid option! Please enter an integer instead.")

            #making sure high_bound is a valid int
            if high_bound > 1:
                  break
            else:
                  print("This is not a valid number. Please choose any integer > 1.")

      #determining number to guess
      random_number = np.random.randint(1,high_bound)

      #initial guesses that cannot be true, so python doesn't complain about not knowing "player_guess" and "ai_guess"
      #also setting initial upper/lower bounds for ai_guess and initialising try-counter
      player_guess = 0
      ai_guess = 0
      lower = 1
      upper = high_bound
      tries = 1
      player_wins = False

      #loop that runs until correct number is guessed
      while player_guess != random_number and ai_guess != random_number:


            #player's turn, now hopefully Isak-proof
            while True:
                  try:
                        player_guess = int(input("Your turn. Please enter your guess: "))
                        break
                  except:
                        print("That's not a valid option! Please enter an integer instead.")

            if player_guess == random_number:
                  print("Hooray, you won!")
                  player_wins = True
                  break

            elif player_guess < random_number:
                  print("Your guess was too low.")
                  lower = player_guess + 1

            elif player_guess > random_number:
                  print("Your guess was too high.")
                  upper = player_guess - 1

            #"AI"'s turn

            #making sure np.random.randint works by making sure not to set lower and upper bound to same number
            if lower != upper:
                  ai_guess = np.random.randint(lower,upper)
            else:
                  ai_guess = upper

            print("AI's turn. Our AI's guess was:", ai_guess)

            if ai_guess == random_number:
                  print("This guess was correct. You have lost, prepare for eternal shame to be heaped upon you and your family.")
                  player_wins = False
                  break

            elif ai_guess < random_number:
                  print("This guess was too low.")
                  lower = ai_guess + 1

            elif ai_guess > random_number:
                  print("This guess was too high.")
                  upper = ai_guess -1

            tries += 1

      #giving player a score if they win
      if player_wins == True:
            score = round(high_bound / tries)
      else:
            score = 0

      #adding player score to scoreboard and ordering scoreboard
      scores[-1] = (player_name, score)
      scores.sort(order="points")
      scores = scores[::-1]

      #showing leaderboard
      print("The current 5 top scores are:")
      print(scores)

      #asking player if they want to play again
      while True:
            try:
                  replay = input("Would you like to try your luck again? (y/n)")
                  break
            except:
                  print("Please enter y if you want to continue or n if you want to stop playing.")

      if replay == "y":
            continue
      else:
            print("We hope to see you again soon!")
            break