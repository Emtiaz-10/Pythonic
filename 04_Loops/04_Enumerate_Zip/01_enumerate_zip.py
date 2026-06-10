names  = [ 'harry','ron']
points = [10,9.5]

for i,name in enumerate(names):
    print("player",i,":",name)

for name,point in zip(names,points):
    print(name,"got :",point)