#!/usr/bin/env python
# coding: utf-8

# In[82]:


import time
import numpy as np


# In[83]:


retry = 100
elem = 500000


# In[84]:


# for list
# lets add 5000 elements + 5000 elements
import random
a = []; b = []
for i in range(elem):
    a.append(random.random())
    b.append(random.random())
len(a)


# In[85]:


# 10回の平均を取る
time1 = []
for i in range(retry):
    start = time.time()
    c = a + b
    end = (time.time() - start) * 1000
    time1.append(end)
nonumpy = np.mean(time1)


# In[86]:


# numpyを使った場合
a = np.random.randn(elem)
b = np.random.randn(elem)
time2 = []

for i in range(retry):
    start = time.time()
    c = a + b
    end = (time.time() - start) * 1000
    time2.append(end)
numpyt = np.mean(time2)


# In[87]:


print("numpyの方が %s 倍高速" % str(nonumpy/numpyt))


# In[88]:


# 10回の平均を取る
a = []; b = []
for i in range(elem):
    a.append(random.random())
    b.append(random.random())
    
time1 = []
for i in range(retry):
    start = time.time()
    c = a * b
    end = (time.time() - start) * 1000
    time1.append(end)
nonumpy = np.mean(time1)

# numpyを使った場合
a = np.random.randn(elem)
b = np.random.randn(elem)

time2 = []
for i in range(retry):
    start = time.time()
    c = a * b
    end = (time.time() - start) * 1000
    time2.append(end)
numpyt = np.mean(time2)

print("numpyの方が掛け算は %s 倍高速" % str(nonumpy/numpyt))


# In[ ]:




