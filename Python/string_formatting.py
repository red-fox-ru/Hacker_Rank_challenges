# Given an integer, 'n', print the following values for each integer 'i' from 1 to 'n' :

# Decimal, Octal, Hexadecimal, Binary

#Prints

# The four values must be printed on a single line in the order specified above for each 'i' from 1 to number . 
# Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.




def print_formatted(number):
    width = len(str(bin(number))) - 2
    for item in range(1, number + 1):
        print(f"{item:{width}d}", f"{item:{width}o}", f"{item:{width}X}", f"{item:{width}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
