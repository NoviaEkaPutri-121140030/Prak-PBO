class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        super().__init__(nama, jenis, harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor
        
class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity):
        super().__init__(nama, jenis, harga, merk)
        self.capacity = capacity

class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity, rpm):
        super().__init__(nama, jenis, harga, merk)
        self.capacity = capacity
        self.rpm = rpm

class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity):
        super().__init__(nama, jenis, harga, merk)
        self.capacity = capacity

class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya):
        super().__init__(nama, jenis, harga, merk)
        self.daya = daya

p1 = Processor('Intel','Core i7 7740X',4350000,'Intel',4,'4.3GHz')
p2 = Processor('AMD','Ryzen 5 3600',250000,'AMD',4,'4.3GHz')
ram1 = RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'V-Gen','4GB')
ram2 = RAM('G.SKILL','DDR4 2400MHz',328000,'G.SKILL','4GB')
hdd1 = HDD('Seagate','HDD 2.5 inch',295000,'Seagate','500GB',7200)
hdd2 = HDD('Seagate','HDD 2.5 inch',295000,'Seagate','1000GB',7200)
vga1 = VGA('Asus','VGA GTX 1050',250000,'Asus','2GB')
vga2 = VGA('Asus','1060Ti',250000,'Asus','8GB')
psu1 = PSU('Corsair','Corsair V550',250000,'Corsair','500W')
psu2 = PSU('Corsair','Corsair V550',250000,'Corsair','500W')

rakit = [[p1, ram1, hdd1, vga1, psu1], [p2, ram2, hdd2, vga2, psu2]]

for i, komputer in enumerate(rakit):
    print(f'Komputer {i+1}')
    for j in komputer:
        print(f'{type(j).__name__} {j.jenis} produksi {j.merk}')
    print()