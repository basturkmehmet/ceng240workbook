import random
list1=[]
print("You are about to create a tuple. Please enter the starting and ending point.")
start=int(input("Starting point:"))
end=int(input("Ending point:"))

#creating a list with range()
if start<end:
  list1.extend(range(start,end))
  list1.append(end)

#counting the list
count=0
for i in list1:
  count=count+1


#inserting "?" into list
indexqmark=random.randint(0,int(count))

list1.insert(int(indexqmark),"?")
list1.pop(int(indexqmark)+1)

#converting to a tuple
tuple1=tuple(list1)
print("Your tuple is: ",tuple1)

replace_num=input("Please enter the number that you want to replace with '?': ")

#tuple to list and inserting the number
list2=list(tuple1)

list2.insert(int(indexqmark),int(replace_num))
list2.pop(int(indexqmark)+1)
tuple2=tuple(list2)
print("Your tuple is: ",tuple2)