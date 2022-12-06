import sys

def main():
     with open(sys.argv[1]) as myFile:
          lines = myFile.readlines()
          lines = [line.strip() for line in lines]

     print(f'There are {part01(lines[0])} characters that need to be processed before the first start-of-packet maker is detected. [part 01]')

def part01(data):

     counter = 0
     while counter < len(data):
          inputSet = set(data[counter:counter + 4])
          if len(inputSet) == 4:
               return counter + 4
          counter += 1


if __name__ == '__main__':
     main()