import os

filepath = os.getcwd()
fullpath = os.path.join(filepath, "sherlock.txt")

if not os.path.exists(fullpath):
    print("No file or directory \'sherlock.txt\' found.")

with open(fullpath, 'r') as file:
    lines = file.read()
    total_characters = len(lines)
    print("Total characters: " + str(total_characters))

vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

for c in lines:
    if c.lower() in vowels:
        vowels[c.lower()] += 1

total_vowels = sum(vowels.values())

print("Total vowels: " + str(total_vowels))

print("Vowel frequency: ")
for vowel, frequency in vowels.items():
    print(f"{vowel} = {frequency}")

percentage_of_vowels = (total_vowels / total_characters) * 100

print(f"Percentage of Vowels in Text: {percentage_of_vowels:.2f}")

lines = []
lines.append("Vowel counts in 'sherlock.txt':")
for vowel, frequency in vowels.items():
    lines.append(f"\n{vowel} = {frequency}")
lines.append(f"\nPercentage of Vowels in 'sherlock.txt': {percentage_of_vowels:.2f}")

with open("vowel_counts.txt", 'w') as file:
    file.writelines(lines)