# x = [1,3,4]
# y = 2
# z = 3

# result = y + z
# print(result)
# result2 = y+x
# print(result2)


import pdb
import pandas as pd

x = [1, 3, 4]
y = 2
z = 3
# initialize list of lists
data = [["tom", 10], ["nick", 15], ["juli", 14]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=["Name", "Age"])

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y + x
print(result2)
