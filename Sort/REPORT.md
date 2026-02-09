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
   <img width="1281" height="462" alt="image" src="https://github.com/user-attachments/assets/a7a20665-d638-4cef-8789-ceff7b39fed1" />

#### II.	Kết luận:
Theo kết quả thử nghiệm có thể thấy:
-	PythonSort luôn cho thời gian thực thi nhanh nhất trên tất cả các bộ dữ liệu (chỉ từ khoảng 20–240 ms), vượt trội so với ba thuật toán còn lại. Điều này cho thấy thuật toán sắp xếp có sẵn trong Python được tối ưu rất tốt.
-	Trong ba thuật toán tự cài đặt, QuickSort có hiệu năng tốt nhất, với thời gian trung bình khoảng 700–1900 ms. MergeSort đứng thứ hai, chậm hơn QuickSort nhưng ổn định hơn HeapSort. HeapSort là thuật toán chậm nhất, với thời gian thường trên 3000–5500 ms.
-	Nhìn chung, thứ tự hiệu năng từ nhanh đến chậm là: **PythonSort → QuickSort → MergeSort → HeapSort**.

