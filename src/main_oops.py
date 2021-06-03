import json
from csv import DictWriter


class PersonHealth:
    gender = None
    height = None
    weight = None
    bmi = None
    bmi_category = None
    health_risk = None

    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = round(weight / (height / 100), 3)

        if self.bmi <= 18.4:
            self.bmi_category = 'Underweight'
            self.health_risk = 'Malnutrition risk'
        if 18.5 < self.bmi < 24.9:
            self.bmi_category = 'Normal weight'
            self.health_risk = 'Low risk'
        if 25 < self.bmi < 25.9:
            self.bmi_category = 'Overweight'
            self.health_risk = 'Enhanced risk'
        if 30 < self.bmi < 34.9:
            self.bmi_category = 'Moderately obese'
            self.health_risk = 'Medium risk'
        if 35 < self.bmi < 39.9:
            self.bmi_category = 'Severely obese'
            self.health_risk = 'High risk'
        if self.bmi > 40:
            self.bmi_category = 'Very severely obese'
            self.health_risk = 'Very High risk'


def create_people_health_list(people_dicts):
    people_health_list = []
    for pd in people_dicts:
        pupil_health = PersonHealth(pd['Gender'], pd['HeightCm'], pd['WeightKg'])
        people_health_list.append(pupil_health)
    return people_health_list


def create_health_dictionary(people_health):
    people = []
    for ph in people_health:
        person = {'Gender': ph.gender, 'Height (in cm)': ph.height, 'Weight (in kg)': ph.weight, 'BMI': ph.bmi,
                  'BMI Category': ph.bmi_category, 'Health risk': ph.health_risk}
        people.append(person)
    return people


if __name__ == '__main__':
    with open(input('Enter absolute path to input json file: ')) as file:
        given_json_data = json.load(file)

    people_health = create_people_health_list(given_json_data)
    people = create_health_dictionary(people_health)

    # print(people)
    with open('../BMI data (OOP).csv', 'w') as outfile:
        writer = DictWriter(outfile,
                            ('Gender', 'Height (in cm)', 'Weight (in kg)', 'BMI', 'BMI Category', 'Health risk'))
        writer.writeheader()
        writer.writerows(people)
