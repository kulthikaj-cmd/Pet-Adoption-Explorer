# เอกสารแผนงาน Sprint 1: Pet Adoption Explorer (Web Application)

## 1. ขอบเขตระบบใน Sprint 1 (System Scope)
- หน้า Web Dashboard หลักแสดงข้อความต้อนรับและเมนูสลับหน้าจอ (Sidebar Navigation)
- ฟอร์มค้นหาสัตว์เลี้ยง พร้อมระบบ Input Validation (ลบช่องว่างด้วย `.strip()` และแปลงเป็นตัวพิมพ์เล็กด้วย `.lower()`)
- การจัดวางโครงสร้างโมดูลาร์เบื้องต้นรองรับ 3-Layer Architecture

## 2. เงื่อนไขความเสร็จสมบูรณ์ (Definition of Done - DoD)
- [x] สร้าง Repository และไฟล์เอกสารวางแผนบน GitHub
- [ ] มีเมนู Sidebar สำหรับสลับหน้าจอหลัก
- [ ] มีช่องรับข้อมูลค้นหาที่ทำ Input Validation ป้องกันค่าว่าง
- [ ] โปรแกรมสามารถรันได้โดยไม่เกิด Exception Error

## 3. สมาชิกและการแบ่งบทบาท (Team Roles)
- **Planner / Team Leader:** วางสเปกงานและเขียนเอกสาร Sprint_1.md
- **Coder & Debugger:** เขียนโค้ดระบบ Presentation Layer (UI) และทดสอบ Input Validation
