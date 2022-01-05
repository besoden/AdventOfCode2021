from time import perf_counter
t1_start = perf_counter()

diveplanX = 0
diveplanZ = 0

with open ('C:\\dev\\git\\AdventOfCode2021\\the-better-solutions\\diveplan.txt') as divePlanFile:
    for line in divePlanFile:
        if ('forward' in line):
            step = line.split(' ')[-1]
            diveplanX = diveplanX + int(step)
        elif ('down' in line):
            step = line.split(' ')[-1]
            diveplanZ = diveplanZ - int(step)
        elif ('up' in line):
            step = line.split(' ')[-1]
            diveplanZ = diveplanZ + int(step)

print(diveplanX)
print(diveplanZ)

answer = diveplanX * diveplanZ

print("The answer is: " + str(answer))

t1_stop = perf_counter()
print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)