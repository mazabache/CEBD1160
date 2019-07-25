import string

words = input("Please enter a sentence: ")
words = words.strip(string.punctuation)
counter = dict()
words = words.split()

for word in words:

        if word in counter:

            counter[word] += 1

        else:

            counter[word] = 1

print(counter)







