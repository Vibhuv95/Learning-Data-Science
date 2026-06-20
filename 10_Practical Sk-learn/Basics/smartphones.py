import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define the number of rows
num_rows = 1000

# Generate Data
data = {
    'camera': np.random.randint(8, 201, size=num_rows),  # Megapixels (8 to 200)
    'age': np.random.randint(0, 4, size=num_rows),       # Age in year (0 tp 3)
    'ram': np.random.choice([2, 4, 6, 8, 12, 16], size=num_rows),  # RAM in GB
    'cpu_score': np.random.randint(40, 101, size=num_rows),  # CPU benchmark score (40 to 100)
    'slot_sd': np.random.choice([0, 1], size=num_rows),  # SD card slot (0 = No or 1 = Yes)
    'sims': np.random.choice([1, 2], size=num_rows),  # Number of SIM slots (1 or 2)
    'price': np.random.randint(8000, 70001, size=num_rows)  # Price in dollars (8000 to 70000)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV (Optional)
df.to_csv('smartphones.csv', index=False)

# Display First few rows
print(df.head())
