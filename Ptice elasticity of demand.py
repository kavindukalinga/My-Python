
def price_elasticity_of_demand(first_price,final_price,first_demand,final_demand):
    
    ''' This function returns the price elasticity of demand (PED) when first and final prices
    and demands are inputted'''

    global percentage_change_in_quantity_demand, percentage_change_in_price

    percentage_change_in_quantity_demand = (final_demand - first_demand)/ first_demand *100
    percentage_change_in_price = (final_price - first_price)/ first_price *100

    PED = -1 * percentage_change_in_quantity_demand / percentage_change_in_price # Econ Formula

    return PED


if __name__ == '__main__':  # Main programme
    print('Finding the price elasticity of demand\n')      # Headline
    
    first_price = float(input('Enter first price: '))      # Input first price
    first_demand = float(input('Enter first demand: '))    # Input first quantity demand

    final_price = float(input('Enter final price: '))      # Input final price
    final_demand = float(input('Enter final demand: '))    # Input final quantity demand

    PED = price_elasticity_of_demand(first_price,final_price,first_demand,final_demand) # Calling PED function

    print('\n\nPercentage change in quantity demand is {0} % '.format(round(percentage_change_in_quantity_demand,2)))
    print('Percentage change in price is {0} % '.format(round(percentage_change_in_price,2)))

    input() # Press Enter to continue

    print('\nPrice elasticity of demand is %.2f' %(PED))  # Output the Answer

    input() # Press Enter to End
