class Saya:
    
    def __init__(self, nama, nim, kelas, sks, presensi):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
        self.presensi = presensi
    
    def Name(self):
        print("Nama  : ", self.nama)
    def NIM(self):
        print("NIM   : ", self.nim)
    def Kelas(self):
        print("Kelas : ", self.kelas)
    def jumlah_sks(self):
        print("Jumlah SKS : ", self.sks)
    def Kehadiran(self):
        print("Presensi   : ", self.presensi)

N = Saya("Novia Eka Putri", 121140030, "RB", 22, "Hadir")
N.Name()
N.NIM()
N.Kelas()
N.jumlah_sks()
N.Kehadiran()