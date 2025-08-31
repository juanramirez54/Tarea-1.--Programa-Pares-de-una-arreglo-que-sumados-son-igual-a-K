encontrado =False
arr = [3, 5, 4, 2, 6, 7, 4, 7, 9, 11]
K = 18
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==K:
            encontrado=True
            print("Par encontrado:" ,arr[i], "y", arr[j])
      
    
if encontrado:
    print("si existe almenos un par que suma",K)
    
else:
    print("No existe un par que sume",K)