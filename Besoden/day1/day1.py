from time import perf_counter

t1_start = perf_counter()

depths = open("day1input.txt").read().splitlines()

numDepth = 0

for i in range(0, len(depths) - 1):
    if int(depths[i + 1]) > int(depths[i]):
        numDepth = numDepth + 1

print(numDepth)

t1_stop = perf_counter()
print("Elapsed time during the whole program in seconds:",
      t1_stop - t1_start)
