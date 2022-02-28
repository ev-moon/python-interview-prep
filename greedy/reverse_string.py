string = input()

changes_to_zero = changes_to_one = 0
if string[0] == "0":
    changes_to_one += 1
else:
    changes_to_zero += 1

for idx, char in enumerate(string[1:]):
    if char != string[idx]:
        if char == "1":
            changes_to_zero += 1
        if char == "0":
            changes_to_one += 1

print(min(changes_to_zero, changes_to_one))