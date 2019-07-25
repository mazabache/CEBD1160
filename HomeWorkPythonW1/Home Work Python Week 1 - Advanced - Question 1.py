import string
import operator

input_str=input("Enter a string:")
Letters=list(string.ascii_letters)
result={}
for char in Letters:
    result.update({char:input_str.count(char)})
print("\nAlphabetical Order")
print(result)

sorted_x={}
sorted_x = sorted(result.items(), key=operator.itemgetter(1),reverse=True)
print("\nSorted by Repetition")
print(sorted_x)







