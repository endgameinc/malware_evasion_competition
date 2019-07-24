import torch
import torch.nn as nn
import torch.nn.functional as F

class MalConv(nn.Module):
    # trained to minimize cross-entropy loss
    # criterion = nn.CrossEntropyLoss()
    def __init__(self, out_size=2, channels=128, window_size=512, embd_size=8):
        super(MalConv, self).__init__()
        self.embd = nn.Embedding(257, embd_size, padding_idx=0)
        
        self.window_size = window_size
    
        self.conv_1 = nn.Conv1d(embd_size, channels, window_size, stride=window_size, bias=True)
        self.conv_2 = nn.Conv1d(embd_size, channels, window_size, stride=window_size, bias=True)
        
        self.pooling = nn.AdaptiveMaxPool1d(1)
        
        self.fc_1 = nn.Linear(channels, channels)
        self.fc_2 = nn.Linear(channels, out_size)
    
    def forward(self, x):
        
        x = self.embd(x.long())
        x = torch.transpose(x,-1,-2)
        
        cnn_value = self.conv_1(x)
        gating_weight = torch.sigmoid(self.conv_2(x))
        
        x = cnn_value * gating_weight
        
        x = self.pooling(x)
        
        #Flatten
        x = x.view(x.size(0), -1)
        
        x = F.relu(self.fc_1(x))
        x = self.fc_2(x)
        
        return x