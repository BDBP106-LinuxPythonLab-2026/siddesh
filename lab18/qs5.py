# def remove_duplicates(sentence):
#     words = sentence.split()
#
#     unique_words = dict.fromkeys(words)
#
#     return " ".join(unique_words)
#
#
# # Example usage
# text = "Python is great and Python is easy to learn"
# print(remove_duplicates(text))





def remove_duplicates(sentence):
    seen = set()
    unique_dict = {}

    for word in sentence.split():
        if word not in seen:
            seen.add(word)
            unique_dict[word] = True

    return " ".join(unique_dict.keys())

text = "Python is great, Python is easy to learn and today I'm learning new things in Python."
print(remove_duplicates(text))
