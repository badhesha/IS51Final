"""
structured-english

Start
Download the text file titled Final.txt, which has the list of students grades.
Next, create a function that will show the total number of grades, the average grades, and the percentage of grades
that are above average. The final percentages the function should output for 
average grade is 83.25%. The percentage for the grade above average 
is 54.17%. The total number of grades is 24.
End

"""
"""
pseudo-code

Open "Final.txt"
create a variable named grades to strip from list
len(grades) #return length of list
Initalize counter and sum to 0
add the grade to the sum
average function = sum(grades)/len(grades)
Initalize counter and sum to 0
num = 0 #for number of grades above average
if grade > average
num += 1
(100*num)/len(grades) #format percentage
print "Number of Grades"
print "Average Grade"
Print "Percentage of grades above average"

"""