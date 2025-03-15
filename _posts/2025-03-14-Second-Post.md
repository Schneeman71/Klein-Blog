---
layout: post
title:  "The lasting impact of COVID-19 on the Gaming Industry"
author: James Klein
description: An analysis of how the COVID-19 pandemic influence the growth of long term gaming habits.
image: /assets/images/gaming-impact.jpg
---

## Introduction: Why This Project Matters
The COVID-19 pandemic drastically altered many aspects of daily life, and one of the most significant shifts occurred in entertainment consumption. With lockdowns and social distancing measures in place, people turned to gaming as a primary source of entertainment, leading to a surge in player counts across various platforms. However, a crucial question remains: **Did this growth in gaming persist beyond the pandemic, or was it a temporary trend?**

This project explores whether the pandemic resulted in lasting growth in gaming by analyzing player count data from Steam, one of the largest PC gaming platforms. By studying historical trends and post-pandemic data, we aim to understand how gaming habits have evolved and whether developers and companies can rely on sustained player engagement.

## Ethical Considerations and Data Collection
When collecting data, it is essential to ensure that it is gathered ethically and in accordance with platform guidelines. The data for this project comes from the following sources:
- **SteamDB & SteamCharts**: These platforms provide historical player count data for PC games.
- **Steam Web API**: This API offers real-time player count data for specific games.

The data was accessed using publicly available tools and was collected without violating any terms of service. Additionally, proper web scraping practices were followed to ensure minimal server load and ethical data retrieval.

## How to Collect Similar Data
If you are interested in conducting a similar analysis, here are the steps to get started:
1. **Identify a Data Source**: Websites like SteamDB, SteamCharts, and APIs such as the Steam Web API offer valuable gaming data.
2. **Use an API or Web Scraping**: If an official API exists, use it to retrieve structured data. Otherwise, ethical web scraping techniques, such as setting request intervals and respecting `robots.txt`, should be followed.
3. **Store and Clean the Data**: Organize your dataset in a structured format (CSV, JSON, etc.), removing any inconsistencies or missing values.
4. **Analyze Trends**: Focus on key metrics such as player counts, growth rates, and overall trends across different time periods.

## Exploratory Data Analysis (EDA) Highlights
### Summary of the Dataset
- **Total Sample Size**: 797 rows
- **Key Features**:
  - **Game Title**: Name of the game
  - **Month**: Time period of observation
  - **Average Player Count**: Mean number of players during that month
  - **Monthly Growth Rate**: Percentage change in player count compared to the previous month
  - **Total Player Count**: Sum of all average player counts for trend observation
- **Time Scope**: Data spans from as early as 2012 to the present
- **Games Included**: Seven popular titles across different genres

### Key Findings
- **Pre-Pandemic vs. Post-Pandemic Trends**: Player counts surged during the pandemic, but some games retained higher engagement levels even after restrictions were lifted.
- **Sustained Growth in Some Genres**: Multiplayer and social games saw a more permanent player increase, while single-player titles experienced a gradual decline post-pandemic.
- **Seasonal Variations**: Gaming spikes align with major holidays and new content releases, independent of pandemic influence.

## Where to Learn More
If you want to dig deeper into this project or replicate it, check out these resources:
- **Steam Web API Documentation**: [https://developer.valvesoftware.com/wiki/Steam_Web_API](https://developer.valvesoftware.com/wiki/Steam_Web_API)
- **SteamDB**: [https://steamdb.info/](https://steamdb.info/)
- **SteamCharts**: [https://steamcharts.com/](https://steamcharts.com/)

### GitHub Repository
For access to the full dataset, data collection scripts, and analysis code, visit: [GitHub Repo Link - Replace with actual link]

## Conclusion
The pandemic undeniably caused a gaming boom, but the lasting effects are nuanced. While some games retained new players, others saw engagement drop as people returned to pre-pandemic routines. Understanding these trends is crucial for game developers, publishers, and industry analysts in predicting future growth patterns.

For students and analysts interested in replicating or extending this research, the dataset and methods outlined here provide a strong foundation for further exploration. Happy analyzing!

