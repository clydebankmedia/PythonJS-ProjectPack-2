import random
import math

num_rolls = 10
total, doubles, mn, mx = 0, 0, math.inf, -math.inf
rolls = []
for _ in range(num_rolls):
  dice = [random.randint(1,6) for _ in range(2)]
  roll = sum(dice)

  # We don't need this here, but will need for median and mode below
  rolls.append(roll)

  # stats
  mn = min(mn, roll)
  mx = max(mn, roll)
  total += roll
  
  # tricky way to check for doubles: sets remove any duplicates, so if
  # all dice are the same the set will only have 1 element. A simple
  # for loop would also work.
  doubles += len(set(dice)) == 1

  print(*dice, f"\t({roll})")

print(f"""---- Stats ----
Min: {mn}
Mean: {total / num_rolls:.2f}         
Max: {mx}
Num doubles: {doubles}""")
