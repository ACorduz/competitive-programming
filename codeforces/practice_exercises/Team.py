n = int(input())
problemsSolved = 0
approvesParticipant = 0

while n != 0:
    problem = input()
    problemList = problem.split()

    for participant in problemList:
        if participant == '1':
            approvesParticipant = approvesParticipant + 1

    if approvesParticipant >= 2:
        approvesParticipant = 0
        problemsSolved = problemsSolved + 1
    else:
        approvesParticipant = 0

    n = n-1
        
print(problemsSolved)    
