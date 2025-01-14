import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa_sea_level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    res_new = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_pred_new = pd.Series([i for i in range(2000, 2051)])
    y_pred_new = res_new.intercept + res_new.slope * x_pred_new
    plt.plot(x_pred_new, y_pred_new, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
