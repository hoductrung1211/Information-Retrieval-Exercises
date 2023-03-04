import re

def read_file():
    arr_docs=[]
    with open("./CĐ CN PM/query-text.txt", "r") as f:
        for line in f:
            if line.startswith(("/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
                continue
            line=re.sub(r"[^a-zA-Z]+", " ", line)
            arr_docs.append(line.lower())

        return arr_docs