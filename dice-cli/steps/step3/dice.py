import random
num_rolls = 3
for _ in range(num_rolls):
  dice = [random.randint(1,6) for _ in range(2)]
  print(*dice)
