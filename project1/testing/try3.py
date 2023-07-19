a = [[3, 'Streams', '10.30.48.178', '10.30.48.183', '10.30.48.185', '', ''], [4, 'Admin5', '10.30.48.153', '10.30.48.154', '10.30.48.192', '', '']]

# print(a[0][1])
# print(a[0][2:7])
# print(a[1][1])
# print(a[1][2:7])

j = 0

for i in a:
    while j < len(a):       
        # print(a[j][1])
        tmp = a[j][1]     
        print(tmp)    
    
        bb = a[j][2:] 
        print(bb)
        j = j+1  
   
              
        
