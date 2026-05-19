import statistics

def analyze_sales(analyst, region, sales): # sales is a list of daily sales amounts
    mean = statistics.mean(sales)
    median = statistics.median(sales)
    try:
        mode = statistics.mode(sales)
    except statistics.StatisticsError:
        mode = None
    stdev = statistics.stdev(sales)
    # variance is the square of stdev; stdev = sqrt(variance)
    variance = statistics.variance(sales)
    total = sum(sales)
    high = max(sales)
    low = min(sales)
    sale_range = high - low
    return mean, median, mode, stdev, variance, total, high, low, sale_range

analyst = input("Analyst name: ")
region = input("Region: ")
print("Enter daily sales for 7 days (one per line):")
sales = [float(input(f"  Day {i+1}: $")) for i in range(7)]

mean, median, mode, stdev, variance, total, high, low, sale_range = analyze_sales(analyst, region, sales)

mode_str = f"${mode:.2f}" if mode is not None else "No unique mode"

print(f"""
======= Weekly Sales Statistics Report =======
Analyst : {analyst}
Region  : {region}
Data    : {sales}
-----------------------------------------------
Total revenue  : ${total:.2f}
Mean (avg)     : ${mean:.2f}
Median         : ${median:.2f}
Mode           : {mode_str}
Std deviation  : ${stdev:.2f}
Variance       : ${variance:.2f}
Highest day    : ${high:.2f}
Lowest day     : ${low:.2f}
Range (hi-lo)  : ${sale_range:.2f}
===============================================
""")
