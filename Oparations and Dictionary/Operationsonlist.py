lis = ['Apple', 'Guava', 'mango', 'Banana', 'Kiwi']

print("Length of list:",len(lis))
print("First Element:",lis[0])
print("Last Element:",lis[-1])

lis.append('Papaya')
print("Updated List :", lis)

lis.remove('Guava')
print("Updated List :", lis)

lis.sort()
print("Sorted List:", lis)

lis.pop(1)
print("Updated pop List:", lis)

lis.reverse()
print("Reversed List:", lis)

print("Multiplication on List:", lis*2)

lis = lis[:2]
print("Sliced List:", lis)

lis.clear()
print("Updated List:", lis)




