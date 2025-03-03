can_full = "Canh, Tân, Nhâm, Quý, Giáp, Ất, Bính, Đinh, Mậu, Kỷ"
can = [c.strip() for c in can_full.split(",")] 

chi_full = "Thân, Dậu, Tuất, Hợi, Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi,"
chi = [c.strip() for c in chi_full.split(",")] 


birth_year = int(input())
can_index = (birth_year) % 10
chi_index = (birth_year) % 12
print(can[can_index],chi[chi_index])
# split() được sử dụng để chia một chuỗi thành một danh sách mà mỗi từ là một phần tử của danh sách.
# Trong trường hợp này, nó chia chuỗi bằng dấu phẩy để tạo ra một danh sách các phần tử.