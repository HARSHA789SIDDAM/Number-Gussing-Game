import random
print("Welcome to Guess The Number Game: ".center(90))
print("\n")
limt = int(input("Enter the guesseing limit from 1 to "))
def guess(limt):
  random_number = random.randint(1,limt)
  count = 0
  guess = 0
  while(guess!=random_number):
    guess = int(input(f"Enter the number betrween 1 and {limt}: "))
    count+=1
    if guess<random_number:
      print("Sorry! your guess is less. Please try again")
    elif guess>random_number:
      print("Sorry! your guess is high. Please try again")
  print(f"Yay,congrats you have gussed the correct number {random_number} in {count} attempts")
guess(limt)
