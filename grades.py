print("=" * 40)
print("  STUDENT GRADE MANAGEMENT")
print("=" * 40)

students = []
names = []
roll_nums = []
all_marks = []

n = int(input("\nHow many students? "))

for i in range(n):
    print(f"\nStudent {i+1}:")
    name = input("Name: ")
    roll = input("Roll Number: ")
    
    print("Enter marks (out of 100):")
    m1 = float(input("  Subject 1: "))
    m2 = float(input("  Subject 2: "))
    m3 = float(input("  Subject 3: "))
    m4 = float(input("  Subject 4: "))
    m5 = float(input("  Subject 5: "))
    
    marks = [m1, m2, m3, m4, m5]
    
    names.append(name.strip().title())
    roll_nums.append(roll.upper())
    all_marks.append(marks)
    
    total = sum(marks)
    avg = total / len(marks)
    percent = (total / 500) * 100
    
    grade = ""
    if percent >= 90:
        grade = "A+"
    elif percent >= 80:
        grade = "A"
    elif percent >= 70:
        grade = "B"
    elif percent >= 60:
        grade = "C"
    elif percent >= 50:
        grade = "D"
    else:
        grade = "F"
    
    status = "Pass" if percent >= 40 else "Fail"
    
    student_data = {
        "name": names[i],
        "roll": roll_nums[i],
        "marks": marks[:],
        "total": total,
        "average": avg,
        "percentage": percent,
        "grade": grade,
        "status": status
    }
    
    students.append(student_data)

print("\n" + "=" * 80)
print("GRADE REPORT")
print("=" * 80)

for s in students:
    print(f"\nName: {s['name']}")
    print(f"Roll No: {s['roll']}")
    print(f"Marks: {s['marks']}")
    print(f"Total: {s['total']:.2f} | Average: {s['average']:.2f} | Percentage: {s['percentage']:.2f}%")
    print(f"Grade: {s['grade']} | Status: {s['status']}")
    print("-" * 80)

print("\n" + "=" * 80)
print("CLASS STATISTICS")
print("=" * 80)

pass_count = 0
fail_count = 0
for s in students:
    if s['status'] == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print(f"Total Students: {len(students)}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")

percentages = []
for s in students:
    percentages.append(s['percentage'])

class_avg = sum(percentages) / len(percentages)
highest = max(percentages)
lowest = min(percentages)

print(f"\nClass Average: {class_avg:.2f}%")
print(f"Highest Percentage: {highest:.2f}%")
print(f"Lowest Percentage: {lowest:.2f}%")

sorted_students = students[:]
for i in range(len(sorted_students)):
    for j in range(i+1, len(sorted_students)):
        if sorted_students[i]['percentage'] < sorted_students[j]['percentage']:
            temp = sorted_students[i]
            sorted_students[i] = sorted_students[j]
            sorted_students[j] = temp

print("\n" + "=" * 80)
print("TOP PERFORMERS")
print("=" * 80)

top_3 = sorted_students[:3]
for idx, student in enumerate(top_3):
    print(f"{idx+1}. {student['name']} - {student['percentage']:.2f}%")

print("\n" + "=" * 80)
print("SUBJECT WISE ANALYSIS")
print("=" * 80)

sub_names = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

for sub_idx in range(5):
    sub_total = 0
    for s in students:
        sub_total += s['marks'][sub_idx]
    
    sub_avg = sub_total / len(students)
    print(f"{sub_names[sub_idx]}: Average = {sub_avg:.2f}")

print("\n" + "=" * 80)

choice = input("\nSearch for a student? (y/n): ")

if choice.lower() == 'y':
    search = input("Enter name or roll number: ").strip()
    found = False
    
    for s in students:
        if search.lower() in s['name'].lower() or search.upper() == s['roll']:
            print(f"\nFound!")
            print(f"Name: {s['name']}")
            print(f"Roll: {s['roll']}")
            print(f"Percentage: {s['percentage']:.2f}%")
            print(f"Grade: {s['grade']}")
            found = True
            break
    
    if not found:
        print("Student not found!")

print("\n" + "=" * 80)
print("Thank you for using the system!")
print("=" * 80)