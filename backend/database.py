from pymongo import MongoClient
import certifi

# mongo db  connection string
MONGO_URI = "mongodb+srv://admin:subash2007@cluster1.okrfsyf.mongodb.net/?appName=cluster1"

try:
    client = MongoClient(
        MONGO_URI,
        tls=True,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=5000
    )

    # Force connection test
    client.admin.command("ping")

    db = client["face_attendance"]
    employees = db["employees"]
    attendance = db["attendance"]

    employees.create_index("emp_id", unique=True)
    attendance.create_index([("emp_id", 1), ("date", 1)])

    print("MongoDB Connected Successfully ✅")

except Exception as e:
    print("MongoDB Connection Failed ❌")
    print(e)

    # Prevent import crash
    employees = None
    attendance = None