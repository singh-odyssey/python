from tabulate import tabulate
import pandas as pd

# for spacing 
def space():
    print("\n")
    # print("\n")

# # 1. Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

space()
# 2. Read data from a CSV file
# df = pd.read_csv('data.csv')

# 3. Select a column
print(df['Name'])
space()
# # 4. Filter rows where Age > 28
print(df[df['Age'] > 28])
space()
# # 5. Add a new column
df['Country'] = ['USA', 'UK', 'Canada']
print(df)
space()
# # 6. Calculate the mean age
print("Mean age:", df['Age'].mean())

df.to_csv('output.csv', index=False)

table_str = tabulate(df, headers='keys', tablefmt='psql')
print(table_str)

table_str = tabulate(df, headers='keys', tablefmt='psql')
with open('table.txt', 'w') as f:
    f.write(table_str)