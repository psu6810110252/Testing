# Software Testing Project (การบ้านวิชาเทสติ้ง)

สวัสดีครับทุกคน! Repo นี้เป็นการบ้านวิชา Software Testing ที่ผมทำไว้ส่งอาจารย์ครับ
หลักๆ คือแยก Production Code ออกจาก Test Code ให้ชัดเจน เขียนเทสให้ครอบคลุม และมีการทำ Stub ตามโจทย์พิเศษครับ

## 📁 โค้ดในนี้มีอะไรบ้าง? แบ่งโฟลเดอร์ยังไง?

ผมแบ่งโปรเจกต์ออกเป็น 3 โฟลเดอร์หลักๆ ตามนี้เลยครับ:

1. **`coe_number/`** -> อันนี้ฟังก์ชันโจทย์แรกเรื่องหาจำนวนเฉพาะ (แก้บั๊ก/Defect จากสไลด์ให้แล้วด้วยนะ)
2. **`hackerrank/`** -> อันนี้เป็นฟังก์ชันสำหรับแก้โจทย์ HackerRank ทั้ง 5 ข้อ 
3. **`tests/`** -> ส่วนสำคัญที่สุด! แหล่งรวมรวมไฟล์ Unit Test ของทุกข้อเลย

## 🎯 ไฮไลท์ของงานนี้

* **แก้โค้ดบั๊กจากสไลด์แล้ว:** ไฟล์ `number_utils.py` แก้ให้ไม่รับ 0, 1 หรือเลขติดลบหลุดไปเป็นจำนวนเฉพาะแล้ว
* **🌟 มีการทำ Stub (ตามล่าคะแนนพิเศษ):** ดูตัวอย่างได้ที่ไฟล์ `tests/test_stub_example.py` ผมใช้ `@patch` จำลองการดึง API ตัวเลขมาเทสครับ ทำตามคอนเซ็ปต์เป๊ะๆ!
* **โจทย์ HackerRank จัดเต็ม:** เขียนเทสให้ทุกข้อ (Funny String, Alternating Characters, Caesar Cipher, Two Characters, Grid Challenge) รันผ่านหมดแน่นอน

## � รันเทสยังไง?

ใครอยากลองรันดูในเครื่องตัวเอง เปิด VSCode Terminal (หรือพิมพ์ใน CMD) โฟลเดอร์โปรเจกต์นี้ แล้วลองก๊อปคำสั่งนี้ไปรันได้เลยครับ

**ถ้าอยากรันดูผลลัพธ์ทั้งหมดทีเดียว (สแกนเทสทุกข้อ):**
```bash
py -m unittest discover -s tests -p "test_*.py"
```

**ถ้าอยากรันทดสอบแค่บางข้อล่ะ?**
รันเฉพาะข้อหาจำนวนเฉพาะ กับส่วนของคะแนนพิเศษ (Stub)
```bash
py -m unittest -v tests/test_number_utils.py tests/test_stub_example.py
```

รันโจทย์ HackerRank แค่ข้อ Funny String
```bash
py -m unittest -v tests/test_funny_string.py
```

รันโจทย์ HackerRank แค่ข้อ Caesar Cipher
```bash
py -m unittest -v tests/test_caesar_cipher.py
```

**หมายเหตุ:** ตอนนี้รันผ่านครบ 22 เคสแล้ว (Ran 22 tests in ...s OK) พร้อมส่งครับ!
