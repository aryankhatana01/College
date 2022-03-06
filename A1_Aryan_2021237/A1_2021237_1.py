pattern = input("Pattern Name: ")
n = int(input("Val of n: "))

if pattern=='Right-angled triangle':
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(j, end=' ')
    print()

elif pattern=='Isosceles triangle':
  x = n-1
  for i in range(0,n):
    print(x*' ', end=' ')
    x-=1
    for j in range(1,(2*i)+2):
      print(str(j), end=' ')
    print()


elif pattern=='Kite':
  x = n-1
  for i in range(0,n):
    print(x*' ', end=' ')
    x-=1
    for j in range(1,(2*i)+2):
      print(str(j), end=' ')
    print()
  
  x=1
  for i in range(n, 1, -1):
    print(x*' ', end=' ')
    x+=1
    for j in range(1, (2*i)-2):
      print(str(j), end=' ')
    print()

  
elif pattern=='Half Kite':
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(j, end=' ')
    print()
  
  for i in range(n-1, 1, -1):
    for j in range(1,i+1):
      print(j, end=' ')

    print()

elif pattern=='X':
  x=1
  for i in range(n+1, 1, -1):
    print(x*' ', end=' ')
    x+=1
    for j in range(1, (2*i)-2):
      print(str(j), end=' ')
    while i!=2:
      print()
      break
  
  x = n-1
  for i in range(0,n):
    print(x*' ', end=' ')
    x-=1
    for j in range(2,(2*i)+2):
      print(str(j), end=' ')
    print()


