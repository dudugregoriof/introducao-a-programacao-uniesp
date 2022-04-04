compradas=int (input('Digite quantas maçãs foram compradas:'))
if compradas <=12:
    val = compradas*1.30
else:
   compradas >=12
   val = compradas*1
print(f'O valor da compra foi R$ {val}')