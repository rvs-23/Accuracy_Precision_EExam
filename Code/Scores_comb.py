#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
plt.style.use('dark_background')


# In[2]:


no_q = 50
start_score = 50
prec_50 = []
acc_50 = []
x_ = []
while start_score<200:
    print(f"Score: {start_score}")
    for i in range(1,no_q):
        for j in range(0,no_q):
            if i*4 + j*-1 == start_score and i+j<=no_q:
                acc = i/no_q
                prec = i/(i+j)
                print(f"TP: {i}\tFP:{j}\tNot Attempted(FN): {50-i-j}\tAccuracy: {acc}\tPrecision: {prec}")
                
                if start_score==100:
                    acc_50.append(acc)
                    prec_50.append(prec)
                    x_.append(i)
    start_score += 5
    print()


# In[3]:


fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x_, acc_50, 'g', label='Accuracy', linewidth=2)
ax.plot(x_, prec_50, 'r--', label='Precision', linewidth=2)
ax.set(xlim=(24.5,30.5), ylim=(0.4, 1.05))
ax.set_title("Accuracy vs Precision for Score 100")
ax.set_xlabel('True Positives')
ax.legend()
plt.show()
fig.savefig('Acc vs Prec.png', bbox_inches='tight')


# <hr>

# <hr>
