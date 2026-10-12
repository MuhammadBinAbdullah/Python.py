classmates = ["Muhammad", "Abdul Ahad", "Safwan", "Murtaza"]
print("Class List :", classmates)

print("Total Students :", len(classmates))
print("First Students :", classmates[0])
print("Last Student :", classmates[-1])
print("First Three :", classmates[:3])

classmates.append("Abdul Ahad")
print("\nAfter Adding Abdul Ahad :", classmates)
classmates.remove("Murtaza")
print("After Removing Murtaza :", classmates)
classmates.sort()
print("Sorted Alphabetically :", classmates)
classmates.reverse()
print("Reversed :", classmates)

teacher = {"Name" : "Muhammad", "Subject" : "Python", "Experience" : 5}
print("\nTeacher Profile :", teacher)

print("Subject :", teacher["Subject"])
print("Experience :", teacher.get("experience", "Not Found"))
teacher["Experience"] = 6
teacher["Email"] = "abdullahmuhmmadbin148@gmail.com"
teacher.pop("Experience")
print("Updated Teacher Profile :", teacher)

roll_numbers = [1, 2, 3, 4, 5]
names = ["Muhammad", "Abdul Ahad", "Safwan", "Murtaza"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory :", student_directory)
print("Student At Roll 3 :", student_directory[3])