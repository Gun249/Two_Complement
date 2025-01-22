def twos_complement_to_integer():
    """
    แปลง binary string ในรูปแบบ Two's Complement เป็นจำนวนเต็ม

    ฟังก์ชันนี้รับ binary string และจำนวนไบต์จากผู้ใช้
    แล้วแปลงค่า binary string ให้เป็นจำนวนเต็มตามกฎของ Two's Complement
    พร้อมทั้งจัดการกรณีข้อผิดพลาด เช่น binary string ไม่ถูกต้อง
    หรือจำนวนบิตไม่ตรงกับจำนวนไบต์ที่ระบุ

    Arguments:
        ไม่มี (รับอินพุตจากผู้ใช้โดยตรง)

    Workflow:
        1. รับ binary string และจำนวนไบต์จากผู้ใช้
        2. ตรวจสอบว่าจำนวนไบต์มีค่าเป็น 1, 2, หรือ 4
        3. ตรวจสอบว่า binary string มีเฉพาะ 0 และ 1
        4. ตรวจสอบว่าความยาวของ binary string ตรงกับจำนวนบิตที่ระบุ
        5. แปลงค่า binary string เป็นจำนวนเต็ม:
            - กรณีเลขบวก (Bit ตัวแรก = 0): แปลงตรงๆ
            - กรณีเลขลบ (Bit ตัวแรก = 1): ใช้กฎ Two's Complement
        6. แสดงผลลัพธ์

    Returns:
        ไม่มี (แสดงผลลัพธ์หรือข้อผิดพลาดบนหน้าจอ)
    """
    binary_input = input("Enter a binary number: ")
    bytes = int(input("Enter the number of bytes: "))
    if bytes in {1, 2, 4}:
        
        checkbyte = bytes * 8
        if set(binary_input) - {'0', '1'}:
            print("Please enter a valid binary number (only 0 and 1)")
            return
        else:
            if checkbyte == len(binary_input):
                checkfrist = binary_input[0]
                number = int(binary_input, 2)
                if checkfrist == "1":
                    number = number - 2**len(binary_input)
                print(number)

            else:
                print("Invalid number of bits. Expected", checkbyte, "bits.")
                return
    else:
        print("Invalid number of bytes. Must be 1, 2, or 4.")
        return

twos_complement_to_integer()