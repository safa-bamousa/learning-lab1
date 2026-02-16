import string
sentence = input("\nPlease type a sentence")
new_sentence = ""
for x in sentence :
    if x not in string.punctuation :
        new_sentence += x

print(f"Your sentence without punctuation: {new_sentence}")