def get_tax(income):
    tax = 0
    if income > 10000:
        tax += 0
        income -= 10000
    else:
        return tax
    if income > 15000:
        tax += 15000 * 0.10
        income -= 15000
    else:
        tax += income * 0.10
        return tax
    tax +=income * 0.23
    return tax
get_tax(58500)
print(get_tax(58500))
