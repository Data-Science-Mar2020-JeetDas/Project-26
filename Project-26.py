# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/Project-26.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project-26 : Probability of dying by age 5 per 1000 live birth [By WHO]");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available country

country = df.groupby(['Location'])[['Period']].count()
print("---------------------------------")
print("\tAvailable country names : ")
print("-------------------------------")
print(country)
print("-------------------------------")
count = 0
for row in range(len(country)): 
        count = count+1
print("total no. of country = ",count)        
print("-----------------------------\n")


# Question - D : Available years data for which data is available

years = df.groupby(['Period'])[['Location']].count()
print("---------------------------------")
print("\tAvailable years data : ")
print("-------------------------------")
print(years)
print("-------------------------------")
count = 0
for row in range(len(years)): 
        count = count+1
print("total no. of years = ",count)        
print("-----------------------------\n")


# Question - E :Types of available indicators

indicator = df.groupby(['Indicator'])[['Period']].count()
print("---------------------------------")
print("\tAvailable types of indicators : ")
print("-------------------------------")
print(indicator)
print("-------------------------------")
count = 0
for row in range(len(indicator)): 
        count = count+1
print("total no. of indicators = ",count)        
print("-----------------------------\n")

#***************[ Question-01 : Creating India data  ]********************

# Number of infant deaths (thousands) 
# Number of neonatal deaths (thousands) 
# Number of under-five deaths (thousands) 

df_india = df[df.Location == 'India']

df1 = df_india[df_india.Indicator == 'Number of infant deaths (thousands)']
df2 = df_india[df_india.Indicator == 'Number of neonatal deaths (thousands)']
df3 = df_india[df_india.Indicator == 'Number of under-five deaths (thousands)']

print("-----------[ Output-A : Number of infant deaths (thousands) ]---------")
print(df1[['Location','Period','First Tooltip']])

print("-----------[ Output-B : Number of neonatal deaths (thousands) ]---------")
print(df2[['Location','Period','First Tooltip']])

print("-----------[ Output-C : Number of under-five deaths (thousands) ]---------")
print(df3[['Location','Period','First Tooltip']])

plt.title('Question - 01 : India ')

plt.xlabel("Years --- >")
plt.ylabel("Number(thousands) --- >")
    
plt.plot(df1['Period'],df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Number of infant deaths (thousands)")

plt.plot(df2['Period'],df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Number of neonatal deaths (thousands)")

plt.plot(df3['Period'],df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Number of under-five deaths (thousands)")

plt.legend()
plt.show()

#***************[ Question-02 : Creating Bangladesh data  ]********************

# Number of infant deaths (thousands) 
# Number of neonatal deaths (thousands) 
# Number of under-five deaths (thousands) 

df_Bangladesh = df[df.Location == 'Bangladesh']

df1 = df_Bangladesh[df_Bangladesh.Indicator == 'Number of infant deaths (thousands)']
df2 = df_Bangladesh[df_Bangladesh.Indicator == 'Number of neonatal deaths (thousands)']
df3 = df_Bangladesh[df_Bangladesh.Indicator == 'Number of under-five deaths (thousands)']

print("-----------[ Output-A : Number of infant deaths (thousands) ]---------")
print(df1[['Location','Period','First Tooltip']])

print("-----------[ Output-B : Number of neonatal deaths (thousands) ]---------")
print(df2[['Location','Period','First Tooltip']])

print("-----------[ Output-C : Number of under-five deaths (thousands) ]---------")
print(df3[['Location','Period','First Tooltip']])

plt.title('Question - 02 : Bangladesh ')

plt.xlabel("Years --- >")
plt.ylabel("Number(thousands) --- >")
    
plt.plot(df1['Period'],df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Number of infant deaths (thousands)")

plt.plot(df2['Period'],df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Number of neonatal deaths (thousands)")

plt.plot(df3['Period'],df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Number of under-five deaths (thousands)")

plt.legend()
plt.show()


#***************[ Question-03 : Creating Bhutan data  ]********************

# Number of infant deaths (thousands) 
# Number of neonatal deaths (thousands) 
# Number of under-five deaths (thousands) 

df_Bhutan = df[df.Location == 'Bhutan']

df1 = df_Bhutan[df_Bhutan.Indicator == 'Number of infant deaths (thousands)']
df2 = df_Bhutan[df_Bhutan.Indicator == 'Number of neonatal deaths (thousands)']
df3 = df_Bhutan[df_Bhutan.Indicator == 'Number of under-five deaths (thousands)']

print("-----------[ Output-A : Number of infant deaths (thousands) ]---------")
print(df1[['Location','Period','First Tooltip']])

print("-----------[ Output-B : Number of neonatal deaths (thousands) ]---------")
print(df2[['Location','Period','First Tooltip']])

print("-----------[ Output-C : Number of under-five deaths (thousands) ]---------")
print(df3[['Location','Period','First Tooltip']])

plt.title('Question - 03 : Bhutan ')

plt.xlabel("Years --- >")
plt.ylabel("Number(thousands) --- >")
    
plt.plot(df1['Period'],df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Number of infant deaths (thousands)")

plt.plot(df2['Period'],df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Number of neonatal deaths (thousands)")

plt.plot(df3['Period'],df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Number of under-five deaths (thousands)")

plt.legend()
plt.show()






