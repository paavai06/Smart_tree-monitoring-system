# Smart Tree Survival Monitoring System

### AI + IoT for Endangered Tree Species Conservation

## Project Overview

The **Smart Tree Survival Monitoring System** is an AI- and IoT-based solution designed to monitor the health and survival conditions of endangered tree species in India.

Traditional tree plantation programs often focus on planting trees without continuous post-plantation monitoring. This makes it difficult to identify environmental stress and take timely action to protect vulnerable trees.

Our system aims to address this problem by combining environmental sensors, machine learning, and a monitoring dashboard to assess tree health and identify trees that may require intervention.

##  Problem Statement

Tree plantation initiatives can experience low survival rates due to environmental stress, unsuitable growing conditions, and insufficient post-plantation monitoring.

Forest departments and conservation organizations need an effective way to monitor individual trees and identify potential survival risks.

## Proposed Solution

The proposed system combines IoT-based environmental monitoring with machine learning to support the early identification of tree survival risks.

The prototype focuses on monitoring endangered Indian tree species and analyzing environmental conditions associated with their survival.

### Key Features

* **Species-Specific Monitoring:** Monitor 20 selected tree species.
* **Environmental Monitoring:** Measure temperature and relative humidity using a DHT11 sensor.
* **IoT Integration:** Use an ESP32 microcontroller to collect sensor readings.
* **Machine Learning:** Classify environmental conditions into Healthy, Vulnerable, and Dead categories using a constraint-based training dataset.
* **Individual Sample Tracking:** Assign unique IDs to planted tree samples.
* **Interactive Dashboard:** Display sensor readings, predictions, and sample statistics.
* **Risk Alerts:** Highlight samples that require further inspection.
* **Survival Analytics:** Calculate and visualize sample health and survival statistics.

> **Note:** The current prototype uses a generated dataset to demonstrate machine learning. Predictions are based on simulated environmental conditions and predefined constraints. They are not yet validated predictions of actual tree survival.

## Target Tree Species

The project focuses on the following 20 species:

1. Hopea erosa
2. Aglaia malabarica
3. Vateria indica
4. Dipterocarpus bengalensis
5. Shorea talura
6. Hildegardia populifolia
7. Drypetes malabarica
8. Hydnocarpus macrocarpus
9. Prioria pinnata
10. Dipterocarpus indicus
11. Cynometra travancorica
12. Litsea kakkachensis
13. Santapauia madurensis
14. Madhuca ponuru
15. Shorea roxburghii
16. Cinnamomum riparium
17. Arenga wightii
18. Palaquium raeburghii
19. Semecarpus travancoricus
20. Gluta travancorica

Species names and conservation classifications should be verified against authoritative botanical and conservation databases before deployment.

## Technologies Used

| Component            | Technology                         |
| -------------------- | ---------------------------------- |
| Programming Language | Python                             |
| Machine Learning     | Scikit-learn                       |
| ML Algorithm         | Random Forest Classifier           |
| Data Processing      | Pandas, NumPy                      |
| Dashboard            | Streamlit                          |
| Microcontroller      | ESP32                              |
| Temperature Sensor   | DHT11                              |
| Dataset              | Generated constraint-based dataset |
| Data Visualization   | Streamlit charts                   |

## System Architecture

```text
       DHT11 SENSOR
    Temperature & Humidity
              |
              v
           ESP32
      Environmental Data
              |
              v
      Data Collection Layer
              |
              v
      Dataset / Data Storage
              |
              v
     Machine Learning Model
      Random Forest Classifier
              |
              v
       Prediction Results
   +----------+-----------+
   |          |           |
   v          v           v
 Healthy  Vulnerable     Dead
   |          |           |
   +----------+-----------+
              |
              v
      Streamlit Dashboard
              |
              v
   Sample Tracking & Alerts
```

*The ESP32-to-dashboard connection is a planned integration until real sensor readings are successfully collected and connected to the application.*

## Machine Learning Methodology

The prototype uses a constraint-based dataset to train a classification model.

### Input Features

* Temperature (°C)
* Relative humidity (%)

### Output Classes

* **Healthy:** Environmental conditions fall within the defined healthy range.
* **Vulnerable:** Environmental conditions indicate potential stress.
* **Dead:** Environmental conditions fall within the predefined high-risk category.

### Model Workflow

1. Generate a synthetic dataset containing environmental measurements.
2. Apply predefined constraints to assign training labels.
3. Split the dataset into training and testing sets.
4. Train a Random Forest classification model.
5. Evaluate the model on the test set.
6. Use the trained model to classify new environmental readings.
7. Display prediction results through the dashboard.

**Important:** These labels represent predefined environmental-condition categories, not confirmed biological outcomes. Reliable tree-survival prediction requires species-specific ecological data and observed survival outcomes.

## Sampling and Monitoring

The proposed sampling design includes:

* 20 tree samples per species.
* 20 selected species.
* 400 planned tree samples in total.

Each sample can be assigned a unique identifier.

Example:

| Sample ID | Species           | Monitoring Status |
| --------- | ----------------- | ----------------- |
| HPE_001   | Hopea erosa       | Healthy           |
| HPE_002   | Hopea erosa       | Vulnerable        |
| HPE_003   | Hopea erosa       | Dead              |
| AGM_001   | Aglaia malabarica | Healthy           |

These entries are illustrative examples, not actual field observations.

The dashboard can be extended to track individual samples, display sensor history, and summarize healthy, vulnerable, and dead counts.

## Installation and Setup

### Prerequisites

* Python 3.10 or a compatible Python version
* Arduino IDE for ESP32 programming
* ESP32 development board
* DHT11 temperature and humidity sensor

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd <your-project-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn
```

### 4. Generate the Dataset

Run the dataset generator:

```bash
python generate_constraint_dataset.py
```

This generates the constraint-based training dataset.

### 5. Train the Model

```bash
python model.py
```

The trained model is saved for use by the dashboard, provided the training script includes model serialization.

### 6. Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard opens in your browser.

*Ensure that your filenames and dataset columns match the scripts in your repository.*

## Hardware Connections

### DHT11 to ESP32

| DHT11 Module Pin | ESP32 Pin |
| ---------------- | --------- |
| + (VCC)          | 3V3       |
| OUT (Data)       | GPIO 4    |
| - (GND)          | GND       |

The sensor readings can be viewed through the Arduino IDE Serial Monitor after uploading the appropriate ESP32 program.

## Expected Impact

### Environmental Impact

* Supports monitoring of endangered tree species.
* Helps identify potentially stressful environmental conditions.
* Encourages data-driven tree plantation management.

### Social Impact

* Supports forest departments and conservation organizations.
* Helps field workers prioritize samples requiring inspection.
* Promotes awareness of biodiversity conservation.

### Economic Impact

* May reduce unnecessary manual monitoring.
* Can help prioritize field visits and maintenance resources.
* Provides a foundation for scalable environmental monitoring.

These are expected benefits and require field testing to establish actual impact.

## Future Enhancements

* Integrate real ESP32 sensor readings into the dashboard.
* Add a soil-moisture sensor for direct measurement of root-zone water availability.
* Investigate appropriate gas sensors for relevant environmental measurements.
* Connect a cloud database for persistent storage and remote monitoring.
* Develop and validate separate models for individual tree species using suitable ecological data.
* Add GPS-based sample location tracking.
* Implement automated notifications for high-risk samples.
* Collect real field data to evaluate and improve prediction accuracy.
* Add historical trend analysis and conservation reports.

## Limitations

* The current dataset is synthetic rather than collected from real trees.
* Environmental thresholds are prototype assumptions and require ecological validation.
* Temperature and humidity alone cannot establish whether a tree is healthy or dead.
* Gas readings cannot be interpreted as tree stress indicators without appropriate sensors, calibration, and supporting evidence.
* Real-world survival prediction requires longitudinal field observations, species-specific information, and independent model evaluation.
* Hardware connectivity, cloud integration, and automated notifications depend on their successful implementation.

## Target Stakeholders

* Forest departments
* Wildlife and biodiversity conservation organizations
* Environmental researchers
* Tree plantation and restoration programs
* Forestry field workers

## Conclusion

The Smart Tree Survival Monitoring System proposes an integrated AI and IoT approach to endangered tree conservation.

By combining environmental monitoring, machine learning, sample-level tracking, and an interactive dashboard, the project provides a foundation for improving post-plantation monitoring and supporting timely conservation decisions.

The long-term goal is to evolve the prototype into a reliable, field-tested system using real sensor measurements and observed tree-survival data.

---

**Project Domain:** Climate Tech | Green Innovation | Artificial Intelligence | Internet of Things

**Project Status:** Prototype Development

**Developed for:** Hackathon Project
