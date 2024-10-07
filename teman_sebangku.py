jumlah_siswa, baris, kolom = map(int, input().split())
denah_kelas = {}

for _ in range(jumlah_siswa):
    nomor_absen, posisi_x, posisi_y = map(int, input().split())
    denah_kelas[(posisi_x, posisi_y)] = nomor_absen

for nomor_urut in range(1, jumlah_siswa + 1):
    teman_ditemukan = False
    for koordinat, siswa in denah_kelas.items():
        if siswa == nomor_urut:
            x, y = koordinat
            if (x, y - 1) in denah_kelas:
                print(denah_kelas[(x, y - 1)])
                teman_ditemukan = True
            elif (x, y + 1) in denah_kelas:
                print(denah_kelas[(x, y + 1)])
                teman_ditemukan = True
            break
    
    if not teman_ditemukan:
        print(0)