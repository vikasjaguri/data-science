```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
```


```python
x = np.linspace(0,5,11)
y = x
x
```




    array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. ])




```python
y
```




    array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. ])




```python
plt.plot(x,y,'r')
#plt.plot(x+2,y+3,'g.-')
#plt.xlim(-2,12)
#plt.ylim(-3,4)
plt.xlabel('This is X axis')
plt.ylabel('This is Y axis')
plt.title('This is a graph')
plt.show
```




    <function matplotlib.pyplot.show(close=None, block=None)>




    
![png](output_3_1.png)
    



```python
a = np.random.normal(0,50,500)
b = np.random.normal(0,50,500)

plt.hist2d(a,b, bins = 60, cmap = 'bone')
plt.colorbar()
```




    <matplotlib.colorbar.Colorbar at 0x1d006f72ee0>




    
![png](output_4_1.png)
    



```python
tips = sns.load_dataset('tips')
tips.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



## Distplot


```python
sns.distplot(tips['total_bill'], kde='False')
```

    C:\Users\DELL\anaconda3\lib\site-packages\seaborn\distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
      warnings.warn(msg, FutureWarning)
    




    <AxesSubplot:xlabel='total_bill', ylabel='Density'>




    
![png](output_7_2.png)
    


## Jointplot


```python
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
```




    <seaborn.axisgrid.JointGrid at 0x1d00434ce50>




    
![png](output_9_1.png)
    



```python
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
```




    <seaborn.axisgrid.JointGrid at 0x1d006fe48b0>




    
![png](output_10_1.png)
    


## Pairplot
Pairplot will plot pairwise relatioships across am entire dataframe (for the numerical columns) and supports a color hue argument (for categorical columns).


```python
sns.pairplot(tips)
```




    <seaborn.axisgrid.PairGrid at 0x1d0076e8f70>




    
![png](output_12_1.png)
    



```python
sns.pairplot(tips, palette='brg')
```




    <seaborn.axisgrid.PairGrid at 0x1d007faec40>




    
![png](output_13_1.png)
    



```python
sns.pairplot(tips,hue='sex',palette='brg')
```




    <seaborn.axisgrid.PairGrid at 0x1d0076e8e20>




    
![png](output_14_1.png)
    


## Countplot


```python
sns.countplot(data = tips)
```




    <AxesSubplot:ylabel='count'>




    
![png](output_16_1.png)
    


## Rugplot


```python
sns.rugplot(tips['total_bill'])
```




    <AxesSubplot:xlabel='total_bill'>




    
![png](output_18_1.png)
    



```python
tips = sns.load_dataset('tips')
tips.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



## Heatmap


```python
heatmap_data = tips.corr()
sns.heatmap(heatmap_data, cmap='bone', annot=True)
```




    <AxesSubplot:>




    
![png](output_21_1.png)
    


## Barplot


```python
sns.barplot(x='day',y='total_bill',data=tips)
```




    <AxesSubplot:xlabel='day', ylabel='total_bill'>




    
![png](output_23_1.png)
    


## Boxplot


```python
sns.boxplot(x='day', y='total_bill', data=tips, palette='rainbow')
```




    <AxesSubplot:xlabel='day', ylabel='total_bill'>




    
![png](output_25_1.png)
    



```python
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker', palette='rainbow')
```




    <AxesSubplot:xlabel='day', ylabel='total_bill'>




    
![png](output_26_1.png)
    



```python
sns.boxplot(data=tips, palette='rainbow', orient='h')
```




    <AxesSubplot:>




    
![png](output_27_1.png)
    



```python
sns.boxplot(data=tips, palette='rainbow', orient='v')
```




    <AxesSubplot:>




    
![png](output_28_1.png)
    



```python
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker', palette='coolwarm')
```




    <AxesSubplot:xlabel='day', ylabel='total_bill'>




    
![png](output_29_1.png)
    


## Violinplot


```python
sns.violinplot(x="day", y="total_bill", data=tips, palette='rainbow')
```




    <AxesSubplot:xlabel='day', ylabel='total_bill'>




    
![png](output_31_1.png)
    



```python
sns.violinplot(x="day", y="total_bill", data=tips, hue='smoker', palette='rainbow')
```




    <AxesSubplot:xlabel='day', ylabel='total_bill'>




    
![png](output_32_1.png)
    


## Swarmplot


```python
sns.swarmplot(x='day', y='total_bill', data=tips)
```




    <AxesSubplot:xlabel='day', ylabel='total_bill'>




    
![png](output_34_1.png)
    



```python
sns.swarmplot(x='day', y='total_bill', data=tips, hue='sex')
```




    <AxesSubplot:xlabel='day', ylabel='total_bill'>




    
![png](output_35_1.png)
    


### Combining violin and swarm plots.

## Heatplot


```python
tips.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_bill</th>
      <td>1.000000</td>
      <td>0.675734</td>
      <td>0.598315</td>
    </tr>
    <tr>
      <th>tip</th>
      <td>0.675734</td>
      <td>1.000000</td>
      <td>0.489299</td>
    </tr>
    <tr>
      <th>size</th>
      <td>0.598315</td>
      <td>0.489299</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.heatmap(tips.corr())
```




    <AxesSubplot:>




    
![png](output_39_1.png)
    



```python
titanic = sns.load_dataset('titanic')
titanic.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## Jointplot


```python
sns.jointplot(x='fare', y='age', data=titanic, kind='scatter')
```




    <seaborn.axisgrid.JointGrid at 0x1d00bb6e700>




    
![png](output_42_1.png)
    


## Distplot


```python
sns.displot(x='fare', data=titanic)
```




    <seaborn.axisgrid.FacetGrid at 0x1d00bb33b80>




    
![png](output_44_1.png)
    


## Boxplot


```python
sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')
```




    <AxesSubplot:xlabel='class', ylabel='age'>




    
![png](output_46_1.png)
    


## Swarmplot


```python
sns.swarmplot(x='class', y='age', data=titanic)
```

    C:\Users\DELL\anaconda3\lib\site-packages\seaborn\categorical.py:1296: UserWarning: 11.0% of the points cannot be placed; you may want to decrease the size of the markers or use stripplot.
      warnings.warn(msg, UserWarning)
    




    <AxesSubplot:xlabel='class', ylabel='age'>




    
![png](output_48_2.png)
    


## Countplot


```python
sns.countplot(x='sex', data = titanic)
```




    <AxesSubplot:xlabel='sex', ylabel='count'>




    
![png](output_50_1.png)
    



```python
sns.countplot(data = titanic)
```




    <AxesSubplot:ylabel='count'>




    
![png](output_51_1.png)
    


## Distplot


```python
sns.distplot(titanic['fare'])
```

    C:\Users\DELL\anaconda3\lib\site-packages\seaborn\distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
      warnings.warn(msg, FutureWarning)
    




    <AxesSubplot:xlabel='fare', ylabel='Density'>




    
![png](output_53_2.png)
    


## Heatmap


```python
heatmap_data = titanic.corr()
sns.heatmap(heatmap_data, cmap='rainbow', annot=True)
```




    <AxesSubplot:>




    
![png](output_55_1.png)
    



```python

```
