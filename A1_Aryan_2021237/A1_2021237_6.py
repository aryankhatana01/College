# f(x) = x^4 + x^3 + x^2 +x
def findRoot(l):
  fx = {}
  fx["powers"] = l
  fx["coeffs"] = [1 for _ in range(len(l))]
  fdashx = {}
  fdashpow = []
  fdashcoeff = []
  for ele in fx["powers"]:
    fdashpow.append(ele-1)
    fdashcoeff.append(ele)
  fdashx["powers"] = fdashpow
  fdashx["coeffs"] = fdashcoeff
  # print(fdashx)
  sums=[]
  for i in range(1,20):
    sum_=0
    for j in range(len(fdashx["powers"])):
      sum_+=(fdashx["coeffs"][j])*(i**fdashx["powers"][j])
    sums.append(sum_)
  x0 = (sums.index(min(sums, key=abs)))+1
  xn=0
  xn1=-1
  while xn!=xn1:
    sum_fdash = 0
    sum_f = 0
    for j in range(len(fdashx["powers"])):
      sum_fdash+=(fdashx["coeffs"][j])*(x0**fdashx["powers"][j])
    for j in range(len(fx["powers"])):
      sum_f+=(fx["coeffs"][j])*(x0**fx["powers"][j])
    xn = x0 - (sum_f/sum_fdash)

    sum_fdash = 0
    sum_f = 0
    for j in range(len(fdashx["powers"])):
      sum_fdash+=(fdashx["coeffs"][j])*(xn**fdashx["powers"][j])
    for j in range(len(fx["powers"])):
      sum_f+=(fx["coeffs"][j])*(xn**fx["powers"][j])
    xn1 = xn - (sum_f/sum_fdash)
    print(xn)
    break

findRoot([2,1,1,1,0.8])

