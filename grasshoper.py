'''
passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
'''
def getGrade (s1, s2, s3):
  avg = (s1 +s2 + s3) / 3
  grades = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 0}
  for grade, score in grades.items():
    if avg >= score:
      return grade