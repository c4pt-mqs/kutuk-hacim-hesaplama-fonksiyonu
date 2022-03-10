# coding=utf-8

# Kütük Hesaplama Fonksiyonu = [(Pi Sayısı(3.14) * (Kütük Yarıçapı'nın karesi) * Kütük Boyu) * 0.1]

print("""
#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                                     #
#            Kabuksuz Kütük Hacim Hesabı              #
#                                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
""")


kutuk_boyu    = float(input("Kütüğün Boyunu Giriniz(m) : "))
kutuk_capi    = float(input("Kütüğün Çapını Giriniz(cm): "))
kutuk_yaricap = (kutuk_capi / 2)
pi_sayisi     = float(3.14)

kutuk_hacmi   = float((pi_sayisi * (kutuk_yaricap ** 2) * kutuk_boyu) * 0.1)

print(kutuk_hacmi)
