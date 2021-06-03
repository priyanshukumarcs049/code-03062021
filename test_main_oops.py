import json

from src import main_oops


def test_json_to_object_conversion():
    json_data = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}]'
    bmi = round(96 / 1.71, 3)
    health_risk = 'Very High risk'
    bmi_category = 'Very severely obese'
    dictionary = json.loads(json_data)
    assert main_oops.create_people_health_list(dictionary)[0].bmi == bmi
    assert main_oops.create_people_health_list(dictionary)[0].health_risk == health_risk
    assert main_oops.create_people_health_list(dictionary)[0].bmi_category == bmi_category


def test_object_to_dictionary_conversion():
    person_obj = main_oops.PersonHealth(gender='Male', height=171, weight=96)
    person_health = [person_obj]
    assert main_oops.create_health_dictionary(person_health) == [
        {'Gender': 'Male', 'Height (in cm)': 171, 'Weight (in kg)': 96, 'BMI': 56.14,
         'BMI Category': 'Very severely obese', 'Health risk': 'Very High risk'}]
