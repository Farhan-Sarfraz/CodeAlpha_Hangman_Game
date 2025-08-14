import random

word_list = ["anger", "nature", "apple", "football", "cricket", "hockey"]

chosen_word  = random.choice(word_list)

lives = 6

print(f"Chosen word is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

wrong_guesses = []
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter. ").lower()

    if guess in display or guess in wrong_guesses:
       print(f"You've already guessed {guess}.\n")
       continue

    if guess in chosen_word:
       for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
         display[position] = letter
    
    else:
       wrong_guesses.append(guess)
       print(f"You guessed {guess}, That's not in word_list.\n")
       lives -= 1
       if lives == 0:
          end_of_game = True
          print("You lose.\n ")

        
    print(' '.join(display))

    print(display)

    if "_" not in display:
       end_of_game = True
       print("You win! \n ")
