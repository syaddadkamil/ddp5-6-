from Animal import Animal

class Kelinci(Animal):
  def __init__(self, nama, makanan, hidup, berkembang_biak, melompat, warna_putih):
    super().__init__(nama, makanan, hidup, berkembang_biak)
    self.melompat = melompat
    self.warna_putih = warna_putih

  def info_kelinci(self):
    super().info_animal()
    print("melompat \t\t : ", self.melompat,
          "\nWarna putih \t\t : ", self.warna_putih)
        
kelinci_minilop = Kelinci("minilop", "wortel", "darat", "melahirkan", "tinggi", "putih")
kelinci_minilop.info_kelinci()
print("=============================================")
kelinci_holland_lop = Kelinci("holland lop", "wortel", "darat", "melahirkan", "tinggi", "putih")
kelinci_holland_lop.info_kelinci()