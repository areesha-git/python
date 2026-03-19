# write a program to accpet marks of 6 students and display them in a sorted manner

#marks=[45,34,87,23,67,87,]
#marks.sort()
# printmarks)

# input by user 
marks = []
s1 = int(input("Enter 1 marks here :"))
marks.append(s1)
s2 = int(input("Enter 2 marks here :"))
marks.append(s2)
s3 = int(input("Enter 3 marks here :"))
marks.append(s3)
s4 = int(input("Enter 4 marks here :"))
marks.append(s4)
s5 = int(input("Enter 5 marks here :"))
marks.append(s5)
s6 = int(input("Enter 6 marks here :"))
marks.append(s6)

marks.sort()
print(marks)