def find_cheapest_operator(number, price_lists):

    cheapest_operator = None
    cheapest_price = float('inf')
    
    # Iterate through each operator price list
    
    for operator, prices in price_lists.items():
        
        # Iterate through each prefix in the prefix-price list to determine the longest prefix for each operator
        
        for prefix in sorted(prices, key=lambda x: len(x), reverse=True):
                              
            if number.startswith(prefix):
                price = prices[prefix]
                
                #Unit testing 1 to validate the code correctness about prefix selection
                print('The selected prefix for ',operator,' is', prefix)
                
                #Unit testing 2 to validate the code correctness about price selection
                print('Cheaspest price with ',operator, 'is', price)
                
                #Check if the current operator has a cheaper price than the previous
                
                if price < cheapest_price:
                    cheapest_operator = operator
                    cheapest_price = price
                break
            
    return cheapest_operator, cheapest_price

#usage:
price_lists = {
    'Operator A': {
        '1': 0.9,
        '268': 5.1,
        '46': 0.17,
        '4620': 0.0,
        '468': 0.15,
        '4631': 0.15,
        '4673': 0.9,
        '46732': 1.1
    },
    'Operator B': {
        '1': 0.92,
        '44': 0.5,
        '46': 0.2,
        '467': 1.0,
        '48': 1.2
    },
    'Operator C': {
        '1': 0.35,
        '44': 0.1,
        '46': 0.0,
        '467': 0.8,
        '48': 1.0,
        '34': 10.0
    }
}

number = input("Enter a phone number please: ")

cheapest_operator, cheapest_price = find_cheapest_operator(number, price_lists)

if cheapest_operator == None:
    
    #Unit testing 3 to validate the correctness of the inserted phone number
    print('There is not any operator to carry calls for the supplied number')
else:
    print(f'The cheapest operator for number {number} is {cheapest_operator} with a price of {cheapest_price} per minute.')