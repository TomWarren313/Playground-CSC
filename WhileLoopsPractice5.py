flag = True
count = 0
total = 0
while flag:
  try:
    score = int(input('Please enter your test scores (-1 to stop): '))
    if score == -1:
      flag = False
    elif score > 0 and score <= 100:
      total = total + score
      count = count + 1
    else:
      print('This number is either too high or too low.')
  except ValueError:
    print('The score you just entered is invalid! Please enter an actual valid score.')
if count > 0:
    average = total / count
    print(f'The average test score is {average:.2f}')
else:
    print('No valid scores were entered.')