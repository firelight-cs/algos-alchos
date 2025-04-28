def amount_of_inputs():
    print("Enter the amount of input values: ")
    amount = int(input())
    return amount

def add_values_to_node(amount):
    print("Now add the value to each node")
    list_of_values = [0] * amount
    for value in range(amount):
        list_of_values[value] = int(input("Enter the value: "))
    return list_of_values

def add_weights(amount):
    print("Now add the weight to each edge")
    list_of_weights = [0] * amount
    for value in range(amount):
        list_of_weights[value] = int(input("Enter the weight: "))
    return list_of_weights

def combine(list_of_values, list_of_weights, b):
    # 1. value - input value x; 2. value - weight of edge; 3. value - bias
    table_of_inputs = dict()
    for i in range(len(list_of_values)):
        table_of_inputs[i] = (list_of_values[i], list_of_weights[i], b)
    print(f"The table of inputs look like this:\n{table_of_inputs}")
    return table_of_inputs

def perceptrone(wvb_dict):
    summ = 0
    for key in wvb_dict:
        summ += wvb_dict[key][0] * wvb_dict[key][1]
    summ += wvb_dict[0][2] # add a bias 
    if summ > 0:
        return 1
    return 0

def tests():
    inputs1 = {0: (0, -2, 3), 1: (0, -2, 3)}
    inputs2 = {0: (0, -2, 3), 1: (1, -2, 3)}
    inputs3 = {0: (1, -2, 3), 1: (0, -2, 3)}
    inputs4 = {0: (1, -2, 3), 1: (1, -2, 3)}
    output1 = perceptrone(inputs1)
    output2 = perceptrone(inputs2)
    output3 = perceptrone(inputs3)
    output4 = perceptrone(inputs4)
    print(f"The table of outputs:\n{output1}\n{output2}\n{output3}\n{output4}")

def main():
    bias = 3
    d_amount = amount_of_inputs()
    ad_values = add_values_to_node(d_amount)
    ad_weights = add_weights(d_amount)
    weight_value_bias = combine(ad_values, ad_weights, bias)
    output = perceptrone(weight_value_bias)
    print(f"The output value of perceptrone is: {output}")
    

if __name__ == "__main__":
    tests()
