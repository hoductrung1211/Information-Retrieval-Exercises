import read_file_to_array as src
import re

#  Select number of lines
documents=src.read_file()[:60]

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]+", " ", text)
    return text.split()

reverse_index = {}
reverse_index2 = {}

for i, document in enumerate(documents):
    words = preprocess_text(document)
    for word in words:
        if word not in reverse_index:
            reverse_index[word] = set()
        reverse_index[word].add(i+1)
    # for j, word in enumerate(words):
    #     if word not in reverse_index2:
    #         reverse_index2[word] = set()
    #     reverse_index2[word].add((i+1, j+1))

sort_reverse_index= {k: reverse_index[k] for k in sorted(reverse_index)}
# print table 
# print(reverse_index)
# print(reverse_index2)

def query_reverse_index(query):
    query_words = preprocess_text(query)
    result = set(range(len(documents)))
    for word in query_words:
        if word in reverse_index:
            result &= reverse_index[word]
    return result

print(query_reverse_index("USE"))
print(query_reverse_index("OF"))
print(query_reverse_index("USE OF"))




