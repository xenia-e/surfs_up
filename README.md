# surfs_up
# Overview of the analysis 
Analysis of temperature data for June and December in Oahu, to determine if the surf and ice cream shop business is sustainable year-round.

### Resources
Data source: [hawaii.sqlite](https://github.com/xenia-e/surfs_up/blob/main/hawaii.sqlite) SQLite database file with weather data for the target island


### Methods
We performed the analysis of data in SQLite database format using SQLAlchemy

## Deliverables

- __Deliverable 1:__ 

![Summary Statistics for June](https://github.com/xenia-e/surfs_up/blob/main/analysis/june_statistic.png)

>Deliverable 1 - Summary Statistics for June

- __Deliverable 2:__ 

![Summary Statistics for December](https://github.com/xenia-e/surfs_up/blob/main/analysis/december_statistics.png)

>Deliverable 1 - Summary Statistics for December

- __Deliverable 3:__ A written report for the statistical analysis [(README.md)](https://github.com/xenia-e/surfs_up/blob/main/README.md)


All corresponded code presented in the Jupiter Notebook file [SurfsUp Challenge](https://github.com/xenia-e/surfs_up/blob/main/SurfsUp_Challenge.ipynb)


# Results

Comparative analysis of June vs December temperatures allow us to point out key differences in weather between June and December

1. Minimum temperature in December is about 14% lower than the minimum temperature in June (with 56℉ and 64℉ respectively)
2. Maximum temperature is about 3% lower in December than in June (83℉ and 85℉ respectively)
3. Average temperature is about 4% lower in December than in June with 71℉ and 75℉ respectively


# Summary

Even though December is colder than June, average monthly temperatures do not differ that much. And December traditionally counted as the high tourist season due to the Christmas holidays. These facts allow us to assume that temperature would not be the factor affecting business sustainability. Nevertheless, we cant make a final decision based only on it.

In addition to this, we advise analyzing precipitation data in June and December and March and September temperatures statistic.

Comparing precipitation statistic for December and June allow us to assume that business sustainability will not be affected by extensive rains either. Anyway, analysis shows that June has more rainy days than December, but at the same time, the average precipitation level is lower in June.

![June presipitation statistic](https://github.com/xenia-e/surfs_up/blob/main/analysis/june_prcp.png)

> Figure 1 - June precipitation statistic


![December presipitation statistic](https://github.com/xenia-e/surfs_up/blob/main/analysis/december_prsp.png)

> Figure 2 - December precipitation statistic



Looking at the summarized analysis of March temperatures, we can say that the average monthly temperature in March is even lower than in December. And unlike December, March has no major holidays in it and does not add to tourist flow. So March might be the month that will affect the net gross in the store.

![March temperature statistic](https://github.com/xenia-e/surfs_up/blob/main/analysis/march_statistic.png)

> Figure 3 - March temperature statistic

![September temperature statistic](https://github.com/xenia-e/surfs_up/blob/main/analysis/september_statistic.png)

> Figure 4 - September temperature statistic

September statistic doesn't seem to give us any new insights. 

Sadly that is all we can do withing provided data. Otherwise, I would suggest analyzing monthly offshore winds and storms. 

