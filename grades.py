# GRADE MANAGEMENT SYSTEM

def average_calculation(marks):
    '''calculates the average from marks'''
    avg=sum(marks) / len(marks)
    return avg

def grading_assign(avg):
  ''' assigns the grade based on average '''
  if avg >= 90:
      grade="A"
  elif avg >= 80:
      grade="B"
  elif avg >= 70:
      grade="C"
  elif avg >= 60:
      grade="D"
  else:
      grade="F"
  return grade
    
def results(name,average,grade):
    ''' displays the results'''
    print(f"Student: {name}")
    print(F"Average Marks : {average}")
    print(f"Grade: {grade}")

name=input("Enter Your name: ")
marks=list(map(float,input("Enter your marks (5 subjects, separated by space): ").split()))

if len(marks)== 5:
  average = average_calculation(marks)
  grade = grading_assign(average)
  results(name,average,grade)
else:
  print("please enter exactly 5 subjects")