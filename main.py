class Data:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, nama, jenis, umur):
        hewan = {
            'nama': nama,
            'jenis': jenis,
            'umur': umur
        }
        self.hewan_list.append(hewan)

    def get_hewan(self):
        return self.hewan_list

class View:
    @staticmethod
    def tampilkan_tabel(hewan_list):
        print(f"{'No':<5} {'Nama':<15} {'Jenis':<15} {'Umur':<5}")
        print("=" * 45)
        for index, hewan in enumerate(hewan_list, start=1):
            print(f"{index:<5} {hewan['nama']:<15} {hewan['jenis']:<15} {hewan['umur']:<5}")


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


def main():
    proses = Proses()
    while True:
        print("\nMenu:")
        print("1. Tambah Hewan")
        print("2. Tampilkan Data Hewan")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            proses.input_hewan()
        elif pilihan == '2':
            proses.tampilkan_data()
        elif pilihan == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()