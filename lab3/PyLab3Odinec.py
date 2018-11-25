# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:19:39 2018

@author: Asus
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5),dpi=80)
plt.subplot(111)

X = np.linspace(-np.pi,np.pi,256,endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5,linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5,linestyle="-", label="sine")

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.ylim(X.min() * 1.1, X.max() * 1.1)
plt.yticks([-1,1],
           [r'$-1$',r'$+1$'])
plt.legend(loc='upper left')

t = 2*np.pi/3
plt.plot(X, C, color="blue", linewidth=2.5,linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5,linestyle="-", label="sine")
plt.plot([t,t],[0,np.cos(t)],
         color='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color='blue')
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)),xycoords='data',
             xytext=(10,30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)],
         color='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color='red')
plt.annotate(r'$cos(\frac{2\pi}{3})=\frac{\sqrt{1}}{2}$',
             xy=(t, np.cos(t)),xycoords='data',
             xytext=(-90,-50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


###### Задание 2

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure(figsize=(6,4))
G = gridspec.GridSpec(3,3)

axes_1 = plt.subplot(G[0,:])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24,alpha=.5)

axes_2 = plt.subplot(G[1,:-1])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24,alpha=.5)

axes_3 = plt.subplot(G[1:,-1])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24,alpha=.5)

axes_4 = plt.subplot(G[-1,0])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24,alpha=.5)

axes_5 = plt.subplot(G[-1,-2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24,alpha=.5)

plt.tight_layout()
plt.show()

###### Задание 3

import matplotlib.pyplot as plt

plt.axes([.1, .1, .8, .8])
plt.xticks(())
plt.yticks(())
plt.text(.6, .6, 'axes([0.1, 0.1, .8, .8])', ha='center', va='center', size=20,alpha=.5)

plt.axes([.2, .2, .3, .3])
plt.xticks(())
plt.yticks(())
plt.text(.5, .5, 'axes([0.2, 0.2, .3, .3])', ha='center', va='center', size=10,alpha=.5)

plt.show()


###### Задание 4

import numpy as np
n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.plot(X,Y+1, color='blue', alpha=1.00)
plt.fill_between(X, Y+1, y2=1, where=None, interpolate=False, step=None, data=None,color='cornflowerblue')
plt.plot(X,Y-1, color='blue', alpha=1.00)
plt.fill_between(X, Y-1, y2=-1, where=Y>0, interpolate=False, step=None, data=None,color='cornflowerblue')
plt.fill_between(X, Y-1, y2=-1, where=Y<0, interpolate=False, step=None, data=None,color='pink')

###### Задание 5

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)


plt.scatter(X, Y,c=np.arctan2(Y,X), alpha=.5)
plt.axis([-1,1,-1,1])

###### Задание 6

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va= 'bottom')

for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va= 'top')

plt.axis([-0.5,12,-1.25,1.25])

###### Задание 7

def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
plt.clabel(C, inline=1, fontsize=16)

###### Задание 8

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)

n = 10
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(f(X, Y), interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.92)
plt.xticks(())
plt.yticks(())
###### Задание 9

Z = np.random.uniform(0,1,20)
Z = np.ones(20)
Z[19] *= 2
['%f' % (i/float(n)) for i in range(n)]
np.arange(0.0,1.0,0.1)
plt.pie(Z, explode=Z*.05, colors = ['%f' % (i/float(20)) for i in range(20)])

###### Задание 10

n = 8
X, Y = np.mgrid[0:n, 0:n]
#plt.quiver(X, Y)
T = np.arctan2(Y - n / 2., X - n/2.)
R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
U = R * np.cos(T)
V = R * np.sin(T)
plt.quiver(X, Y, U, V, R, alpha=.5)
plt.quiver(X, Y, U, V, edgecolor='black', facecolor='None', linewidth=.5)

plt.xticks(())
plt.yticks(())

###### Задание 11

axes = plt.gca()
ax = plt.axes([0.025, 0.025, 0.95, 0.95])
axes.set_xlim(0, 4)
axes.set_ylim(0, 3)
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
axes.set_xticklabels([])
axes.set_yticklabels([])


ax = plt.axes([0.025, 0.025, 0.95, 0.95])
ax.set_xlim(0,4)
ax.set_ylim(0,3)
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
ax.set_xticklabels([])
ax.set_yticklabels([])

###### Задание 12

fig = plt.figure()

plt.subplot(2, 1, 1)
plt.xticks(()), plt.yticks(())

plt.subplot(2, 3, 4)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 5)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 6)
plt.xticks(())
plt.yticks(())

plt.show()

###### Задание 13
plt.axes([0, 0, 1, 1])

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)
    
    plt.axes([0, 0, 1, 1])



N = 20
ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)
    
plt.xticks(())
plt.yticks(())
###### Задание 14

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
ax.set_zlim(-2, 2)


ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
