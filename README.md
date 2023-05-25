# IPL-Data-Analysis

This project analyzes a dataset of IPL matches from 2008 - 2019 using Python and various libraries such as numpy, pandas, matplotlib, and seaborn. The code performs various data exploration, visualization, and statistical analysis tasks to gain insights into the matches.

## Dataset

The dataset used for this analysis is "matches.csv". It contains information about cricket matches, including details like match results, teams, players, venues, toss information, and more.

The dataset contains two files: deliveries.csv and matches.csv. The file used for this analysis is matches.csv.

Things analysed:

Here are the bulleted points for the analysis:

- Match won by the maximum margin of runs.
- Match won by maximum wickets.
- Match won by the minimum margin of runs.
- Match won by minimum wickets.
- Matches where D/L method was and wasn't applied.
- No. of matches held in each city.
- No. of matches won by each team.
- No. of matches held every season.
- Top 10 players based on the number of Man of Match (MOM) awards won.
- Does winning the toss mean winning the match?
- What was the decision taken by captains when they won the toss?
- No. of matches where D/L method was applied every season.
- Different results for matches.
- How many times did a team win the toss?
- Best venue for defending and chasing a total.
- Best defending and chasing teams.
- No. of matches played in different stadiums.

## Analysis Steps

The code performs the following analysis and visualizations:

1. Loading the dataset: The dataset is loaded using the pandas library and stored in a DataFrame.
2. Data Exploration: The code displays the shape of the dataset, the first few rows, and provides descriptive statistics and information about the dataset.
3. Season Analysis: Unique seasons present in the dataset are displayed.
4. Margin of Victory: The largest margin of victory by runs and by wickets are identified, along with the details of the matches.
5. D/L Method: The code analyzes matches where the Duckworth-Lewis (D/L) method was applied, providing counts and percentages.
6. City and Venue Analysis: The number of matches held in each city and the best venues for defending and chasing totals are visualized.
7. Team Analysis: The code analyzes the number of matches won by each team and the top players based on the number of Man of Match (MOM) awards.
8. Toss Analysis: The percentage of matches won by the toss-winning team, the decisions made by captains after winning the toss, and the number of tosses won by each team are analyzed.
9. Visualization: The code creates various plots to visualize the number of matches held in each season, matches played in different stadiums, and more.

## Results and Insights

The analysis provides valuable insights into cricket matches, including the performance of teams, players, venues, and the impact of toss decisions on match outcomes. The visualizations help in understanding the distribution of matches, the dominance of certain teams, and the popularity of stadiums.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or additional analyses to add, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The dataset used in this analysis is sourced from https://www.kaggle.com/nowke9/ipldata
- The code and analysis are inspired by various data analysis projects and resources available online.
