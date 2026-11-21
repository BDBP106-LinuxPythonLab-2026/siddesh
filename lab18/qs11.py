
# qs 11
#  Magic date
# # Months = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
# # date = int(input("Enter a Date: "))
# # month = int(input("Enter the Month in numbers : "))
# # year = month*date
# #
# # for i in Months:
# #     if i == month:
# #       print(date,"/",Months[month],"/","19",year)
# #       break
#
# import calendar
#
#
# def is_magic_date(month, day, year):
#     """Determines whether a given date is a magic date."""
#     two_digit_year = year % 100
#     return (month * day) == two_digit_year
#
#
# def main():
#     print("Magic Dates in the 20th Century (1901 - 2000):")
#     magic_dates_count = 0
#
#     #  20th century starts from 1901 to 2000
#     for year in range(1901, 2001):
#         for month in range(1, 13):
#             # calendar.monthrange returns (first_weekday, number_of_days)
#             # This automatically handles leap years (e.g., 1904, 1996, 2000)
#             _, days_in_month = calendar.monthrange(year, month)
#
#             for day in range(1, days_in_month + 1):
#                 if is_magic_date(month, day, year):
#                     month_name = calendar.month_name[month]
#                     print(f"{month_name} {day}, {year}")
#                     magic_dates_count += 1
#
#     print(f"Total magic dates found: {magic_dates_count}")
#
#
# if __name__ == "__main__":
#     main()
#
