import os
import string

filepath = os.getcwd()
inputpath = os.path.join(filepath, "CT08_09/encrypted_note.txt")
outputpath = os.path.join(filepath, "CT08_09/hidden_message.txt")

if os.path.exists(inputpath):
    with open(inputpath, 'r') as file:
        content = file.read()
        print(content)
else:
    print("ERROR: The encrypted note has vanished. Is someone trying to hide the truth?")

clean_text = content
for c in clean_text:
    if c in string.punctuation:
        clean_text = clean_text.replace(c, " ")
clean_text = clean_text.lower()
print(clean_text)

words = clean_text.split()
decoded_message = ""
for word in words:
    decoded_message = decoded_message + word[0]
print(decoded_message)

with open(outputpath, 'w')as file:
    file.write(decoded_message[::-1])