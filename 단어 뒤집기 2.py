"""
n=input()
stack=["<",">"]
cnt=[]
for i in range(len(n)):
    if stack[0] in n[i]:
        for j in n:
            cnt.append(j)
            if j == stack[1]:
                cnt.append(j)
                break
    else:
"""
end=0
start=0
data=list(input())
while end<len(data):
      if data[end]=="<":
          while data[end]!=">":
               end+=1
          end+=1
      elif data[end].isalnum():
           start=end
           while end<len(data) and data[end].isalnum():
                end+=1
           pos=data[start:end]
           pos.reverse()
           data[start:end]=pos
      else:
          end+=1
print("".join(data))
