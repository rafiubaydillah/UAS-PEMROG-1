class Proses:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def input_hewan(self):
        try:
            nama = input("Masukkan nama hewan: ")
            jenis = input("Masukkan jenis hewan: ")
            umur = int(input("Masukkan umur hewan (dalam tahun): "))

            if umur < 0:
                raise ValueError("Umur tidak boleh negatif.")

            self.data.tambah_hewan(nama, jenis, umur)
            print("Hewan berhasil ditambahkan.")
        except ValueError as e:
            print(f"Input tidak valid: {e}")

    def tampilkan_data(self):
        hewan_list = self.data.get_hewan()
        if not hewan_list:
            print("Tidak ada data hewan.")
        else:
            self.view.tampilkan_tabel(hewan_list)