---
layout: post
title:  "5 minute trip from R to Python: Visualization"
author: James Klein
description: A guide for R users to quickly master visualization in Python using the Plotnine package.
image: "/assets/images/penguin_plotP.png"
---

## ggplot2 to plotnine: A Guide for Data Science Students

### **Introduction**  
If you’ve worked with ggplot2 in R, you know how powerful and intuitive it is. With just a few lines of code, you can create visually appealing graphs that effectively communicate your data. But if you’re transitioning from R to Python, working on a project in Python, or simply curious, you may have wondered if Python has an equivalent.  

The good news is that Python does—Plotnine. Built on the same grammar-of-graphics principles as ggplot2, Plotnine allows you to create layered visualizations with familiar syntax, making the transition to Python’s visualization ecosystem feel seamless.  

This guide will walk you through the similarities, differences, and practical applications of Plotnine to help you get started.  

### What is Plotnine?
Plotnine is a Python library inspired by R’s ggplot2 and developed by Hassan Kibirige. It provides a structured, grammar-of-graphics approach to visualization, enabling users to build complex plots with minimal code. Whether you’re moving from R to Python or frequently switching between the two, Plotnine offers a smooth learning curve and an intuitive way to create high-quality visualizations.  

### Why Should You Use Plotnine?
- **Familiar Syntax** – If you’re comfortable with ggplot2, transitioning to Plotnine feels natural. The grammar-of-graphics approach remains the same, so you can start visualizing data in Python with minimal learning curve.  
- **Structured & Layered Visualizations** – Plotnine follows the grammar of graphics, allowing you to build complex plots by adding layers, themes, and scales—just like in ggplot2. This makes it easier to create customized and insightful visualizations.  
- **Seamless Integration with Pandas** – Since Plotnine works directly with Pandas DataFrames, you can seamlessly integrate it into your Python data analysis workflow, making it a great choice for those already using Pandas for data manipulation.  

### What is the Grammar of Graphics?  
The grammar of graphics is a structured approach to data visualization that breaks a chart into fundamental components rather than treating it as a single entity. These components include data, aesthetics, geometric objects, scales, and layers, which can be combined systematically to build complex yet intuitive visualizations.  

Both ggplot2 (R) and Plotnine (Python) follow this approach, allowing users to construct plots in a declarative and layered manner. Instead of specifying a chart all at once, you start with data, define how variables are mapped to aesthetics (such as axes, colors, and shapes), and then add geometric objects (such as points, lines, or bars) to visually represent the data. This makes it easy to incrementally refine a plot by adding, modifying, or customizing elements.  

### Key Similarities Bewteen ggplot2 and Plotnine
Plotnine modeled after ggplot2, they share many fundamental similarities such as: 
- **Layered Composition** – Both libraries use the + operator to add elements incrementally, such as geoms (geometric objects), themes, scales, and labels.  
- **Aesthetic Mapping (aes())** – Both use aesthetic mappings to link data attributes (e.g., x/y position, color, size) to visual properties dynamically.  
- **Faceting for Multi-Panel Plots** – Functions like facet_wrap() and facet_grid() allow users to split data into multiple subplots, making it easier to compare different categories.  
- **Customization & Extensibility** – Users can modify themes, define custom geoms, and extend functionality in both libraries, ensuring flexibility in visualization design.

### Key Differences Between ggplot2 and Plotnine
There are a few minor distinction between ggplot and plotnine that should be considered:
- **Data Handling** - while both function on dataframes, R uses tidyverse while Python uses Pandas. While similar, there may be cases where Pandas and Tidyverse handle the data slightly differently meaning the code may not be identical across languages.
- **Performance** – ggplot2 is highly optimized for R, making it efficient for handling large datasets. In contrast, Plotnine can be slower in Python, particularly with larger datasets, because it lacks the same level of performance optimizations as ggplot2.
- **Functionality Gaps** – While Plotnine replicates most ggplot2 features, some advanced functionalities, such as interactive plotting and certain statistical transformations, may be more developed in ggplot2. Python users often rely on Matplotlib or Seaborn to bridge in these gaps.  

### Code Comparison: ggplot2 vs. Plotnine

#### Example 1: Penguins Scatter Plot

Since the palmer penguins data is accessible in both Python (seaborn) and R (palmerpenguins), we will use it to demonstrate the similarities and differences between ggplot2 and Plotnine in making a basic scatterplot.

**ggplot2 (R)**
```r
library(ggplot2)
library(palmerpenguins)
ggplot(data = penguins, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point() +
  theme_minimal() +
  labs(title = "Flipper Length vs Body Mass in Penguins",
       x = "Flipper Length (mm)",
       y = "Body Mass (g)")
```
![Flipper Length vs Body Mass in Penguins (R)](https://schneeman71.github.io/Klein-Blog/assets/images/penguin_plotG.jpg)


**Plotnine (Python)**
```python
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import seaborn as sns

penguins = sns.load_dataset("penguins")

plot = (
    ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g", color="species")) +
    geom_point() +
    theme_light() +
    labs(title="Flipper Length vs Body Mass in Penguins", 
         x="Flipper Length (mm)", 
         y="Body Mass (g)")
)
```
![Flipper Length vs Body Mass in Penguins (R)](https://schneeman71.github.io/Klein-Blog/assets/images/penguin_plotG.png)



As you can see, the syntax is nearly identical. You may also notice that matplotlib is also imported for python, however that's simply because it's a dependency for plotnine. In case you are unfamiliar with python, "from plotnine import *" simply means import all functions from the plotnine library. 


### When Should You Use Plotnine in Python?
Plotnine is best used as a transitory tool between visualization in R vs Python. It's most useful when:
- You are transitioning from R to Python and want similar syntax
- You prefer a declarative approach to visualization
- You are primarily working in R, but sometimes use Python

However, as mentioned slightly before, plotnine works slower in python than it's competitors. As such for performance-heavy tasks, matplotlib and seaborn might be preferable in Python due to better optimization and support


### Further Resources
- [Plotnine Documentation](https://plotnine.readthedocs.io/)
- [ggplot2 Official Site](https://ggplot2.tidyverse.org/)
- [Data Visualization in Python with Plotnine](https://towardsdatascience.com/using-plotnine-for-python-data-visualization-31d4c54e6eaf)


### Call to Action
For R users moving to Python, plotnine is a powerful alternative to ggplot2, preserving the grammar of graphics approach while integrating with Python's ecosystem. While some trade-offs exist, it remains an excellent option for those seeking familiarity in a new environment.

Try converting some of your existing ggplot2 visualizations into plotnine and see how quickly you can get the graphs working! If you found this tutorial helpful, consider sharing it with others who might be making the switch from R to Python.
