#writing a program to convert numbers from base ten to other bases and vice versa.
print("1.From base ten to binary, octadecimal and hexadecimal.\n2.From other bases to base ten.")
mode=input("Choose the mode you want:")
if mode == "1":
    print("1.Binary\n2.octadecimal\n3.hexadecimal")
    base=input("choose the destination base:")
    if base == "1":
        number=int(input("Enter the number:"))
        bin_number=format(number, "b")
        print(bin_number)
    if base == "2":
        number=int(input("Enter the number:"))
        oct_number=oct(number)
        print(oct_number)
    if base == "3":
        number=int(input("Enter the number:"))
        hex_number=format(number, "0x")
        print(hex_number)
else:
    number=input("Enter the number:")
    base=int(input("Enter the base of the number you entered:"))
    result=int(number, base)
    print(result)




