# A die roll is really just a RNG: 1-6. So this is not much
# more than the RNG, though the simulation and statistical aspect adds
# a bit more.
# We'll use `argparse` here for some extra meat.
# https://docs.python.org/3/library/argparse.html
import random
import math
from argparse import ArgumentParser
from collections import Counter

parser = ArgumentParser(description="Simulate dice rolls and optionally show statistics.")

# could use `dest="verbose"`, but it figures it out.
parser.add_argument("-v", "--verbose", action="store_true", default=False,
                    help="show result of all coin flips, even if stats=True")
# could specify `action="store"`, but that's the default.
parser.add_argument("-d", "--num-dice", type=int, default=1,
                    help="specify the number of dice [default %(default)s]")
parser.add_argument("-r", "--num-rolls", type=int, default=1,
                    help="specify the number of rolls [default %(default)s]")
parser.add_argument("-s", "--num-sides", type=int, default=6,
                    help="specify the number of die sides [default %(default)s]")
parser.add_argument("-t", "--stats", action="store_true", default=False,
                    help="compute and show stats")
args = parser.parse_args()

# You can pass a function to the `type` argument in `add_argument` to
# make this a bit cleaner.
if args.num_rolls <= 0 or args.num_dice <= 0:
  print("Number of rolls and number of dice require positive integers.")
  exit(1)
if args.num_sides < 2:
  print("Number of sides must be at least 2.")
  exit(1)

total, doubles = 0, 0
mn, mx = math.inf, -math.inf
rolls = []
for _ in range(args.num_rolls):
  dice = [random.randint(1, args.num_sides) for _ in range(args.num_dice)]
  roll = sum(dice)
  rolls.append(roll)
  mn = min(mn, roll)
  mx = max(mx, roll)
  total += roll
  #doubles += (sum([x == dice[0] for x in dice]) == len(dice))
  doubles += len(set(dice)) == 1
  if args.verbose or not args.stats:
    print(*dice, end='')
    if args.num_dice > 1:
      print(f"\t({roll})", end='')
    print() # newline

if args.stats:
  #mode = Counter(rolls).most_common()[0]
  most_common = Counter(rolls).most_common()
  mode_vals = [most_common[0][0]]
  mode_count = most_common[0][1]
  for val, count in most_common[1:]:
    if count == mode_count:
      mode_vals.append(val)
    else:
      break

  
  mid = args.num_rolls // 2
  sorted_rolls = sorted(rolls)
  median = sorted_rolls[mid]
  if args.num_rolls % 2 == 0:
    median += sorted_rolls[mid-1]
    median /= 2
  print(f"""---- Stats ----
Min: {mn}
Mean: {total / args.num_rolls:.2f}         
Median: {median}
Mode: {', '.join(str(x) for x in mode_vals)} (each appeared {mode_count} time(s))
Max: {mx}""")
  if args.num_dice > 1:
    print(f"Num doubles: {doubles}")         
  

  


