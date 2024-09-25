import pandas as pd

# arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
#             ['Captive', 'Wild', 'Captive', 'Wild']]
#
# index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
#
# df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]}, index=index)

l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
df = pd.DataFrame(l, columns=["a", "b", "c"])

print(df)
# Group by calculates row statistics
print(df.groupby("b").describe())
