numbers=input("Enter numbers")
num_list=numbers.split() #creates a list of numbers lie ['1','2','3']

num_list=[int(num) for num in num_list]  #Covertes a list converted by split to list of type int [1,2,3]
even=[]
odd=[]
for num in num_list:
  if num%2==0:
    even.append(num)
  else:
    odd.append(num)
print("Even Numbers",even)
print("Odd numbers",odd)
#To sort if required
even.sort()
odd.sort()

print("Sorted")
print("Even:",even)
print("odd:",odd)