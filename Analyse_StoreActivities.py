#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[151]:


df = pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv')


# In[152]:


df.head()


# In[102]:


df['Total'] = df[list(df)[4:]].sum(axis=1)
print(df[["Proveedor","Costo", "Total"]])


# ### Cobro por Proveedor = Costo * Total

# In[103]:


df['Cobro'] = df['Costo']*df['Total']
print(df[["Proveedor","Costo", "Total", "Cobro"]])


# ### Suma acumulativa del cobro por proveedor:

# In[104]:


new_df = df
new_df['Ganancia'] = df.groupby(['Proveedor'])['Cobro'].transform('sum')
new_df = df.drop_duplicates(subset=['Proveedor'])
print(new_df.sort_values(by='Ganancia', ascending=False)[["Proveedor", "Ganancia"]])


# In[51]:


#new_df.duplicated(subset=['Proveedor'])


# In[64]:


#new_df.sort_values(by='Total', ascending=False)[["Proveedor", "Total"]]


# ### Los 5 proveedores que más cobraron en el año fueron:

# In[105]:


new_df.nlargest(5, 'Ganancia')[["Proveedor", "Ganancia"]]


# ### Los 5 proveedores que le dieron servicio a más tiendas en el año:

# In[138]:


df['Servicio'] = 1
df.groupby(['Proveedor']).Servicio.count().reset_index().nlargest(5, 'Servicio')


# ### La tienda con mayor gasto de mantenimiento en marzo

# **Gasto por Tienda = Costo * Marzo**

# In[150]:


df['Gasto'] = df['Costo']*df['Marzo']
new_df = df
new_df['GastoCum'] = df.groupby(['Tienda'])['Gasto'].transform('sum')
new_df.drop_duplicates(subset=['Tienda'])
new_df.nlargest(1, 'GastoCum')[['Tienda', 'GastoCum']]


# ### La tienda con mayor gasto de mantenimiento en julio

# **Gasto por Tienda = Costo * Julio**

# In[153]:


df['Gasto'] = df['Costo']*df['Julio']
new_df = df
new_df['GastoCum'] = df.groupby(['Tienda'])['Gasto'].transform('sum')
new_df.drop_duplicates(subset=['Tienda'])
new_df.nlargest(1, 'GastoCum')[['Tienda', 'GastoCum']]


# ### La tienda con mayor gasto de mantenimiento en todo el año:

# In[156]:


df = pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv')
df['Total'] = df[list(df)[4:]].sum(axis=1)
df['Gasto'] = df['Costo']*df['Total']
new_df = df
new_df['Gasto_Anual'] = df.groupby(['Tienda'])['Gasto'].transform('sum')
new_df = df.drop_duplicates(subset=['Tienda'])
new_df.nlargest(1, 'Gasto_Anual')[['Tienda', 'Gasto_Anual']]


# ### El mes en que se gastó más en mantenimiento a balanceadoras:

# In[193]:


df = pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv')
rslt_df = df[df['Equipo'] == "BALANCEADORA"]
GastoB = rslt_df[list(rslt_df)[4:]].multiply(rslt_df["Costo"], axis="index").sum()
print(GastoB.nlargest(1))


# ### Se gastó por cada tipo de artículo en septiembre:

# In[178]:


df = pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv')
df['GastoSep'] = df['Costo']*df['Septiembre']
new_df = df
new_df['GastoSep_Eq'] = df.groupby(['Equipo'])['GastoSep'].transform('sum')
new_df.drop_duplicates(subset=['Equipo'])[['Equipo', 'GastoSep_Eq']]


# ### Gasto por cada proveedor en mayo

# In[183]:


df = pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv')
df['GastoMayo'] = df['Costo']*df['Mayo']
new_df = df
new_df['GastoMay_Pr'] = df.groupby(['Proveedor'])['GastoMayo'].transform('sum')
new_df.drop_duplicates(subset=['Proveedor'])[['Proveedor', 'GastoMay_Pr']].sort_values(by=['Proveedor'])


# ### Gasto por cada tipo de artículo en el año

# In[184]:


df = pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv')
df['Total'] = df[list(df)[4:]].sum(axis=1)
df['GastoAn'] = df['Costo']*df['Total']
new_df = df
new_df['GastoAn_Eq'] = df.groupby(['Equipo'])['GastoAn'].transform('sum')
new_df.drop_duplicates(subset=['Equipo'])[['Equipo', 'GastoAn_Eq']]


# ### Número total de servicios a antenas por mes

# In[200]:


import pandas as pd

def TotServAntMes(df):
    rslt_df = df[df['Equipo'] == "ANTENAS"]
    GastoA = rslt_df[list(rslt_df)[4:]].multiply(rslt_df["Costo"], axis="index").sum()
    return GastoA


# In[201]:


TotServAntMes(pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv'))


# ________________________________________________________________________
# **Descripción:** Los proveedores cuyo número termina en 9 ofrecen 15% de descuento. Mientras que los que terminan en 6 solamente 3% de descuento.

# Crea una nueva columna que contenga la suma del costo total anual y otra con el costo total anual con descuento incluido.

# In[246]:


df = pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv')
df['Total'] = df[list(df)[4:]].sum(axis=1)

import numpy as np
conditions = [
    (df['Proveedor'].mod(10) == 9),
    (df['Proveedor'].mod(10) == 6)]
choices = [.85, .97]

df['Reduc'] = np.select(conditions, choices, default=1)

df['CostoReduc'] = (df['Costo']*df['Reduc']).astype(int)
new_df = pd.read_csv('Ejercicios_entrevista/dataset_mantenimiento.csv')
new_df['Costo Total Anual'] = df['Costo']*df['Total']
new_df['Costo Reducido Anual'] = df['CostoReduc']*df['Total']
new_df


# In[ ]:




