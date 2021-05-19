#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to Data Visualization with Python")


# In[2]:


first_name = "Joseph"
print(type(first_n
           ame))


# In[3]:


first_name = "Joseph"
print(type(first_name))


# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


import matplotlib.pyplot as plt
import numpy as np
import math 

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot (x_vals, y_vals)


# In[7]:


import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
fig = plt.figure()
ax = plt.axes()
ax.plot(x_vals, y_vals)


# In[8]:


import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams["figure.figsize"] = [8,6]

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
fig = plt.figure()
ax = plt.axes()
ax.plot(x_vals, y_vals)


# In[9]:


import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals)


# In[10]:


import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals)
plt.plot(x_vals, y_vals, 'r')


# In[11]:


import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
y2_vals = x_vals ** 3
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals)
plt.plot(x_vals, y_vals, 'r', label = 'Square Root')
plt.legend(loc='upper center')


# In[14]:


import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
y2_vals = x_vals ** 3
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals, 'b', label = 'Cube')
plt.plot(x_vals, y_vals, 'r', label = 'Square Root')
plt.legend(loc='upper center')


# In[15]:


import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
y2_vals = x_vals ** 3
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals, 'r', label = 'Square Root')
plt.plot(x_vals, y_vals, 'b', label = 'Cube')
plt.legend(loc='upper center')


# In[17]:


import matplotlib.pyplot as plt 
import numpy as np 
import math 
x_vals = np.linspace(0, 20, 20) 
y_vals = [math.sqrt(i) for i in x_vals] 
y2_vals = x_vals ** 3 
plt.xlabel('X Values')

plt.ylabel('Y Values') 
plt.title('Square Roots') 
plt.plot(x_vals, y_vals, 'r', label = 'Square Root') 
plt.plot(x_vals, y2_vals, 'b', label = 'Cube') 
plt.legend(loc='upper center')



# In[18]:


import matplotlib.pyplot as plt
import numpy as np
import math

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Sepal vs Petal Length')
plt.plot(data[sepal_length], data[petal_length], 'b')


# In[19]:


import matplotlib.pyplot as plt
import numpy as np
import math

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Sepal vs Petal Length')
plt.plot(data[sepal_length], data[petal_length], 'b')


# In[ ]:




