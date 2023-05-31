#!/usr/bin/env python
# coding: utf-8

# #PHYTON EXAMPLES BEGıNNER LEVEL-BAHADIR ÖZCANLI

# In[6]:


# ÇARPANLARI BUL.(Bir sayının tüm çarpanlarını listeleyen fonksiyon.)
def carpan(sayi):
    sonuc=[]
    for i in range(1,sayi+1):
        if sayi % i == 0:
            sonuc.append(i)
    return sonuc


# In[ ]:


# HANGİ YÜZYIL(Tarihi alan ve hangi yüzyılda olduğunu döndüren fonksiyon.) 
def yuzyil(yil):
    if yil > 100:
        return f'{(yil // 100)+1}. Yüzyıl'
    elif 0 < yil < 100:
        return "1. Yüzyıl"


# In[19]:


#İNDEX ÇARPICI(Liste elemanlarının kendi indexleriyle çarpılıp toplandığı bir fonksiyon.)
def carp(liste):
    toplam=0
    for i in range(len(liste)):
        toplam += liste[i]*i
    return toplam


# In[47]:


#KAÇ HARF VE RAKAM(Verilen stringde ki harf ve rakamların sayısını döndürür.)
def say(yazi):
    rakam = 0
    harf = 0
    for i in yazi:
        if i.isalpha():
            harf += 1
        elif i.isdigit():
            rakam += 1
    return f'Harf:{harf} Rakam:{rakam}'


# In[56]:


#EN BÜYÜK VE KÜÇÜK SAYILAR(Verilen değerdeki en büyük ve küçük olanları string olarak döndüren bir fonksiyon.)
def buyuk_kucuk(deger):
    deger = deger.split()
    return str(max(deger)) +  " " +str(min(deger))


# In[63]:


#ORTA HARF'LER(String uzunluğu çift ise orta 2 harf, tek ise ortadaki harfi döndüren fonksiyon.)
def ters(yazi):
    if len(yazi) % 2 == 0:
        return yazi[(len(yazi) // 2)-1 : (len(yazi) // 2)+1 ]
    return yazi[len(yazi) // 2]


# In[1]:


#FİBONACCİ(Fibonacci sayılarını hesaplayan bir fonksiyon.)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-2) + fib(n-1)


# In[50]:


#APOCALYPTIC(Bir sayının apocalyptic olup olmadığını kontrol eder.)
def apocalyp(sayi):
    us = pow(2,sayi)
    us = str(us)
    if us.count("666") == 0:
        return ("Güvenli")
    elif us.count("666") == 1:
        return ("Tek")
    elif us.count("666") == 2:
        return ("Çift")
    elif us.count("666") == 3:
        return ("Üç")


# In[23]:


#SAKLI STRİNG(bir stringin ilk ve son harflerini aynı tutup diğerlerini gizleyen bir fonksiyon.)
def gizle(yazi):
    yazi = yazi.split()#Cümle kelimelerine ayrılıyor.
    yeni = list()
    for i in yazi:
        if len(i) < 2:
            yeni.append(i)
        else:
            yeni.append(i[0]+"-"*(len(i)-2)+i[-1])
    return " ".join(yeni)

