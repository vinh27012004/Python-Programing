# import pandas as pd

# print(pd.__version__)


# # numbers = pd.Series(['Bưởi', 'Cam', 'Chanh', 'Dưa hấu', 'Dưa gang', 'Dưa lê', 'Dưa đỏ', 'Dưa vàng'])
# # print(numbers)

# # print(numbers.index)
# # print(numbers.values)

# # RangeIndex = pd.RangeIndex(start=0, stop=4, step=1)
# # ['Bưởi', 'Dưa vàng']

# # fruit11 = pd.Series([0 , 1 , 2, 3 ,4, 5, 6, 7], index=['Bưởi', 'Cam', 'Chanh', 'Dưa hấu', 'Dưa gang', 'Dưa lê', 'Dưa đỏ', 'Dưa vàng'])

# # print(fruit11.index['Bưởi'])


# data = {'province': ['Khánh Hòa', 'Đà Nẵng', 'Hà Nội', 'Hồ Chí Minh'], 'area': [1, 2, 3, 4], 'population': [5, 6, 7, 8]}
# df = pd.DataFrame(data)
# print(df)
import pandas as pd


# Create Labels
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])
# Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)

myvar1 = pd.Series(calories, index = ["day1", "day2"])
print(myvar1)
#DataFrame
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)