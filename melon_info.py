"""Print out all the melons in our inventory."""


from melons import melons_dict


def print_melon(dictionary):
    """Print each melon with corresponding attribute information."""

    for melon in melons_dict:
        print(melon[0])
        print(f"seedless: {melon[2]}")
        print(f"price: {melon[1]}")
        print(f"flesh_color: {melon[3]}")
        print(f"weight: {melon[4]}")
        print(f"rind_color: {melon[5]}")
        print("---------------------------")
    
    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'

    # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')

print_melon(melons_dict)
# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
