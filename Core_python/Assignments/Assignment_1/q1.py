#Write a program to calculate the percentage of student based on marks of any 5 subjects.


#input marks of 5 subjects from user

sub1 = float(input("Enter marks for subject 1 out of 100: "))
sub2 = float(input("Enter marks for subject 2 out of 100: "))
sub3 = float(input("Enter marks for subject 3 out of 100: "))
sub4 = float(input("Enter marks for subject 4 out of 100: "))
sub5 = float(input("Enter marks for subject 5 out of 100: "))


#calculate total marks obtained

total_marks_obtained = sub1 + sub2 + sub3 + sub4 + sub5

#calculate percentage
per = total_marks_obtained / 5

#print the percentage
print("The percentage of the student is:", per, "%")