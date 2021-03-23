import torch 
import torchvision
import time 
model = torchvision.models.vgg16().cuda()
with torch.no_grad():
    inputs = torch.rand(64, 3, 128, 128).cuda() 
    while True:
        for step in range(500):
            outputs = model(inputs) 
        time.sleep(15)