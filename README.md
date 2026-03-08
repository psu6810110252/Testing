# Software Testing Project

โปรเจกต์นี้เป็นการจำลองการเขียนชุดทดสอบ (Unit Testing) สำหรับโค้ดที่ได้รับมอบหมาย โดยได้ทำการแยกโครงสร้างระหว่าง **Production Code** และ **Test Code** จัดเจนตามหลักการทำ Software Testing  

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

โปรเจกต์แบ่งออกเป็น 3 โฟลเดอร์หลักสำหรับแยกหมวดหมู่การทำงาน:

```plaintext
my_testing_project/
│
├── coe_number/             # โฟลเดอร์สำหรับ Production Code (ตอนโจทย์ COE)
│   ├── __init__.py         # (Empty file) ให้ Python มองเป็น Module
│   └── number_utils.py     # โค้ดเช็ค List ของจำนวนเฉพาะ (แก้ไข Defect แล้ว)
│
├── hackerrank/             # โฟลเดอร์สำหรับ Production Code (โจทย์ HackerRank 5 ข้อ)
│   ├── __init__.py 
│   ├── alternating_characters.py 
│   ├── caesar_cipher.py    
│   ├── funny_string.py     
│   ├── grid_challenge.py   
│   └── two_characters.py   
│
└── tests/                  # โฟลเดอร์สำหรับรวบรวม Test Code ทั้งหมด
    ├── __init__.py
    ├── test_number_utils.py          # Test case สำหรับ coe_number/number_utils.py
    ├── test_stub_example.py          # (คะแนนพิเศษ 🌟) ตัวอย่างการทำ Stub ด้วย @patch
    ├── test_alternating_characters.py# Test case โจทย์ Alternating Characters
    ├── test_caesar_cipher.py         # Test case โจทย์ Caesar Cipher
    ├── test_funny_string.py          # Test case โจทย์ Funny String
    ├── test_grid_challenge.py        # Test case โจทย์ Grid Challenge
    └── test_two_characters.py        # Test case โจทย์ Two Characters
```

---

## 🚀 ฟีเจอร์และการแก้ไขที่ทำ (What's Included)

* **แก้โค้ดบั๊กจากสไลด์แล้ว:** ไฟล์ `number_utils.py` แก้ให้รองรับ Edge Cases โดยไม่ให้เลข 0, 1 หรือเลขติดลบหลุดไปเป็นจำนวนเฉพาะแล้ว
* **🌟 มีการทำ Stub (ตามล่าคะแนนพิเศษ):** ดูตัวอย่างได้ที่ไฟล์ `tests/test_stub_example.py` ผมใช้ `@patch` จำลองการดึง API ตัวเลขมาเทส
* **โจทย์ HackerRank จัดเต็ม:** เขียนเทสให้ทุกข้อ (Funny String, Alternating Characters, Caesar Cipher, Two Characters, Grid Challenge) รันผ่านหมดแน่นอน

## รันเทส

ใครอยากลองรันดูในเครื่องตัวเอง เปิด VSCode Terminal (หรือพิมพ์ใน CMD) โฟลเดอร์โปรเจกต์นี้ แล้วลองก๊อปคำสั่งนี้ไปรันได้เลย

**ถ้าอยากรันดูผลลัพธ์ทั้งหมดทีเดียว (สแกนเทสทุกข้อ):**
```bash
py -m unittest discover -s tests -p "test_*.py"
```

### คำสั่งสำหรับเลือกรันเทสเฉพาะหมวดที่ต้องการ:
**1. รันเฉพาะโจทย์เรื่อง จำนวนเฉพาะ (Prime) และการจำลอง (Stub):**
```bash
py -m unittest -v tests/test_number_utils.py tests/test_stub_example.py
```

**2. รันเฉพาะโจทย์ HackerRank แต่ละข้อ:**
```bash
# ตัวอย่าง: รันเฉพาะคำสั่ง Funny String 
py -m unittest -v tests/test_funny_string.py
```

รันโจทย์ HackerRank แค่ข้อ Caesar Cipher
```bash
py -m unittest -v tests/test_caesar_cipher.py
```

📝 **หมายเหตุ:** เทสเคสทั้งหมดรวม 22 เคสทำงานผ่าน `OK` ทั้งหมด (100% Code Coverage & Passing Tests)
