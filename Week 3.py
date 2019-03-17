
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np

url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

df=pd.read_html(url, header=0)[0]

new_df = df[~df["Borough"].str.contains('Not assigned')]

sdf = new_df.groupby(['Postcode','Borough'])['Neighbourhood'].apply(', '.join).reset_index()

sdf['Neighbourhood'] = np.where(sdf['Neighbourhood'].str.contains('Not assigned'), sdf["Borough"], sdf['Neighbourhood'])

sdf

