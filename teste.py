
items = 'box 1,'
items+= 'box 2,'

# Pegar a string e transformar em um array tirando a última virgula
array = items[:-1].split(',')
print (array)

# Voltar o array para uma String

items = ''
for item in array:
    items += item + ','
items += 'box 3,'
items += 'box 4,'
items += 'box 5,'
print ("Esse é o array string -> " + items)

array = items[:-1].split(',')

print (array)
items = ''
for item in array:
    items += item + ','
print (items)

# if 'box 1' in array:
#     array.remove('box 1')
#     print(array)
#     items = ''
#     for box in array:
#         items += 'box 1' + ','
#     print (items)
#     print(items[:-1].split(','))
#     print()

