# -*- coding: utf-8 -*-
"""odev.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xhvFGduFx-zrf7gcYYntKQ3P5YNgn7k2
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi renkli olarak oku (BGR formatında)
resim = cv2.imread('paralar.jpg')

# BGR'den RGB'ye çevir
rgb_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

# Gri tonlamaya çevir
gri_resim = cv2.cvtColor(rgb_resim, cv2.COLOR_RGB2GRAY)

# Gauss bulanıklaştırma uygula
bulanık_resim = cv2.GaussianBlur(gri_resim, (5,5), 0)

# Eşikleme uygula
_, esik_resim = cv2.threshold(bulanık_resim, 127, 255, cv2.THRESH_BINARY)

# Canny kenar bulma uygula
kenar_resim = cv2.Canny(esik_resim, 50, 150)

# Kontur tespiti yap
konturlar, _ = cv2.findContours(kenar_resim, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Konturlar üzerinde işlem yap
for kontur in konturlar:
    (x, y), yaricap = cv2.minEnclosingCircle(kontur)
    merkez = (int(x), int(y))
    yaricap = int(yaricap)
    cv2.circle(rgb_resim, merkez, yaricap, (255, 0, 0), 2)  # Mavi daire çiz

    x, y, w, h = cv2.boundingRect(kontur)
    cv2.rectangle(rgb_resim, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Yeşil dikdörtgen çiz
    cv2.putText(rgb_resim, "M.A", (x + w//2, y + h//2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Mavi metin ekle

# Sonuçları göster
plt.figure(figsize=(15,5))
plt.subplot(1,4,1)
plt.imshow(rgb_resim)
plt.title('RGB Resim')
plt.axis('off')

plt.subplot(1,4,2)
plt.imshow(gri_resim, cmap='gray')
plt.title('Gri Tonlu')
plt.axis('off')

plt.subplot(1,4,3)
plt.imshow(esik_resim, cmap='gray')
plt.title('Eşiklenmiş')
plt.axis('off')


plt.subplot(1,4,4)
plt.imshow(kenar_resim, cmap='gray')
plt.title('Kenar Tespiti')
plt.axis('off')

plt.show()