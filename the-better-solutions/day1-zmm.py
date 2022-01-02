sonarData = []
with open ('sonarreport.txt') as sonarIn:
    for line in sonarIn:
        sonarData.append(int(line))
sonarIncrease = 0
for i in range(len(sonarData)):
    if sonarData[i] > sonarData[i-1]:
        sonarIncrease += 1
print(sonarIncrease)