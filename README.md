# code-03062021
How to run program in local environment (steps):
Navigate to the project directory for running either version of the program
../<project root dir>/src
Run the following command in terminal to run all the tests at root directory (-v for verbose output)
pytest
To generate the output (using either versions of the program) csv file, run the following command in terminal
python main_oops.py
(will produce BMI data (OOP).csv)

OR
python main_procedural.py
(will produce BMI data (P).csv)
and enter the path as prompted.

Requirements:

Pytest: Run following command in terminal to install pytest
pip install pytest
Input data: Create a valid JSON file having following structure:
[
   {
      "Gender":"Male",
      "HeightCm":171,
      "WeightKg":96
   },
   {
      "Gender":"Male",
      "HeightCm":161,
      "WeightKg":85
   }
   ...
   ...
]
NOTE: A sample JSON file (data.json) is also present in the repository
