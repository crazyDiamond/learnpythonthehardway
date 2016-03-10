data = [line.strip() for line in open("clients_to_delete", 'r')]
target = open("clients_to_delete", 'w')
result = []

for item in data:
    index = item.index(',')
    result.append(item[1:index])

for item in result:
    target.write(item + ', \n')






