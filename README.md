# 🚆 Sarva – Wheel Specification API

This project is developed for **Sarva Company** as part of a backend assignment to build a RESTful API using Django and PostgreSQL. The API allows engineers to **submit** and **retrieve** wheel specification form data in a structured format.

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 5.x
- Django REST Framework
- PostgreSQL
- Postman (for testing)

---

## 📌 Features

- ✅ Submit Wheel Specification form (POST API)
- ✅ Retrieve filtered Wheel Specification data (GET API)
- ✅ PostgreSQL database integration
- ✅ Customized JSON responses
- ✅ DRF serializers for data validation
- ✅ Swagger (Browsable API view) support

---

## 📁 API Endpoints

### ✅ 1. Submit Wheel Specification

**URL:** `http://localhost:8000/api/forms/wheel-specifications/`  
**Method:** `POST`  
**Content-Type:** `application/json`  

#### 🔸 Sample Request (POST Body):
```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
  "bearingSeatDiameter": "130.043 TO 130.068",
  "condemningDia": "825 (800-900)",
  "intermediateWWP": "20 TO 28",
  "lastShopIssueSize": "837 (800-900)",
  "rollerBearingBoreDia": "130 (+0.0/-0.025)",
  "rollerBearingOuterDia": "280 (+0.0/-0.035)",
  "rollerBearingWidth": "93 (+0/-0.250)",
  "treadDiameterNew": "915 (900-1000)",
  "variationSameAxle": "0.5",
  "variationSameBogie": "5",
  "variationSameCoach": "13",
  "wheelDiscWidth": "127 (+4/-0)",
  "wheelGauge": "1600 (+2,-1)",
  "wheelProfile": "29.4 Flange Thickness"
}

 Expected Response:
{
  "data": {
    "formNumber": "WHEEL-2025-001",
    "status": "Saved",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03"
  },
  "message": "Wheel specification submitted successfully.",
  "success": true
}

 2. Retrieve Wheel Specification Data
URL: http://localhost:8000/api/forms/wheel-specifications/list/
Method: GET

✅ Expected Response:
{
  "data": [
    {
      "fields": {
        "condemningDia": "825 (800-900)",
        "lastShopIssueSize": "837 (800-900)",
        "treadDiameterNew": "915 (900-1000)",
        "wheelGauge": "1600 (+2,-1)"
      },
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03"
    }
  ],
  "message": "Filtered wheel specification forms fetched successfully.",
  "success": true
}

🚀 How to Run Locally
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/KishoreChatterjee/sarva-wheel-api.git
cd sarva-wheel-api
2. Create a virtual environment
bash
Copy
Edit
python -m venv env
env\Scripts\activate  # for Windows
# or
source env/bin/activate  # for macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure PostgreSQL Database
In settings.py, update:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Run migrations

python manage.py makemigrations
python manage.py migrate

6. Start development server

python manage.py runserver

📦 Postman Collection
A Postman collection is included (sarva.postman_collection.json) that contains:

✅ POST request to submit form data
✅ GET request to retrieve filtered fields
