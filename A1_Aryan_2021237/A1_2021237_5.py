def getreverse(n):
  n_str = str(n)
  n_rev = n_str[::-1]
  return int(n_rev)

def checkpalindrome(n):
  if n==getreverse(n):
    print(True)
  else:
    print(False)

def checknarc(n):
  sum_=0
  n_str = str(n)
  for i in range(len(n_str)):
    dig = int(n_str[i])
    sum_+=dig**3
  if sum_==n:
    print('True')
  else:
    print('False')

def finddigitsum(n):
  sum_=0
  n_str = str(n)
  for i in range(len(n_str)):
    dig = int(n_str[i])
    sum_+=dig
  print(sum_)

def squaredigitsum(n):
  sum_=0
  n_str = str(n)
  for i in range(len(n_str)):
    dig = int(n_str[i])
    sum_+=dig**2
  print(sum_)

print(
  '''
  1. Get Reverse
  2. Check Palindrome
  3. Check Narcissitic
  4. Find digit sum
  5. Squared digit sum
  '''
)
choice = int(input("Enter choice: "))
n = int(input("Enter Number: "))
if choice==1:
  print(getreverse(n))
elif choice==2:
  checkpalindrome(n)
elif choice==3:
  checknarc(n)
elif choice==4:
  finddigitsum(n)
elif choice==5:
  squaredigitsum(n)