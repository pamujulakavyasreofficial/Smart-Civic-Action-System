# 🌍 Smart Civic Action System



### AI-Powered Waste Detection & Automated Civic Complaint Management



<p align="center">

&#x20; <b>Detect • Locate • Report • Track</b>

</p>



<p align="center">

&#x20; An intelligent civic monitoring system that uses Computer Vision and YOLO-based object detection to identify waste, assess its severity, generate civic complaints, and track their resolution.

</p>



---



## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Key Features](#-key-features)
- [AI-Based Waste Detection](#-ai-based-waste-detection)
- [Severity Classification](#-severity-classification)
- [System Workflow](#-system-workflow)
- [System Modules](#-system-modules)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Run the Backend](#-run-the-backend)
- [Run the Frontend](#-run-the-frontend)
- [API Endpoints](#-api-endpoints)
- [Detection Process](#-detection-process)
- [Example Output](#-example-output)
- [Complaint Lifecycle](#-complaint-lifecycle)
- [Advantages of the System](#-advantages-of-the-system)
- [Future Scope](#-future-scope)
- [Project Highlights](#-project-highlights)
- [License](#-license)
- [Contact](#-contact)



---



## 🚀 Overview



The **Smart Civic Action System** is an AI-based solution designed to improve waste monitoring and civic complaint management.



Traditional waste reporting often depends on citizens or sanitation workers manually identifying and reporting waste. This can result in delayed reporting and slower response.



The proposed system automates the initial stages of the process by analyzing an input image using a trained **YOLO model**, counting detected waste objects, classifying the severity, identifying the associated location, generating a complaint, and maintaining its status through the complaint lifecycle.



### 🔄 Core Workflow



**Image → AI Detection → Waste Count → Severity → Location → Complaint → Tracking**



---



## 🎯 Problem Statement



Public waste is often identified and reported manually, which can lead to:



- Delayed identification of waste

- Manual complaint registration

- Lack of structured complaint information

- Difficulty in monitoring complaint status

- Delayed escalation of serious waste conditions

- Limited data for analysis and reporting



The **Smart Civic Action System** addresses these challenges through an automated AI-assisted workflow.



---



## 💡 Key Features



- 🧠 **AI Waste Detection** – Detects waste using a trained YOLO model.
  
- 🔢 **Waste Counting** – Counts detected waste objects.

- ⚠️ **Severity Classification** – Categorizes waste conditions as Low, Medium, or High.

- 📍 **Location Identification** – Associates the detected issue with location information.

- 📄 **Automatic Complaint Generation** – Creates a structured civic complaint automatically.

- 📊 **Complaint Tracking** – Tracks complaint status.

- 🚨 **Escalation** – Identifies cases requiring escalation.

- 🗄️ **Database Storage** – Stores complaint information using SQLite.

- 📈 **Data Analysis** – Provides complaint-related analytical information.

- 🗺️ **Map Visualization** – Displays location information through the frontend.



---



## 🧠 AI-Based Waste Detection



The system uses a trained **YOLO-based object detection model** to identify waste from an input image.



The detection pipeline follows:



```text

Input Image

    ↓

YOLO Model

    ↓

Waste Detection

    ↓

Number of Detected Objects

    ↓

Severity Classification

```



The trained model is stored in:



```text

models/best.pt

```



---



## ⚠️ Severity Classification



The system determines severity based on the number of detected waste objects.



🟢 **Low** — 0–3 waste objects

🟡 **Medium** — 4–7 waste objects

🔴 **High** — 8 or more waste objects



High-severity cases are marked as requiring escalation.



---



## 🔄 System Workflow



```text

             Input Image

                  ↓

         YOLO Waste Detection

                  ↓

         Count Detected Waste

                  ↓

         Severity Classification

                  ↓

         Location Identification

                  ↓

      Automatic Complaint Generation

                  ↓

         Store in Database

                  ↓

         Complaint Tracking

                  ↓

       ┌──────────┴──────────┐

       ↓                     ↓

  High Severity         Normal Case

       ↓                     ↓

Escalation Required     Monitoring

       └──────────┬──────────┘

                  ↓

         Dashboard / Analysis

```



---



## 🏗️ System Modules



### 1. 🧠 Waste Detection Module



Uses the trained YOLO model to identify waste from the input image.



### 2. 📍 Location Identification Module



Associates the detected waste with location information.



### 3. 📝 Automatic Complaint Generation



Creates a unique complaint ID and prepares complaint information automatically.



### 4. 📋 Complaint Management & Tracking



Maintains the complaint lifecycle and updates its status.



Example:



```text

Pending

  ↓

In Progress

  ↓

Resolved

```



### 5. 🚨 Escalation & Notification



High-severity cases are identified for escalation.



### 6. 📊 Data Analysis & Reporting



Complaint information stored in the database can be analyzed to support monitoring and reporting.



---



## 🛠️ Technology Stack



### Backend



- Python

- FastAPI

- Uvicorn



### Artificial Intelligence



- YOLO

- Ultralytics

- OpenCV



### Data & Database



- SQLite

- Pandas



### Frontend



- HTML

- CSS

- JavaScript

- Leaflet

- OpenStreetMap



### Development Tools



- Visual Studio Code

- Git

- GitHub



---



## 📁 Project Structure



```text

Smart-Civic-Action-System/

│

├── 📂 evidence/

│   └── detected.jpg

│

├── 📂 frontend/

│   └── index.html

│

├── 📂 models/

│   └── best.pt

│

├── 📂 uploads/

│   └── test.jpg

│

├── 📄 smart_civic_action.py

├── 📄 main.py

├── 📄 complaint.py

├── 📄 severity.py

├── 📄 location.py

├── 📄 escalation.py

├── 📄 tracking.py

├── 📄 database.py

├── 📄 data_analysis.py

├── 📄 requirements.txt

├── 📄 test.jpg

├── 📄 complaints.db

├── 📄 yolov8n.pt

└── 📄 .gitignore

```



---



## 💻 Installation



### 1. Clone the Repository



```bash

git clone https://github.com/pamujulakavyasreofficial/Smart-Civic-Action-System.git

```



### 2. Open the Project



```bash

cd Smart-Civic-Action-System

```



### 3. Install Required Packages



```bash

python -m pip install -r requirements.txt

```



---



## ▶️ Run the Backend



Start the FastAPI application:



```bash

python -m uvicorn smart_civic_action:app --reload

```



The backend will run at:



```text

http://127.0.0.1:8000

```



FastAPI documentation:



```text

http://127.0.0.1:8000/docs

```



---



## 🌐 Run the Frontend



After starting the backend, open:



```text

frontend/index.html

```



in a web browser.



The frontend communicates with the FastAPI backend to display detection and complaint information.



---



## 🔌 API Endpoints



**GET /**  

Check application status.


**GET /complaints**  

View all complaints.


**POST /detect**  

Upload an image and perform waste detection.


**GET /complaints/{complaint_id}**  

View a specific complaint.


**GET /analysis**  

Retrieve analytical information.


---



## 📸 Detection Process



A sample input image can be provided to the system.



The system:



- Receives the image

- Processes it using the YOLO model

- Detects waste objects

- Counts the detected objects

- Determines severity

- Identifies the location

- Generates a complaint

- Stores the complaint

- Tracks its status

- Identifies whether escalation is required



---



## 📊 Example Output



A sample detection can produce information such as:



```text

Waste Detected     : 11

Severity           : High

Escalation         : Required

Complaint Status   : Pending

```



The detected output image is stored in:



```text

evidence/detected.jpg

```



---



## 🗺️ Complaint Lifecycle



```text

Detection

   ↓

Complaint Created

   ↓

Pending

   ↓

In Progress

   ↓

Resolved

```



For high-severity conditions:



```text

High Severity

    ↓

Escalation Required

```



---



## 🌟 Advantages of the System



- Reduces dependence on manual waste identification

- Automates initial complaint creation

- Provides structured complaint information

- Supports severity-based prioritization

- Enables complaint status tracking

- Provides a foundation for data-driven civic monitoring

- Integrates AI with a practical civic application



---



## 🔮 Future Scope



The system can be extended with:



- 📡 Real-time CCTV integration

- 📍 Live GPS-based location detection

- 📱 Mobile application support

- 🔔 SMS and email notifications

- ☁️ Cloud deployment

- 🧠 Improved AI detection models

- 📊 Advanced analytics dashboards

- 🏛️ Integration with municipal systems

- 🔐 User authentication and role-based access

- 🌐 Large-scale deployment across multiple locations





---



## ⭐ Project Highlights



- 🤖 Artificial Intelligence

- 👁️ Computer Vision

- 🎯 YOLO Object Detection

- ⚡ FastAPI Backend

- 📝 Automated Complaint Generation

- 📍 Location Identification

- 🚨 Severity-Based Escalation

- 📊 Data Analysis

- 🗺️ Interactive Map



---



## 📜 License



This project was developed as an academic project for educational and demonstration purposes.



---



## 📧 Contact

**Maintainer:** Pamujula Kavya Sre

**GitHub:** [pamujulakavyasreofficial](https://github.com/pamujulakavyasreofficial)

**Email:** pamujulakavyasreofficial@gmail.com

**Project Repository:** [Smart Civic Action System](https://github.com/pamujulakavyasreofficial/Smart-Civic-Action-System)



---


<p align="center">

&#x20; <b>🌍 Smart Technology for Cleaner Communities</b>

</p>



<p align="center">

&#x20; Built with Python • FastAPI • YOLO • Computer Vision

</p>

