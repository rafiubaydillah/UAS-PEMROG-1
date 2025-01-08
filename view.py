class View:
    @staticmethod
    def tampilkan_tabel(hewan_list):
        print(f"{'No':<5} {'Nama':<15} {'Jenis':<15} {'Umur':<5}")
        print("=" * 45)
        for index, hewan in enumerate(hewan_list, start=1):
            print(f"{index:<5} {hewan['nama']:<15} {hewan['jenis']:<15} {hewan['umur']:<5}")

