import json

students = []
count = 0

def save_data():
    global students
    f = open("student_data.json", "wt")
    json.dump({"student_data": students}, f)

def load_data():
    global students
    try:
        f = open("student_data.json")
        students = json.load(f)["student_data"]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        students = []

load_data()

def addStudent():
    global count
    newStudent = {
        "rollNumber": int(input("Enter Roll Number: ")),
        "name": input("Enter Name: "),
        "parentAddress": input("Enter Parent's Address: "),
        "parentContact": input("Enter Parent's Contact: "),
        "studentContact": input("Enter Student's Contact: "),
        "marksMaths": int(input("Enter Marks in Maths: ")),
        "marksPhysics": int(input("Enter Marks in Physics: ")),
        "marksEEE": int(input("Enter Marks in EEE: ")),
        "marksSemiconductor": int(input("Enter Marks in Semiconductor: ")),
        "marksEnglish": int(input("Enter Marks in English: ")),
        "marksPPS": int(input("Enter Marks in PPS: ")),
        "totalHoursMaths": int(input("Enter Total Hours in Maths: ")),
        "attendedHoursMaths": int(input("Enter Attended Hours in Maths: ")),
        "totalHoursPhysics": int(input("Enter Total Hours in Physics: ")),
        "attendedHoursPhysics": int(input("Enter Attended Hours in Physics: ")),
        "totalHoursEEE": int(input("Enter Total Hours in EEE: ")),
        "attendedHoursEEE": int(input("Enter Attended Hours in EEE: ")),
        "totalHoursSemiconductor": int(input("Enter Total Hours in Semiconductor: ")),
        "attendedHoursSemiconductor": int(input("Enter Attended Hours in Semiconductor: ")),
        "totalHoursEnglish": int(input("Enter Total Hours in English: ")),
        "attendedHoursEnglish": int(input("Enter Attended Hours in English: ")),
        "totalHoursPPS": int(input("Enter Total Hours in PPS: ")),
        "attendedHoursPPS": int(input("Enter Attended Hours in PPS: "))
    }

    students.append(newStudent)
    count += 1
    save_data()
    print("Student added successfully!")

def editStudent(rollNumber):
    found = False
    for student in students:
        if student["rollNumber"] == rollNumber:
            print("\nStudent Found! Enter new details:\n")
            student["name"] = input("Enter Name: ")
            student["parentAddress"] = input("Enter Parent's Address: ")
            student["parentContact"] = input("Enter Parent's Contact: ")
            student["studentContact"] = input("Enter Student's Contact: ")
            student["marksMaths"] = int(input("Enter Marks in Maths: "))
            student["marksPhysics"] = int(input("Enter Marks in Physics: "))
            student["marksEEE"] = int(input("Enter Marks in EEE: "))
            student["marksSemiconductor"] = int(input("Enter Marks in Semiconductor: "))
            student["marksEnglish"] = int(input("Enter Marks in English: "))
            student["marksPPS"] = int(input("Enter Marks in PPS: "))
            student["totalHoursMaths"] = int(input("Enter Total Hours in Maths: "))
            student["attendedHoursMaths"] = int(input("Enter Attended Hours in Maths: "))
            student["totalHoursPhysics"] = int(input("Enter Total Hours in Physics: "))
            student["attendedHoursPhysics"] = int(input("Enter Attended Hours in Physics: "))
            student["totalHoursEEE"] = int(input("Enter Total Hours in EEE: "))
            student["attendedHoursEEE"] = int(input("Enter Attended Hours in EEE: "))
            student["totalHoursSemiconductor"] = int(input("Enter Total Hours in Semiconductor: "))
            student["attendedHoursSemiconductor"] = int(input("Enter Attended Hours in Semiconductor: "))
            student["totalHoursEnglish"] = int(input("Enter Total Hours in English: "))
            student["attendedHoursEnglish"] = int(input("Enter Attended Hours in English: "))
            student["totalHoursPPS"] = int(input("Enter Total Hours in PPS: "))
            student["attendedHoursPPS"] = int(input("Enter Attended Hours in PPS: "))
            print("Student information updated successfully!")
            found = True
            save_data()
            break

    if not found:
        print("Student not found!")



def deleteStudent(rollNumber):
    found = False
    for i, student in enumerate(students):
        if student.rollNumber == rollNumber:
            print("\nStudent Found! Deleting student...\n")
            students.pop(i)
            count -= 1
            print("Student deleted successfully!")
            found = True
            save_data()
            break

    if not found:
        print("Student not found!")


def findStudent(rollNumber):
    found = False
    for student in students:
        if student["rollNumber"] == rollNumber:
            print("\nStudent Found!")
            print("Roll Number:", student["rollNumber"])
            print("Name:", student["name"])
            print("Parent's Address:", student["parentAddress"])
            print("Parent's Contact:", student["parentContact"])
            print("Student's Contact:", student["studentContact"])
            print("Marks in Maths:", student["marksMaths"])
            print("Physics Marks:", student["marksPhysics"])
            print("EEE Marks:", student["marksEEE"])
            print("Semiconductor Marks:", student["marksSemiconductor"])
            print("English Marks:", student["marksEnglish"])
            print("PPS Marks:", student["marksPPS"])
            print("Maths Attendance: {:.2f}%".format((student["attendedHoursMaths"] / student["totalHoursMaths"]) * 100))
            print(
                "Physics Attendance: {:.2f}%".format((student["attendedHoursPhysics"] / student["totalHoursPhysics"]) * 100))
            print("EEE Attendance: {:.2f}%".format((student["attendedHoursEEE"] / student["totalHoursEEE"]) * 100))
            print("Semiconductor Attendance: {:.2f}%".format(
                (student["attendedHoursSemiconductor"] / student["totalHoursSemiconductor"]) * 100))
            print(
                "English Attendance: {:.2f}%".format((student["attendedHoursEnglish"] / student["totalHoursEnglish"]) * 100))
            print("PPS Attendance: {:.2f}%".format((student["attendedHoursPPS"] / student["totalHoursPPS"]) * 100))
            found = True
            break

    if not found:
        print("Student not found!")


def calculateAttendance(student):
    attendanceMaths = 0.0
    attendancePhysics = 0.0
    attendanceEEE = 0.0
    attendanceSemiconductor = 0.0
    attendanceEnglish = 0.0
    attendancePPS = 0.0

    if student.totalHoursMaths > 0:
        attendanceMaths = (student["attendedHoursMaths"] / student["totalHoursMaths"]) * 100

    if student.totalHoursPhysics > 0:
        attendancePhysics = (student["attendedHoursPhysics"] / student["totalHoursPhysics"]) * 100

    if student.totalHoursEEE > 0:
        attendanceEEE = (student["attendedHoursEEE"] / student["totalHoursEEE"]) * 100

    if student.totalHoursSemiconductor > 0:
        attendanceSemiconductor = (student["attendedHoursSemiconductor"] / student["totalHoursSemiconductor"]) * 100

    if student.totalHoursEnglish > 0:
        attendanceEnglish = (student["attendedHoursEnglish"] / student["totalHoursEnglish"]) * 100

    if student.totalHoursPPS > 0:
        attendancePPS = (student["attendedHoursPPS"] / student["totalHoursPPS"]) * 100

    print("\nAttendance Details for Roll Number {}:".format(student["rollNumber"]))
    print("Maths: {:.2f}%".format(attendanceMaths))
    print("Physics: {:.2f}%".format(attendancePhysics))
    print("EEE: {:.2f}%".format(attendanceEEE))
    print("Semiconductor: {:.2f}%".format(attendanceSemiconductor))
    print("English: {:.2f}%".format(attendanceEnglish))
    print("PPS: {:.2f}%".format(attendancePPS))


def displayMenu():
    print("\n----- Student Record Management System -----")
    print("1. Add Student")
    print("2. Edit Student")
    print("3. Delete Student")
    print("4. Find Student")
    print("5. Calculate Attendance")
    print("6. Exit")
    print("--------------------------------------------")


def main():
    choice = 0

    while choice != 6:
        displayMenu()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            addStudent()
        elif choice == 2:
            rollToEdit = int(input("Enter Roll Number of the student to edit: "))
            editStudent(rollToEdit)
        elif choice == 3:
            rollToDelete = int(input("Enter Roll Number of the student to delete: "))
            deleteStudent(rollToDelete)
        elif choice == 4:
            rollToFind = int(input("Enter Roll Number of the student to find: "))
            findStudent(rollToFind)
        elif choice == 5:
            roll = int(input("Enter Roll Number of the student to calculate attendance: "))
            found = False
            for student in students:
                if student["rollNumber"] == roll:
                    calculateAttendance(student)
                    found = True
                    break
            if not found:
                print("Student not found!")
        elif choice == 6:
            print("Exiting...")
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
