if __name__ == '__main__':
    # A = 60x
    # B = 120-40x
    # x = waktu
    start = 9
    x = 1.2*60
    sisamenit = x%60
    jam = x//60
    print(f"(mobil A dan B bertemu pukul {start+jam} lebih {sisamenit} menit)")
    