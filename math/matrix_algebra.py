# Matrix Algebra
import numpy as np
import scipy


A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.matrix('6,2,-3,5')
v = np.matrix('3,5,-1,4')
w = np.matrix('1;8;0;5')
alpha = 6

#finding shapes
a = A.shape
b = B.shape
c = C.shape
d = D.shape
udim = u.shape
vdim = v.shape
wdim = w.shape
print('The shapes of the matricies are:')
print(a,b,c,d,udim,vdim,wdim)

a = A.ndim
b = B.ndim
c = C.ndim
d = D.ndim
udim2 = u.ndim
vdim2 = v.ndim
wdim2 = w.ndim
print('The dimensions of the matricies are:')
print(a,b,c,d,udim2,vdim2,wdim2)

#Vector Algebra
q21 = u + v
q22 = u-v
q23 = alpha*u
q24 = np.vdot(u,v)
q25 = np.linalg.norm(u)
print('The answers to the vector algebra questions are:')
print (q21,q22,q23,q24,q25)

# Matrix Algebra
#q31 = A + C undefined
q32 = A + C.T
q33 = C.T + 3*D
q34 = B*A
#q35 = B*A.T undefined
#q36 = B*C undefined
q37 = C*B
q38 = B^4
q39 = A*A.T
q310 = D.T*D
print('The answers to the matrix algebra questions are:')
print(q32)
print(q33)
print(q34)
print(q37)
print(q38)
print(q39)
print(q310)

PLACE YOUR CODE HERE
