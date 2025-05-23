# Shipping Cost Calculation

## Input package weight and shippiing rate
weight = float(input("Enter the package weight in Kilograms: "))
rate = float(input("Enter the shipping rate per Kilogram: "))

## Calculation shipping cost
shipping_cost = weight * rate

## Display the result
print(f"shipping_cost: {shipping_cost} USD")
