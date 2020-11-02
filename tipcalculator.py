meal = 55.70
tax = 0.0675
tip = 0.20

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
