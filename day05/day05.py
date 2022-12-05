import sys

def main():
     #reads the input file and separates into two parts
     with open(sys.argv[1]) as myFile:
          cratesAndDirections = myFile.read()[:-1].split('\n\n')
          crates = cratesAndDirections[0].split('\n')
          #list containing sublists that represents every stack
          stacks = [[] for _ in range(len(crates))]
          
          for i in range(len(crates)):
               line = crates[i]
               letters = line[1::4]
               for s in range(len(letters)):
                    if letters[s] != ' ':
                         stacks[s].append(letters[s])

     #make the bottom of the stack index 0 - reverse the string
     stacks = [stack[::-1] for stack in stacks]

     #print(f'The crates that end up on top of each stack is {part01(stacks, cratesAndDirections[1])} [part 01]')
     #print(f'The crates that end up on top of each stack is {part02(stacks, cratesAndDirections[1])} [part 02]')

def part01(crateStacks, directions):

     for line in directions.split('\n'):
          tokens = line.split(' ')
          n, source, destination = map(int, [tokens[1], tokens[3], tokens[5]])
          source -= 1
          destination -= 1

          #moves the crate to the desired location
          for _ in range(n):
               pop = crateStacks[source].pop()
               crateStacks[destination].append(pop)

     topOfStacks = [stack[-1] for stack in crateStacks]

     return ''.join(topOfStacks)

def part02(crateStacks, directions):

     for line in directions.split('\n'):
          tokens = line.split(' ')
          n, source, destination = map(int, [tokens[1], tokens[3], tokens[5]])
          source -= 1
          destination -= 1

          crateStacks[destination].extend(crateStacks[source][-n:])
          crateStacks[source] = crateStacks[source][:-n]

     topOfStacks = [stack[-1] for stack in crateStacks]

     return ''.join(topOfStacks)


if __name__ == '__main__':
     main()