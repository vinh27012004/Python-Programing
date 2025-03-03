height = float(int(input())/100)
weight = int(input())

bmi = float(weight/(height**2))
bmi = round(bmi, 1)

print(bmi)

if (bmi < 18.5):
    print("Gầy ốm")
elif (bmi >= 18.5 and bmi < 25):
    print("Bình thường")
elif (bmi >= 25 and bmi < 30):
    print("Thừa cân")
else:
    print("")