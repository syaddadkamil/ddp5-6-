from Animal import Animal

class Ular(Animal):
  def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, warna_kulit):
    super().__init__(nama, makanan, hidup, berkembang_biak)
    self.berbisa = berbisa
    self.warna_kulit = warna_kulit

  def info_Ular(self):
    super().info_animal()
    print("berbisa \t\t : ", self.berbisa,
          "\nWarna kulit \t\t : ", self.warna_kulit)
    
ular_tanah = Ular("tanah", "kodok", "semak semak", "bertelur", "Mematikan", "coklat")
ular_tanah.info_Ular()
print("====================================================")
Ular_sanca_kembang = Ular("Sanca kembang", "burung", "darat", "bertelur", "tidak berbisa", "kuning muda")
Ular_sanca_kembang.info_Ular()
