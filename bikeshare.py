import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    city = input(' Please specify a city ( chicago, new york city, washington )\n').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print('Invalid Input, Please Try Agian')
        city = input(' Please specify a city (chicago, new york city, washington)\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter the name of the month to filter by (january, february, ... , june) , or "all" to apply no month filter\n').lower()
    while month not in ['january', 'february', 'march', 'april','may','june', 'all']:
        print('Invalid Input, Please Try Agian')
        month = input('Please enter the name of the month to filter by (january, february, ... , june) , or "all" to apply no month filter\n').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the name of the day to filter by ( monday, tuesday, ... sunday) , or "all" to apply no day filter\n').lower()
    while day not in ['monday', 'tuesday', 'wedensday', 'thursday','friday','saturday', 'sunday','all']:
        print('Invalid Input, Please Try Agian')
        day = input('Please enter the name of the month to filter by (january, february, ... , june) , or "all" to apply no month filter\n').lower()

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        global months
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most commn month is: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The most commn day is: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The most commn Start Time is: ', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The Most Popular Start Stations is:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The Most Popular End Stations is:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The Most frequent combination of start station and end station trip is: \n' , (df['Start Station'] + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total trip duration is:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The Mean of travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The User Types counts: \n' , df['User Type'].value_counts())
    if city != 'washington':
        # TO DO: Display counts of gender
        print('The Gender counts: \n' , df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest , most recent year is: ' , df['Birth Year'].max())
        print('\n The most Common Year of birth is: ' , df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
	display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
