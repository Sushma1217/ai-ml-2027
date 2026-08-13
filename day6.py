import numpy as np

import numpy as np

numbers = np.array([10,20,30,40,50,60])
print("ndim", numbers.ndim)
print("shape",numbers.shape)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("arr_2d",arr_2d.shape)  

print("size", numbers.size)
print("arr_2d size", arr_2d.size)

print("dtype", numbers.dtype)
print("arr_2d dtype", arr_2d.dtype)

# np calculations

sum = np.sum(numbers)
print("sum",sum)
mean = np.mean(numbers)
print("mean",mean)
minimum = np.min(numbers)
print("minimum",minimum)
maximum = np.max(numbers)
print("maximum",maximum)
standard_deviation = np.std(numbers)
print("standard_deviation",standard_deviation)

# Vectorization
print("numbers * 2: ",numbers * 2)
print("numbers +10 : ",numbers + 10)
print("numbers / 10: ",numbers / 10)
print("numbers ** 2: ",numbers ** 2)

# Indexing and slicing
scores  = np.array([45, 67, 89, 32, 76, 91, 55])

# Find:

# First score
print("first score", scores[0])

# Last score
print("first score", scores[-1])

# First three scores
print("First three scores", scores[0:3])

# Last three scores
print("last three scores", scores[-3:])

# Scores from index 2 to 5
print("Scores from index 2 to 5", scores[2:6])

# Every second score
print("Every second score", scores[::2])

# Find all scores greater than 60.
high_scores = scores[scores>60]
print("Every second score", high_scores)
# if we want index then
print("Every second score", np.where(scores>60))

# 2d arrays
marks = np.array([
    [80, 75, 90],
    [65, 70, 60],
    [90, 88, 95],
    [55, 60, 58]
])
# Think of this as:
#            Math  Science English
# Student 1   80     75      90
# Student 2   65     70      60
# Student 3   90     88      95
# Student 4   55     60      58

# Number of students
num_of_students = np.shape(marks)[0]
print("num_of_students",num_of_students)

# Number of subjects
num_of_subjects = np.shape(marks)[1]
print("num_of_subjects",num_of_subjects)

# Marks of Student 1
num_of_student_1 = marks[0]
print("num_of_student_1",num_of_student_1)

# English marks of all students
english_marks = marks[:,2]  
print("english_marks",english_marks)

# Average marks of each student
avg_marks = np.mean(marks, axis=1)
print("avg_data",avg_marks)

# Average marks of each subject
avg_subject_marks = np.mean(marks, axis=0)
print("avg_subject_marks",avg_subject_marks)

# Highest mark
highest_marks = np.max(marks)
print("highest_marks",highest_marks)

# Student with the highest total
total_marks = np.sum(marks, axis=1)
highes_mark = np.max(total_marks)
highest_mark_Student = np.argmax(total_marks)
print("highest_mark_Student ",highest_mark_Student, highes_mark)

# Find the students whose average is greater than 75.
# students_above_75 = [i for i, val in enumerate(avg_marks) if val >75]
students_above_75 = np.where(avg_marks>75)[0]
print("students_above_75 ",students_above_75)


# Day 6 mini-project
# Student Performance Analyzer

# Total marks for each student
total_marks_student = np.sum(marks, axis=1)
print("total_marks_student",total_marks_student)

# Average marks for each student
avg_each_student  = np.mean(marks, axis=1)
print("avg_each_student",avg_each_student)

# Highest scorer
highest_scorer = np.argmax(total_marks_student)
print("highest_scorer",highest_scorer)

# Lowest scorer
lowesr_scorer = np.argmin(total_marks_student)
print("lowesr_scorer",lowesr_scorer)

# Subject-wise average
sub_wise_avg  = np.mean(marks, axis=0)
print("sub_wise_avg",sub_wise_avg)

# Students who scored >75 average
student_scoded_above_75 = np.where(avg_each_student>75)
print("student_scoded_above_75",student_scoded_above_75)

# Overall class average
overall_class_avg = round(np.mean(marks),2)
print("overall_class_avg",overall_class_avg)
