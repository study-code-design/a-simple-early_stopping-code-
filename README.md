# a-simple-early_stopping-code-


## 1.invoking the class
```python
from easily_stopping import EarlyStopping as es
```
## 2.creat the object
```python
easily_stopper = es()
```

## parsing code
you can customize your model, I provide the 10 parameters to let you set freely.
### 1. patience=int:in brief, it is time which you can bear the loss of not reducing,this is 10 times by default
### 2. min_delta=float: it is subjective thing.What you think how much decrease loss is appropriate(**if you set it too big, and resulting in the run out of the "patience "prematurely )
### 3. warmup=int:this parameter come from AI, he think losses fluctuated wildly before 50 times, I can`t ensure whether it is right.
### 4. saving_dict=string:haha, this is by myself,because i am learning the saving model and loading model.this parameter will decide your dictionary name, you can name a good name.
### 5. model_name="xxx.pth":this your model name. As we all know, deepseek-r1, llama, Qwen, this is the model name, you can name the "deepsearch" or "deepdig"
---
this the function of __call__ parameters
### 6. loss:
you can get loss like:
```python
loss = torch.L1Loss(y_pred, y_train)
```
you only upload your loss, and this fucntion will do gardient desceent and backpropagation.

## extra-func
you can invoke :es.save_model(model), es.load_model(model_class, modep_path)
### 7. model:


## reason of  writing this code
Because I am learning Pytorch at present,this is a link of course[Pytorch](https://youtu.be/V_xro1bcAuA?si=b0_8yWiFXzLcFdnr).When I start the training loop, finding that the too many loops will waste possibly.For example,when I set the "epoch = 10000",but maybe it can achieve good fitting effect in 100times,and remaining times will consume mermory.**So, I want to design the programming to stop the loop previously.**(notice: I write the code with deepseekR1)
