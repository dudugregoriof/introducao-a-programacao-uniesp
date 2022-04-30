VET=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,2,24,25,26,27,28,29,30,31,32,2,34,35,36,37,38,39,40,41,42,43,44,45,2,47,48,49,50]
for num in VET:
  if VET.count(num)>1:
    print(f'O número {num} se repete {VET.count(num)} vezes nas posições {VET.index(2)}, {VET.index(2,2)}, {VET.index(2,23)}, {VET.index(2,33)}')
    break

