# https://realpython.com/python-coding-interview-tips/

# defaultdict to not have to check if key exists

from collections import defaultdict

student_grades = defaultdict(list)

grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88)
]

for name, grade in grades:
    student_grades[name].append(grade)

print(student_grades)
# prints out: defaultdict(<class 'list'>, {'elliot': [91, 88], 'neelam': [98], 'bianca': [81]})
