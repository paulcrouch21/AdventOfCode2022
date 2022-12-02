import sys

def main():
     with open(sys.argv[1]) as myFile:
          lines = myFile.readlines()
          lines = [line.strip() for line in lines]
          lines = [line.split() for line in lines]

     #part 01
     score = 0
     for x in lines:
          score += checkPoints(x[0], x[1])

     print(f'The total score for the player is {score}')

def checkPoints(opponent, player):
     points = 0

     #points for the shape used by the player
     if player == 'X':
          points += 1
     elif player == 'Y':
          points += 2
     elif player == 'Z':
          points += 3

     #points for the outcome of the round
     if (opponent == 'A' and player == 'Y') or (opponent == 'B' and player == 'Z') or (opponent == 'C' and player == 'X'):
          points += 6
     elif (opponent == 'A' and player == 'X') or (opponent == 'B' and player == 'Y') or (opponent == 'C' and player == 'Z'):
          points += 3

     return points

if __name__ == '__main__':
     main()