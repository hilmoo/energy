Convert acceleration to velocity and displacement using integrate from csv file

## Requirement
- python
- pandas
- matplotlib
- scipy
- send2trash

## How To Use
1. Fork or clone the project
2. Open main.py
3. Change `YOUR_MASS = 50` to your mass
4. Change `INPUT_ACCE_CSV = 'example.csv'` to your csv file
5. Make sure yout csv file contain this header
   ```
   time,ax,ay,az,aT
6. Change `INPUT_AXIS = 'T'` if you want to another axis (x / y / z / T)
7. Change `DATA_SMOOTHING = 1` to 0 if you dont want to smooth the data
8. If you want to smooth the data, replace this line so that your data is more accurate
   ```
    CUTOFF_FREQUENCY = 0.00355  # Adjust this value according to your requirements
    FILTER_ORDER = 4  # You can adjust the filter order as needed
   ```
9. Run the code

## How To Combine Graph
1. ComboGraph.py
2. Run the code

## License
This code is open-sourced software licensed under the [MIT License](https://opensource.org/licenses/MIT).
