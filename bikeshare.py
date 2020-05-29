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
    city=input('Please enter city name, Chicago, New York City or Washington ').lower()
    while city not in CITY_DATA:
        print('Please enter valid city')
        city=input('Please enter city name, Chicago, New York City or Washington ').lower()    
    month=input('if you want to filter by month, please enter the valid maonth between janruary and june, otherwise type "all" ').lower()
    while month not in ('january', 'february','march','aprtil', 'may', 'june', 'all'):
        print ('please enter valid month or choose option "all"')
        month=input('if you want to filter by month, please enter the valid maonth between janruary and june, otherwise type "all" ').lower()       
        


    # TO DO: get user input for month (all, january, february, ... , june)

    day=input('if you want to filter by day, plase enter day of the week starting with capital letter, otherwise print"all" ').lower()
    while day not in('all', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
               print ('please enter valid input')
               day=input(' if you want to filter by day, plase enter day of the week starting with capital letter, otherwise print"all" ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
    df=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    print('The most common month:', df['month'].mode()[0])
               

    # TO DO: display the most common day of week
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['day']=df['Start Time'].dt.weekday_name
    print('The most common day:', df['day'].mode()[0])

    # TO DO: display the most common start hour
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    print('The most common hour:', df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
 
    print('The most common start station:', df['Start Station'].mode()[0])
    
    # TO DO: display most commonly used end station
  
    print('The most common end station:', df['End Station'].mode()[0])
   
    
    # TO DO: display most frequent combination of start station and end station trip
    x=pd.concat([df['Start Station'],df['End Station']])
    print('The most common station among start and end stations:', x.mode()[0])
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time:\n', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The average travel time:\n', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('value counts for each user type:\n', user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        
        gender_counts=df['Gender'].value_counts()
        print('count of each gender:\n', gender_counts)
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        most_common_year_of_birth=df['Birth Year'].mode()[0]
        print('The oldest person was born in:', df['Birth Year'].min())
        print('The youngest person was born in:', df['Birth Year'].max())
        print('The most common year of birth:', most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    while True:
        question=input('Do you want to see raw data?')
        while question.lower()not in ('yes', 'no'):
            print('please type "yes" or "no"')
            question=input('Do you want to see raw data?')
        if question=='yes':
            print(df.head())
        elif question=='no':
            break
    

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
