

years = []

for year in range (1990 , 2018):
    years.append(year)

print(years)

leap_year = []
for year in years:
    if not year % 4:
        leap_year.append(year)

print(leap_year)

#year_to_enter = input ("Введіть рік для перевірки >>> ")

while True:
    year_to_enter = input("Введіть рік для перевірки >>> ")
    year_to_enter = int(year_to_enter)
    if leap_year.count(year_to_enter) > 0:
        print("рік є високосним")
    else:
        print("рік не є високосним")






