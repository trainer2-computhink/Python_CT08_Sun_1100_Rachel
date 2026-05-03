f = open("CT08_08/sherlock.txt", "r")
words = f.read().lower().split()
newchar = []
for char in words:
    if char.isalnum() or char == " ":
        newchar.append(char.lower())
print("done")

word = input("What word are you searching for?: ").lower().strip()
newword = []
for char in word:
    if char.isalpha():
        newword.append(char)
word = "".join(newword)
wordcount = 0



while True:
    if word in words:
        wordcount += 1
        words.remove(word)
    else:
        break
print(f'The word "{word}" appears {wordcount} times.')