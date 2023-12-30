import numpy as np
import pandas as pd
from scipy.signal import find_peaks

# Assuming you have a dataframe 'df' with columns 'timestamp', 'accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z'
# Make sure the data is sorted by timestamp

# Function to calculate step counts using peaks in accelerometer data
def calculate_step_counts(accel_data, threshold=0.8):
    # Combine accelerometer readings to get a single measure of activity
    accel_magnitude = np.linalg.norm(accel_data[['accel_x', 'accel_y', 'accel_z']].values, axis=1)

    # Find peaks in the combined accelerometer data
    peaks, _ = find_peaks(accel_magnitude, height=threshold)

    return len(peaks)

# Function to calculate activity level
def calculate_activity_level(gyro_data):
    # Combine gyroscope readings to get a single measure of activity
    gyro_magnitude = np.linalg.norm(gyro_data[['gyro_x', 'gyro_y', 'gyro_z']].values, axis=1)

    # Calculate the average angular velocity as a measure of activity
    activity_level = np.mean(gyro_magnitude)

    return activity_level

# Function to estimate energy consumption based on activity level
def calculate_energy_consumption(activity_level):
    # A simple linear relationship between activity level and energy consumption
    # You may need to calibrate this based on your specific use case and data
    energy_consumption = 0.5 * activity_level  # This is just an example, you may need to adjust the coefficient

    return energy_consumption

# Assuming 'df' is your dataframe with timestamp, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z columns
step_counts = calculate_step_counts(df[['accel_x', 'accel_y', 'accel_z']])
activity_level = calculate_activity_level(df[['gyro_x', 'gyro_y', 'gyro_z']])
energy_consumption = calculate_energy_consumption(activity_level)

print(f"Step Counts: {step_counts}")
print(f"Activity Level: {activity_level}")
print(f"Energy Consumption: {energy_consumption}")
