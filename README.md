# a-simple-early_stopping-code/一个简单的早停代码
## notice: I`m not prefessional programmer and not being good at my English,so this will occur to lots of erros,if you find the errors or bugs,please tell me

## ==the log of update!!!!!!==
I creat a new class--Saving_and_loading,it can work out the errors of MODEL_SAVE_PATH.
what you only need to input the two parameters can implement saving and loading model automatically,you can see following method if you want to learn more.


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
you only upload your loss, and this fucntion will do gardient desceent and backpropagation automatically.

## extra-func
you can invoke :es.save_model(model), es.load_model(model_class, modep_path)
### 7. model:this The model for this call is the model that you created the object in the first place
### 8. model_class: beacuse load the new model need creat the new object, so we need recreat the object


## reason of  writing this code
Because I am learning Pytorch at present,this is a link of course[Pytorch](https://youtu.be/V_xro1bcAuA?si=b0_8yWiFXzLcFdnr).When I start the training loop, finding that the too many loops will waste possibly.For example,when I set the "epoch = 10000",but maybe it can achieve good fitting effect in 100times,and remaining times will consume mermory.**So, I want to design the programming to stop the loop previously.**(notice: I write the code with deepseekR1)



## 一个简单的早停代码
## ==更新日志!!!!!!==
我创建了一个类，这样就不会出现有关 MODEL_SAVE_PATH.的报错了
你只需要传入两个参数就可以实现存储并载入模型，如果你想要了解更多，可以看一下下面的方法。

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
### 5. model_name="xxx.pth":这个是你的模型名字. 类似的, deepseek-r1, llama, Qwen, 这个是他们的模型名字, 你可以给你的模型命名为"deepsearch" or "deepdig"
---
### 这个是__call__函数的参数
### 6. loss:
你可以像这样获得你模型的损失
```python
loss = torch.L1Loss(y_pred, y_train)
```
你只需要上传你的loss，然后这个函数会自动梯度下降和反向传播

## 额外的函数
你可以调用 :es.save_model(model), es.load_model(model_class, modep_path)
### 7. model:这个调用的模型是你刚开始创建对象的模型
### 8. model_class:因为加载一个新的模型需要创建一个新的对象，所以我们需要重新创建新的对象

## 写这个类的原因
因为我目前正在学习Pytorch，这当然是一个链接[Pytorch]（https://youtu.be/V_xro1bcAuA?si=b0_8yWiFXzLcFdnr）。当我开始训练循环时，发现太多的循环可能会浪费时间。例如，当我设置“epoch = 10000”时，但可能100次就能达到很好的拟合效果，剩余的次数会消耗内存。所以，我想设计的程序，以停止循环之前。**（注意：我和deepseekR1一起写代码）


