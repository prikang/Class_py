"""
{
    1: {"math": 36, "science": 80, "english": 90},
    2: {"math": 36, "science": 80, "english": 90},
    3: {"math": 36, "science": 80, "english": 90},
    4: {"math": 36, "science": 80, "english": 90},
    5: {"math": 36, "science": 80, "english": 90}
}

#create function get_grade(mark) return grade
"""
def get_grade(marks):
    if marks>=90 and marks<=100:
        print("A+")
    elif marks>=80 and marks<=90:
        print("A")
    elif marks>=70 and marks<=80:
        print("B+")
    elif marks>=60 and marks<=70:
        print("B")
    elif marks>=50 and marks<=60:
        print("C+")
    elif marks>=40 and marks<=50:
        print("C")
    elif marks>=30 and marks<=40:
        print("D+")
    elif marks>=20 and marks<=30:
        print("D")
    else:
        print("Fail")

marks = {
1: {"math": 36, "science": 80, "english": 90},
2: {"math": 36, "science": 80, "english": 90},
3: {"math": 12, "science": 10, "english": 5},
4: {"math": 92, "science": 54, "english": 80},
5: {"math": 54, "science": 90, "english": 90},
}
for student_id,scores in marks.items():
    total_marks=sum(scores.values())
    average_marks=total_marks/len(scores)
    get_marks=get_grade(average_marks)



print(f"Student{student_id}-Average Mark:{average_marks:2f},Grade:{get_marks}")
