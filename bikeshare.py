import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_data(input_str,input_type):
   
    while True:
        input_read=input(input_str).lower()
        try:
            if input_read in ['chicago','new york city','washington'] and input_type == "city":
                break
            elif input_read in ['january', 'february', 'march', 'april', 'may', 'june','all'] and input_type == "month":
                break
            elif input_read in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'] and input_type == "day":
                break
            else:
                if input_type == "city":
                    print("Sorry, your input should be: chicago new york city or washington")
                if input_type == "month":
                    print("Sorry, your input should be a month")
                if input_type == "day":
                    print("Sorry, your input should be a day")
        except ValueError:
            print("Sorry wrong input")
    return input_read
def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
      # ask for city month date
    
    cities = ['chicago', 'new york city', 'washington']
    city = check_data("which city : ","city")
    #input('enter ur city : \n').lower()
    while True:
        if city in cities:
                    break
        else :   
          print("sorry wrong input")
          break
    
    
    months = ['january', 'febuaray', 'march', 'april', 'june']
    month = check_data("which month : ","month")
    #input("which month \n").lower()
    while True:
        if month in months:
                    break
        else : print("Sorry, your input is wrong")  
        break
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = check_data("which day :" ,"day" )
    #input("which day \n").lower()
    while True:
        if day in days:
                    break
        else  : print("Sorry, your input is wrong") 
        break
        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
 # load data
    df = pd.read_csv(CITY_DATA[city]) 
    df ['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df ['month'] = pd.to_datetime(df['Start Time']).dt.month
    df ['day_of_week'] = pd.to_datetime(df['Start Time']).dt.weekday_name
    df ['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

   
    commen_month = df['month'].mode()[0]

    print('Most Popular Month:', commen_month)

    # display the most common day of week
    commen_day = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', commen_day)

    # display the most common start hour
    commen_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', commen_hour)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    commen_start_station = df['Start Station'].mode()[0]
    
    print("commen start station \n" , commen_start_station)
    


    #  display most commonly used end station
    commen_end_station = df['End Station'].mode()[0]
    
    print("commen end station \n" , commen_end_station)


    #  display most frequent combination of start station and end station trip
    #combine_station = df.groupby('Start Station','End Station' )
    group_field=df.groupby(['Start Station','End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)

   
   # print("combine station \n" , combine_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    total_time = df['Trip Duration'].sum()
   
    print("total time \n", total_time,)                           
                                  
                                  
                    


    #  display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("mean time \n", mean_time/3600 ,"hours")     


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if 'city' != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)
    print("\nThis took %s seconds." % (time.time() - start_time))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
