import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
word = random.choice(word_list)
output_str = "-"*len(word)
print(logo)
while lives:
    guess = input("Guess a letter\n")
    correct = False
    if guess in output_str:
      print("you already guessed "+guess)
      print(output_str)
      print(stages[lives])
    else:
      for i in range(len(word)):
          if(word[i] == guess ):
              replace = list(output_str)
              replace[i] = guess
              output_str = "".join(replace)
              correct = True
      if not correct:
          lives-=1
          print("you guessed "+guess+", that's not in the word. You lose a life")
          print(stages[lives])
          print(output_str)
      else:
        print(output_str)
        print(stages[lives])
    if output_str == word:
        print("you won")
        quit()
    
print("you lost, the word was "+word)