from requests import get
import csv
import pandas as pd

# เรียก API เพื่อดึงข้อมูลสายพันธุ์สุนัขทั้งหมด
api_url = "https://dog.ceo/api/breeds/list/all"
response = get(api_url)
data = response.json()

# สร้าง list เพื่อเก็บข้อมูลสายพันธุ์หลักและย่อย
breed_data = []
# กำหนดตัววิ่งรับค่า Key , Value เพื่อไปเก็บใน breed_data เพื่อให้ได้ List ที่เก็บค่าเป็น tuple
# ใน tuple จะเก็บ main_breeds เป็น string และเก็บ sub_breeds เป็น list
for main_breed, sub_breeds in data['message'].items():
    breed_data.append((main_breed, sub_breeds))

# กำหนดชื่อไฟล์ CSV
csv_filename = "dog_breeds.csv"

# เขียนข้อมูลลงในไฟล์ CSV
with open(csv_filename, 'w', newline='') as csvfile:
    # กำหนดชื่อ columns
    fieldnames = ['Main_breeds', 'Sub_breeds']
    writer = csv.writer(csvfile)
    # เขียน header ของ colums
    writer.writerow(fieldnames)
    # ใช้ loop เพื่อใส่ค่าแต่ละ rows
    for main_breed, sub_breeds in breed_data:
        # ถ้าไม่มีสายพันธุ์ย่อย ให้ใส่ค่าว่าง
        if not sub_breeds:
            sub_breeds = ['']
        for sub_breed in sub_breeds:
            writer.writerow([main_breed, sub_breed])

print("ไฟล์ CSV ถูกสร้างเรียบร้อยแล้ว: ", csv_filename)

# ใช้ pandas เพื่อสร้าง column ที่บอกชื่อเต็มของสายพันธุ์นั้น
df = pd.read_csv("dog_breeds.csv")
df["Full_breeds_name"] = df["Sub_breeds"] + " " + df["Main_breeds"]
df.to_csv('dog_breeds.csv', index=False)