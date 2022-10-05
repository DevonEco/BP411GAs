n = int(input("Enter a number to calculate sum: "))

sum = 0

for current_number in range(1, n+1):
    sum = sum + current_number
print("The sum of the first " + str(n) + "numbers is: " + str(sum))

print("The average of the first " + str(n) + "numbers is: " + str(sum/n))
