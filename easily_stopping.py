from typing import Self
import torch
import abc
import copy
from pathlib import Path
# def CheckOverloop(weights, bias, loss, minimum_threshold = 0.0001, patience = 5):
#     current_loss = float('inf')
#     if abs(current_loss - loss) <= minimum_threshold:
#         break;
#     if current_loss > loss:
#         current_loss = loss
#     return 


class EarlyStopping:
    def __init__(self, patience=10, min_delta=0.001, warmup=50, saving_dict = "models", model_name = "01.pth"):
        self.patience = patience
        self.min_delta = min_delta
        self.warmup = warmup  # 新增：前50轮不启动早停
        self.best_loss = float('inf')
        self.counter = 0
        self.epoch = 0  # 新增：总训练轮次跟踪
        self.best_model_state = None
        self.MODEL_PATH = Path(saving_dict)
        self.MODEL_SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)

        self.MODEL_SAVE_PATH = self.MODEL_PATH / model_name
        
        
       


    def __call__(self, current_loss):
        current_val = round(current_loss.item(), 5)  # 关键！四舍五入到5位小数
        self.epoch += 1
        
        if self.epoch < self.warmup:
            return False  # 热身阶段不触发
        
        # 改进条件判断：需同时满足绝对值和相对改进
        if current_val < (self.best_loss - max(self.min_delta, self.best_loss*0.01)):
            self.best_loss = current_val
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                print(f"Early stopping triggered at epoch {self.epoch}")
            return True
        
        print(current_loss, self.best_loss, abs(current_loss-self.best_loss))
        
        return False

    # def __call__(self, current_loss, model):
    #     if abs(current_loss - self.best_loss) <= self.min_delta:
    #         if self.save_path: # 保存路径是否存在
    #             self.best_model_state = model.state_dict().copy() # 自动保存模型权重和偏差
    #         return True
    #     if current_loss < self.best_loss:
    #         self.best_loss = current_loss.detach().item()
    #         self.count = 0
    #     else:
    #         self.count += 1
    #         if self.count >= self.patience:
    #             return True
        # print(current_loss, self.best_loss, abs(current_loss-self.best_loss))
    #     return False
    
    



    def save_model(self, model):
        if self.best_model_state:
            model.load_state_dict(self.best_model_state)
            torch.save(obj=model.state_dict(), f=self.MODEL_SAVE_PATH)

    def load_model(self, model_class):
        model = model_class()
        model.load_state_dict(torch.load(f=self.MODEL_SAVE_PATH, weights_only=False))
        model.eval()
        return model
        
    
