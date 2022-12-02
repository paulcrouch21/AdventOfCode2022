import sys

def main():
     with open(sys.argv[1]) as myFile:
          lines = myFile.readlines()
          lines = [line.strip() for line in lines]
          lines = [line.split() for line in lines]

     #part 01
     score = 0
     newScore = 0
     for x in lines:
          score += checkPoints(x[0], x[1])
          newScore += newCheckPoints(x[0], x[1])

     print(f'The total score for the player is {score} [part 01]')
     print(f'The total score for the player is {newScore} [part 02]')

#checking points for part 01
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

#checking points for part 02
def newCheckPoints(opponent, outcome):
     points = 0

     #points for the outcome
     if outcome == 'Y':
          points += 3
     elif outcome == 'Z':
          points += 6

     #points for the shape used by the player
     if (opponent == 'B' and outcome == 'X') or (opponent == 'A' and outcome == 'Y') or (opponent == 'C' and outcome == 'Z'):
          #if we need to use rock
          points += 1
     elif (opponent == 'C' and outcome == 'X') or (opponent == 'B' and outcome == 'Y') or (opponent == 'A' and outcome == 'Z'):
          #if we need to use paper
          points += 2
     elif (opponent == 'A' and outcome == 'X') or (opponent == 'C' and outcome == 'Y') or (opponent == 'B' and outcome == 'Z'):
          #if we need to use scissors
          points += 3

     return points

if __name__ == '__main__':
     main()