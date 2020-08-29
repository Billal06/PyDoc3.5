lists = ["Indonesia", "Majalengka", 1945, 8, 17]
lists2 = ["Jawa", "Sumatra", "Sulawesi", "Kalimantan", "Papua"]

negara = lists[0]
kabupaten = lists[1]
tahun = lists[2]
bulan = lists[3]
tanggal = lists[4]

print (lists)
print (negara)
print (kabupaten)
print (tahun)
print (bulan)
print (tanggal)

# tambah list
lists.append("Jakarta")
print (lists)
ibu_kota = lists[5]
print (ibu_kota)

# Menggabungkan list
gabung = lists + lists2
print (gabung)

# Mengubah isi
lists[1] = "Subang"
print (lists)
