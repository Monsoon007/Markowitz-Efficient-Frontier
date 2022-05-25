import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import math

stocks_monthly_return = pd.read_excel('stocks_monthly_return.xlsx')
stocks_monthly_return.index=pd.DatetimeIndex(stocks_monthly_return.日期) # 日期索引变换
stocks_monthly_return.drop(labels=['日期'],axis=1,inplace=True)

R_cov = stocks_monthly_return.cov()
R_mean = stocks_monthly_return.mean()
R_corr=stocks_monthly_return.corr()    #计算相关系数矩阵
x=np.random.random(5)
weights=x/np.sum(x)       #生成和为1的随机数权重矩阵
# print('股票投资组合的权重：',weights)
R_port=np.sum(weights*R_mean)
# print('投资组合的预期收益率:',round(R_port,4))
risk_port=np.sqrt(np.dot(weights,np.dot(R_cov,weights.T)))
# print('投资组合收益风险',round(risk_port,4))

def gener_weights():
    weights = np.zeros(5)
    while weights.any() == False :
        x=np.random.random(5)*2-1
        # print(x)
        # weights = x/np.sum(x) 
        if np.sum(x) == 0:
            weights = np.zeros(5)
        else:
            weights = x/np.sum(x) 

        # 为了绘图集中，排除“异常点”
        R_port = np.sum(weights*R_mean)   
        risk_port = np.sqrt(np.dot(weights,np.dot(R_cov,weights.T)))

        if abs(R_port)>0.1 or abs(risk_port)>0.3:
            weights = np.zeros(5)

    return weights

#构造投资组合
Rp_list=[]
Vp_list=[]
plt.figure(figsize=(8,6))
plt.xlabel('Risk')
plt.xticks(fontsize=13)
plt.ylabel('Expected Return')
plt.yticks(fontsize=13)
plt.title('Efficient Frontier')
plt.grid('True')
for i in np.arange(30000):
    print(i)
    weights = gener_weights()
    Rp_new = np.sum(weights*R_mean)
    Vp_new = np.sqrt(np.dot(weights,np.dot(R_cov,weights.T)))
    Rp_list.append(Rp_new)
    Vp_list.append(Vp_new) ##dot矩阵乘法    
    if i <= 20:
        plt.scatter(Vp_list,Rp_list,c='blue')        
        plt.pause(0.03)
    # elif i <= 80:
    #     plt.scatter(Vp_list,Rp_list,c='blue')        
    #     plt.pause(0.01)
    elif i == 200:
        plt.scatter(Vp_list,Rp_list,c='blue')        
        plt.pause(0.01)
    elif i > 200 and (i%1000 == 0):
        plt.scatter(Vp_list,Rp_list,c='blue')        
        plt.pause(0.0002)
    # elif i > 20000 and (i%4000 == 0):
    #     plt.scatter(Vp_list,Rp_list,c='blue')        
    #     plt.pause(0.0002)