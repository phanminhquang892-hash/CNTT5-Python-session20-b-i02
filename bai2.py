"""
1. Giải thích lỗi IndexError: tuple index out of range
Dữ liệu:

    ("Levi", 120, 2500)
    ("SofM", 150)

Đối với Levi:
- Tuple có 3 phần tử.
- Các vị trí:
    p[0] = "Levi"
    p[1] = 120
    p[2] = 2500

=> Dòng:
    r = p[2]

truy cập hợp lệ nên chương trình chạy bình thường.

--------------------------------------------------

Đối với SofM:

    ("SofM", 150)

Tuple chỉ có 2 phần tử:

    p[0] = "SofM"
    p[1] = 150

Khi chương trình thực hiện:

    r = p[2]

Python cố truy cập phần tử thứ 3 nhưng không tồn tại.

Do đó phát sinh lỗi:

    IndexError: tuple index out of range

Ý nghĩa:
- Index = vị trí phần tử.
- Out of range = vượt quá phạm vi cho phép.


2. Nếu sửa dữ liệu của SofM thành:
Nguyên nhân:
- Hàm int() chỉ chuyển đổi được chuỗi chứa số.
- "N/A" là văn bản nên không thể ép kiểu.

3. Vai trò của lệnh Debug
Khi chương trình bị lỗi ngay sau dòng này, ta dễ dàng xác định
bản ghi SofM chính là dữ liệu gây crash.

4. Đánh giá tên biến theo Clean Code
Lợi ích:
- Dễ đọc.
- Dễ bảo trì.
- Tự mô tả ý nghĩa.
- Hạn chế nhầm lẫn khi làm việc nhóm.



"""
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]
def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)
def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        try:
            name = record[0]
            matches = record[1]
            mmr = record[2]
            mmr = int(mmr)
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
        except IndexError:
            name = record[0]
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
        except ValueError:
            name = record[0]
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

    print("--- HOÀN TẤT ---")
process_bonus(player_records)