#Cris Ramirez
# Sales Summary Calculator
# Concepts: user input, f-string, type cast, user-defined function
 
def sales_summary(name, region, units, price): 
    revenue = units * price               # type cast already done by caller, so no need to cast here
    bonus   = revenue * 0.10              # 10% performance bonus 
    return revenue, bonus 
 
# ── Collect input ────────────────────────────────────── 
name   =       input("Associate name:   ") 
region =       input("Store region:     ") 
units  = int  (input("Units sold:       "))   # cast str -> int 
price  = float(input("Price per unit $: "))   # cast str -> float 
 
# ── Call the function ────────────────────────────────── 
revenue, bonus = sales_summary(name, region, units, price) 
 
# ── Print formatted report ───────────────────────────── 
print(f""" 
===== RetailEdge Inc. — Sales Summary ===== 
Associate : {name} 
Region    : {region} 
Units sold: {units} 
Unit price: ${price:.2f} ------------------------------------------- 
Total revenue           : ${revenue:.2f} 
Performance bonus (10%) : ${bonus:.2f} 
=========================================== 
""") 