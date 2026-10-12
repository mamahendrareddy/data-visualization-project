import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Rakesh", "Rahul", "Anu", "Priya", "Kiran",
        "Sneha", "Arjun", "Divya", "Manoj", "Keerthi"
    ],
    "Gender": [
        "Male", "Male", "Female", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],
    "Department": [
        "AI", "CSE", "AI", "CSE", "AI",
        "AI", "CSE", "CSE", "AI", "CSE"
    ],
    "Python": [85, 72, 91, 79, 68, 94, 80, 88, 76, 83],
    "Maths": [78, 81, 88, 85, 74, 92, 77, 90, 69, 86],
    "DBMS": [90, 76, 95, 82, 70, 96, 84, 89, 78, 85],
    "Statistics": [82, 75, 90, 87, 72, 93, 79, 91, 74, 88]
}

df = pd.DataFrame(data)

df.to_csv("student_data.csv", index=False)

print("Dataset created successfully!")
print(df)
print("\nDataset shape:", df.shape)