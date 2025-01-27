def twos_complement_to_integer():
    """
    รายชื่อกลุ่ม : 
    1.กันต์ธร ศิริเจริญวัฒน์ 1650706474
    2.พรปวีณ์ จิรกุลธนินโชตน์ รหัสนักศึกษา 1650708710
    3.อนันต์ มิ่งมิตรพัฒนะกุล 1660706688

    แปลง binary string ในรูปแบบ Two's Complement เป็นจำนวนเต็ม

    Workflow:
        1. รับ binary string และจำนวนไบต์จากผู้ใช้
        2. ตรวจสอบว่าจำนวนไบต์มีค่าเป็น 1, 2, หรือ 4
        3. ตรวจสอบว่า binary string มีเฉพาะ 0 และ 1
        4. ตรวจสอบว่าความยาวของ binary string ตรงกับจำนวนบิตที่ระบุ
        5. แปลงค่า binary string เป็นจำนวนเต็ม:
            - กรณีเลขบวก (Bit ตัวแรก = 0): แปลงตรงๆ
            - กรณีเลขลบ (Bit ตัวแรก = 1): ใช้กฎ Two's Complement
        6. แสดงผลลัพธ์

    Test Cases:

    1. เลขบวก:
        Input:
            Enter a binary number: 00001111
            Enter the number of bytes: 1
        Output:
            15

    2. เลขติดลบ:
        Input:
            Enter a binary number: 11110000
            Enter the number of bytes: 1
        Output:
            -16


    3. กรณีข้อผิดพลาด (จำนวนบิตไม่ตรงกับจำนวนไบต์):
        Input:
            Enter a binary number: 101010
            Enter the number of bytes: 1
        Output:
            Invalid number of bits. Expected 8 bits.


    4. กรณีตัวอักษร (ไม่ใช่เลขฐานสอง):
        Input:
            Enter a binary number: 11010AB
            Enter the number of bytes: 1
        Output:
            Please enter a valid binary number (only 0 and 1)
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
