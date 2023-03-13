class AkunBank:
    listPelanggan = 0
    
    def __init__(self, nopel, nama, saldo):
        self.__nopel = nopel
        self.__nama = nama
        self.__saldo = saldo
        AkunBank.listPelanggan += 1
        
    def cek_saldo():
        print(f"{Akun1.__nama} memiliki saldo Rp {Akun1.__saldo}")
        
    def tarik_tunai():
        while True:
            nominal = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
            if nominal > Akun1.__saldo:
                print("Nominal saldo yang Anda punya tidak cukup!")
            else:
                Akun1.__saldo -= nominal
                print("Saldo berhasil ditarik!")
        
    def transfer():
        nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
        norek_tujuan = int(input("Masukkan no rekening tujuan: "))
        
        # for pelanggan in self.listPelanggan:
        if Akun2.__nopel == norek_tujuan:
            Akun3.__saldo += nominal
            Akun1.__saldo -= nominal
            print(f"Transfer Rp.{nominal} ke {Akun2.__nama} sukses!")
        elif Akun3.__nopel == norek_tujuan:
            Akun3.__saldo += nominal
            Akun1.__saldo -= nominal
            print(f"Transfer Rp.{nominal} ke {Akun3.__nama} sukses!")
        else:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama.")
        
    def lihatMenu():
        print("Selamat datang di Bank Jago")
        print(f"Halo {Akun1.__nama}, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        n = int(input("Masukan nomor input : "))

        print()
        if n == 1:
            AkunBank.cek_saldo()
        elif n == 2:
            AkunBank.tarik_tunai()
        elif n == 3:
            AkunBank.transfer()
        elif n == 4:
            exit(0)
 
        print()
        print()
        AkunBank.lihatMenu()

Akun1 = AkunBank(1234, "Novia Eka Putri", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

AkunBank.lihatMenu()