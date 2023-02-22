
def avg(mark):
    length = len(mark)
    sum = 0
    for i in mark:
        sum = sum + int(i)
        
    avg = sum / (length+1)
    return avg

def cgpa(percent):
    if(percent >= 90):
        return "O"
    elif(percent >= 80):
        return "E"
    elif(percent >= 70):
        return "A"
    elif(percent>=60):
        return "B"
    else:
        return "F"

def display(mark):
    average = avg(mark)
    CGPA = cgpa(average)
    
    print("the average mark of the student is ",average)
    print("And the CGPA is ",CGPA)

marks = []
n = int(print("Enter number of subjects: "))
for i in range(1,n+1):
    x = float(print("Enter marks: "))
    marks.append(x)
display(marks)
