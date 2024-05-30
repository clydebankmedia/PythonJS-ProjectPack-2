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

# For median, the key is sorting, and averaging if len is even.
mid = num_rolls // 2
sorted_rolls = sorted(rolls)
median = sorted_rolls[mid]
if num_rolls % 2 == 0:
  median += sorted_rolls[mid-1]
  median /= 2

print(f"Median: {median}")  

# Mode can be tricky since there can be multiple modes
from collections import Counter
most_common = Counter(rolls).most_common()
mode_vals = [ most_common[0][0] ] # at least that value, but maybe more
mode_count = most_common[0][1] # count of most common value
for val, count in most_common[1:]:
  if count == mode_count:
    mode_vals.append(val)
  else: # we hit something different; all rest will be smaller
    break

print(f"Mode: {', '.join(str(x) for x in mode_vals)} (each appeared {mode_count} time(s))")
