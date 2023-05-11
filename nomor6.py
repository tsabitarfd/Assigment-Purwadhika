if __name__ == '__main__':
    apel = int(input("masukkan jumlah apel "))
    jeruk = int(input("masukkan jumlah jeruk "))
    anggur = int(input("masukkan jumlah anggur "))
    totalapel = apel*10000
    totaljeruk = jeruk*15000
    totalanggur = anggur*20000
    totalbelanja = totalapel+totaljeruk+totalanggur
    print("detail belanja")
    print(f"apel: {apel}*10000 = {totalapel}")
    print(f"jeruk: {jeruk}*15000 = {totaljeruk}")
    print(f"anggur: {anggur}*20000 = {totalanggur}")
    print(f"(total belanja buah hari ini: {totalbelanja})")