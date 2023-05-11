if __name__ == '__main__':
    x = 485
    tahun = x//360
    sisahari = x%360
    bulan = sisahari//30
    sisahari1 = sisahari%30
    minggu = sisahari1//7
    sisahari2 = sisahari1%7
    print(f"{x} hari = {tahun} tahun {bulan} bulan {minggu} minggu {sisahari2} hari")