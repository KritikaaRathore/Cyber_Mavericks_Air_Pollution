## Cyber_Mavericks_Air_Pollution
Analyze Air Pollution Impact on Health Metrics and visualize correlations


**Group Members**

Kritika Rathore  - KU2407U318
<br/>Maddukuri Arithaa - KU2407U258
<br/>Pratham Namdev - KU2407U355
<br/>Khushi Shah - KU2407U316
<br/>Unnati Takkur - KU2407U385

**Objective Of The Project**

Analyze Air Pollution's impact on Health Metrics and visualize correlations

**Tools And Libraries Used**

* Visual Studio Code
* NumPy 
* Pandas
* Matplotlib

**Data Source**

* World Health Organization (WHO)
* IQAir (World Air Quality Index)
* NASA Earth Observatory

**Execution Steps**


---

1. Define the Scope of the Project

Purpose: Predict air quality index (AQI) or pollutant levels (e.g., PM2.5, CO, NO2).

Target Audience: Industrial use, public health, or personal use.

Key Metrics: Choose pollutants and environmental parameters to monitor.



---

2. Hardware Setup

Required Components:

Microcontroller/Single-Board Computer: Arduino, Raspberry Pi, or ESP32.

Sensors: Air quality sensors like MQ135 (general pollutants), PMS5003 (PM2.5/PM10), or DHT22 for temperature and humidity.

Power Source: Battery or USB power.

Display: LCD or OLED for real-time data, or connect to a PC/mobile app.


Assemble the Device:

Connect sensors to the microcontroller.

Ensure proper wiring and connections for power and communication.




---

3. Software Setup

Programming Environment:

Use Arduino IDE, Python, or other tools depending on the microcontroller.

Install necessary libraries for sensor communication.


2. Code Implementation:

Write code to collect sensor data.

Use algorithms to process and predict air quality based on collected data.

(Optional) Integrate machine learning models for advanced predictions using platforms like TensorFlow Lite or Edge Impulse.


3. Data Display:

Display data on an LCD or send it to a web dashboard/mobile app using Wi-Fi or Bluetooth.

Use platforms like ThingSpeak for cloud-based monitoring.



4. Testing and Calibration

Sensor Calibration: Ensure sensors provide accurate readings by comparing them with standard equipment.

Test Environment: Test the device in different conditions (indoor, outdoor, polluted areas).


5. Running the Project:

1. Power the Device: Connect it to a power source.


2. Monitor Data: Observe real-time data on the device display or a connected app.


3. Predict Air Quality:

Use collected data to predict trends in air pollution using machine learning models or predefined algorithms.

Provide alerts or recommendations based on AQI thresholds.




6. Deployment and Usage

Place the device in a location where air quality monitoring is needed.

Regularly update software and calibrate sensors for accuracy.



---

Additional Features (Optional)

Mobile App: Develop an app to visualize and predict air pollution trends.

IoT Integration: Connect the device to IoT platforms for remote monitoring.

AI Models: Use historical data to predict future air pollution levels.


---


**Challenges Faced**

*Air pollution affects people in several ways, leading to significant challenges:

1. Health Challenges

Respiratory Problems: Increases asthma, bronchitis, and other lung diseases.

Cardiovascular Issues: Long-term exposure raises risks of heart attacks and strokes.

Premature Deaths: Millions die annually due to polluted air.

Weakened Immunity: Makes individuals more susceptible to infections and diseases.


2. Economic Challenges

Increased Healthcare Costs: Medical expenses rise due to pollution-related illnesses.

Loss of Productivity: Sick individuals miss work or cannot perform efficiently.

Damage to Livelihoods: Polluted air affects agriculture and other outdoor jobs.


3. Social and Psychological Challenges

Reduced Quality of Life: People avoid outdoor activities due to poor air quality.

Mental Health Impact: Fear and anxiety about pollution can harm mental well-being.


4. Environmental Challenges Affecting People

Food Security: Pollution damages crops, reducing food supply.

Water Contamination: Pollutants in the air also affect water sources.

Climate Change: Intensified by air pollution, leading to extreme weather conditions that disrupt lives.


Addressing air pollution is critical for improving health, livelihoods, and overall quality of life.



---



**Summary of Results**


*Air Pollution Predictor Device Using Python - Summary

Objective: Predict air quality and monitor pollution levels using Python.

Key Components:

Sensors: Measure pollutants (PM2.5, PM10, CO2) and environmental factors (temperature, humidity).

Microcontroller: Collects sensor data for processing (optional for hardware integration).

Python: Processes data, calculates AQI, and predicts air quality trends.


Features:

Real-time data collection and processing using Python.

Air quality prediction using algorithms or machine learning (e.g., Scikit-learn).

Data visualization (graphs, charts, or simple GUI with Matplotlib/Tkinter).


Applications:

Personal Use: Alerts users about air quality.

Educational Tool: Demonstrates air pollution monitoring.

Research: Used for environmental health studies.


Benefits:

Simple and cost-effective.

Scalable for additional sensors or advanced models.

Easy to develop with Python and accessible to beginners.



This project allows users to monitor and predict air pollution with a simple Python-based device.
