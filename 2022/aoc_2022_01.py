# https://adventofcode.com/2022/day/1

def create_elf_calorie_roster(file):
	with open(file) as f:
		elf, elves = 0, []
		file_handler = f.read()
		
		for each in file_handler.split('\n'):
			if each == '':
				elves.append(elf)
				elf = 0
			else:
				elf = elf + int(each)
	return(elves)

def most_calories(elf_calorie_roster):
	return(max(elf_calorie_roster))

def top_three_calories(elf_calorie_roster):
	top_three = []
	for i in range(0,3):
		# Find the most calories held
		top_calories = most_calories(elf_calorie_roster)
		top_three.append(top_calories)

		# Remove that value from list
		elf_calorie_roster.pop(elf_calorie_roster.index(top_calories))
	return(top_three)

# Using test input
elf_roster_test = create_elf_calorie_roster('aoc_2022_01_test.txt')
print(most_calories(elf_roster_test))
print(sum(top_three_calories(elf_roster_test)))

# Using puzzle input
elf_roster = create_elf_calorie_roster('aoc_2022_01.txt')
print(most_calories(elf_roster))
print(sum(top_three_calories(elf_roster)))
