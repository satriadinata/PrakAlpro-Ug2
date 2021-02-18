# Satriadinata Ratnanto
# Universitas Kristen Duta Wacana

# ada sebuah perusahaan mebel, mereka kesulitan dalam mengatur keuangan mereka

# Hasil Jual
# Modal
# jumlah tukang

# Laba Kotor
# Gaji Tukang 70% dari laba kotor dibagikan jumlah karyawan
# Pajak 10% dari laba kotor
# Laba bersih

hasilJual = int(input('Hasil jual : '))
modal = int(input('Modal : '))
jumlahTukang = int(input('Jumlah Tukang : '))

labaKotor = hasilJual - modal
gaji = 0.7 * labaKotor
gaji2 = gaji / jumlahTukang
pajak = 0.1 * labaKotor
labaBersih = labaKotor - gaji - pajak
print('Laba kotor = Rp', labaKotor)
print('Pajak = Rp', pajak)
print('Gaji masing-masing karyawan = Rp', gaji2)