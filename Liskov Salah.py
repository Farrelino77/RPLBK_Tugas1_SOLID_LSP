# Bagas Farrelino Harsono Putro 21120122140101
class Pengguna:
    def __init__(self, nama):
        self.nama = nama

    def hitung_diskon(self):
        return 0  # Default pengguna tidak dapat diskon

class PenggunaPremium(Pengguna):
    def hitung_diskon(self):
        return 20  # Diskon 20% untuk pengguna premium

class PenggunaVIP(Pengguna):
    def hitung_diskon(self):
        raise NotImplementedError("Pengguna VIP harus menggunakan metode lain untuk diskon.")  # Tidak menghormati kontrak


def cetak_diskon(pengguna):
    print(f"Pengguna {pengguna.nama} mendapatkan diskon sebesar {pengguna.hitung_diskon()}%.")


# Pengguna Reguler
pengguna1 = Pengguna("Bagas")
cetak_diskon(pengguna1)

# Pengguna Premium
pengguna2 = PenggunaPremium("Farrelino")
cetak_diskon(pengguna2)

# Pengguna VIP, akan menyebabkan error
pengguna3 = PenggunaVIP("Harsono Putro")
cetak_diskon(pengguna3)  # Ini akan menyebabkan NotImplementedError
