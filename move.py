import csv 
with open("movie.csv", encoding="utf8")as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovies=data[1:]
    headers=data[0]
headers.append("poster_link")
with open("final.csv","a+",encoding="utf8")as f:
    writer=csv.writer(f)
    writer.writerow(headers)
with open("d.csv",encoding="utf8")as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovielinks=data[1:]

for movieitem in allmovies:
    posterfound=any(movieitem[8]in movielinkitems for movielinkitems in allmovielinks)
    if posterfound:
        for movielink in allmovielinks:
            if movieitem[8]==movielink[0]:
                movieitem.append(movielink[1])
                if len(movieitem)==28:
                    with open("final.csv","a+",encoding="utf8")as f:
                        writer=csv.writer(f)
                        writer.writerow(movieitem)

                