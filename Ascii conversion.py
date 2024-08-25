#writing a program to print Ascii charcters and numbers.
print("1. From character to number.\n2. From number to character.")
mode=input("Enter the mode you want:")
if mode =="1":
    char=input("Enter the character to be converted:")
    print(ord(char))
else:
    num=int(input("Enter the number to be converted:"))
    print(chr(num))
