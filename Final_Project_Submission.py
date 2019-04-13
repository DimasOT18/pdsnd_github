import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ['chicago','new york','washington']
    options = ['month','day','not at all']

    class Illegal(Exception):
        pass

    month = 'all'
    day = 'all'

    while True:
        try:
            city = input('Would you like to see data for Chicago, New York, or Washington?: \n').lower().strip()
            if city not in cities:
                raise Illegal
            break
        except Illegal:
            print('The proper city was not chosen. Please choose from Chicago, New York, or Washington.')
        else:
            pass

    #option for month or day. if neither, pass

    while True:
        try:
            option = input('Would you like to filter the data by month, day, or not at all?: \n').lower().strip()
            if option not in options:
                raise Illegal
            break
        except Illegal:
            print('A proper selection was not made. Please select month, day, or not at all.')
        else:
            pass

    # TO DO: get user input for month (all, january, february, ... , june)

    while option == 'month':
        try:
            month = input('Which month - January, February, March, April, May, or June?: \n').lower().strip()
            if month not in ['january','february','march','april','may','june']:
                raise Illegal
            break
        except Illegal:
            print('A proper month was not selected. Please select January, February, March, April, May, or June.')
        else:
            pass

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while option == 'day':
        try:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?: \n').lower().strip()
            if day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                raise Illegal
            break
        except Illegal:
            print('A proper day was not selected. Please select Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.')
        else:
            pass

    print('-'*40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    # adding hour and trip columns for use in statistics
    # trip column is the concatination of each start and end station
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['Trip'] = df['Start Station']+' to '+df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].value_counts().idxmax()
    common_month_count = df['month'].value_counts().max()
    print('Popular times of travel: \nThe most common month is {}. The count is {}.'.format(common_month,common_month_count))

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].value_counts().idxmax()
    common_day_count = df['day_of_week'].value_counts().max()
    print('The most common day of the week is {}. The count is {}.'.format(common_day,common_day_count))

    # TO DO: display the most common start hour

    common_hour = df['hour'].value_counts().idxmax()
    common_hour_count = df['hour'].value_counts().max()
    print('The most common hour is {}. The count is {}.'.format(common_hour,common_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_st_st = df['Start Station'].value_counts().idxmax()
    common_st_st_count = df['Start Station'].value_counts().max()
    print('Popular Stations and Trip: \nThe most popular start station is {}. The count is {}.'.format(common_st_st,common_st_st_count))

    # TO DO: display most commonly used end station

    common_end_st = df['End Station'].value_counts().idxmax()
    common_end_st_count = df['End Station'].value_counts().max()
    print('The most popular end station is {}. The count is {}.'.format(common_end_st,common_end_st_count))

    # TO DO: display most frequent combination of start station and end station trip

    common_trip = df['Trip'].value_counts().idxmax()
    common_trip_count = df['Trip'].value_counts().max()
    print('The most common trip was from {}. The total count is {}.'.format(common_trip,common_trip_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time

    avg_travel_time = df['Trip Duration'].mean()
    print('Trip Duration: \nThe total travel time is {}. \nThe average travel time is {}.'.format(total_travel_time,round(avg_travel_time,2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_series = df['User Type'].value_counts()

    print('User Info:')

    user_num = 0

    for i, v in user_series.items():
        user_num +=1
        print('The count for user type number {} is: '.format(user_num))
        print(i,':', v)

    # TO DO: Display counts of gender
    # adding if loop to check if Gender data is available for analysis

    if df.columns.isin(['Gender']).any():
        gender_series = df['Gender'].value_counts()

        print('The gender counts are:')
        for i, v in gender_series.items():
            print(i,':', v)
    else:
        print('There is no gender data in the Washington dataset.')

    # TO DO: Display earliest, most recent, and most common year of birth

    if df.columns.isin(['Birth Year']).any():

        year_series = df['Birth Year'].value_counts()
        old_year = df['Birth Year'].min()
        new_year = df['Birth Year'].max()
        common_year = df['Birth Year'].value_counts().idxmax()
        print('The most common year of birth is {}.'.format(int(common_year)))
        print('The earliest year of birth is {}. The most recent year of birth is {}.'.format(int(old_year),int(new_year)))
    else:
        print('There is no birth year data in the Washington dataset.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        iterable = 0

        while input('Would you like to see the raw data? Choose yes or no. ').lower().strip() == 'yes':
            print('Here are 5 rows of raw data: \n')
            for i in df.to_dict(orient='records')[iterable:(iterable+5)]:
                print(i)
            iterable += 5
        else:
            pass

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
