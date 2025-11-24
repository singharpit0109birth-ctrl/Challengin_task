LAND_AREA = "x"
# x is in acres
#CROP_YIELD_PER_ACRE = "y"
# y is in quintals
#selling price =" z"
# z is in rupees
#cost_of_plantation_of_per_acre = "c"
 # c should be in rupeeCROP PROFIT CALCULATOR
#selling_price_of_crop_per_quintalss
x = float(input ("enter your land area :")) 
y = float(input ("enter crop yield per acres "))
z = float (input ("enter selling price of crop per quintals "))
c = float (input ("enter cost of plantation of crop per acre "))
                   #calculation part 
total_yield = x * y
total_cost = x * c
total_revenue = total_yield * z
profit = total_revenue - total_cost
               
print ("your total profit is", profit) #IF OUTPUT IS NEGATIVE THEN IT IS A LOSS ELSE IT IS PROFIT
