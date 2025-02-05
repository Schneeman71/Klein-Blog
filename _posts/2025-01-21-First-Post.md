---
layout: post
title:  "5 minute trip from R to Python: Visualization"
author: James Klein
description: A guide for R users to quickly master visualization in Python using the Plotnine package.
image: "/assets/images/penguin_plotP.png"
---

## ggplot2 to plotnine: A Guide for Data Science Students

### Introduction
If you're coming from an R background and are interested in transitioning to Python for data visualization, or if you're working on a Python project but are already familiar with ggplot2, you might be wondering if Python has an equivalent.

Fortunately, Plotnine brings the elegance and power of ggplot2 to Python, making the transition smoother than you might expect. This guide will walk you through the similarities, differences, and practical implementations of Plotnine, helping you seamlessly adapt to Python's visualization ecosystem.

### What is Plotnine?
Plotnine is a Python library inspired by R's ggplot2, providing a grammar-of-graphics approach for creating layered visualizations easily. It allows users to build plots using the same structured syntax as ggplot2, making it highly attractive for people considering transitioning to Python from R, or for people who frequently work with both. 

### Why Should You Use Plotnine?
- Familiar Syntax: If you already know ggplot2, transitioning to plotnine is easy.
- Grammar of Graphics: Allows for structured and layered visualization building.
- Integration with Pandas: Works well with Python's data manipulation ecosystem.

### Key Similarities Between ggplot2 and Plotnine
Both libraries operate under the grammar of graphics paradigm, allowing users to construct plots in a declarative manner. Some fundamental similarities include:

- **Layered Approach**: Both use the + operator to add elements like geoms, themes, and scales.
- **Aesthetic Mapping (aes): Both libraries use aesthetic mappings to bind data attributes to visual properties.
- **Faceting (facet_wrap, facet_grid): Multi-panel plots are supported in both ggplot2 and plotnine.
- Extensibility: Users can easily create custom geoms, themes, and extensions in both environments.

### Key Differences Between ggplot2 and Plotnine
While plotnine is modeled after ggplot2, there are some notable differences:
While in R GGplot works locally with tidyverse dataframes, Python uses Pandas dataframes
GGplot is optimized for R, so comparitively Plotnine will work slower in Python.

### Code Comparison: ggplot2 vs. Plotnine

#### Example 1: Penguins Scatter Plot

Since the palmer penguins data is accessible in both Python (seaborn) and R (palmerpenguins), we will use it to demonstrate the similarities and differences between ggplot2 and Plotnine

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
![Flipper Length vs Body Mass in Penguins (R)](/assets/images/penguin_plotG)


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
![Flipper Length vs Body Mass in Penguins (Python)](/assets/images/penguin_plotP)


As you can see, the syntax is nearly identical. You may also notice that matplotlib is also imported for python, however that's simply because it's a dependency for plotnine. In case you are unfamiliar with python, "from plotnine import *" simply means import all functions from the plotnine library. 

### When Should You Use Plotnine in Python?
While plotnine offers a familiar ggplot2-like experience, it may not always be the best choice. Consider `plotnine` when:
- You are transitioning from R and want a similar syntax.
- You prefer a declarative approach to visualization.
- You are working with structured tabular data in Pandas.

However, as mentioned slightly before, plotnine works slower in python than it's competitors. As such for performance-heavy tasks, matplotlib and seaborn might be preferable in Python due to better optimization.

### Further Resources
- [Plotnine Documentation](https://plotnine.readthedocs.io/)
- [ggplot2 Official Site](https://ggplot2.tidyverse.org/)
- [Data Visualization in Python with Plotnine](https://towardsdatascience.com/using-plotnine-for-python-data-visualization-31d4c54e6eaf)

### Call to Action
For R users moving to Python, plotnine is a powerful alternative to ggplot2, preserving the grammar of graphics approach while integrating with Python's ecosystem. While some trade-offs exist, it remains an excellent option for those seeking familiarity in a new environment.

Try converting some of your existing ggplot2 visualizations into plotnine and see how quickly you can get the graphs working! If you found this tutorial helpful, consider sharing it with others who might be making the switch from R to Python.
