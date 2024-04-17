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


Run the script (network_traffic_generator.py).

The script will generate synthetic network traffic data and display various statistics including missing values, summary statistics, counts of anomalies, distribution of labels and anomaly types, and details of each anomaly.

Additionally, it will visualize the network traffic patterns and anomalies using matplotlib and seaborn.

