♟️ 42 Chess Engine & Web Analyzer
"จากพื้นฐาน List/Array สู่ระบบ AI หมากรุกที่เอาชนะคนได้จริง"
โปรเจกต์นี้เป็นส่วนหนึ่งของการเรียนรู้ในหลักสูตร Piscine Python @42Bangkok โดยเริ่มตั้งแต่การปูพื้นฐาน Logic การจัดการข้อมูล จนพัฒนาออกมาเป็นระบบหมากรุกที่มีความซับซ้อน ทั้งในแง่ของอัลกอริทึมและการเชื่อมต่อผ่าน Web API

(วิธีใส่รูป: นำรูปสกรีนช็อตไปวางในโฟลเดอร์เดียวกับ README แล้วเปลี่ยนชื่อไฟล์ในวงเล็บข้างบนครับ)

🚀 สิ่งที่ได้เรียนรู้จาก 42 Bangkok
การทำโปรเจกต์นี้ไม่ใช่แค่การเขียนโปรแกรมให้ทำงานได้ แต่คือการเข้าใจโครงสร้างของภาษา Python อย่างลึกซึ้ง:

Data Structures: การนำ List และ Array มาประยุกต์ใช้จัดการตารางหมากรุกแบบ 2 มิติ

Algorithm Thinking: การเขียน Logic เพื่อคำนวณการเดินที่ถูกต้องตามกฎสากล

Teamwork: การทำงานร่วมกันในสภาพแวดล้อมที่กดดัน การแบ่งหน้าที่ และการแก้ปัญหา Logic ร่วมกับเพื่อนในทีม

Scalability: การออกแบบ Code ให้รองรับกระดานขนาดเท่าไหร่ก็ได้ (Custom Size) ไม่จำกัดแค่ 8x8

✨ Key Features (ฟีเจอร์เด่น)
🧠 Intelligent Chess Engine (AI)
ระบบไม่ได้แค่สุ่มเดิน แต่มี "สมอง" ในการคิด:

Minimax Algorithm: ระบบพยากรณ์การเดินล่วงหน้าเพื่อหาทางที่ดีที่สุด

Alpha-Beta Pruning: การตัดกิ่งก้านของ Logic ที่ไม่จำเป็นออก เพื่อให้ AI คำนวณได้รวดเร็วและลึกขึ้น

Best Move Finder: ระบบแนะนำตาเดินที่ดีที่สุดในสถานการณ์นั้นๆ

Human vs AI: AI ตัวนี้สามารถเล่นกับมนุษย์และเอาชนะผู้เล่นได้จริงด้วยการคำนวณที่แม่นยำ

🔍 Checkmate & Logic Detection
ระบบตรวจหาการ Checkmate และการถูกรุก (Check) อย่างละเอียด

รองรับกระดานหลายขนาด (NxN) โดยที่ Logic ยังทำงานได้ถูกต้อง

🌐 Full-stack Web Integration
สร้าง UI ด้วย HTML/Tailwind CSS ที่สวยงามและใช้งานง่าย

เชื่อมต่อ Frontend กับ Python ผ่าน API เพื่อประมวลผล Logic หนักๆ ที่ฝั่ง Server

🛠️ Tech Stack
Language: Python 3.x

Engine: python-chess (for move validation & board state)

Frontend: HTML5, Tailwind CSS, JavaScript

Algorithm: Minimax, Alpha-Beta Pruning