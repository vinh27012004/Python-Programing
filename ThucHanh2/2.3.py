input_string = input()

#Tách các khoảng trắng và dấu phẩy
word = [word.strip() for word in input_string.split(',')]

sorted_word = sorted(word)

#Sắp xếp các từ theo thứ tự từ điển
print(", ".join(sorted_word))