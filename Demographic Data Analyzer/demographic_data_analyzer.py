import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many people of each race are represented in this dataset?
    race_count = df["race"].value_counts()


    # Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(),
        1
    )


    # Percentage of people who have a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100,
        1
    )


    # Percentage of people with advanced education (Bachelors, Masters, Doctorate)
    # who earn more than 50K

    higher_education = df[
        df["education"].isin(
            ["Bachelors", "Masters", "Doctorate"]
        )
    ]

    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100,
        1
    )


    # Percentage of people without advanced education
    # who earn more than 50K

    lower_education = df[
        ~df["education"].isin(
            ["Bachelors", "Masters", "Doctorate"]
        )
    ]

    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100,
        1
    )


    # Minimum number of hours a person works per week

    min_work_hours = df["hours-per-week"].min()


    # Percentage of people who work minimum hours
    # and earn more than 50K

    min_hours_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    rich_percentage = round(
        (min_hours_workers["salary"] == ">50K").mean() * 100,
        1
    )


    # Country with highest percentage of people earning >50K

    country_percentage = (
        df[df["salary"] == ">50K"]["native-country"]
        .value_counts()
        /
        df["native-country"].value_counts()
        * 100
    )

    highest_earning_country = country_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_percentage.max(),
        1
    )


    # Most popular occupation for people earning >50K in India

    india_high_salary = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = (
        india_high_salary["occupation"]
        .value_counts()
        .idxmax()
    )


    if print_data:

        print("Number of each race:")
        print(race_count)

        print("\nAverage age of men:")
        print(average_age_men)

        print("\nPercentage with Bachelors degrees:")
        print(percentage_bachelors)

        print(
            "\nPercentage with higher education that earn >50K:"
        )
        print(higher_education_rich)

        print(
            "\nPercentage without higher education that earn >50K:"
        )
        print(lower_education_rich)

        print("\nMinimum work hours:")
        print(min_work_hours)

        print(
            "\nPercentage of rich among minimum hours workers:"
        )
        print(rich_percentage)

        print(
            "\nCountry with highest percentage of rich:"
        )
        print(highest_earning_country)

        print(
            "\nHighest percentage of rich people in country:"
        )
        print(highest_earning_country_percentage)

        print(
            "\nTop occupation in India for >50K:"
        )
        print(top_IN_occupation)


    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }