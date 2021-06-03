# Python BMI Calculator Coding Challenge

#### How to run program in local environment (steps):
1. Navigate to the project directory for running either version of the program
```
../<project root dir>/src
```

2. Run the following command in terminal to run all the tests at root directory (```-v``` for verbose output)
```
pytest
```
3. To generate the output (using either versions of the program) ```csv``` file, run the following command in terminal
```
python main_oops.py
```
(will produce ```BMI data (OOP).csv```)
#### OR
```
python main_procedural.py
``` 
(will produce ```BMI data (P).csv```) <br>
and enter the path as prompted.



Requirements:
1. Pytest: Run following command in terminal to install ```pytest```<br>
```
pip install pytest
```
2. Input data: Create a valid ```JSON``` file having following structure:
```
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
````
###### NOTE: A sample JSON file (```data.json```) is also present in the repository
