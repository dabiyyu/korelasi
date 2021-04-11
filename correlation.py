import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

class Korelasi:
    def __init__(self, panjang, lebar, judul, majortick, minortick):
        self.panjang = panjang
        self.lebar = lebar
        self.judul = judul
        self.majortick = majortick
        self.minortick = minortick
        self.fig = plt.figure(figsize=(lebar, panjang))
        self.fig.canvas.set_window_title('Well Correlation')
    
    def mainwell(self, WellName, top, bottom, depth, GR, Res, MarkerName, MarkerDepth):
        self.WellName = WellName
        self.top = top
        self.bottom = bottom
        self.depth = depth
        self.GR = GR
        self.Res = Res
        self.MarkerName = MarkerName
        self.MarkerDepth = MarkerDepth
        
        Jml = len(self.MarkerName)
        # buat posisi garis marker
        x_log = Jml*[[0,150],[0.2,200]]
        y_log = [[x,x] for x in self.MarkerDepth]
        warna = Jml*(['green', 'red', 'blue'])
        # Siapkan layout log GR/RES well-1 
        self.ax1 = self.fig.add_axes([0.05, 0.1, 0.1, 0.7])
        self.ax11 = self.fig.add_axes([0.15, 0.1, 0.1, 0.7])
        
        self.ax1.set_yticklabels([])
        self.ax11.set_xscale('log')
        self.ax1.text(80, self.top-100, self.WellName, fontsize=15)
        #self.ax1.set_title(self.WellName)
        # generate log plot
        self.ax1.plot(self.GR, self.depth, color='green') 
        self.ax1.fill_betweenx(self.depth, self.GR, 75, where=self.GR < 75, facecolor='yellow')
        self.ax11.plot(self.Res, self.depth, color='black')
        
        #Tampilkan marker pada kolom GR/RES 
        for i in range(Jml):
            self.ax1.plot(x_log[i], y_log[i], color=warna[i])
            self.ax11.plot(x_log[i], y_log[i], color=warna[i])
        
    def secondwell(self, WellName, top, bottom, depth, GR, Res, MarkerName, MarkerDepth):
        self.WellName = WellName
        self.top = top
        self.bottom = bottom
        self.depth = depth
        self.GR = GR
        self.Res = Res
        self.MarkerName = MarkerName
        self.MarkerDepth = MarkerDepth  
        Jml = len(self.MarkerName)
        x_log = Jml*[[0,150],[0.2,200]]
        y_log = [[x,x] for x in self.MarkerDepth]
        warna = Jml*(['green', 'red', 'blue'])
    
       # Siapkan layout log GR/RES well-2 
        self.ax2 = self.fig.add_axes([0.4, 0.1, 0.1, 0.7])
        self.ax22 = self.fig.add_axes([0.5, 0.1, 0.1, 0.7])
          
        self.ax2.set_yticklabels([])
        self.ax22.set_xscale('log')
        self.ax2.text(80, self.top-100, self.WellName, fontsize=15)
        # generate log plot
        self.ax2.plot(self.GR, self.depth, color='green')
        #Fill warna kuning GR sand
        self.ax2.fill_betweenx(self.depth, self.GR, 75, where=self.GR < 75, facecolor='yellow')
        self.ax22.plot(self.Res, self.depth, color='black')
        
        #Tampilkan marker pada kolom GR/RES 
        for i in range(Jml):
            self.ax2.plot(x_log[i], y_log[i], color=warna[i])
            self.ax22.plot(x_log[i], y_log[i], color=warna[i])
    
    def thirdwell(self, WellName, top, bottom, depth, GR, Res, MarkerName, MarkerDepth):
        self.WellName = WellName
        self.top = top
        self.bottom = bottom
        self.depth = depth
        self.GR = GR
        self.Res = Res
        self.MarkerName = MarkerName
        self.MarkerDepth = MarkerDepth  
        Jml = len(self.MarkerName)
        x_log = Jml*[[0,150],[0.2,200]]
        y_log = [[x,x] for x in self.MarkerDepth]
        warna = Jml*(['green', 'red', 'blue'])
        # Siapkan layout log GR/RES well-3 
        self.ax3 = self.fig.add_axes([0.75, 0.1, 0.1, 0.7])
        self.ax32 = self.fig.add_axes([0.85, 0.1, 0.1, 0.7])
          
        self.ax3.set_yticklabels([])
        self.ax32.set_xscale('log')
        self.ax3.text(80, self.top-100, self.WellName, fontsize=15)
        # generate log plot
        self.ax3.plot(self.GR, self.depth, color='green')

        #Fill warna kuning GR sand
        self.ax3.fill_betweenx(self.depth, self.GR, 75, where=self.GR < 75, facecolor='yellow')
        self.ax32.plot(self.Res, self.depth, color='black')
        #Tampilkan marker pada kolom GR/RES       
        for i in range(Jml):
            self.ax3.plot(x_log[i], y_log[i], color=warna[i])
            self.ax32.plot(x_log[i], y_log[i], color=warna[i])
        
    def format_axis(self):       
        CurveNm = ['GR','Res']
        CurveScl = [[0,150], [0.2, 200]]
        CurveClr = ['green','black']
        
        #Format keluaran tiap sumbu kurva
        j = 0
        for i, self.ax in enumerate(self.fig.axes):
            self.ax.set_xlim(CurveScl[j])
            #self.ax.set_xticks(CurveScl[j])
            self.ax.set_xticks([])
            #self.ax.xaxis.tick_top()
            self.ax.set_xlabel(CurveNm[j], color = CurveClr[j])
            self.ax.xaxis.set_label_position('top')
            #self.ax.tick_params(axis='x',colors = CurveClr[j])
            self.ax.set_ylim(self.top, self.bottom)
            self.ax.invert_yaxis()
            self.ax.yaxis.set_major_locator(MultipleLocator(self.majortick))
            self.ax.minorticks_on()
            self.ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
            self.ax.grid(b=True, which='major', color='#666666', linestyle='-')
            j+= 1
            if j == 2:
                j = 0 
         
    
    def show_2wells_correlation(self, MarkerNm, Marker1, Marker2):
        self.Marker1 = Marker1
        self.Marker2 = Marker2
        self.MarkerNm = MarkerNm
        Jml = len(self.MarkerNm)
        x_m = Jml*[[0,1],[0,1]]
        y_m = [[x,y] for x,y in zip(Marker1, Marker2)]
        warna = Jml*(['green', 'red', 'blue'])
        
        self.format_axis()
        
        #Plot antar well, buat bidang kosong well 1 dan 2
        self.ax12 = self.fig.add_axes([0.25, 0.1, 0.15, 0.7])
        self.ax12.set_axis_off()
        self.ax12.set_ylim(self.top, self.bottom)
        self.ax12.invert_yaxis()
        
        #Tampilkan garis marker
        for i in range(Jml):
            self.ax12.plot(x_m[i], y_m[i], color=warna[i])
            #Tampilkan nama marker
            self.ax12.text(0.01, self.Marker1[i]-2, self.MarkerNm[i])
        self.fig.suptitle(self.judul, fontsize=20, x=0.33, y=0.9)
        plt.show()
        
    def show_3wells_correlation(self, MarkerNm, Marker1, Marker2, Marker3):
        self.Marker1 = Marker1
        self.Marker2 = Marker2
        self.Marker3 = Marker3
        self.MarkerNm = MarkerNm
        
        Jml = len(self.MarkerNm)
        x_m = Jml*[[0,1],[0,1]]
        y_m = [[x,y] for x,y in zip(Marker1, Marker2)]
        y_m2 = [[x,y] for x,y in zip(Marker2, Marker3)]
        warna = Jml*(['green', 'red', 'blue'])
        
        self.format_axis()
        #Plot antar well, buat bidang kosong well 2 dan 3
        self.ax12 = self.fig.add_axes([0.25, 0.1, 0.15, 0.7])
        self.ax12.set_axis_off()
        self.ax12.set_ylim(self.top, self.bottom)
        self.ax12.invert_yaxis()
        
        self.ax23 = self.fig.add_axes([0.6, 0.1, 0.15, 0.7])
        self.ax23.set_axis_off()
        self.ax23.set_ylim(self.top, self.bottom)
        self.ax23.invert_yaxis()
       
        #Tampilkan garis marker
        for i in range(Jml):
            self.ax12.plot(x_m[i], y_m[i], color=warna[i])
            #Tampilkan nama marker
            self.ax12.text(0.01, self.Marker1[i]-2, self.MarkerNm[i])
            self.ax23.plot(x_m[i], y_m2[i], color=warna[i])
            #Tampilkan nama marker
            self.ax23.text(0.01, self.Marker2[i]-2, self.MarkerNm[i])
        self.fig.suptitle(self.judul, fontsize=20, x=0.5, y=0.88)
        plt.show()