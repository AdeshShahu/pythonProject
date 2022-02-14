

num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10  #gets the reminder into the digit variable
   sum += digit ** 3  # multiplies the digit value 3 times
   temp //= 10    #gets the questioned to the temp variable

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")