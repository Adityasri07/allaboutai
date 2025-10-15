marks = []

for i in range(5):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)      

    average = sum(marks) / len(marks)
def get_grade(avg) :
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
grade = get_grade(average)

print(f"Marks: {marks}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
