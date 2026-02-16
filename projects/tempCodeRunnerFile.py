sentence = input("enter a sentence please: ")
words = sentence.split()
reverse_words = words[::-1]
reverse_sentence = " ".join(reverse_words)
print(reverse_sentence)
