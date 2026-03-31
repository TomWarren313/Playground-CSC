guess = int(input('Please enter a number between 1 and 10: '))
while guess != 7:
  try:
    if guess < 1 or guess > 10:
      print('That number is out of range, try again!')
      guess = int(input('Please enter a number between 1 and 10: '))
    else: 
    print('That is not the correct number, try again!')
    guess = int(input('Please enter a number between 1 and 10: '))
  except ValueError:
    print('Please enter a valid number!')
    guess = int(input('Please enter a number between 1 and 10: '))
print('Congratulations, you guessed the correct number!')