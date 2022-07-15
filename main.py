countries = ["Ghana","Mexico","Sierra Leone","Senegal"]
for each in countries:
  print(each)
  print(f"I really want to visit {each}")
#In line 4 the code goes through each item in the countries list and prints it out, before going to the next item.Line 4 instruction gets carried out for as many times as the for loop needs to print. So if 3 items in list then it gets carried out 3 times.

print("==============================")

student_heights = input("Input a list of random student heights").split()


#One method of calculating average height of students
#total_height = sum(student_heights)
#number_of_students = len(student_heights)
#average_height = round(total_height) / round(number_of_students)
#print(average_height)
#print("==========================")
#second method of calculating average height of students.

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
#Line 25 states that for each item(height) in the student heights list we are going to add the height all together.
for height in student_heights:
  total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
  number_of_students +=1
#line 31 says we will add 1 to 0, each time the for loop runs. This will tell us how many items in for loop, as for loop will run for as many times as there are items in the list. 
print(number_of_students)

average_height = round(total_height) / round(number_of_students)
print(average_height)

print("=============================")
#Code to generate the highest score student score in list
student_scores = input ("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f" The highest score in the class is:{highest_score}")

print("================================")
# The below code will find the sum of all numbers from 1 to 100 by using for loop.
total = 0
for number in range(1, 101):
  total += number
print(total)

print("======================")
#The below code will add up all the even numbers from 0 to 100
total = 0
for number in range(2, 101, 2):
  total += number
print(total)
