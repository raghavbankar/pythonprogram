
mat1=[[12,34,54],[32,43,54]]
mat2=[[12,34,54],[32,43,54]]
result=[[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        result[i][j]=mat1[i][j]+ mat2[i][j]
for r in result:
    print(r)