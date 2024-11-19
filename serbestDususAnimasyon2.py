"""
Serbest düşüş animasyonu ve çarpma anındaki hız hesabı
Ek olarak momentumdan kaynaklanan etkinin statik bir kütleyi kaldırma eşdeğeri gösterilir.

"""
from matplotlib import pyplot as plt

yukseklik = 100
m = 83
g = 9.81

Vy = 0.0  # ilk hız
Konum_Y = yukseklik
zamanAdimi = 0.1  # simülasyon zaman adımı

Fy = m * g  # cisim üzerine etki eden kuvvetler
a_y = Fy / m  # etki eden kuvvetlerden doğan ivme

while Konum_Y >= 0:
    plt.axis([-50, 50, 0, 1000])
    plt.scatter(0, Konum_Y, s=50)
    plt.text(10, 900, f"Mevcut hız: {Vy:.2f} m/s", fontsize=10, color='red')  # Sağ üst köşeye hız bilgisi
    plt.text(10, 850, f"Mevcut konum: {Konum_Y:.2f} m", fontsize=10, color='blue')  # Sağ üst köşeye konum bilgisi
    
    Vy = a_y * zamanAdimi + Vy
    Konum_Y = Konum_Y - Vy * zamanAdimi
    plt.pause(0.001)
    plt.clf()

# Çarpma anındaki kütle eşdeğerini hesaplayalım
momentum = m * Vy
m_g = momentum / g  # Sabit duran cismin kütlesi

# Son hız ve hissedilen kuvvetin grafikte gösterilmesi
plt.axis([-50, 50, 0, 1000])
plt.scatter(0, 0, s=50, color='blue')  # Cismi yerde göster
plt.text(10, 900, f"Mevcut hız: {Vy:.2f} m/s", fontsize=10, color='red')  
plt.text(10, 850, f"Mevcut konum: {0:.2f} m", fontsize=10, color='blue')  # Mevcut konum 0 olarak gösterilir
plt.text(-40, 750, f"Yere çarpma hızı: {Vy:.2f} m/s", fontsize=12, color='green')  
plt.text(-40, 700, f"Hissedilen kuvvet: {momentum:.2f} Ns", fontsize=12, color='green')  # Momentum bilgisi
plt.text(-40, 650, f"Hissedilen kuvvet: {m_g:.2f} kg kaldırmaya eşdeğer", fontsize=12, color='purple')  # Eşdeğer kütle bilgisi
plt.show()  # Grafik açık kalır

print("Yere çarpma anındaki hız: ", Vy, "m/s")
print("Momentum ile hissedilecek kuvvet: ", momentum, "Ns")
print("Çarpma kuvveti eşdeğer kütle: ", m_g, "kg")
