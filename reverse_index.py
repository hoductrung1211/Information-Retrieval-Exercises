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


sort_reverse_index= {k: reverse_index[k] for k in sorted(reverse_index)}


def query_reverse_index(query):
    query_words = preprocess_text(query)
    result = set(range(1,len(documents)+1))
    for word in query_words:
        if word in sort_reverse_index:
            result &= sort_reverse_index[word]
            
    
    return result




def df(word):
    # print(query_reverse_index(word))
    return len(list(query_reverse_index(word)))

def tf(word):
    count=0
    for doc in documents:
        doc_spilit=preprocess_text(doc)
        for i in range(len(doc_spilit)):
            if doc_spilit[i]==word:
                count+=1
    return count




        

# print(df())
# print(query_reverse_index_skip("USE OF",))




