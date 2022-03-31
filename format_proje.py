

webSite="https://www.sadikturan.com/"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

print(len(course))  #63
print(webSite[8:11]) # 8 başlayarak 3 karekter yazdırdı
print(webSite[23:26])  # altarnetifi alt tarafta
print(webSite[len(webSite)-4:len(webSite)-1]) # son 3 karekteri yazdırdı
print(course[0:15]) # ilk 15 karekteri
print(course[-15:]) # son 15 karekteri
print(course[::-1]) # testen yazdırdı

hello ="hello world"
newHello = hello[6:7].upper()
print(newHello)