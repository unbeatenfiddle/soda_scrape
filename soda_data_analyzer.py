import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv('soda_data.csv')
data = data.drop(columns=['Ingredient'])




# Consolidate ingredients into a single list and count frequencies
all_ingredients = data.filter(like='Ingredient').values.flatten()
cleaned_ingredients = [ingredient for ingredient in all_ingredients if pd.notna(ingredient)]
ingredient_counts = pd.Series(cleaned_ingredients).value_counts()
most_common_ingredients = ingredient_counts.head(12)

# Font Setup
plt.rcParams.update({
    'font.size': 12,  # General font size
    'font.family': 'Arial',  # General font family
    'axes.facecolor': '#faf3e0', #background
    'axes.labelsize': 14,  # Font size for labels
    'axes.titlesize': 18,  # Font size for title
    'font.style': 'italic',  # Font style (normal, italic, etc.)
    'font.weight': 'bold',  # Font weight (normal, bold, etc.)
})

colors = plt.get_cmap('tab10')(np.linspace(0, 1, 10))
# Bar Chart
plt.figure(figsize=(11, 7), facecolor='#faf3e0')
most_common_ingredients.plot(kind='bar', color=colors)
plt.title('Top 12 most common ingredients across 65 American soda products', fontweight= 'bold', style = 'normal')
plt.xlabel('Ingredients', fontsize = 12, style ='normal')
plt.ylabel('Number of occurrences', fontsize = 12, style='normal')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()  

# Pie Chart

# explode = [0.05] * 12
# plt.figure(figsize=(9, 9), facecolor='#faf3e0')
# most_common_ingredients.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=colors, shadow =True, explode=explode)
# plt.title('Ingredient Distribution in 65 Different American Soda Products', fontsize= 16, fontweight = 'bold', style = 'normal', y=1.05)
# plt.ylabel('')  # Remove the y-label
# plt.show() 
