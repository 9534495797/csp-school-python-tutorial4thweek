# import calendar
# c = calendar.Calendar()
# for week in c.monthdayscalendar(2020, 12):
#     print(week)

# import calendar
# print(calendar.month_name[12])

# Python program to print the calendar of 
# the given year
    
# importing calendar module   
# import calendar  
    
# # using calendar to print calendar of year  
# print ("The calender of year 2020 is : ")  
# print (calendar.calendar(2020, 2, 1, 6)) 



# import calendar
# print(calendar.calendar(2019))

# Python program to print the calendar of 
# the given year
    
# importing calendar module   
# import calendar  
    
# # using calendar to print calendar of year  
# print ("The calender of year 2020 is : ")  
# print (calendar.calendar(2020, 2, 1, 6)) 


# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
