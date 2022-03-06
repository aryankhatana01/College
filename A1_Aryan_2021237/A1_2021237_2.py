def p_square(s):
  print(4*s)

def p_rectangle(l, b):
  print((2*l)+ (2*b))

def a_rhombus(s, d1, d2):
  print(0.5*d1*d2)

def s_parallelogram(l, b, h):
  print((2*l)+ (2*b))

def a_parallelogram(l, b, h):
  print(l*h)

def p_circle(r):
  print(2*3.14*r)

def a_circle(r):
  print(3.14*r*r)

def csa_cuboid(l, b, h):
  print(2*(l+b)*h)

def vol_cuboid(l,b,h):
  print(l*b*h)

def tsa_cuboid(l,b,h):
  print(2*((l*b)+(b*h)+ (l*h)))

def csa_cube(s):
  print(4*(s**2))

def vol_cube(s):
  print(s**3)

def tsa_cube(s):
  print(6*(s**2))

def csa_cone(l,r,h):
  print(3.14*r*l)

def tsa_cone(l,r,h):
  print(3.14*r*(l+r))

def vol_cone(l,r,h):
  print((1/3)*(r**2)*3.14*h)

def csa_hem(r):
  print(2*3.14*r*r)

def tsa_hem(r):
  print(3*3.14*r*r)

def vol_hem(r):
  print((2/3)*3.14*r*r*r)

def csa_sp(r):
  print(4*3.14*r*r)

def tsa_sp(r):
  print(4*3.14*r*r)

def vol_sp(r):
  print((4/3)*3.14*r*r*r)

def csa_cyl(r, h):
  print(2*3.14*r*h)

def tsa_cyl(r, h):
  print(2*3.14*r*(r+h))

def vol_cyl(r, h):
  print(3.14*r*r*h)
n = int(input("Number of students: "))
for _ in range(n):
  print("1. 2D, 2. 3D")
  typ = int(input("Enter Serial Number: "))
  if typ==1:
    print('''
    1. Square input: side s
    2. Rectangle input: length l, breadth b
    3. Rhombus input: side a, diagonals d1,d2
    4. Parallelogram input: length l, breadth b, height h
    5. Circle input: radius r
    ''')
    shape = int(input("enter shape: "))
    print('''
    1. Area
    2. Perimeter
    ''')
    sur = int(input("Enter serial number: "))
    if shape==1 and sur==1:
      s = int(input("side:"))
      print(s*s)
    
    elif shape==1 and sur==2:
      s = int(input("side:"))
      p_square(s)
    
    elif shape==2 and sur==1:
      l = int(input("length:"))
      b = int(input("breadth:"))
      print(l*b)
    
    elif shape==2 and sur==2:
      l = int(input("length:"))
      b = int(input("breadth:"))
      p_rectangle(l, b)
    
    elif shape==3 and sur==1:
      s = int(input("side:"))
      d1= int(input("d1:"))
      d2 = int(input("d2:"))

      a_rhombus(s,d1,d2)
    
    elif shape==3 and sur==2:
      s = int(input("side:"))
      d1= int(input("d1:"))
      d2 = int(input("d2:"))

      p_square(s)
    
    elif shape==4 and sur==1:
      l = int(input("len:"))
      b= int(input("breadth:"))
      h = int(input("height:"))

      a_parallelogram(l,b,h)
    
    elif shape==4 and sur==2:
      l = int(input("len:"))
      b= int(input("breadth:"))
      h = int(input("height:"))

      p_rectangle(l,b)
    
    elif shape==5 and sur==1:
      r = int(input("radius:"))

      a_circle(r)
    
    elif shape==5 and sur==2:
      r = int(input("radius:"))

      p_circle(r)


  else:
    print('''
    1. Cube input: side s
    2. Cuboid input: length l, breadth b, height h
    3. Right circular cone: slant height l, radius r, height h
    4. Hemisphere input: radius r
    5. Sphere input: radius r
    6. Solid cylinder input: radius r, height h
    ''')
    shape = int(input("enter shape: "))
    print(
      '''
      1. CSA
      2. TSA
      3. Vol
      '''
    )

    sur = int(input("Enter serial number: "))
    if shape==1 and sur==1:
      s = int(input("side:"))
      csa_cube(s)
    
    elif shape==1 and sur==2:
      s = int(input("side:"))
      tsa_cube(s)

    elif shape==1 and sur==3:
      s = int(input("side:"))
      vol_cube(s)
    
    elif shape==2 and sur==1:
      l = int(input("length:"))
      b = int(input("breadth:"))
      h = int(input("height:"))
      csa_cuboid(l, b,h)

    elif shape==2 and sur==2:
      l = int(input("length:"))
      b = int(input("breadth:"))
      h = int(input("height:"))
      tsa_cuboid(l, b,h)

    elif shape==2 and sur==3:
      l = int(input("length:"))
      b = int(input("breadth:"))
      h = int(input("height:"))
      vol_cuboid(l, b,h)
    
    elif shape==3 and sur==1:
      l = int(input("len:"))
      r= int(input("rad:"))
      h = int(input("height:"))

      csa_cone(l,r,h)
    
    elif shape==3 and sur==2:
      l = int(input("len:"))
      r= int(input("rad:"))
      h = int(input("height:"))

      tsa_cone(l,r,h)
    
    elif shape==3 and sur==3:
      l = int(input("len:"))
      r= int(input("rad:"))
      h = int(input("height:"))

      vol_cone(l,r,h)
    
    elif shape==4 and sur==1:
      r = int(input("rad:"))


      csa_hem(r)

    elif shape==4 and sur==2:
      r = int(input("rad:"))


      tsa_hem(r)

    elif shape==4 and sur==3:
      r = int(input("rad:"))


      vol_hem(r)
    
    elif shape==5 and sur==1:
      r = int(input("radius:"))

      csa_sp(r)
    
    elif shape==5 and sur==2:
      r = int(input("radius:"))

      tsa_sp(r)

    elif shape==5 and sur==3:
      r = int(input("radius:"))

      vol_sp(r)

    elif shape==6 and sur==1:
      r = int(input("radius:"))
      h = int(input("height:"))
      csa_cyl(r,h)

    elif shape==6 and sur==2:
      r = int(input("radius:"))
      h = int(input("height:"))
      tsa_cyl(r,h)

    elif shape==6 and sur==3:
      r = int(input("radius:"))
      h = int(input("height:"))
      vol_cyl(r,h)

