# Tuple for fixed courses
tuple1 = (("CS101", "Dr.Mehta"), ("CS102", "Dr.Ajay Parikh"), ("CS103", "Dr.Dhirenbhai"))
print("Available Courses : ", tuple1)

# Dictionary for course-wise students
dict1 = {"CS101": {"hardik", "dikshit"}, "CS102": set(), "CS103": set()}

# List to store multiple students name
List1=["hardik","dikshit"]
choise = 0

while choise != 2:
    print("\nDo you want to add a Student \n 1.Yes \n 2.No ")
    choise =input("Enter your choice 1 or 2 : ")
    
    if choise.isdigit():
        choise=int(choise)
        if choise<3 and choise>0:
            if choise == 1:
                    CourseCode = input("Enter Course Code as Above : ")
                    std = input("Enter Student Name : ")

                    if CourseCode not in dict1:
                        print(" Invalid Course Code!")
                    elif std in dict1[CourseCode]:
                        print(f" Student '{std}' already enrolled in {CourseCode}")
                    else:
                        dict1[CourseCode].add(std)
                        List1.append(std)
                        print(f" Added '{std}' to {CourseCode}")
                        print("Updated Students in this course: ", dict1[CourseCode])
            else:
                print("\n All Enrolled Students")
                print(List1)
                print("\n All Enrolled Students (Course-wise):")
                for code, students in dict1.items():
                    print(f"{code}: {students}")
        else:
            print("Choise is not 1 or 2 Enter valid choise..")
    else:
            print("Enter Valid input...")
