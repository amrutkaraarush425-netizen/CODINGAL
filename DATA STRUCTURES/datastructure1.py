n = 4

guess = input("Total point:1+2+3+4=")

input("Formula: One calculation. Press Enter To Run")
total = n (n + 1) // 2
print(" total=", total, "steps = 1")

input("Loop: adds one student at a time. Press Enter to run")
total = 0
for student in range(1, n+1):
    total+= student
    print("toal =", total, "steps=", n)

input("Double Loop: Counts every single point. Press Enter to Run")
total =0
steps =0
for students in range(1, n+1):
    for