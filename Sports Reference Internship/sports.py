import json

data = open('/Users/revantkantamneni/Downloads/team.json')
teamData = json.load(data) #Load json data into dictionary

#Printing First Line of Team Names
print('\n')
print('Team', end = '\t')
for team in teamData:
    print(team, end ='\t')
print('\n')

#Iterating through dictionary to find head-to-head record between two teams
for team in teamData:
    print(team, end ='\t')
    for opposition in teamData:
        if team != opposition:
            print(teamData[team][opposition]['W'], end ='\t')
        else:
            print('--', end ='\t')
    print('\n')

#Printing Bottom Line of Team Names
print('Team', end = '\t')
for team in teamData:
    print(team, end ='\t')
print('\n')


    




