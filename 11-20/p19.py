from datetime import date
import pandas as pd



def mondays_between_years(year_1, year_2):
    start_date = date(year_1, 1, 1)
    end_date = date(year_2, 12, 31)
    dates = pd.date_range(start_date, end_date, freq = 'MS').strftime('%A')
    dates = pd.Series(dates)
    return dates.value_counts()

if __name__ == "__main__":
    year_1 = int(input("starting year = "))
    year_2 = int(input("ending year = "))
    print(mondays_between_years(year_1, year_2))
