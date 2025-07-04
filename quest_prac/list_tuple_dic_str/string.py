# string concatenation
str1="hi"
str2="A S"
print(f"{str1} {str2}")

#filter all string starting with vowel
words = ["apple", "banana", "orange", "umbrella", "grape", "elephant"]
vowels = ("a", "e", "i", "o", "u")
filtered = [word for word in words if word.lower().startswith(vowels)]
print("Strings starting with a vowel:", filtered)

# seperate printing particular words which are present in a tuple
names=("hi","apple","orange","A")
filter2=[word for word in words if word in names]
print(filter2)

