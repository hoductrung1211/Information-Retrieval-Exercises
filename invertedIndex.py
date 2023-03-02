import re

docs = [{
    "id": 1,
    "text": "I did enact Julius Caesar: I was killed in the Capitol; Brutus killed me.",
}, {
    "id": 2,
    "text": "So let it be with Caesar. The noble Brutus hath told you Caesar was ambitious:",
}]

# Preprocess the documents to remove special characters and convert to lowercase
processed_docs = []
for doc in docs: 
    processed_doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc["text"]).lower()
    processed_docs.append({
        "id": doc["id"],
        "text": processed_doc
    })
 
 
term_docIDs = {}
for doc_obj in processed_docs:
    for word in doc_obj["text"].split():
        if word in term_docIDs:
            length = len(term_docIDs[word])
            if term_docIDs[word][length - 1] != doc_obj["id"]:
                term_docIDs[word].append(doc_obj["id"])
        else:
            term_docIDs[word] = [doc_obj["id"]]


# for key in term_docIDs:
#     print(key, term_docIDs[key])

# ########################################
# ########################################

# p1: posting 1
# p2: posting 2
def intersect(p1, p2):
    ans = []
    len1 = len(p1)
    len2 = len(p2)
    i1 = 0
    i2 = 0

    while (i1 < len1 and i2 < len2): 
        if p1[i1] == p2[i2]:
            ans.append(p1[i1])
            i1 += 1
            i2 += 1
        elif p1[i1] < p2[i2]:
            i1 += 1
        else:
            i2 += 1
    
    return ans 

# # print(intersect(term_docIDs['caesar'], term_docIDs['brutus']))


# ########################################
# ########################################
def intersect_step(p1, p2, step):
    if step < 1:
        step = 1
    ans = []
    len1 = len(p1)
    len2 = len(p2)
    i1 = 0
    i2 = 0

    while (i1 < len1 and i2 < len2): 
        if p1[i1] == p2[i2]:
            ans.append(p1[i1])
            i1 += 1
            i2 += 1
        elif p1[i1] < p2[i2]: 
            i1 += step
        else: 
            i2 += step
    
    return ans 

print(intersect_step( [2, 4, 8, 41, 48, 64, 128], [1, 2, 3, 8, 11, 17, 21, 31], 1))

 
def intersect_with_skip(postings_list_1, postings_list_2, skip_size):
    result = []
    i = 0
    j = 0
    while i < len(postings_list_1) and j < len(postings_list_2):
        if postings_list_1[i] == postings_list_2[j]:
            result.append(postings_list_1[i])
            i += 1
            j += 1
        elif postings_list_1[i] < postings_list_2[j]:
            # Skip over entries in postings_list_1
            k = i + skip_size
            while k < len(postings_list_1) and postings_list_1[k] < postings_list_2[j]:
                k += skip_size
            i = k
        else:
            # Skip over entries in postings_list_2
            k = j + skip_size
            while k < len(postings_list_2) and postings_list_2[k] < postings_list_1[i]:
                k += skip_size
            j = k
    return result
