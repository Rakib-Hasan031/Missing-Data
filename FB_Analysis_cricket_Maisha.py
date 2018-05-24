
# coding: utf-8

# In[1]:


import requests
import time
import pickle
import random


# In[2]:


token='EAACEdEose0cBAHlT9GOqRyyzNZAaxCKYcC7sopYos5ddNMffmPuWW8eWcQ4cUhpxBjSdnHgi25Sk8mpEHV0k8W0SuURr94ZCePCVNKleeawxs95T8Gl7foHAZBybtZChnZCB6CIUdXo9YFtXetIw78I4qGFLQNjRTI0Vm8QiCKLg6rfIqu576g6VRfcGqZCsWTnalA3ZCSIRQZDZD'


# In[3]:


graph_url = 'https://graph.facebook.com/v3.0/'
req_url = '1374983146102829?fields=posts{message,created_time,comments.limit(0).summary(true), likes.limit(0).summary(true)}'
final_url = graph_url + req_url


# In[4]:


results = requests.get(final_url,{'access_token':token})


# In[7]:


print(results.json())

