## Title: Condominium Investment - Return on Investment (ROI) Calculator
## Developer: Blake Swenson
## Date: 3/23/2021
## Purpose: This application calculates ROI on a condominium purchase over the life of the investment.

def calculate_total_investment(purchase_price, annual_property_taxes, monthly_condo_fees, number_of_years):
    return (purchase_price + (annual_property_taxes * number_of_years) + (monthly_condo_fees * 12 * number_of_years))
    ## The investment cost adds condominium purchase price, total annual taxes over the life of the investment and the total monthly fees paid over the life of the investment.

def calculate_sale_price(purchase_price, appreciation_rate, number_of_years):
    sale_price = purchase_price
    for year in range(number_of_years):
        sale_price = sale_price * (1 + (appreciation_rate / 100))
    return sale_price
    ## Expected sale price is calculated by a function appreciating each year over the life of the investment the purchase price at the % rate provided using a loop.

def calculate_roi(total_investment, sale_price, purchase_price):
    investment_profit = sale_price - total_investment
    ## Investment profit is calculated as expected sale price – total investment cost. 
    return_on_investment = (investment_profit / purchase_price) * 100
    return return_on_investment
    ## ROI is calculated as Investment profit/Purchase price * 100 


def condo_investment_calculator():
    print('CONDOMINIUM INVESTMENT ROI CALCULATOR')

    purchase_price = int(input('Condo Purchase Price ($):'))
    while purchase_price <= 0:
        print('Invalid input')
        purchase_price = int(input('Condo Purchase Price ($):'))
    ## User input for purchase price, must be greater than zero
    
    annual_property_taxes = int(input('Annual Property Taxes ($):'))
    while annual_property_taxes <= 0:
        print('Invalid input')
        annual_property_taxes = int(input('Annual Property Taxes ($):'))
    ## User input for property taxes, must be greater than zero

    monthly_condo_fees = int(input('Monthly Condo Fees ($): '))
    while monthly_condo_fees <= 0:
        print('Invalid input')
        monthly_condo_fees = int(input('Monthly Condo Fees ($): '))
    ## User input for monthly condo fees, must be greater than zero

    number_of_years = int(input('Number of Years to Hold Investment (1-10):'))
    while number_of_years < 1 or number_of_years > 10:
        print('Invalid input')
        number_of_years = int(input('Number of Years to Hold Investment (1-10):'))
    ## User input for number of years, must be between 1-10

    appreciation_rate = int(input('Expected Annual Investment Appreciation Rate (%):'))
    while appreciation_rate <= 0:
        print('Invalid input')
        appreciation_rate = int(input('Expected Annual Investment Appreciation Rate (%):'))
    ## User input for appreciation rate, must be greater than zero

    total_investment = calculate_total_investment(purchase_price, annual_property_taxes, monthly_condo_fees, number_of_years)
    ## Call a function to calculate the total investment
    #print("Total Investment ($):", total_investment)

    sale_price = calculate_sale_price(purchase_price, appreciation_rate, number_of_years)
    ## Call a function to calculate the total sale price
    #print(f'Expected Sale Price: {sale_price:.0f}%')

    return_on_investment = calculate_roi(total_investment, sale_price, purchase_price)
    print(f'Expected ROI: {return_on_investment:.1f}%')
    ## Call a function to calculate the ROI and display it to the user
    ## ROI should be displayed with one significant digit 

#The application is executed by calling the calculate_condo_roi() function
if __name__ == '__main__':
    condo_investment_calculator()
    ## Call the function that contains code for the program