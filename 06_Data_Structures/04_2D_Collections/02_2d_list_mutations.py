matrix = [[1,2],[3,4]]
row = matrix[0]

row.append(9)
print("mutation",row,matrix)

matrix[0] = [0,0]     # loc changed
print("reassignment")
print(row, matrix)




