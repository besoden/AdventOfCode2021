from time import perf_counter

t1_start = perf_counter()

commands = []

i = 0
with open('day2input.txt', 'r') as openfile:
    for line in openfile:
        commands.append([])
        commands[i] = tuple(line.split(' '))
        i += 1

depth = 0
x_pos = 0
for command in commands:
    if command[0] == 'forward':
        x_pos += int(command[1])
    elif command[0] == 'up':
        depth -= int(command[1])
    else:
        depth += int(command[1])

print('answer = ' + str((int(depth) * int(x_pos))))

t1_stop = perf_counter()
print("Elapsed time during the whole program in seconds:",
      t1_stop - t1_start)