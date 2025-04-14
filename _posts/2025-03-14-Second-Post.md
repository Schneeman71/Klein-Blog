---
layout: post
title:  "Through sickness and health, gaming?"
author: James Klein
description: A pre-emptive explorative EDA walkthrough of how the covid-19 pandemic may have impacted the gaming industry.
image: "/assets/images/game.jpg"
---

## **Introduction**

A few years ago, in March of 2020, one of the strangest events of the decade unfolded, turning everyday life upside down overnight. 

The Covid-19 pandemic uprooted daily routines, especially how we spent our free time. With lockdowns and social distancing in full effect, millions of people were suddenly stuck at home with minimal social activity outside immediate family. With nothing to do but watch any mildly entertaining TV show, start a new hobby, or simply twiddle our thumbs, some people turned to gaming.

With nowhere to go and nothing to do, people who had never really gamed before suddenly decided to give it a try. Player counts across different platforms skyrocketed as gaming became not just a pastime, but also a way to stay connected with friends despite pandemic protocol.  

Thankfully the pandemic ended, but now that life has mostly gone back to normal and a few years have passed, a crucial question remains:  

**Did these pandemic-era gamers stick around, or did they abandon their new hobby once the world reopened?**  

As such, we will analyze playercount data from steamcharts to analyze growth by game (PC) to determine whether single or multiplayer games were more popular, and whether the growth spike caused by the pandemic created lasting growth or just a one time jump.

## Ethical Considerations and Data Collection

When collecting our data, we aimed to be mindful of ethical concerns. Typically, the first step would be to check for a robots.txt file, which outlines a website's scraping permissions. However, SteamCharts does not appear to have one.

Despite this, we took precautionary measures to ensure we were not interfering with traffic. To minimize server load, we implemented a 2-second delay between requests, preventing excessive strain on their infrastructure.

Furthermore, all data was collected without violating any terms of service, and we adhered to proper web scraping practices to ensure ethical and responsible data retrieval.

## How to Collect Similar Data
If you're interested in conducting a similar analysis, here’s how you can get started:

- Identify a Data Source
Websites like SteamDB, SteamCharts, and the Steam Web API offer valuable gaming data. While I used SteamCharts for this analysis, Steam’s official API is well structured and easy to work with. If you choose to use webscraping, just ensure to follow terms of service or the requests detailed in a robots.txt (if there is one)

If you're looking to expand the analysis beyond PC gaming, you could explore PlayStation Network or Xbox Live reports. However, these platforms don’t publicly release their player data, making it much more challenging to obtain.

- Store and Clean the Data
Organize your dataset in a structured format such as CSV, JSON, or a database, and make sure to remove inconsistencies, handle missing values, and format date columns properly to ensure accurate analysis. I found it useful in this analysis to store each game as a seperate dataframe and merge them back together (it helped retain proper months and dates when they weren't in proper format)

- Analyze Trends
Once the data is cleaned, focus on key metrics such as average player counts, monthly growth rates, and long-term trends. Comparing different time periods, such as pre- and post-pandemic trends, can provide deeper insights into player retention and industry shifts.

-As far as web scraping, the data was collected from steamCharts. The data is cleanly organized into charts that can relatively easily be turned into a pandas dataframe. However, since player counts are by game by month, it required eliminating the first and final rows of the column in order to calculate the growth metric. Since to do so I took the change from the previous month to the current month. Overall the data is easy to work with and I recommend using the beautiful soup package when scraping the data.


## Exploratory Data Analysis (EDA) Highlights
### Summary of the Dataset
- **Total Sample Size**: 777 rows
- **Features**:
  - **Game Titles**: Counter-Strike, Dota 2, PUBG, Apex Legends, Rust, Terraria 
  - **Month**: As early as October 1st 2012 - January 1st 2025
  - **Average Player Count**: Mean number of players during that month
  - **Monthly Growth Rate**: Percentage change in player count compared to the previous month
  - **Total Player Count**: Sum of all average player counts for trend observation
  - **Game Type**: Multiplayer or Non-Multiplayer

## Key Findings
First let's look at player counts over time:
![Player Count](https://schneeman71.github.io/Klein-Blog/assets/images/player_count.png)

You can see a clear bump when the pandemic started (noted by the red line), although it's not directly clear whether it had a lasting impact or not. They do seem to become more popular over time, but nothing quite compares with the initial spike soon after a game comes out.

Next let's look at growth rates over time for multiplayer vs non-multiplayer games:
![Growth Comparison 2018-2022](https://schneeman71.github.io/Klein-Blog/assets/images/growth_comparison.png)
From this graph, it fluctuates drastically and seemingly centered around 0 and potentially. Soon after the largest spike as the pandemic hits, the growth rate plumets to nearly -50%.

Now let's look at growth rate over the 4 years before the pandemic and 4 years after:
![Growth Rate_Comparison 2016-2020](https://schneeman71.github.io/Klein-Blog/assets/images/growth_rate_comparison1.png)

![Growth Rate_Comparison 2020-2024](https://schneeman71.github.io/Klein-Blog/assets/images/growth_rate_comparison2.png)
Based upon our graphs, it seems only Counter-strike 2 and Dota 2 saw more increase in growth rate over the 4 years after covid than the 4 years before.

# Conclusion
Based upon our results, I found my analysis was majorly inconclusive. While it's clear that there was a large spike due to the pandemic, it isn't clear the impact it had on the gaming industry afterward. If I were to do the study again, I would consider a more comprehensive list of games, or potentially look at overall player count including Xbox, Playstation, and Switch numbers rather than exclusively PC games.

For students and analysts interested in replicating or extending this research, the dataset and methods outlined here provide a strong foundation for further exploration. Happy analyzing!

## Where to Learn More
If you want to dig deeper into this project or replicate it, check out these resources:
- <a href="https://steamcharts.com/" target="_blank" rel="noopener noreferrer">SteamCharts</a>

### GitHub Repository
For access to the full dataset, data collection scripts, and analysis code, visit:
- <a href="https://github.com/Schneeman71/kleinstat386post2/" target="_blank" rel="noopener noreferrer">Work Repository</a>


