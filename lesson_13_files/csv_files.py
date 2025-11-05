import csv
with open('output.csv', newline='') as f:
    reader = list(csv.reader(f))
    # for row in reader:
    #     # print(row)
    #     print(','.join(row))
for row in reader:
        # print(row)
    print(','.join(row))

headers = reader[0]
rows = reader[1:]
data_list = [dict(zip(headers, row)) for row in rows]
print(data_list)