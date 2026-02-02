import random
import os

def sinh(folder="data", n=1_000_000):
    # Tạo folder nếu chưa tồn tại
    os.makedirs(folder, exist_ok=True)

    idx = 1  # đánh số file

    #Tạo dãy số nguyên tăng dần
    x = sorted(random.randint(0, 1_000_000) for _ in range(n))
    with open(f"{folder}/data{idx}.txt", "w") as f:
        f.write(" ".join(map(str, x)))
    del x
    idx += 1

    #Tạo dãy số nguyên giảm dần
    x = sorted((random.randint(0, 1_000_000) for _ in range(n)), reverse=True)
    with open(f"{folder}/data{idx}.txt", "w") as f:
        f.write(" ".join(map(str, x)))
    del x
    idx += 1

    #Tạo thêm 3 dãy số nguyên ngẫu nhiên
    for _ in range(3):
        x = [random.randint(0, 1_000_000) for _ in range(n)]
        with open(f"{folder}/data{idx}.txt", "w") as f:
            f.write(" ".join(map(str, x)))
        del x
        idx += 1

    #Tạo 5 dãy số thực ngẫu nhiên
    for _ in range(5):
        x = [random.uniform(0, 1_000_000) for _ in range(n)]
        with open(f"{folder}/data{idx}.txt", "w") as f:
            f.write(" ".join(map(str, x)))
        del x
        idx += 1

if __name__ == "__main__":
    sinh()
