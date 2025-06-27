word  = input("enter a word: ")
result = list("_"  * len(word))
print(result)
result2 = []
for i in word:
    result2.append('_')
print(result2)    

result3 = ["_" for i in word]
print(result3) 
print('*******************')