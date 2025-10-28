from graphycs.rect import *
from graphycs.cir import *
from graphycs.graphycs3d.cuboid import *
from graphycs.graphycs3d.sphere import *
while(1):
    print("1.Rectangle \n2.Circle\n3.Cuboid\n4.Shpere\n5.Exit")
    c=int(input("Enter your choioce : "))
    if(c==1):
        l=float(input("Enter the length of the rectangle : "))
        w=float(input("Enter the width of the rectangle : "))
        rect.area(l,w)
        rect.perimtr(l,w)
    elif(c==2):
        r=float(input("Enter the radious of the circle : "))
        cir.area(r)
        cir.perimtr(r)
    elif(c==3):
        l=float(input("Enter the length of the Cuboid : "))
        w=float(input("Enter the width of the Cuboid : "))
        h=float(input("Enter the height of the Cuboid : "))
        cuboid.area(l,h,w)
        cuboid.perimtr(l,h,w)
    elif(c==4):
        r=float(input("Enter the radious of the Sphere : "))
        sphere.area(r)
        sphere.perimtr(r)
    else:
        print("Exiting")
        break
