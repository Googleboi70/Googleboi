#writing a program to print the even, odd and prime numbers in a range or list and their respective sum and count.
print("1. Range", "2. List", sep = "\n")
mode = input("Enter the mode you want:")
sum = 0
count = 0
lst = []
if mode == "1":
    start = int(input("Enter the start range:"))
    stop = int(input("Enter the stop range:"))
    step = int(input("Enter the step range:"))
    for i in range(start, stop+1, step):
        if i % 2 == 0:
            sum += i
            count += 1
            lst.append(i)
    else:
        print(f"The even numbers in this range are {lst}", f"Their sum is {sum}", f"Their count is {count}.",  sep = "\n")
        print("\n")
    count = 0
    sum = 0
    lst = []
    for i in range(start, stop+1, step):
        if i % 2 == 1:
            sum += i
            count += 1
            lst.append(i)

    else:
        print(f"The odd numbers in this range are {lst}",f"Their sum is {sum}", f"Their count is {count}", sep = "\n")
        print("\n")
    sum = 0
    count = 0
    lst = []
    for i in range(start, stop+1, step):
        if i > 1:
            for num in range(2, i):
                if i % num == 0:
                    break
            else:
                sum += i
                count += 1
                lst.append(i)
    print(f"The prime numbers in this range are: {lst}", f"The sum of the prime numbers in this range is {sum}.", f"The count of the prime numbers in this range is :{count}.", sep = "\n")
else:
    if mode == "2":
        num = [int(i) for i in input("Enter the list of integers:").split()]
        sum = 0
        count = 1
        lst = []
        for i in num:
            if i % 2 == 0:
                sum += i
                count += 1
                lst.append(i)
        else:
            print(f"The even numbers in this list are: {lst}.", "Their sum is {}".format(sum), "Their count is %d" % (count), sep="\n")
            print("\n\n")
        sum = 0
        count = 0
        lst = []
        for i in num:
            if i % 2 == 1:
                sum += i
                count += 1
                lst.append(i)
        else:
            print(f"The odd numbers in this list are: {lst}", f"The sum of the odd numbers in this list is :{sum}", f"Their count is :{count}", sep="\n")
            print("\n\n")
            sum = 0
            count = 0
            lst = []
            for i in num:
                if i > 1:
                    for j in range(2, i):
                        if i % j == 0:
                            break
                    else:
                        sum += i
                        count += 1
                        lst.append(i)
            else:
                print(f"The prime numbers in this list is :{lst}", f"The sum of the prime numbers in this list is :{sum}", f"Their count is :{count}", sep="\n")





