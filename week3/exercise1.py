import torch
import torch.nn as nn
import torch.nn.functional as F


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return F.softmax(x, dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        # Trừ giá trị lớn nhất của x để tránh tràn số khi tính toán softmax
        max_val = torch.max(x)
        exp_x = torch.exp(x - max_val)
        return exp_x / torch.sum(exp_x)


# Ví dụ sử dụng
data = torch.Tensor([1, 2, 3])
# data = torch . Tensor([5, 2, 4])
# data = torch.Tensor ([1 , 2 , 300000000])

# Sử dụng Softmax
softmax = Softmax()
output = softmax(data)
# print("Softmax Output:", output)

# Sử dụng SoftmaxStable
softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data)
# print("Softmax Stable Output:", output_stable)

softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)


my_softmax = Softmax()
output = my_softmax(data)
print(output_stable)
