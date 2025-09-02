
#  Count the frequency of words in a sentence.

sentence = "                    Count the frequency of words in a sentence.            "
stripped_str = sentence.strip()

count_of_words = stripped_str.count(' ')+1

print(f"count of words in given sentence {count_of_words}")


# Output:
# count of words in given sentence 8
