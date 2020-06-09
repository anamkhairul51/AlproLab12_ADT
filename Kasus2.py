class Clock:   
    def __init__(self, jam, menit, detik):
        self.jam = jam
        self.menit = menit
        self.detik = detik
        
    def cek_valid(self):
        if self.jam <= 24 and self.menit <= 60 and self.detik <= 60:
            print(True)
        else:
            print(False)
    
    def tampil_jam(self):
        print(self.jam,':',self.menit,':',self.detik)

    def ubah_second(self):
        print(self.jam*3600 + self.menit*60 + self.detik)
        
    def alarm(self, second):
        total = second + self.jam*3600 + self.menit*60 + self.detik
        menit, detik = divmod(total, 60)
        jam, menit = divmod(menit, 60)
        print(jam,':',menit,':',detik)
        
clk = Clock(1, 5, 30)
clk.cek_valid()
clk.tampil_jam()
clk.ubah_second()
clk.alarm(5000)


__author__ = 'A11201911712'

