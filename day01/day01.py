import sys

with open(sys.argv[1]) as myFile:
     lines = myFile.readlines()
     lines = [line.strip() for line in lines]

#part 01
totalWeightPerElf = []

weight = 0
for x in lines:
     if x != '':
          weight += int(x)
          if x == lines[len(lines) - 1]:
               totalWeightPerElf.append(weight)
     else:
          totalWeightPerElf.append(weight)
          weight = 0

print(f'The highest calories the elf is carrying is {max(totalWeightPerElf)}')

#part 02
totalWeightPerElf = sorted(totalWeightPerElf, reverse=True)
counter = 0
topThreeElves = 0
while counter < 3:
     topThreeElves += totalWeightPerElf[counter]
     counter += 1

print(f'The top 3 elves are carrying a total of {topThreeElves} calories')
