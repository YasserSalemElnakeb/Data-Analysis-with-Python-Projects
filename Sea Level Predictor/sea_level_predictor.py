import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Import data
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))


    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )


    # First line of best fit (1880 - 2014)

    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )


    years = range(
        1880,
        2051
    )


    predicted_sea_level = [
        slope * year + intercept
        for year in years
    ]


    ax.plot(
        years,
        predicted_sea_level
    )


    # Second line of best fit (2000 - 2014)

    recent_df = df[
        df["Year"] >= 2000
    ]


    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        recent_df["Year"],
        recent_df["CSIRO Adjusted Sea Level"]
    )


    years2 = range(
        2000,
        2051
    )


    predicted_recent = [
        slope2 * year + intercept2
        for year in years2
    ]


    ax.plot(
        years2,
        predicted_recent
    )


    # Labels

    ax.set_title(
        "Rise in Sea Level"
    )

    ax.set_xlabel(
        "Year"
    )

    ax.set_ylabel(
        "Sea Level (inches)"
    )


    return ax