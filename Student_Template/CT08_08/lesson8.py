import os

filepath = os.getcwd()
fullpath = os.path.join(filepath, "sherlock.txt")

if not os.path.exists(fullpath):
    print("sherlock.txt is not found")

with open(fullpath, 'r') as file:
    lines = file.read()

print('Total characters: ' + str(len(lines)))

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for c in lines:
    if c in vowels:
        vowels[c] += 1

print('Total vowels: ' + str(sum(vowels.values())))

print('Vowel counts:')
for vowel, count in vowels.items():
    print(f"{vowel}: {count}")