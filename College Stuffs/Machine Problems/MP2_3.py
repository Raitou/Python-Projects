strGrade = ""
strGrade = str(input("Enter grade:"))

fGradePoints = -1.0

if strGrade == "A+":
  fGradePoints = 4.0
elif strGrade == "A":
  fGradePoints = 4.0
elif strGrade == "A-":
  fGradePoints = 3.7
elif strGrade == "B+":
  fGradePoints = 3.3
elif strGrade == "B":
  fGradePoints = 3.0
elif strGrade == "B-":
  fGradePoints = 2.7
elif strGrade == "C+":
  fGradePoints = 2.3
elif strGrade == "C":
  fGradePoints = 2.0
elif strGrade == "C-":
  fGradePoints = 1.7
elif strGrade == "D+":
  fGradePoints = 1.3
elif strGrade == "D":
  fGradePoints = 1.0
elif strGrade == "F":
  fGradePoints = 0
  
  
if fGradePoints == -1.0:
  print("Invalid grade entered.")
else:
  print("For this grade, you will receive a grade points of {}".format(fGradePoints))
  
  