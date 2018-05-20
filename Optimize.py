from PSO import *

Tree=[]                                                  #contains branches of trees and its respective radius
for i in range(int(len(tree))):
    Tree.append([tree[i][0],tree[i][2]])                 #tree array is the area filling trees #output of area filling fractal code 
Tree=[[[400.0, 0], 1]]+Tree                              #adding root branch

def func(x):                                             #cost function to be minimised #volume of the tree in this case
    return dis(temp[0][0][0],temp[0][0][1],x[0],x[1])*(Tree[i+1][1])**2+dis(temp[1][0][0],temp[1][0][1],x[0],x[1])*temp[1][1]**2+dis(temp[2][0][0],temp[2][0][1],x[0],x[1])*temp[2][1]**2

Tree1=[]                                                #only contains branches of trees i.e. startin and ending point of branch
for i in range(31):
    if i is 0:
        Tree1.append([Tree[0][0],Tree[1][0]])
    else:
        Tree1.append([Tree[i][0],Tree[2*i][0]])
        Tree1.append([Tree[i][0],Tree[2*i+1][0]])

sol=[]
initial=[0,0] 
bounds=[[0,800],[0,800]]                               #explained in the PSO algorithm
bound=[[400,400],[0,800]]
k=0
fun=[]

while k<10:                                          
    Tree1=[]
    sol=[]
    for i in range(63):         #int((len(tree))/2)-1)
        for j in range(31):     #int((len(tree))/4)-1)
            if j is 0:
                Tree1.append([Tree[0][0],Tree[1][0]])
            else:
                Tree1.append([Tree[j][0],Tree[2*j][0]])
                Tree1.append([Tree[j][0],Tree[2*j+1][0]])    
    
        temp=[Tree[2*i+2],Tree[2*i+3]]
        temp=[Tree[int((i+1)/2)]]+temp
        triangle=[temp[0][0],temp[1][0],temp[1][0]]
        Tree2=Tree1.copy()
        del Tree2[i]
        del Tree2[2*i+1]
        del Tree2[2*i+1]
        if i is 0:
            psw=PSO(func,initial,2,bounds,num_particles=25,maxiter=130)
        else:
            psw=PSO(func,initial,2,bounds,num_particles=25,maxiter=130)
        Tree[i+1][0]=optimise(tree[i][0],psw,Tree2,triangle)
        sol.append(func(Tree[i+1][0]))
    fun.append(sum(sol))
    print(k)
    k=k+1

def Draw_branch(start,end):
    pt1=Point(start[0],start[1])
    pt2=Point(end[0],end[1])
    ln=Line(pt1,pt2)
    ln.setWidth(3)
    ln.draw(win)
from graphics import *
win = GraphWin('Face',800, 800)
win.setBackground('white')

P=[[50,750],[50,50],[750,50],[750, 750]]
coc=[]
for i in range(len(P)):
    coc.append(Point(P[i][0],P[i][1]))
triangle = Polygon(coc)
triangle.setFill('light gray')
triangle.setOutline('light grey')
triangle.draw(win)

for i in range(len(tree)):
    f=tree[i]
    f1=Point(f[0][0],f[0][1])
    f2=Point(f[1][0],f[1][1])
    ln=Line(f1,f2)
    ln.setWidth(2)
    ln.setFill('red')
    ln.draw(win)
    
Draw_branch(Tree[0][0],Tree[1][0])
for i in range(127):
    Draw_branch(Tree[i+1][0],Tree[2*i+2][0])
    Draw_branch(Tree[i+1][0],Tree[2*i+3][0])

win.getMouse()
win.close()
