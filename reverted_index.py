import read_file_to_array as src
import re

#  Select number of lines
documents=src.read_file()[:60]

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]+", " ", text)
    return text.split()

reverse_index = {} 

for i, document in enumerate(documents):
    # Split documents into words
    words = preprocess_text(document)

    for word in words:
        if word not in reverse_index:
            reverse_index[word] = set()
        reverse_index[word].add(i+1) 


sort_reverse_index= {k: reverse_index[k] for k in sorted(reverse_index)}


def query_reverse_index(query):
    # Tokenize query into separated words
    query_words = preprocess_text(query)

    result = set(range(len(documents)))

    for word in query_words:
        if word in sort_reverse_index:
            result &= sort_reverse_index[word]
       
    return result

# print(query_reverse_index("USE"))
# print(query_reverse_index("OF"))
# print(query_reverse_index("USE OF"))




def intersect_with_skip(p1, p2, skip):
    i1 = 0
    i2 = 0
 
    ans = []

    len1 = len(p1)
    len2 = len(p2)

    while ( i1 < len1 and i2 < len2):
        
        if p1[i1] == p2[i2]:
            ans.append(p1[i1])
            i1 += 1
            i2 += 1
        
        elif p1[i1] < p2[i2]:
            if (i1 + skip < len1 and p1[i1 + skip] <= p2[i2]):
                while (i1 + skip < len1 and p1[i1 + skip] <= p2[i2]):
                    i1 += skip
            else:
                i1 += 1
        elif (i2 + skip < len2 and p2[i2 + skip] <= p1[i1]):
            while (i2 + skip < len2 and p2[i2 + skip] <= p1[i1]):
                i2 += skip 
        else: i2 += 1

    return ans



def set_to_array(s):
    arr = list(s)
    arr.sort() 
    return arr
    
    


def final_skip(query, skip = 3):
    # Tokenize query into separated words
    query_words = preprocess_text(query)

     
    set_doremon = sort_reverse_index[query_words[0]]
    doremon = set_to_array(set_doremon)

 
    for word in query_words[1:]:
        arr_word = set_to_array(sort_reverse_index[word])
        doremon = intersect_with_skip(doremon, arr_word, skip)
    
    return doremon

res = final_skip("use of", 3) 
print(res)
