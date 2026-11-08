# AI Assignment 1
# Car Evaluation Dataset
# Stage 2: Dataset Loading and Exploration

import csv
from pathlib import Path
from collections import Counter

# Step 1: Locate the dataset
file_path = Path(__file__).resolve().parent / "data" / "car.data"

# Step 2: Read the dataset
with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    car_data = list(reader)

# Step 3: Display the total number of records
print("CAR EVALUATION DATASET")
print("----------------------")

print("Total vehicle records:", len(car_data))

# Step 4: Display the first vehicle record
print("\nFirst vehicle record:")
print(car_data[0])

# Step 5: Identify the dataset attributes
attributes = [
    "Buying Price",
    "Maintenance Cost",
    "Number of Doors",
    "Passenger Capacity",
    "Luggage Boot Size",
    "Safety",
    "Car Acceptability"
]

print("\nDataset attributes:")

for attribute in attributes:
    print("-", attribute)

# Step 6: Count the classification categories
classifications = Counter(row[6] for row in car_data)

print("\nVehicle classifications:")

for category, count in sorted(classifications.items()):
    print(category, ":", count)

print("\nDataset loaded successfully!")