def sum_numbers_list ( number_list : list ):
    sum = 0
    for num in number_list:
        sum += num
    
    return float(sum)

def median_numbers_list(number_list : list):
    number_list.sort()

    first_item_list = number_list[0]
    last_item_list = number_list[-1]

    length_list = len(number_list)
    length_is_even = length_list % 2 == 0 
    
    if length_is_even:
        index_num_less = len(number_list)/2 - 1
        num_less = number_list[int(index_num_less)]

        index_num_over = len(number_list)/2 
        num_over = number_list[int(index_num_over)]
        
        median = (num_over + num_less) / 2

        return float(median)
    
    index_median =  (first_item_list + last_item_list)/2 - 0.5
    median = number_list[int(index_median)]

    return float(median)

def mean_numbers_list(number_list : list):
    length_list = len(number_list)
    sum_numbers_list = sum_numbers_list( number_list )

    mean = sum_numbers_list / length_list

    return float(mean)

def module_subtraction_two_numbers(num1:float, num2:float):
    if num1 > num2:
        result = num1 - num2
        return result
    
    result = num2 - num1
    return result

def deviation(numbers_list : list):
    deviations = []
    mean = mean_numbers_list(numbers_list)

    for num in numbers_list:
        module_deviation = module_subtraction_two_numbers(num, mean)
        deviations.append(module_deviation)

    return deviations

def variance_numbers_list(numbers_list : list):
    deviations_list = deviation(numbers_list)
    squares_deviations = [deviation ** 2 for deviation in deviations_list]
    variance = mean_numbers_list(squares_deviations)

    return variance

def default_deviation(number_list : list):
    variance = variance_numbers_list(number_list)
    default_deviation = variance ** (1/2)

    return float(default_deviation)
