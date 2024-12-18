from Animal import Animal

class Ikan(Animal):
  def __init__(self, nama, makanan, hidup, berkembang_biak, cara_bernapas, warna_Ikan):
    super().__init__(nama, makanan, hidup, berkembang_biak)
    self.cara_bernapas = cara_bernapas
    self.warna_Ikan = warna_Ikan

  def info_ikan(self):
    super().info_animal()
    print("cara bernapas \t\t : ",self.cara_bernapas,
          "\nWarna Ikan \t\t : ", self.warna_Ikan)
    

Ikan_mas = Ikan("mas", "pelet", "Air", "Bertelur", "bernapas", "Warna Warni")
Ikan_mas.info_ikan()
print("===========================================================")
Ikan_sepat = Ikan("sepat", "serangga", "Air", "Bertelur", "bernapas", "abu abu")
Ikan_sepat.info_ikan()