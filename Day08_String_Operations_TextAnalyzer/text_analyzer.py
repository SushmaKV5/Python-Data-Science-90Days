#Text analyzer

text = input("Enter a paragraph:")

#Convert to lower case for consistent analysis
clean_text = text.lower()
word_list = clean_text.split()

num_characters = len(text)
num_words = len(word_list)
num_sentence = text.count(".") + text.count("!") + text.count("?")

vowels = "aeiou"
vowel_count = 0

for char in clean_text:
    if char in vowels:
        vowel_count += 1


print("\nText analysis result:")
print("Number of characters:", num_characters)
print("Number of words:", num_words)
print("Number of sentence:", num_sentence)
print("Number of vowels:", vowel_count)

#Most frequent word
word_frequency = {}
for word in word_list:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

most_frequent_word = max(word_frequency, key=word_frequency.get)

print("Most frequent word:", most_frequent_word)
print("Frequenct:", word_frequency[most_frequent_word])

