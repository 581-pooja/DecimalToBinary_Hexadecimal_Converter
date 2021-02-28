print("Welcome to the Binary/Hexadecimal Converter App");
# Binary :Base 2 no.system Hexadecimal base:16 decimal base: 10

# Get user input and generate lists:
max_value = int(input("\nCompute binary and hexadecimal values up to the following decimal number:"))
decimal = range(1,max_value+1)
binary = []
hexadecimal = []    
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating lists...complete!")

# print(binary)
# print(hexadecimal)
# print(decimal)

# bin(number)
# number ,Return the binary representation of an integer.
# eg bin(2) 

# Get Slicing index from User:
print("Using slices, we will now show a portion of each list.")
lower_range = int(input("What decimal number would you like to start at: "))
upper_range = int(input("What decimal number would you like to stop at: "))

# Slice through each list individually
print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")
for num in decimal[lower_range-1:upper_range]:
    print(num)
# Since lower_range start from 0 it takes 2 index as 1 therefore lower_range-1

print("\nBinary values from " + str(lower_range) + " to " + str(upper_range) + ":")
for num in binary[lower_range-1:upper_range]:
    print(num)

print("\nHexadecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)

# Output the whole list to the screen
input("\nPress Enter to see all values from 1 to " + str(max_value) + ".")
print("Decimal----------Binary----------Hexadecimal")
for d, b, h in zip(decimal,binary,hexadecimal):
    print(str(d)+ "---------" + str(b) + "---------" + str(h) )


# zip:Here, you use zip(decimal , binary , hexadecimal) to create an iterator 
# that produces tuples of the form (x, y ,z). 
# In this case, the x values are taken from decimal and the y values are taken from binary.
# z values are taken from hexadecimal.
# Notice how the Python zip() function returns an iterator: 
# To retrieve the final list object, you need to use list() to consume the iterator.