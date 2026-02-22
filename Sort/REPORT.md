# BÁO CÁO KẾT QUẢ THỬ NGHIỆM
### Sinh viên thực hiện: Lê Nhựt Trí
### MSSV: 25521904
### Lớp: IT003.Q21.CTTN

#### I.	Kết quả thử nghiệm
   1.	Bảng dữ liệu thời gian thực thi
<div align="center">

## Kết quả đo thời gian thực thi (ms)

| Bộ dữ liệu | Quicksort | Heapsort | Mergesort | PythonSort |
|--------:|----------:|---------:|----------:|-------------:|
| data1.txt  | 3078.456  | 19473.805 | 6945.784 | 37.770 |
| data2.txt  | 3102.832 | 16404.543 | 7261.820 | 26.218 |
| data3.txt  | 5556.329 | 17004.363 | 11864.841 | 13.892 |
| data4.txt  | 5476.895 | 17779.264 | 11829.100 | 15.350 |
| data5.txt  | 5926.655 | 17368.245| 11135.504 | 15.076 |
| data6.txt  | 5397.915 | 52556.743 | 30277.798 | 17.657 |
| data7.txt  | 13253.769 | 33349.404 | 19295.978 | 50.030|
| data8.txt  | 9047.313 | 31492.39| 22408.572 | 25.735 |
| data9.txt | 8598.433 | 22763.799 | 15453.320 | 16.724 |
| data10.txt  | 5496.110  | 17441.999 | 13701.595  | 26.218 |
</div>

2. Biểu đồ thời gian thực thi
   
   <img width="1400" height="800" alt="image" src="https://github.com/user-attachments/assets/52d7d089-8e42-4aa3-a794-dc1c326cc214" />

#### II.	Kết luận:
Theo kết quả thử nghiệm có thể thấy:
- Hiệu năng vượt trội: PythonSort (Timsort) nhanh hơn các thuật toán tự cài đặt từ 100 - 1000 lần, khẳng định ưu thế tuyệt đối của các hàm thư viện đã được tối ưu hóa ở cấp độ hệ thống.
- Trong các thuật toán cài đặc thủ công, hiệu năng hay tốc độ giảm dần theo thứ tự: **Quicksort > Mergesort > Heapsort**.
- Về độ ổn định thì Quicksort hoạt động ổn định nhất trên các bộ dữ liệu thử nghiệm, trong khi Heapsort và Mergesort bị chậm đáng kể ở các tệp dữ liệu đặc biệt (như data6.txt).

