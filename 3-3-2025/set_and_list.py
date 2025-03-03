fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']

for f in fruits:
    print(f)
fruits_set = set(fruits)
print(fruits_set)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

u = s1.union(s2)
print(u)

giao = s1.intersection(s2)
print(giao)

hieu = s1.difference(s2)

numbers = [1,2,'34',56,'79A']
print(len(numbers))
for i in numbers:
    print(i)

for i in range(len(numbers)):
    print(numbers[i])

#thêm phần tử vào list
numbers.append(100)
#xóa phần tử 
numbers.remove('34')
print(numbers)

s = sum([ i for i in numbers if isinstance(i, int)])

print("tổng các số nguyên trong list: ",s)  