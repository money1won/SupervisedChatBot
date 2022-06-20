
import torch


# x = torch.tensor([1.0])
#
# y = torch.tensor([2.0])
# w = torch.tensor([1.0], requires_grad=True)
#
# # Forward pass
# y_hat = w*x
# loss = (y_hat-y)**2
#
# print(loss)
#
#
# # Backward pass
# loss.backward()
# print(w.grad)
#
# ### update weights
# # next forward / backward pass


import numpy as np


X = np.array([1,2,3,4], dtype=np.float32)
Y = np.array([2,4,6,8], dtype=np.float32)

w = 0.0

# model prediction
def forward(x):
    return w*x

# loss

# gradient
