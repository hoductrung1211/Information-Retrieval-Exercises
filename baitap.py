# Ma trận đánh dấu
# 1. Đưa câu Doc về dạng List các từ -> List to Set để khử trùng
# 2. Vẽ bảng với cột bên trái là danh sách các từ lấy ở Set trên
#   Cột bên phải là index document đó xuất hiện

# f = open("query-text.txt", "r")
arr_docs=[]

with open("./CĐ CN PM/query-text.txt", "r") as f:
    for line in f:
        if line.startswith(("/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
            continue
        arr_docs.append(line.strip().lower())
            
arr_docs=arr_docs[:60]

arr_query="USE OF COMPUTERS ".lower().rstrip().split(" ")
def get_query(doc, query):    
    count=0
    for word2 in query:
        for word in doc.split(" "):
            if word2==word:
                count+=1
                break
    return count

arr_result=[]

for index, doc in enumerate(arr_docs):
    if get_query(doc, arr_query)>=len(arr_query):
        # arr_result.append(doc)
        print("[",index+1,"] =>", doc)


# print(arr_result)
