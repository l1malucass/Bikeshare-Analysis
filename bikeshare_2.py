import time
import pandas as pd
import numpy as np
from numpy import mean
import statistics

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
CITIES = list(CITY_DATA.keys())

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('US Bikeshare Data')
    time.sleep(2)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Cities available for exploration: Chicago, New York City and Washington. Please choose one: ").lower()
        if city not in CITIES:
            print("That's not a valid city. Please try again.")
            time.sleep(1)
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        time.sleep(1)
        month = input(f"Which month would you like to see data from {city}? January to June. Or would you like to see all? ").lower()
        if month not in MONTHS:
            print("That's not a valid month. Please try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        time.sleep(1)
        day = input(f"And which day would you like to see data from {city} in {month}? From MONDAY to SUNDAY or all ").lower()
        if day not in DAYS:
            print("That's not a valid day. Please try again.")
            continue
        else:
            break

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
    #Loads datafile into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #This converts Start Time column to DateTime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    #Extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    #It filters by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTHS.index(month) + 1
    
        # Filter by month to create the new DataFrame
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new DataFrame
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    if most_common_month == 1:
        most_common_month = "January"
    elif most_common_month == 2:
        most_common_month = "February"
    elif most_common_month == 3:
        most_common_month = "March"
    elif most_common_month == 4:
        most_common_month = "April"
    elif most_common_month == 5:
        most_common_month = "May"
    elif most_common_month == 6:
        most_common_month = "June"
    else:
        pass
    print("The most common month is:", most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]

    print("The most common day is:", most_common_day)

    # TO DO: display the most common start hour
    # Convert Start Time column to Date Time
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # Finnd the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    
    print("The most frequent start hour is:", popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_station = df['Start Station'].mode()[0]
    
    print("The most commonly used Start Station is:", most_used_station)

    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    
    print("The most commonly used End Station is:", most_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination = df["Start Station"].mode()[0] + " | " + df["End Station"].mode()[0]
    
    print("The most frequent combination of Start Station and End Station is:", combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    
    df["hour"] = df["Start Time"].dt.hour
    df["hour"] = df["End Time"].dt.hour
    
    total_time = df["hour"].count()
    
    print("The total travel time is:", total_time, "hours")

    # TO DO: display mean travel time
    avg = df["hour"].mean()
    
    print("The mean travel time is:", int(avg))
    #avg = mean(total_time)
    
    #print("The mean travel time is:", round(avg, 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    
    print(user_types)
    # TO DO: Display counts of gender
    try:
        gender = df["Gender"].value_counts()
        print("\nGender:\n", gender)
    except:
        print("\nNo Gender found in this file.")    
    # TO DO: Display earliest, most recent, and most common year of birth
    #Earliest
    try:
        earliest = int(df["Birth Year"].min())
        print("\nThis is the earliest year of birth:", earliest)
    except:
        print("No Earliest year of birth year found in this file.")
    
    #Most recent
    try:
        most_recent = int(df["Birth Year"].max())
        print("This is the most recent year of birth:", most_recent)
    except:
        print("No most recent year of birth year found in this file.")

    
    #Most common
    try:
        most_common_year = int(df["Birth Year"].mode())
        print("This is the most common year of birth:", most_common_year)
    except:
        print("No most common year of birth year found in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    ''' This function asks the user if he wants to raw data. The first 5 rows and so on...'''
    input_data = input("Would you like to see raw data? The first 5 rows. Enter yes or no: ")
    Question = True
    i = 0
    while (Question):
        if input_data != "yes":
            break
        print(df.iloc[i:i + 5])
        i += 5
        input_data = input("Do you wish to see next 5 rows? Enter yes or no: ")
        if input_data != "yes":
            break
        else:
            continue

    print('-'*40)
    time.sleep(1)        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        while True:
            restart = input('Would you like to restart? Enter yes or no: ')
            if restart.lower() == 'yes':
                break
            elif restart.lower() == "no":
                print("Closing US Bikeshare Data...")
                quit()
            else:
                print("That's not a valid answer. Try again.")
                continue


if __name__ == "__main__":
	main()
