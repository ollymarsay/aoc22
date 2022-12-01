elves = open("01/input.txt").read().split("\n\n")
calories = [sum(map(int, elf.split())) for elf in elves]
print(max(calories), sum(sorted(calories)[-3:]))