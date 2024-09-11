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
        return 30  # Diskon 30% untuk pengguna VIP


def cetak_diskon(pengguna):
    print(f"Pengguna {pengguna.nama} mendapatkan diskon sebesar {pengguna.hitung_diskon()}%.")


# Pengguna Reguler
pengguna1 = Pengguna("Bagas")
cetak_diskon(pengguna1)

# Pengguna Premium
pengguna2 = PenggunaPremium("Farrelino")
cetak_diskon(pengguna2)

# Pengguna VIP, sekarang tidak menyebabkan error
pengguna3 = PenggunaVIP("Harsono Putro")
cetak_diskon(pengguna3)
