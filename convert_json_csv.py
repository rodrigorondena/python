import csv
import json

file_in = open('teste.json')
x = json.load(file_in)
file_in.close()

f = csv.writer(open("test.csv", "wb+"))

# Header, pode remover se quiser
f.writerow(["pk", "model", "codename", "name", "content_type"])

for x in x:
    f.writerow([x["pk"],
                x["model"],
                x["fields"]["codename"],
                x["fields"]["name"],
                x["fields"]["content_type"]])