def tax_info(selection):
    amount = n
    tax = amount * 0.25
    total_amount = amount * 1.25
    switcher = {
        "1": f"{amount}",
        "2": f"{tax}",  
        "3": f"{total_amount}"
    }
    '''The first argument will be returned if the match found and
        nothing will be returned if no match found'''
    return switcher.get(selection, f"That tax option {selection} does not exist")

n = float(input("Provide amount: "))
print("Selection are:\n1. Amount.\n2. Tax\n3. Total.\n")
selection = input("Enter input number: ")
# Print the output
print(tax_info(selection))