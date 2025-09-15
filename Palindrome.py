word=input("Enter a word")
word=word.replace(" ","").lower()
r=word[::-1]
if word==r :
  print("Its a palindrome")
else:
  print("Not a palindrome ")