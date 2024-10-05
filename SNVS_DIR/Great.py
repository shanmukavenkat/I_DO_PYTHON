n = int(input())  # Read the input number

# Initialize variables for sum and product of digits
m = 0  # Sum of digits
j = 1  # Product of digits

# Loop through each digit of the number
temp = n  # Copy of the original number
while temp > 0:
    digit = temp % 10  # Get the last digit
    m += digit  # Add the digit to the sum
    j *= digit  # Multiply the digit to the product
    temp //= 10  # Remove the last digit

# Check if sum of digits (m) + product of digits (j) equals the original number (n)
if m + j == n:
    print("Great")
else:
    print("no")
