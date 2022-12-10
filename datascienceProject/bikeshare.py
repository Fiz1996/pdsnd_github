import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TODO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:

            city = input("Enter a city:").lower()

            if city not in CITY_DATA.keys():
                raise ValueError

            # TODO: get user input for month (all, january, february, ... , june)
            month = input('Enter a month:').lower()
            # TODO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input("Enter a day of week: ")
            print('-' * 40)
            return city, month, day
        except ValueError:
            print('That\'s not a valid input!')


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data first
    df = pd.read_csv(CITY_DATA[city])

    # change to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # filter by months
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

        # filter by month
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TODO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start Month:', popular_month)

    # TODO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Frequent day of week:', popular_day_of_week)

    # TODO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TODO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common  start station: {}".format(popular_start_station))

    # TODO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most common  end station: {}".format(popular_end_station))
    # TODO: display most frequent combination of start station and end station trip
    start_station_count = df['Start Station'].value_counts().max()
    print("number of the most appeared start station : {}".format(start_station_count))
    end_station_count = df['End Station'].value_counts().max()
    print("number of the most appered end station: {} ".format(end_station_count))

    if start_station_count > end_station_count:
        print("the most popular station is : {}".format(popular_start_station))
    elif end_station_count > start_station_count:
        print("the most popular station is : {}".format(popular_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TODO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time is:{} ".format(total_travel_time))

    # TODO: display mean travel time
    mean_of_travel_time = df["Trip Duration"].mean()
    print("mean of trips are : {} ".format(mean_of_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print(df.shape)
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TODO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TODO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    if 'Birth Year' in df:
        # TODO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        print("earliest year of birth:  {}".format(earliest_year_of_birth))
        most_recent_year_of_birth = df['Birth Year'].max()
        print("most recent year of birth:  {}".format(most_recent_year_of_birth))
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print("most common year of birth:  {}".format(most_common_year_of_birth))
    else:
        print('Birth Year stat cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """ user's ability to check for rows upon request """
    print("\n printing row user input \n")
    start_time = time.time()
    view_data = input("\n Would you like to view 5 rows of individual trip data? Enter yes or no. \n")
    start_loc = 5
    while True:
        print(df.iloc[0:start_loc])
        inc = start_loc + 5
        if df.__len__() < inc:
            break
        user_data = input('\nDo you want to see the first 5 rows of data? Enter yes or no. \n')
        start_loc += 5
        if user_data.lower() != 'yes':
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
