cricket = input('Please enter your scores: ')
count = 1
all_cricket = cricket.split()

for score in cricket.split():
  print(f'score {count} = {score}')
  count = count + 1
