

def diamond_pattern(start, end,step):
    for i in range(start,end,step):
       row=''
       for k in range(i, 0, -1):
           if i==k:
               if start<end:
                   row+= (end-i-1)*' '
               else:
                   row+= (start-i+1)*' '
           row+=str(k)
           
           if k==1:
               for z in range(2,i+1):
                   row+=str(z)
       print(row)
 
            
    
        
    

diamond_pattern(1,6,1)
diamond_pattern(4,0,-1)











#Output



    1
   212
  32123
 4321234
543212345
 4321234
  32123
   212
    1
