# Importing pyyaml so we can read yml in python 
import yaml
import pandas as pd
import json

# Read setting from yml
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)


# Get settings
max_days_since_calibration = config["max_days_since_calibration"]
output_file = config["output_file"]

print(max_days_since_calibration)
print(output_file)

# Read sensor data
sensors = pd.read_excel("sensors.xlsx")

# Check the data
print(sensors.head())


# Read calibration data
calibrations = pd.read_csv("calibrations.csv")

# Check the data
print(calibrations.head())

# Checking columns to see if we can merge them (both need to have sensor_id)
print(sensors.columns)
print(calibrations.columns)

# Match sensor information with calibration and making a sensor_data as new df
sensor_data = pd.merge(sensors,calibrations, on = "sensor_id")
print(sensor_data.head())

# Now we identify sensor that are overdue
identidy_overdue_sensors = sensor_data[sensor_data["days_since_calibration"] > max_days_since_calibration]

# Converting df to a list of dictionaries
overdue_data = identidy_overdue_sensors.to_dict(orient="records")

# Export identidy_overdue_sensors to JSON
with open(output_file, "w") as file:
    json.dump(overdue_data, file, indent=2)


#Chatgpt
#You asked for help understanding the assignment, debugging errors,
# improving code comments, understanding concepts like safe_load() 
# and to_dict(orient="records"), and finding relevant Stack Overflow 
# examples to verify the approach. You also asked for help setting 
# up and organizing the GitHub repository and using Git correctly in VS Code.