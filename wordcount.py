import sys 
import collections

text_file = open(sys.argv[1])
big_word_list = []

#clean words, line by line, and add them to big_word_list
for line in text_file:
    cleaned_words = []
    line = line.replace("--", " ")
    raw_words = line.split(" ")

    for word in raw_words:
        #strip all punctuation and lowercase word
        word = word.strip("\'\"\n\t-,./?!:;()*[]_").lower()
        #add word to list of cleaned words
        cleaned_words.append(word)

    #add all cleaned words from this line to overall list of words
    big_word_list.extend(cleaned_words)

    

    #     # #if word not found, add it
    #     # if word not in word_counts:
    #     #     word_counts[word] = 1

    #     # # otherwise, word already in word_counts, so increment count
    #     # else:  
    #     #     word_counts[word] += 1

    #     #if word not found, add it
    #     if word_counts.get(word) == None:
    #         word_counts[word] = 1

    #     # otherwise, word already in word_counts, so increment count
    #     else:
    #         word_counts[word] += 1

word_counts = collections.Counter(big_word_list)

for word, count in word_counts.items():
    print word, count

# print word_counts.keys()