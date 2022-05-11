from rplidar import RPLidar
import numpy as np
from math import *

def donnee():

    lidar = RPLidar('/dev/ttyUSB0')

    info = lidar.get_info()
    print(info)

    health = lidar.get_health()
    print(health)

    for i, scanf in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i, len(scanf)))
       

        if i > 1:
            break
    scan=[]  
    for i in scanf:
        
        scan.append(list(i))
        
    print(scan);


    res=[]
    n=10
    zone=180/n
    #scan=[[15,5,49],[15,281,49],[15,281,49],[15,280,49],[15,360,49],[15,360,49],[14,360,250]]
    for i in range(len(scan)):
       if ((scan[i][0]>=15) and (scan[i][1]<90 or scan[i][1]>270)):
         res.append(scan[i])  
    for i in range(len(res)):
      if res[i][1]>=270:
        a=res[i][1]-180
        res[i][1]=a


    f=[]
    for i in range(1,n+1):
      f.append([])
    for i in range(len(res)):
      for j in range(1,n+1):
        if res[i][1]<=j*zone:
          if res[i][2]<300:
            f[j-1].append(1)
          break


    c=0
    for i in range(len(f)): 
      c=0
      for j in range(len(f[i])):
        
        if f[i][j]==1:
          c=c+1
          
      if c>=2:
        f[i].clear()
        f[i].append(False)
      else:
        f[i].clear()
        f[i].append(True)      
    fin=[]  
    while len(f) > 5 :
        fin.append(f[len(f)-1])
        f.pop(len(f)-1)
    final=fin+f  
    final2=[]
    for i in range(0,len(final),2):
        print(i)
        print(final[i])
        print(final[i+1])
         
        final2.append(final[i][0] and final[i+1][0])
     
    
            
    print(final)
    print(final2)

  





