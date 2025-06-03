# 🎓 Invigilation Management System

A smart and interactive Streamlit web application to automatically assign faculty as invigilators for college exams based on their availability and load balancing.

---

## 🚀 Features

- ✅ Upload teacher and exam timetables in Excel format
- ✅ Automatically detects faculty availability based on slot schedule
- ✅ Assigns invigilators based on least invigilation count
- ✅ Dynamic selection of number of invigilators per exam
- ✅ Prevents same faculty from multiple assignments in a day
- ✅ Stores and updates data using a local SQLite database
- ✅ Download final assignment summary in Excel format
- ✅ Reset database to start fresh for a new semester
- ✅ Fully interactive, intuitive UI built with Streamlit

---

## 📁 File Structure

📦IMS/
┣ 📄app.py # Main Streamlit application
┣ 📄faculty.db # SQLite database storing faculty and assignment info
┣ 📄requirements.txt # All required Python libraries
┣ 📄README.md # Project documentation
┣ 📁/sample_timetables/ # (Optional) example Excel files


---

## 🧾 Excel Format Requirements

### 🔹 Teacher Timetable:
- Rows: Faculty names
- Columns: Day-wise and slot-wise schedule
- Empty slots are considered **available**

### 🔹 Exam Timetable:
| Column    | Description                                |
|-----------|--------------------------------------------|
| `Date`    | Exam date (YYYY-MM-DD or DD-MM-YYYY)       |
| `Day`     | Weekday (e.g., MON, TUE, WED)              |
| `Session` | FN (morning) or AN (afternoon) for Mid exams |
| `Subject` | Exam/course name                           |
| `Slots`   | Comma-separated slot numbers (I, II, III...) |

### 🔸 Slot Mapping

| Slot | Time               |
|------|--------------------|
| I    | 09:00 AM – 10:00 AM |
| II   | 10:00 AM – 11:00 AM |
| III  | 11:10 AM – 12:10 PM |
| IV   | 12:10 PM – 01:10 PM |
| V    | 12:55 PM – 01:55 PM |
| VI   | 01:55 PM – 02:55 PM |
| VII  | 02:55 PM – 03:45 PM |

---

## 🛠 Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/RajanRoshini31/Invigilator-Management-System
   cd Invigilator-Management-System
 Install Dependencies -pip install -r requirements.txt
To run the app -streamlit run app.py

