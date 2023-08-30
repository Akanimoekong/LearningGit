# A simple program to cal a student's score base on their grade:
score=0
grades=['A','B','C','D','E','F']
for grade in grades:
    if grade=='A':
        score+=5
    elif grade=='B':
        score+=4
    elif grade=='C':
        score+=3
    elif grade=='D':
        score+=2
    elif grade=='E':
        score=1
    print (f"score:{score}")
