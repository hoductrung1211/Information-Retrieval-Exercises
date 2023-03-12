import math
import reverse_index



# Data:
list_wordInput=["of", "use", "computers"]
data=[]
N = len(reverse_index.documents)

for word in list_wordInput:
    data.append({
        "term": word,
        "tf": reverse_index.tf(word),
        "df":reverse_index.df(word)
    })


def wtf(tf):
    return 1 + math.log10(tf) if tf else 0


def idf(df):
    raw = math.log10(N / df)
    return round(raw * 10) / 10


res = []
for d in data:
    a = wtf(d["tf"])
    b = idf(d["df"])
    res.append({"term": d["term"], "tf": d["tf"], "df": d["df"], "Wtf": round(a,1), "idf": b, "wt": round(a * b,1)})

print(res)

raw_cosine=0
for i in res:
    raw_cosine+=i['wt']**2
    
        
for i in res:
    print(round(i['wt']/math.sqrt(raw_cosine), 2))


    

        



