deg = int(input("Degree of eq: "))
coeffs = []
for i in range(1,deg+2):
  coeff = int(input(f'Coeff{i}: '))
  coeffs.append(coeff)
# print(coeffs)
l_b = int(input("Enter lower bound for x: "))
u_b = int(input("Enter upper bound for x: "))
step = int(input("Enter increment steps: "))

n = len(coeffs)
def poly(deg_, coeffs, l_b, u_b):
  for i in range(l_b, u_b+1, step):
    sum_ = 0
    deg = deg_
    for j in range(n):
      sum_+=round(coeffs[j]*(i**deg))
      deg = deg-1
      # if deg==0:
      #   break
    print('|'+'*'*sum_, end=' ')
    print()

poly(deg, coeffs, l_b, u_b)

