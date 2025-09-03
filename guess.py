# Write code below 
guess = 0
tries = 5
guess = int(input("Guess the number:  "))
while guess != 6 and tries <= 5:
  
  tries -= 1
  if tries <= 0:
    break
  

    print("you are out of tries")

  if guess != 6 and tries >0:
  
    print("guess again")
  
    print(f"You have {tries} left")
  
    guess = int(input("Guess the number: "))
  
  
  
  
  

if guess == 6:
  print("You got it")