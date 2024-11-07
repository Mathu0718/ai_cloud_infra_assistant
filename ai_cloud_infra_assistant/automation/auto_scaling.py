from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Simulated instance data (CPU usage)
data = np.array([
    [1, 50],  # Instance 1: 50% CPU
    [2, 80],  # Instance 2: 80% CPU
    [3, 30],  # Instance 3: 30% CPU
    [4, 90],  # Instance 4: 90% CPU
])

labels = np.array([0, 1, 0, 1])  # 1 = Scaling required, 0 = No scaling

# Train the RandomForest model
model = RandomForestRegressor()
model.fit(data, labels)

def predict_scaling(instance_id, cpu_usage):
    prediction = model.predict([[instance_id, cpu_usage]])
    return prediction > 0.5
