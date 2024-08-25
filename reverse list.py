#write a program to print the reverse of a list.
lst=[int(i) for i in input("Enter the list of integers:").split()]
size=len(lst)-1
for i in range(size,-1,-1):
    print((lst[i]), end="\t\n")
print()
print()
print()

#Another way to do this is as follows.
lst=[int(i) for i in input("Enter the list of integers:").split()]
for i in list(lst[ : :-1]):
    print(i,end="\t")
print()
print()
print()


#Another way to do this is as follows.
lst=[int(i) for i in input("Enter the list of integers:").split()]
lst=list(reversed(lst))
print(lst)