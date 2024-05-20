
while 1:
     cnt=[] 
     n=list((input()))
     if n[0]=='.':
        break
     
     for i in n:  
        if i=='(' or i=='[':
            cnt.append(i)
        elif i==')' or i==']':
             cnt.append(i)
        elif i==".":
             cnt.append(i)     
     if cnt.count('(')==0 and cnt.count('[')==0:
        print("yes")  
          
     elif cnt[1]=='[' and cnt[2]==')':
            print("no")
            
     elif (cnt.count('(')==cnt.count(')') or cnt.count('[')==cnt.count(']')) and (cnt[0]=='(' or cnt[0]=='['):
            print("yes")
            
     else:
            print("no")
            
        
         
     
       
                      
            