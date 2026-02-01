import numpy as np
import matplotlib.pyplot as plt
L1= 2
L2=1.5
angle1=np.deg2rad(30)
angle2=np.deg2rad(45)

#joint 1 position
x1=L1*np.cos(theta1)
y1=L1*np.sin(theta1)

# End effector Position
x2= x1+L2*np.cos(theta1+theta2)
y2= y1+L2*np.sin(theta1+theta2)

#plot robo arm
plt.figure()
plt.plot([0,x1,x2],[0,y1,y2], marker='o',label="L1")
plt.plot([x1,x2],[y1,y2],marker='o',label="L2")
#mark length on diagram
plt.text(x1/2,(y1-1)/2,f"L1={L1}", fontsize=10)
plt.text(x1+1/2,y1+1 /2,f"L2={L2}", fontsize=10)

plt.scatter([x2],[y2])
plt.text(x2,y2,"END EFFECTOR", fontsize=10)

plt.xlim(-4,4)
plt.ylim(-4,4)
plt.grid()
plt.title("2- link robot arm forward Kinematics ")
plt.xlabel(" X Position")
plt.ylabel("y Position ")
plt.show()
print (" END effector Position")
print ("x=", round (x2,2))
print("y=",round(y2,2))
