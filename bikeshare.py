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
    
    # Ask user for city, if not in city list, ask again
    
    city = str(input("Input the city you would like to explore (Chicago, New York City, or Washington) :)"))
    city = city.lower()
    city_options = ['chicago', 'new york city', 'washington']
    city_index = 0 
    while city_index < 1:
        if city not in city_options:
            city = str(input("Please enter a city in the database (Chicago, New York City, or Washington: "))
        else:
            city_index = city_index + 1
    

    # Ask user for month
    month = str(input("Input the month you would like to learn about (january, february, march, april, may, june, or all) :)"))
    month_options = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    not_months = ['july', 'august', 'september', 'october', 'november', 'december'] 
    month = month.lower()
    month_index = 0
    
   #if a month unaviable data let user know, if not a month let user know
    while True:
        if month in not_months:
             month = str(input("Please try again. There is no available data for selected month (Available data: january, february, march, april, may, june) ) : "))
        if month not in month_options:
            month = str(input("Please try again: "))          
        

    # Ask user for day of week, if not in list, ask again
    day = str(input("Input the day of the week you would like to learn about :)"))
    day_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday', 'all']
    day = day.lower()
    while True:
        if day not in day_options:
            day = str(input("Please try again: "))
        else:
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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

   #Calaculate most common month, user dictionary to convert index to month name 
    com_month = df['month'].mode()[0]
    month_dict = {1: 'january', 2: 'feburary', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
    com_month = month_dict[com_month]


    # display the most common day of week
    com_day = df['day_of_week'].mode()[0]

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hour = df['hour'].mode()[0]
    com_hour = round(com_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(f"\nThe most common month, day of week and time are: {com_month}, {com_day}, {com_hour}")


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]


    # display most commonly used end station
    com_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip (concatenate)
    df['Combo'] = df['Start Station'] + ' to ' + df['End Station']
    com_combo = df['Combo'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(f"\nThe most common Start Station: {com_start_station}\nEnd Station: {com_end_station}\nCombo of start and end: {com_combo}")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_duration = round(df['Trip Duration'].sum())
   

    # display mean travel time
    mean_duration = round(df["Trip Duration"].mean())
  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(f"\nThe total time spent traveling was {total_duration} seconds and the average traveling time was {mean_duration} seconds")

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        sub = df[df['User Type'] == "Subscriber"]
        sub_index = sub.index
        sub_ct = len(sub_index)
    except KeyError:
        sub_ct = 'No Data Available'
    #Find subscriber count 
    
    
    #Find customer count
    try:
        cust = df[df['User Type'] == "Customer"]
        cust_index = cust.index
        cust_ct = len(cust_index)
    # Add error code
    except KeyError:
        cust_ct = 'No Data Available'
    
    #Find Male count 
    try:
        male =  sub = df[df['Gender'] == "Male"]
        m_index = male.index
        m_ct = len(m_index)
    except KeyError:
        m_ct = 'No Data Available'
    
    
    #Find female count 
    try:
        female =  sub = df[df['Gender'] == "Female"]
        f_index = female.index
        f_ct = len(f_index)
    except KeyError:
        f_ct = 'No Data Available'

   
    
            
    # Find earliest, most recent, and most common year of birth
    try:
        oldest = round(df['Birth Year'].min())
        youngest = round(df['Birth Year'].max())
        com_age =  round(df['Birth Year'].mode()[0],0)
        
    except KeyError:
        oldest = 'No Data Available'
        youngest = 'No Data Available'
        com_age = 'No Data Available'

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(f"\n Subscriber Count: {sub_ct}, Customer Count: {cust_ct}, Female Count: {f_ct}, Male Count: {m_ct}, Earliest Birth Year: {oldest}, Most Recent Birth Year: {youngest}, Most Common Birth Year: {com_age}")

def display_raw_data(df):
    # Ask user if they would like to see raw data
    i = 0
    raw = input("Would you like to see the raw data?").lower() 
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no' or raw =='n':
            break
        elif raw == 'yes' or raw =='y':
            print(df.iloc[i:i+5]) 
            raw = input("Would you like to see more: ").lower() 
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


#Runs all the definitions 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



