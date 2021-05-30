from utils import find_max

def lbs_to_kg(weight):
    return weight*0.45


def kg_to_lbs(weight):
    return weight/0.45


# maximum number in list

numbers = [10, 3, 9, 13]
maximum = find_max(numbers)
print(maximum)



