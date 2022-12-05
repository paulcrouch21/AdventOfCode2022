import sys

def main():
     with open(sys.argv[1]) as myFile:
          lines = myFile.readlines()
          lines = [line.strip() for line in lines]
          lines = [line.split(',') for line in lines]

     print(f'There are {part01(lines)} assignment pairs that are contained in another [part 01]')
     print(f'There are {part02(lines)} assignment pairs that overlap at all [part 02]')

def part01(input):

     totalPairs = 0
     for x in input:
          firstSet = x[0].split('-')
          secondSet = x[1].split('-')
          pair1 = [x for x in range(int(firstSet[0]), int(firstSet[1]) + 1)]
          pair2 = [x for x in range(int(secondSet[0]), int(secondSet[1]) + 1)]
          if (all(x in pair1 for x in pair2)) or (all(x in pair2 for x in pair1)):
               totalPairs += 1

     return totalPairs

def part02(input):

     totalPairs = 0
     for x in input:
          firstSet = x[0].split('-')
          secondSet = x[1].split('-')
          pair1 = [x for x in range(int(firstSet[0]), int(firstSet[1]) + 1)]
          pair2 = [x for x in range(int(secondSet[0]), int(secondSet[1]) + 1)]
          
          for value in pair1:
               if value in pair2:
                    totalPairs += 1
                    break

     return totalPairs

if __name__ == '__main__':
     main()