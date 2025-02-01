import torch
import numpy as np

x = torch.empty(5,3)
print(x)

x = torch.rand(5,3)
print(x)
x = torch.randn(5,3)
print(x)
x = torch.randint(1,5,(5,3))
print(x)

x_zero=torch.zeros(5,3)
print(x_zero)
x_ones=torch.ones(5,3)
print(x_ones)
x_ones=torch.ones_like(x_zero)
print(x_ones)
x = torch.rand_like(x_zero)
print(x)
x = torch.randn_like(x_zero)
print(x)
x = torch.randint_like(x_zero,1,10)
print(x)

data = [[1,2],[3,4],[5,6]]
x_data = torch.tensor(data)
print(x_data)

x_np = torch.from_numpy(np.arange(3,10,2))
print(x_np)

x = torch.rand(3,4)
print(f"{x.shape}")
print(f"{x.dtype}")
print(f"{x.device}")

tensor = torch.randint(2,5,(4,4))
print(tensor)
print(tensor[1:3,1])

x = torch.randint(2,5,(4,4))
y = torch.randint(2,5,(4,4))
print(x)
print(y)
print(torch.cat([x,y], dim=1))
print(torch.cat([x,y], dim=0))

x = torch.randint(1,3,(3,))
y = torch.randint(1,3,(3,))
print(x)
print(y)
print(torch.matmul(x,y))
x = torch.randint(1,3,(2,2))
y = torch.randint(1,3,(2,2))
print(x)
print(y)
print(torch.matmul(x,y))

a = torch.ones(5)
print(a)
b = a.numpy()
print(b)
a.add_(1)
print(a)
print(b)