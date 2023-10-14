Convert acceleration to velocity and displacement using integrate

## Requirement
- pandas
- matplotlib
- scipy
- send2trash

## How To Use
1. Fork or clone the project
2. Change `YOUR_MASS = 50` to your mass
3. Change `INPUT_ACCE_CSV = 'example.csv'` to your csv file
4. Make sure yout csv file contain this header
   time,ax,ay,az,aT
5. Change `INPUT_AXIS = 'T'` if you want to another axis (x / y / z / T)
6. Change `DATA_SMOOTHING = 1` to 0 if you dont want to smooth the data
7. If you want to smooth the data, replace this line so that your data is more accurate
   ```
    CUTOFF_FREQUENCY = 0.00355  # Adjust this value according to your requirements
    SAMPLING_RATE = 200.0  # Replace with your actual sampling rate
    FILTER_ORDER = 4  # You can adjust the filter order as needed
   ```
8. Run the code

## License
This code is open-sourced software licensed under the [MIT License](https://opensource.org/licenses/MIT).
