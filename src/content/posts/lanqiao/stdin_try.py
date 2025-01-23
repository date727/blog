import sys
name=sys.stdin.readline().strip()
grades=sys.stdin.readline().strip()
grade1=int(grades.split()[0])
grade2=int(grades.split()[1])
print("{}:{} {}".format(name,grade1,grade2))