import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize Faker to generate fake data
fake = Faker()


# Generate synthetic network traffic data
def generate_network_traffic_data(num_samples):
    data = []
    anomaly_types = ['Normal', 'Intrusion Attempt', 'Port Scanning', 'DDoS Attack']

    for _ in range(num_samples):
        timestamp = fake.date_time_between(start_date='-1d', end_date='now')
        source_ip = fake.ipv4()
        destination_ip = fake.ipv4()
        source_port = random.randint(1024, 65535)
        destination_port = random.randint(1, 1023)
        protocol = random.choice(['TCP', 'UDP'])
        packet_length = random.randint(64, 1500)
        payload = fake.text(max_nb_chars=random.randint(10, 100))
        anomaly_type = random.choice(anomaly_types)
        label = 1 if anomaly_type != 'Normal' else 0

        data.append([timestamp, source_ip, destination_ip, source_port, destination_port, protocol,
                     packet_length, payload, anomaly_type, label])

    return data


# Define the number of samples
num_samples = 10

# Generate synthetic network traffic data
network_traffic_data = generate_network_traffic_data(num_samples)

# Create DataFrame
columns = ['Timestamp', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port',
           'Protocol', 'Packet Length', 'Payload', 'Anomaly Type', 'Label']
df = pd.DataFrame(network_traffic_data, columns=columns)

# Output missing values
print("Missing values:\n", df.isnull().sum())

# Output summary statistics
print("\nSummary statistics:")
print(df.describe())

# Count anomalies
num_anomalies = df[df['Anomaly Type'] != 'Normal'].shape[0]
print("\nNumber of anomalies:", num_anomalies)

# Output distribution of labels
print("\nDistribution of labels:")
print(df['Label'].value_counts())

# Output distribution of anomaly types
print("\nDistribution of anomaly types:")
print(df['Anomaly Type'].value_counts())

# Output details of each anomaly
print("\nDetails of anomalies:")
anomalies = df[df['Anomaly Type'] != 'Normal']
for idx, row in anomalies.iterrows():
    print(f"Alert: Suspicious activity detected - {row['Anomaly Type']} at {row['Timestamp']}. "
          f"Source IP: {row['Source IP']}, Destination IP: {row['Destination IP']}, "
          f"Source Port: {row['Source Port']}, Destination Port: {row['Destination Port']}, "
          f"Protocol: {row['Protocol']}, Packet Length: {row['Packet Length']}, Payload: {row['Payload']}")

# Data Visualization: Display network traffic patterns and anomalies
plt.figure(figsize=(16, 10))

# Plot network traffic by protocol
plt.subplot(2, 2, 1)
sns.countplot(x='Protocol', data=df)
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.title('Network Traffic by Protocol')

# Plot distribution of packet lengths
plt.subplot(2, 2, 2)
sns.histplot(df['Packet Length'], bins=30, kde=True)
plt.xlabel('Packet Length')
plt.ylabel('Frequency')
plt.title('Distribution of Packet Length')

# Plot scatter plot of packet length vs source port
plt.subplot(2, 2, 3)
plt.scatter(df['Packet Length'], df['Source Port'], c=df['Label'], cmap='viridis', alpha=0.5)
plt.xlabel('Packet Length')
plt.ylabel('Source Port')
plt.title('Packet Length vs Source Port')

# Plot scatter plot of packet length vs destination port
plt.subplot(2, 2, 4)
plt.scatter(df['Packet Length'], df['Destination Port'], c=df['Label'], cmap='viridis', alpha=0.5)
plt.xlabel('Packet Length')
plt.ylabel('Destination Port')
plt.title('Packet Length vs Destination Port')

plt.tight_layout()
plt.show()
