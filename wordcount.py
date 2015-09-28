text_file = open("test.txt")
word_counts = {}

for line in text_file:
    words = line.split(" ")
    for word in words:
        word = word.rstrip()
        if word not in word_counts:
            word_counts[word] = 1
        else:  # word already in word_counts
            word_counts[word] += 1

for word, count in word_counts.items():
    print word, count