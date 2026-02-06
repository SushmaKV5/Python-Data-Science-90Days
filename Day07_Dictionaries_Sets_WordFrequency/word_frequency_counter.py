# Word Frequency Counter

text = input("Enter a sentence: ").lower()

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

frequency = {}
print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
    frequency[word] = count

print(frequency)

# Using set to show unique words
unique_words = set(words)

print("\nUnique words:")
print(unique_words)
