n = int(input("Enter the number of elements to be entered: "))
a = []
for i in range (0, n):
    elem = int(input("Enter elem: "))
    a.append(elem)
avg = sum(a)/n

print ("Ave. elements in the list ", round(avg,2))
