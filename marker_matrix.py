import read_file_to_array as src

class MarkerMatrix:
    def __init__(self, documents):
        self.documents = documents
        self.marker_matrix = self.build_marker_matrix()

    def build_marker_matrix(self):
        # Initialize an empty marker matrix
        marker_matrix = {}

        # Iterate over each document
        for doc_id, doc in enumerate(self.documents):
            # Split the document into words
            words = doc.split()

            # Iterate over each word in the document
            for word in words:
                # If the word has not been seen before, create a new list for it
                if word not in marker_matrix:
                    marker_matrix[word] = [0] * len(self.documents)

                # Mark the document as containing the word
                marker_matrix[word][doc_id] = 1

        return marker_matrix

    def search(self, query):
        # Split the query into words
        query_words = query.split()

        # Initialize a list of documents that match the query
        matching_docs = []

        # Iterate over each document
        for doc_id, doc in enumerate(self.documents):
            # Assume the document matches the query
            matches_query = True

            # Iterate over each query word
            for query_word in query_words:
                # If the query word is not in the marker matrix, the document cannot match
                if query_word not in self.marker_matrix:
                    matches_query = False
                    break

                # If the document does not contain the query word, it cannot match
                if self.marker_matrix[query_word][doc_id] != 1:
                    matches_query = False
                    break

            # If the document matches the query, add it to the list of matching documents
            if matches_query:
                matching_docs.append(doc_id+1)

        return matching_docs

# arr_docs=[]

# with open("./CĐ CN PM/query-text.txt", "r") as f:
#     for line in f:
#         if line.startswith(("/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
#             continue
#         line=re.sub(r"[^a-zA-Z]+", " ", line)
#         arr_docs.append(line.lower())
            

# Read documents from a file
documents= src.read_file()
documents = documents[:10]

# Create a marker matrix for the documents
mm = MarkerMatrix(documents)

# Search for documents containing the words "quick" and "brown"
matching_docs = mm.search("USE OF COMPUTERS".lower())

# Print the matching documents
print(matching_docs)
