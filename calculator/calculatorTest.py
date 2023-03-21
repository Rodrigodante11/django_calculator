
def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:

    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    coverage = 0

    average = (consumption[0] + consumption[1] + consumption[3]) / 3

    if average < 10000:
        coverage = 0.9

        if tax_type == "Comercial":
            applied_discount = 0.18
        elif tax_type == "Comercial":
            applied_discount = 0.16
        elif tax_type == "Industrial":
            applied_discount = 0.12

    elif 10000 <= average <= 20000:
        coverage = 0.95

        if tax_type == "Comercial":
            applied_discount = 0.22
        elif tax_type == "Comercial":
            applied_discount = 0.18
        elif tax_type == "Industrial":
            applied_discount = 0.15


    elif average > 20000:
        coverage = 0.99

        if tax_type == "Comercial":
            applied_discount = 0.25
        elif tax_type == "Comercial":
            applied_discount = 0.22
        elif tax_type == "Industrial":
            applied_discount = 0.18


    return (
        round(annual_savings, 2),
        round(monthly_savings, 2),
        applied_discount,
        coverage,
    )
