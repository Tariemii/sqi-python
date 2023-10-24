"""
write a program that will ask user to write an article, when the user is done,
the program should ask the user to replace words, print the new article
"""
article = input("Write your own article\n")
replacement = input("Enter the word you want to replace\n")
new_word = input("Enter the word you want to replace it with\n")
if replacement not in article:
    print("Word not found")
else:
  new_article = article.replace(replacement, new_word)
print(new_article)