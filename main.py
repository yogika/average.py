# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

print(student_heights)
#Write your code below this row 👇

total=0
for i in student_heights:
  total=i+total
print(total)  
no_of_student=0
for j in student_heights:
  no_of_student+=1
print(no_of_student)  

average_of_student=total/no_of_student
print(average_of_student)





