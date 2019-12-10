import torch
import torch.nn as nn
import torch.nn.functional as F
import pipeline

class MyClassifier(nn.Module):
    def __init__(self):
        super(MyClassifier,self).__init__()
        #Our network consists of 3 layers. 1 input, 1 hidden and 1 output layer
        #This applies Linear transformation to input data.
        self.fc1 = nn.Linear(11,5)
        self.fc2 = nn.Linear(5,4)
        self.fc3 = nn.Linear(4,3)
        #This applies linear transformation to produce output data
        self.fc4 = nn.Linear(3,2)

    #This must be implemented
    def forward(self,x):
        #Output of the first layer
        x = self.fc1(x)
        x = F.tanh(x)
        x = self.fc2(x)
        x = F.tanh(x)
        x = self.fc3(x)
        x = F.tanh(x)
        x = self.fc4(x)
        #This produces output
        return x

    #This function takes an input and predicts the class, (0 or 1)
    def predict(self,x):
        #Apply softmax to output.
        pred = F.softmax(self.forward(x))
        # ans = []
        #Pick the class with maximum weight
        # for t in pred:
        #     if t[0]>t[1]:
        #         ans.append(0)
        #     else:
        #         ans.append(1)
        return pred.detach().numpy()




