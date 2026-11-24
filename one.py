fees = {"Everest":   {"Nepali": 100, "SAARC": 1500, "Foreign": 3000},
        "Annapurna": {"Nepali": 100, "SAARC": 1000, "Foreign": 3000},
        "Langtang":  {"Nepali": 100, "SAARC": 1500, "Foreign": 3000}}

visitors = [("Aarav", "Nepali", 22, "Everest"),
            ("Emma", "Foreign", 34, "Annapurna"),
            ("Rahul", "SAARC", 8, "Langtang"),
            ("John", "Foreign", 65, "Everest"),
            ("Mina", "Nepali", 30, "Annapurna"),
            ("Li", "Foreign", 28, "Everest")]

# Initializing variables
revenue = {"Everest": 0, "Annapurna": 0, "Langtang": 0}
count = {"Everest": 0, "Annapurna": 0, "Langtang": 0}
categories = set()
total = 0

# Processing visitor information
for name, category, age, area in visitors:

    fee = fees[area][category]

    if age < 10:
        fee = 0
    elif age >= 60:
        fee = fee // 2

    print(name, area, "Rs", fee)

    revenue[area] += fee
    count[area] += 1
    categories.add(category)
    total += fee

# Finding the busiest area
busiest = max(count, key=count.get)

# Displaying results
print("Revenue by area:", revenue)
print("Busiest area:", busiest, "(", count[busiest], "visitors)")
print("Visitor categories:", sorted(categories))
print("Total revenue: Rs", total)
