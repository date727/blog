import numpy as np

a = np.array([1,2,3,4,5])
arr1 = np.ones_like(a)
arr2 = np.zeros_like(a)
print(a)
print(arr1)
print(arr2)

b = np.array([[1,2],[3,4]])
print(b)

c = np.empty((4,3,1),dtype=int)
print(c)

d = np.random.rand(4,4)
print(d)
e = np.random.randint(1,10,(2,4))
print(e)

arr = np.arange(2,15,3,dtype=float)
print(arr)

f = np.random.rand(3,4)
print(f)
print(f"{f.ndim},{f.shape},{f.size},{f.dtype}")

a = np.arange(10)
sli = slice(3,10,3)  #取下标为3，6，9
b = a[sli]
print(b)
b = a[3:10:3]
print(b)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[1:,0:2]) #从第1行到最后一行，每一行输出第0到第1列
print(a[0:2,...]) #从第0行到第1行，每一行都完整输出

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[2,5],[6,1],[3,4]])
print(np.vdot(a,b))

a = np.array([[1,2],[4,5]])
print(np.linalg.det(a))