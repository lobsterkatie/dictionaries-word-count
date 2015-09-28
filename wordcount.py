text_file = open("test.txt")
word_counts = {}

for line in text_file:
    words = line.split(" ")
    for word in words:
        word = word.rstrip()

        # #if word not found, add it
        # if word not in word_counts:
        #     word_counts[word] = 1

        # # otherwise, word already in word_counts, so increment count
        # else:  
        #     word_counts[word] += 1

        #if word not found, add it
        if word_counts.get(word) == None:
            word_counts[word] = 1
            
        # otherwise, word already in word_counts, so increment count
        else:
            word_counts[word] += 1

for word, count in word_counts.items():
    print word, count