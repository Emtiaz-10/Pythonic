students = [{"name":"Harry","house":"Gryffindor","Patronus":"Stag"},
            {"name":"Ron","house":"Gryffindor","Patronus":"Jack Russell terrier"},
            {"name":"Hermione","house":"Gryffindor","Patronus":"Otter"}
            ]

for i in students:
    
    for j in i:
        print(j,i[j],sep=" : ",end ="   " )
    print()