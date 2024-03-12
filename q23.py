list=[[1,2],[3,4],[4,6]]

print(list)

result=[[list[j][i]for j in range(len(list))] for i in range(len(list[0]))]

print(result)
