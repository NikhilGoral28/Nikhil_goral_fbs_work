""". Enter number of students from user. For those many students accept marks of 5  
 
subject marks from user and calculate percentage. Display all percentage and  
average percentage of students."""


n = int(input("Enter number of students: "))

percentages = []
for i in range(n):
    print(f"Enter marks for student {i + 1}:")
    total_marks = 0
    for j in range(5):
        marks = float(input(f"  Subject {j + 1} marks: "))
        total_marks += marks
    percentage = (total_marks / 500) * 100
    percentages.append(percentage)
    print(f"Percentage of student {i + 1}: {percentage:.2f}%")
average_percentage = sum(percentages) / n
print(f"Average percentage of all students: {average_percentage:.2f}%")