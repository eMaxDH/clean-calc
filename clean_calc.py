
WAGE = 25 # [€/hour]

# function which calculates the number of hours a person can work with a given amount of money and hourly wage
def calculate_hours(money, wage):
    return money / wage

def calucte_money(number_of_payer, amount_per_payer):
    return number_of_payer * amount_per_payer

def calculate_number_of_visits(hours, min_visit_time):
    return hours / min_visit_time

def get_number_of_weeks_per_month_average():
    return 4.345

def get_cleaning_period(no_visits, no_weeks):
    return no_weeks / no_visits

def main():
    number_of_payer = 6
    amount_per_payer = 20
    money = calucte_money(number_of_payer, amount_per_payer)

    # calculate the number of hours a person can work with a given amount of money and hourly wage
    hours = calculate_hours(money, WAGE)
    print(f"Number of hours a person can work with {money} €: {hours}")
    
    no_visits = calculate_number_of_visits(hours, 4)
    print(f"Number of visits: {no_visits}")
    
    no_weeks = get_number_of_weeks_per_month_average()
    periode = get_cleaning_period(no_visits, no_weeks)
    print(f"Periode: {periode}")

if __name__ == "__main__":
    main()
