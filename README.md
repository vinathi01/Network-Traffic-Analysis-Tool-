# Network-Traffic-Analysis-Tool-
The code implements:-1) packet sniffing techniques to capture network traffic. -2) Use data visualization to display network traffic patterns. -3) Incorporate machine learning algorithms to detect anomalies and potential threats.

# Synthetic Network Traffic Data Generator and Visualization

This Python script generates synthetic network traffic data and visualizes it using pandas, numpy, faker, matplotlib, and seaborn libraries. It simulates network traffic events such as normal activity and various types of anomalies including intrusion attempts, port scanning, and DDoS attacks.

## Installation

1. Clone the repository or download the script file (`network_traffic_generator.py`).
2. Install the required Python libraries:

## Usage

1. Import the required libraries:
```python
import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
```


Run the script (network_traffic_generator.py).

The script will generate synthetic network traffic data and display various statistics including missing values, summary statistics, counts of anomalies, distribution of labels and anomaly types, and details of each anomaly.

Additionally, it will visualize the network traffic patterns and anomalies using matplotlib and seaborn.









## Contributing


You can customize the following parameters in the generate_network_traffic_data function to generate different types and quantities of synthetic network traffic data:

num_samples: Number of samples to generate.
anomaly_types: List of anomaly types including 'Normal', 'Intrusion Attempt', 'Port Scanning', and 'DDoS Attack'.

## Output


The script outputs the following information:

Missing values in the generated DataFrame.
Summary statistics of the generated data.
Number of anomalies detected.
Distribution of labels (normal vs. anomalies).
Distribution of anomaly types.
Details of each anomaly detected.
It also visualizes the network traffic patterns and anomalies through various plots:

Network traffic by protocol.
Distribution of packet lengths.
Scatter plot of packet length vs source port.
Scatter plot of packet length vs destination port.
Contributing
Contributions are welcome! If you have any suggestions, improvements, or feature requests, please open an issue or submit a pull request.

## License



Feel free to adjust any details or add more sections as needed!
