import json

from src import main_procedural


def test_json_to_object_conversion():
    json_data = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}]'
    people = json.loads(json_data)
    assert main_procedural.calculate_and_create_final_data(people) == [
        {'Gender': 'Male', 'Height (in cm)': 171, 'Weight (in kg)': 96, 'BMI': 56.14,
         'BMI Category': 'Very severely obese', 'Health risk': 'Very High risk'}]
