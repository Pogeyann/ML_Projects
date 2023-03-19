#console
#current year
##current _month
#current date
#birth year
#birth month
#birth date

#print age= current year-birth year

#2022
#9
#18

#2021
#9
#19

#age=2022-2021=1

current_year=int(input('enter current_year'))
current_month=int(input('enter current month'))
current_date=int(input('enter current date'))
birth_year=int(input('enter birth year'))
birth_month=int(input('enter birth_month'))
birth_date=int(input('enter birth date'))
age=current_year-birth_year
if(current_date<=31)or(current_month<=12)or(current_year>birth_year):
    if(birth_month<=12)or(birth_date<=31):
        print(age)

