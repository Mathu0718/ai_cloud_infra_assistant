from sklearn.ensemble import IsolationForest
import numpy as np

# Simulated usage data (CPU, RAM)
data = np.array([
    [50, 2.0],  # 50% CPU, 2GB RAM
    [80, 4.0],  # 80% CPU, 4GB RAM
    [30, 1.5],  # 30% CPU, 1.5GB RAM
    [95, 5.5],  # High usage (Anomaly)
])

anomaly_detector = IsolationForest(contamination=0.1)
anomaly_detector.fit(data)

def detect_anomalies(instance_data):
    predictions = anomaly_detector.predict(instance_data)
    return predictions == -1  # Returns True if anomaly detected
