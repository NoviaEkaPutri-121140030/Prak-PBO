class Mobil:
    def __init__(self, merk, tahun_produksi, warna, jumlah_roda, kecepatan):
        self.__merk = merk                      #Atribut private
        self.__tahun_produksi = tahun_produksi
        self._warna = warna                     #Atribut protected
        self.jumlah_roda = jumlah_roda          #Atribut public
        self.kecepatan = kecepatan

    def ubah_kecepatan(self, kecepatan_baru):   #Fungsi public untuk mengubah nilai dari atribut "kecepatan"
        self.kecepatan = kecepatan_baru

    def tampil_data(self):                      #Fungsi protected untuk menampilkan data mobil yang dapat diakses oleh objek turunan
        print("Merk:", self.__merk)
        print("Tahun Produksi:", self.__tahun_produksi)
        print("Warna:", self._warna)
        print("Jumlah Roda:", self.jumlah_roda)
        print("Kecepatan:", self.kecepatan)

class MobilSport(Mobil):
    def __init__(self, merk, tahun_produksi, warna, kecepatan):
        super().__init__(merk, tahun_produksi, warna, 4, kecepatan)

mobil1 = Mobil("Honda Jazz", 2021, "Putih", 4, 0)
mobil2 = Mobil("Toyota Avanza", 2019, "Hitam", 4, 50)
mobil3 = MobilSport("Lamborghini Aventador", 2020, "Kuning", 300)

#mengubah kecepatan mobil2
mobil2.ubah_kecepatan(80)

#menampilkan data mobil1
print("Data Mobil 1")
mobil1.tampil_data()

#menampilkan data mobil2
print("Data Mobil 2")
mobil2.tampil_data()

#menampilkan data mobil3
print("Data Mobil 3")
mobil3.tampil_data()
