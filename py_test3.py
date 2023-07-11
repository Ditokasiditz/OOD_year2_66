print(" *** String count ***")

text = input("Enter message : ")
upper = []
upper_n = 0  
lower = []
lower_n = 0
for i in text:
    if i.isupper():
        upper_n += 1
        if i not in upper:
            upper.append(i)
    elif i.islower() :
        lower_n += 1
        if i not in lower:
            lower.append(i)

upper.sort()
lower.sort()

print("No. of Upper case characters :",str(upper_n))
print("Unique Upper case characters :", end=" ")
for j in upper:  
  print(j, end="  ")
print()  

print("No. of Lower case Characters :",str(lower_n))
print("Unique Lower case characters :", end=" ")
for k in lower: 
    print(k, end="  ") 



