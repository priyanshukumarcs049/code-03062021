import json
from csv import DictWriter


def calculate_category_and_risk(bmi):
    if bmi <= 18.4:
        return {'bmi_category': 'Underweight',
                'health_risk': 'Malnutrition risk'}
    if 18.5 < bmi < 24.9:
        return {'bmi_category': 'Normal weight',
                'health_risk': 'Low risk'}
    if 25 < bmi < 25.9:
        return {'bmi_category': 'Overweight',
                'health_risk': 'Enhanced risk'}
    if 30 < bmi < 34.9:
        return {'bmi_category': 'Moderately obese',
                'health_risk': 'Medium risk'}
    if 35 < bmi < 39.9:
        return {'bmi_category': 'Severely obese',
                'health_risk': 'High risk'}
    if bmi > 40:
        return {'bmi_category': 'Very severely obese',
                'health_risk': 'Very High risk'}


def calculate_bmi(height, weight) -> float:
    return round(weight / (height / 100), 3)


def calculate_and_create_final_data(dictionary):
    health_dictionary_list = []
    for ph in dictionary:
        bmi = calculate_bmi(ph['HeightCm'], ph['WeightKg'])
        c_r = calculate_category_and_risk(bmi)
        person = {'Gender': ph['Gender'], 'Height (in cm)': ph['HeightCm'], 'Weight (in kg)': ph['WeightKg'],
                  'BMI': bmi, 'BMI Category': c_r['bmi_category'], 'Health risk': c_r['health_risk']}
        health_dictionary_list.append(person)
    return health_dictionary_list


if __name__ == '__main__':
    with open(input('Enter absolute path to input json file: ')) as file:
        people_dicts = json.load(file)

    people_health_dictionary_list = calculate_and_create_final_data(people_dicts)

    with open('../BMI data (P).csv', 'w') as outfile:
        writer = DictWriter(outfile,
                            ('Gender', 'Height (in cm)', 'Weight (in kg)', 'BMI', 'BMI Category', 'Health risk'))
        writer.writeheader()
        writer.writerows(people_health_dictionary_list)
