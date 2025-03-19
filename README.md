![009BF2CA](https://github.com/user-attachments/assets/e3baadec-1f0b-4e8a-8875-519a88ac2b84)# a-simple-early_stopping-code-


## 1.invoking the class
```python
from easily_stopping import EarlyStopping as es
```
## 2.creat the object
```python
easily_stopper = es()
```

## parsing code
you can customize your model, I provide the 8 parameters to let you set freely.
### 1. patience=int:in brief, it is time which you can bear the loss of not reducing,this is 10 times by default
### 2. min_delta=float: it is subjective thing.What you think how much decrease loss is appropriate(**if you set it too big, and resulting in the run out of the "patience "prematurely )
### 3. warmup=int:this parameter come from AI, he think losses fluctuated wildly before 50 times, I can`t ensure whether it is right.
### 4. saving_dict=string:haha, this is by myself,because i am learning the saving model and loading model.this parameter will decide your dictionary name which you store model, you can name a good name.
### 5. model_name="xxx.pth":this your model name. As we all know, deepseek-r1, llama, Qwen, this is the model name, you can name the "deepsearch" or "deepdig"
---
### this the function of __call__ parameters
### 6. loss:
you can get loss like:
```python
loss = torch.L1Loss(y_pred, y_train)
```
you only upload your loss, and this fucntion will do gardient desceent and backpropagation.

## extra-func
you can invoke :es.save_model(model), es.load_model(model_class, modep_path)
### 7. model:this model is what you write class by yourself which include the weight, bias,and inheriting nn.Model.
### 8. model_class: beacuse load the new model need creat the new object, so we need recreat the object

## reason of  writing this code
Because I am learning Pytorch at present,this is a link of course[Pytorch](https://youtu.be/V_xro1bcAuA?si=b0_8yWiFXzLcFdnr).When I start the training loop, finding that the too many loops will waste possibly.For example,when I set the "epoch = 10000",but maybe it can achieve good fitting effect in 100times,and remaining times will consume mermory.**So, I want to design the programming to stop the loop previously.**(notice: I write the code with deepseekR1)


# 一个简单的早停代码


## 1.如何调用这个类
```python
from easily_stopping import EarlyStopping as es
```
## 2.创建一个对象
```python
easily_stopper = es()
```

## 解析代码
你可以定制你自己的模型，我提供了8个参数来让你自由设置
### 1. 这是你可以忍受损失不下降的次数，默认是10次
### 2. min_delta=float: 这是个主观的参数，你认为你减少多少损失适合你。(**如果你设置的太大了，将会导致"耐心"过早的消耗完** ) 
### 3. warmup=int:这个参数是ai加上去的，他认为前50次损失波动较大，我不确认这个是否知真的
### 4. saving_dict=string:哈哈，这个是我自己加上去的，因为我现在正在学习存储模型和加载模型，这个参数决定了你存放模型文件夹的名字，你可以起一个好听的名字.
### 5. model_name="xxx.pth":this your model name. As we all know, deepseek-r1, llama, Qwen, this is the model name, you can name the "deepsearch" or "deepdig"
---
### this the function of __call__ parameters
### 6. loss:
you can get loss like:
```python
loss = torch.L1Loss(y_pred, y_train)
```
you only upload your loss, and this fucntion will do gardient desceent and backpropagation.

## extra-func
you can invoke :es.save_model(model), es.load_model(model_class, modep_path)
### 7. model:this model is what you write class by yourself which include the weight, bias,and inheriting nn.Model.
### 8. model_class: beacuse load the new model need creat the new object, so we need recreat the object

## reason of  writing this code
Because I am learning Pytorch at present,this is a link of course[Pytorch](https://youtu.be/V_xro1bcAuA?si=b0_8yWiFXzLcFdnr).When I start the training loop, finding that the too many loops will waste possibly.For example,when I set the "epoch = 10000",but maybe it can achieve good fitting effect in 100times,and remaining times will consume mermory.**So, I want to design the programming to stop the loop previously.**(notice: I write the code with deepseekR1)


