---
layout: post
title:  "Finding Treasure Among the Trash"
author: James Klein
description: A further analysis of the effects of the Covid-19 pandemic on the gaming industry, with interactive Streamlit tool
image: "/assets/images/game2.jpg"
---

# Finding Treasure Among the Trash

## Introduction: Why This Still Matters

In a continuation of the previous post, we aim to finalize our exploration of how the **Covid-19 pandemic** impacted the **gaming industry** in the long term.
Back in 2020, player counts on PC games spiked as millions were stuck at home. But years later, one question still lingers:

> **Did those new gamers stick around, or did they move on as the world reopened?**

In our previous post, we gathered data from [SteamCharts](https://steamcharts.com/) and did a basic exploratory analysis. Now, we’ll build on that with new insights and an **interactive Streamlit app** so *you* can explore the trends yourself.

## Player Counts Over Time

To refresh your memory, here’s a plot showing **average monthly player counts** for six popular games from **2012 to early 2024**:

![Player Count](https://schneeman71.github.io/Klein-Blog/assets/images/player_count.png)

Across all games, we see a clear **pandemic-era spike** starting in early 2020. But, for most titles, that spike doesn’t last—player counts taper off and return to prior trends or even decline.

## Multiplayer vs Non-Multiplayer Growth

To dig deeper, we compared **growth rates between 2018–2023**, dividing games into **multiplayer** and **non-multiplayer**.

![Growth Comparison 2018-2022](https://schneeman71.github.io/Klein-Blog/assets/images/growth_comparison.png)

Interestingly, **non-multiplayer games** experienced a larger spike in growth just after the pandemic hit, but the boost was **short-lived**. A second spike around 2.5 years later seems unrelated to the pandemic—possibly tied to new game releases or updates.

## Main Takeaways

While our dataset is limited, a few patterns stand out:

- **The pandemic caused a clear short-term spike** in player activity across all games.
- **Multiplayer games (like Dota 2, CS2)** seem to retain players slightly better over time.
- However, the data is ultimately **inconclusive** about long-term pandemic impact, due to limited sample size and game diversity.

To help others explore these trends and maybe find insights we missed, we built an interactive Streamlit app.

## Explore the Data Yourself: Streamlit App

To make this analysis more interactive, we created a Streamlit app that lets you:

- **Select games** you want to analyze  
- **Filter by year range** using a slider  
- Switch between **Average Player Count** and **Growth Rate** views  
- **Download** filtered datasets for your own projects

> [Click here to open the Streamlit App](#)

This tool lets you create your own charts and ask your own questions:
- How does Apex Legends compare to PUBG over time?
- Did Rust grow faster post-pandemic than pre-pandemic?
- Do multiplayer games recover faster from dips in activity?

## Limitations & Future Work

As mentioned, this analysis is based on just **six games**, all from **Steam/PC**. The gaming industry is massive and fragmented—future work could include:

- Expanding the sample to 50+ games
- Including data from consoles (Xbox, PlayStation, Switch)
- Factoring in game releases and major updates

## Resources

- <a href="#" target="_blank" rel="noopener noreferrer"> Streamlit App </a>
- <a href="https://steamcharts.com/" target="_blank" rel="noopener noreferrer"> SteamCharts </a>
- <a href="https://github.com/Schneeman71/kleinstat386post2/" target="_blank" rel="noopener noreferrer"> GitHub Repo </a>  
- <a href="https://schneeman71.github.io/Klein-Blog/" target="_blank" rel="noopener noreferrer"> Blog Posts</a>

Thanks for reading—and don’t forget to check out the app and dig into the data yourself!

