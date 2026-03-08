# Software Testing Project

โปรเจกต์นี้เป็นการจำลองการเขียนชุดทดสอบ (Unit Testing) สำหรับโค้ดที่ได้รับมอบหมาย โดยได้ทำการแยกโครงสร้างระหว่าง **Production Code** และ **Test Code** จัดเจนตามหลักการทำ Software Testing ที่ดี โค้ดทั้งหมดเขียนด้วยภาษา Python และใช้ไลบรารีเบื้องต้น `unittest` รวมถึงมีการใช้งาน `unittest.mock` สำหรับการจำลองข้อมูล (Stubbing) 

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

1. **โอมิย Defect ໃນ `number_utils.py`:** ได้ปรับแก้โค้ดจากในสไลด์เรียนที่มีข้อผิดพลาด (เช่น เลข 0, 1 หรือเลขติดลบหลุดไปเป็นจำนวนเฉพาะ) โดยเพิ่มเช็ค Edge cases ให้ถูกต้องสมบูรณ์
2. **การทำ Stubbing (สำหรับคะแนนพิเศษ):** 
   - ใช้งาน `@patch` จาก `unittest.mock` ในไฟล์ `test_stub_example.py` 
   - จำลองการคืนค่ากลับของฟังก์ชัน `get_numbers_from_api()` เพื่อให้สามารถรัน Unit Test ได้โดยไม่ต้องพึ่งพาระบบภายนอกจริงๆ หรือรอข้อมูลจาก API
3. **แก้โจทย์ Algorithm ของ HackerRank ทั้ง 5 ข้อ:**
   - ได้เขียนชุดฟังก์ชันสำหรับแก้ปัญหาทั้ง 5 ข้อในโฟลเดอร์ `hackerrank/`
   - เขียน Unit tests กำกับความถูกต้องไว้ในโฟลเดอร์ `tests/` ครบทุกกรณี (Passing 100%)

---

## 🛠️ วิธีการรันเทส (How to Run Tests)

เปิด Terminal หรือ Command Prompt ขึ้นมา และเข้าไปยังโฟลเดอร์โปรเจกต์ `my_testing_project` จากนั้นรันคำสั่งด้านล่างนี้:

### รันเทสทั้งหมดในรวดเดียว (ค้นหาไฟล์ `test_*.py` อัตโนมัติ):
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
> สามารถเปลี่ยนชื่อไฟล์ตามข้ออื่นๆ เพื่อหาผลลัพธ์ย่อยได้ครับ

---

📝 **หมายเหตุ:** เทสเคสทั้งหมดรวม 22 เคสทำงานผ่าน `OK` ทั้งหมด (100% Code Coverage & Passing Tests)
