c = int(input("Initial Cost:"))
r = int(input("Depreciation rate:"))

years=0
main_cost=0
dep_cost=0
val=0
i=1
while (main_cost+dep_cost)<=val:
  if i in [1,2,3,4,5]:
    main_cost += 0.01*c
  else:
    main_cost+=0.5* main_cost
  dep_cost+=(r/100)*c
  val+=50*6000
  years+=1
  i+=1
print(years-1)
