#split in half
#determine most common value in each half
#determine the priority of that value
#sum all of them up together
import sys

def main():
     with open(sys.argv[1]) as myFile:
          lines = myFile.readlines()
          lines = [line.strip() for line in lines]

     print(f'The sum of the priorities of the item types are {part01(lines)} [part01]')
     print(f'The sum of the priorities of the item types are {part02(lines)} [part02]')

def part01(input):
     sum = 0

     #splits the string in half
     for x in input:
          n = len(x)
          if n % 2 == 0:
               firstHalf = x[0:n//2]
               secondHalf = x[n//2:]
          else:
               firstHalf = x[0:(n//2+1)]
               secondHalf = x[(n//2+1):]
          #get the character that appears in each half
          mostCommonChar = ''.join(set(firstHalf).intersection(secondHalf))
          #adds the value of each character to the sum
          sum += valueOfLetter(mostCommonChar)

     return sum

def part02(input):
     sum = 0

     #divide the list by groups of 3
     counter = 0
     while counter < len(input):
          string1 = input[counter]
          string2 = input[counter + 1]
          string3 = input[counter + 2]
          #determines the most common character in each group
          mostCommonChar = ''.join(set(string1).intersection(string2))
          mostCommonChar = mostCommonChar.join(set(mostCommonChar).intersection(string3))
          sum += valueOfLetter(mostCommonChar)
          counter += 3

     return sum

def valueOfLetter(letter):
     #create a list of the alphabet
     alphabet = []
     for i in range(97, 123):
          alphabet.append(chr(i))

     #if the letter is uppercase, we add 26
     value = 1
     if letter.isupper():
          value += 26
          letter = letter.lower()

     #determines what value the letter is
     for x in alphabet:
          if letter == x:
               return value
          else:
               value += 1  

     return value

if __name__ == '__main__':
     main()