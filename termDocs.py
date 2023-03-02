import re

docs = [
    "I did enact Julius Caesar: I was killed in the Capitol; Brutus killed me.",
    "So let it be with Caesar. The noble Brutus hath told you Caesar was ambitious: I did",
]

# Preprocess the documents to remove special characters and convert to lowercase
processed_docs = []
for doc in docs: 
    processed_doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc).lower()
    processed_docs.append(processed_doc)

# Split the processed documents into words and create a set of unique terms
terms = set()
for doc in processed_docs:
    for word in doc.split():
        terms.add(word)

# Sort the terms and create a dictionary to map each term to its index
sorted_terms = sorted(list(terms))
term_indices = {term: i for i, term in enumerate(sorted_terms)}

# Create an empty term-document matrix
matrix = [[0] * len(processed_docs) for _ in range(len(sorted_terms))]

# Fill in the matrix with the counts of each term in each document
for j, doc in enumerate(processed_docs):
    for word in doc.split():
        i = term_indices[word]
        matrix[i][j] += 1

# print(sorted_terms)

# for index, row in enumerate(matrix):
#     print(sorted_terms[index], row)



###########################################################
###########################################################
""" We first split the query into individual terms and 
initialize a list to store the scores of each document. 
Then, we iterate over the query terms and 
add the corresponding term frequencies from the term-document matrix
to the document scores. 
Finally, we sort the document scores in descending order and
print the ranked documents along with their scores."""

def query1(query_str, term_doc_matrix, unique_terms, documents):
    # Split query into individual terms
    query_terms = re.sub(r'[^a-zA-Z0-9\s]', '', query_str).lower().split()
    print("Query term here buddy: ", query_terms, "\n\n")

    # Initialize a list to store the document scores
    scores = [0] * len(documents)
    # print("Scores: ", scores, "\n\n")

    # Calculate the score for each document
    for i in range(len(documents)):
        for term in query_terms:
            if term in unique_terms:
                term_index = unique_terms.index(term)
                scores[i] += term_doc_matrix[term_index][i]
                print(scores)

    # Sort the document scores in descending order
    ranked_docs = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    # Print the ranked documents and their scores
    print("Ranked Documents:")
    for i in ranked_docs:
        print(f"Document {i+1}: {documents[i]} (Score: {scores[i]})")


# query1("Julius Caesar", matrix, sorted_terms, docs)

# def query2(docs, query):
#     # Split query into individual terms
#     query_terms = re.sub(r'[^a-zA-Z0-9\s]', '', query).lower().split()
#     print("Query term here buddy: ", query_terms, "\n\n")

#     i = 0
#     for query_term in query_terms:
#         for doc in docs:
#             if query_term == doc:
#                 i += 1
#                 break

#     return i 

# for doc in sorted_terms:
#     print(query2(doc, "julius caesar"))


def query(term_indices, matrix, query):
    # Split query into individual terms
    query_terms = re.sub(r'[^a-zA-Z0-9\s]', '', query).lower().split()
    print("Query term here buddy: ", query_terms, "\n\n")
    
    doc_arr = []
    for query_term in query_terms:
        idx = term_indices[query_term]
        doc_arr.append(matrix[idx])

    res = [1] * len(doc_arr[0])

    for doc in doc_arr:
        for idx, term_doc in enumerate(doc):
            res[idx] = res[idx] and term_doc

    print(res)        

query(term_indices, matrix, "I did")