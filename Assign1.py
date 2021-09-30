import pandas as pd
import matplotlib.pyplot as plt
import math

def skip_a(index):# function to check line number(even or odd)
    if index % 2 ==0:
        return True
    return False

df1 = pd.read_csv('raw.txt', delimiter=',', skiprows = lambda x: skip_a(x)) #data frame 1 by skipping odd lines in dataset.

df2 = pd.read_csv('raw.txt', delimiter=',', skiprows = lambda x: not skip_a(x)) #data frame 2 by skipping even lines in dataset. 

df = pd.concat([df2, df1], axis=1) #merging df1 and df2.
df = df.dropna(how='all', axis='columns') #removing empty columns.

#seperating important columns from data frame.
Q0 = df.q0
Q1 = df.q1
Q2 = df.q2
Q3 = df.q3
t = list(df.time)

#creating empty list of values of yaw, pitch and roll.
yaw = list()
pitch = list()
roll = list()

#filling values in above lists.
for i in range(0,len(df)):
    psi = math.atan((2*(Q0[i]*Q3[i] + Q1[i]*Q2[i]))/(1-2*(Q2[i]*Q2[i] + Q3[i]*Q3[i])))
    yaw.append(psi)
    theta = math.asin(2*(Q0[i]*Q2[i] - Q3[i]*Q1[i]))
    pitch.append(theta)
    phi = math.atan((2*(Q0[i]*Q1[i] + Q2[i]*Q3[i]))/(1-2*(Q1[i]*Q1[i] + Q2[i]*Q2[i])))
    roll.append(phi)

#plotting curve which shows motion of ship(yaw,roll and pitch) with time.
plt.plot(yaw, t, label = "YAW")
plt.plot(pitch, t, label = "PITCH")
plt.plot(roll, t, label = "ROLL")
plt.xlabel("time")
plt.legend()
plt.title("Different Motion of Ship.")
plt.show()