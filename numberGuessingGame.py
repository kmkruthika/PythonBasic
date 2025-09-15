import random
number_to_guess=random.randint(1,100)
attempts=0

while True:
  guess=int(input("Enter the number u have guessed from 1 to 100"))
  attempts+=1

  if guess<number_to_guess:
    print("too low")
  elif guess>number_to_guess:
    print("Too high")
  else:
    print("Congratulations guessed it right")
    print("Total number of attempts:",attempts)
    print("Thank you")
    break