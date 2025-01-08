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