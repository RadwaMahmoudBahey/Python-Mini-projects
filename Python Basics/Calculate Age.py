def main(): 
    startYear = int(input("Enter start year = "))
    endYear = int(input("Enter end year = "))
    age = 0
    if endYear >= startYear:
        age = endYear - startYear
    return age
age = main()
print(f'age = {age}')