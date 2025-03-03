
s1 = "Welcome to Python"
print(s1)
print(len(s1))
for ch in s1:
    print(ch,end=" ")   

s2 = "Python"
s3 ="THe girl is beautiful"

result = s3.find("is")
print("\n",result)
chuyen_Kieu = """
Buồn trông cửa bể chiều hôm
Thuyền ai thấp thoáng cánh buồm xa xa
buồn trông ngọn nước mới sa
hoa trôi man mác biết là về đâu ?
Buồn trông nội cỏ rầu rầu
Chân mây mặt đất một màu xanh xanh
buồn trông gió cuốn mặt duềnh
ầm ầm tiếng tiếng sóng kêu quanh ghế ngồi đâu"""

words = [w.strip() for w in chuyen_Kieu.split()]
print(words)

words_count = {}
for w in words:
    if w in words_count:
        words_count[w] += 1
    else:
        words_count[w] = 1

for w in words_count:
    print(w,words_count[w])

    
for k,v in words_count.items():
    print(k,v)


sorted_dict = {k : v for k, v in 
               sorted(words_count.items(), key=lambda x: x[1], reverse=True)}
print(list(sorted_dict.items())[0])
