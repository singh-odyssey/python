#creating a dictionary and user will enter word and its meaning will be showed
dic = {
	"Hello": "A greeting or expression of goodwill",
	"Goodbye": "A farewell or parting phrase",
	"Please": "A polite expression used when making a request",
	"Thank you": "An expression of gratitude",
	"Sorry": "An expression of regret or apology"
} 
word=input("Enter the word to see its meaning -> ")
print(dic[word.capitalize()])