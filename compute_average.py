data = {
    "('Alabama', 'Age (years)', '18 - 24')": 24.9,
    "('Alabama', 'Age (years)', '25 - 34')": 33.0,
    "('Alabama', 'Age (years)', '35 - 44')": 35.0,
    "('Alabama', 'Age (years)', '45 - 54')": 34.333333333333336,
    "('Alabama', 'Age (years)', '55 - 64')": 35.225,
    "('Alabama', 'Education', 'College graduate')": 34.93333333333333,
    "('Alabama', 'Education', 'High school graduate')": 31.799999999999997,
    "('Alabama', 'Education', 'Less than high school')": 34.0,
    "('Alabama', 'Education', 'Some college or technical school')": 34.15,
    "('Alabama', 'Income', '$15,000 - $24,999')": 31.625,
    "('Alabama', 'Income', '$35,000 - $49,999')": 37.06666666666667,
    "('Alabama', 'Income', '$50,000 - $74,999')": 30.9,
    "('Alabama', 'Income', '$75,000 or greater')": 36.86666666666667,
    "('Alabama', 'Income', 'Data not reported')": 31.75,
    "('Alabama', 'Income', 'Less than $15,000')": 27.7,
    "('Alabama', 'Race/Ethnicity', '2 or more races')": 38.3,
    "('Alabama', 'Race/Ethnicity', 'American Indian/Alaska Native')": 28.45,
    "('Alabama', 'Race/Ethnicity', 'Asian')": 34.5,
    "('Alabama', 'Race/Ethnicity', 'Hawaiian/Pacific Islander')": 34.5,
    "('Alabama', 'Race/Ethnicity', 'Hispanic')": 37.93333333333333,
    "('Alabama', 'Race/Ethnicity', 'Non-Hispanic White')": 36.4,
    "('Alabama', 'Race/Ethnicity', 'Other')": 34.5,
    "('Alabama', 'Total', 'Total')": 34.3,
}

# Compute the average
average = sum(data.values()) / len(data)

print(f"The average of all the values is {average}")

