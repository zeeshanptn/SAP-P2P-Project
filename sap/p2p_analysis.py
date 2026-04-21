import csv

total_debit = 0
total_credit = 0
cost_center_spend = {}
monthly_spend = {}

with open('sample_data.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        month = row['Month']
        cc = row['Cost_Center']
        debit = float(row['Debit'])
        credit = float(row['Credit'])

        # total
        total_debit += debit
        total_credit += credit

        # cost center
        if cc not in cost_center_spend:
            cost_center_spend[cc] = 0
        cost_center_spend[cc] += debit - credit

        # monthly
        if month not in monthly_spend:
            monthly_spend[month] = 0
        monthly_spend[month] += debit - credit

# OUTPUT
print("------ SAP P2P ANALYSIS ------\n")

print("Total Debit:", total_debit)
print("Total Credit:", total_credit)

print("\nCost Center Spend:")
for cc, value in cost_center_spend.items():
    print(cc, ":", value)

print("\nMonthly Spend:")
for m, value in monthly_spend.items():
    print(m, ":", value)

# Highest cost center
max_cc = max(cost_center_spend, key=cost_center_spend.get)
print("\nHighest Spending Cost Center:", max_cc)