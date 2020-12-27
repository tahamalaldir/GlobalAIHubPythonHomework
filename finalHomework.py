import random as rnd
# classes


class Lessons():
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def showLesson(self):
        return(self.args[0])

    def countLesson(self):
        if len(self.args[0]) < 3:
            print("\n")
            return("You failed in class!", False)
        else:
            print("\n")
            return("Your number of lessons is enough", True)

    def gradeInfo(self):
        # calculating average
        result = (self.kwargs["midterm"]*0.3) + \
            (self.kwargs["final"]*0.5) + (self.kwargs["project"]*0.2)
        message = f"{self.kwargs} and your average : {result}"
        # course passing grade
        if result >= 90:
            return(message, "(AA)")
        elif 90 > result >= 70:
            return(message, "(BB)")
        elif 70 > result >= 50:
            return(message, "(CC)")
        elif 50 > result >= 30:
            return(message, "(DD)")
        elif 30 > result:
            print("\n")
            print("You Failed!!")
            return(message, "(FF)")


class Student():
    def __init__(self, name, srename):
        self.name = name
        self.surname = surname

    def hello(self):
        print(f"Welcome, {self.name} {self.surname}")


# variables
lesson_list = list()
entry = True
w_entries = 0
les_entry = True
cont_entry = ""
# taking login name and surname from user
log_name = input("Enter your login name : ").title()
log_surname = input("Enter your login surname : ").title()
print("\n")
while entry:
    # taking name and surname from user for check if it exist
    name = input("Name : ").title()
    surname = input("Surname : ").title()
    # check existing
    if (log_name == name) and (log_surname == surname):
        entry = False
        student = Student(name, surname)
        student.hello()
        print("\n")
        print("Lets enter your lessons!")
        while les_entry:
            print("\n")
            # taking lessons name from user
            lesson = input("Enter a lesson : ").title()
            lesson_list.append(lesson)
            # checking lessons nuber under 5
            if len(lesson_list) < 5:
                cont_entry = input(
                    "Do you want to enter another lesson? (press 'y' if you want to enter another lesson) : ").lower()
                if cont_entry == "y":
                    les_entry = True
                else:
                    cont_entry = input(
                        "Are you sure to entered all of your lessons? (press 'y' if you are sure) : ").lower()
                    if cont_entry == "y":
                        les_entry = False
                    else:
                        les_entry = True
            else:
                print("\n")
                print("Lesson list fully loaded. You can take 5 lessons!!")
                les_entry = False
        les_obj = Lessons(lesson_list)
        les = les_obj.countLesson()
        print(les[0])
        calc_grade = (les[1])
    else:  # if user enter name and surname 3 times incorrect
        if w_entries >= 3:
            print("\n")
            print("Please try again later")
            entry = False
            calc_grade = False
            break
        w_entries += 1
        print("\n")
        print("Check name and surname then please try again!",
              "\n", f"wrong entries : {w_entries}")
while calc_grade:
    calc_grade = False
    show_les = les_obj.showLesson()  # showing entered lessons
    print("\n")
    print("Entered lessons", show_les)
    sl_les = True
    while sl_les:
        print("\n")
        selected_les = input(
            "Select a lesson to calculating the grade : ").title()
        if selected_les in show_les:  # if selection is on the list
            print(f"Your selection is : {selected_les}")
            sl_les = False
        else:  # if selection is not on the list
            print("Your selection is not available. Please try again!")
    mid = rnd.randint(0, 100)  # assign a random number to midterm
    fin = rnd.randint(0, 100)  # assign a random number to final
    pro = rnd.randint(0, 100)  # assign a random number to project
    grad_obj = Lessons(midterm=mid, final=fin, project=pro)
    grad = grad_obj.gradeInfo()
    print("\n")
    print(grad)
print("\n")
print("Transaction Accomplished!")
