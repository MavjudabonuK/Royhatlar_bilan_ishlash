cars = ["bmw", "mersides bens", "volvo", "tesla", "audi" ]
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "mersides bens", "volvo", "tesla", "audi" ]
cars.sort()
print(cars)

cars = ["BMW", "mersides bens", "volvo", "tesla", "audi" ]
cars.sort()
print(cars)

mehmonlar = [ "Odil", "Hamid", "Asil", "Ali", "Guli", "Asal", "Temur", "Murod", "Nurbek", "Mavjudabonu"]
print("sorted( qaytargan royhat:)", sorted(mehmonlar))
print("Asil royhat ozgarmay qoldi:", mehmonlar)


ages = [ 12, 23, 45, 21, 17, 36, 18, 88]
ages.sort()
print(ages)
print(sorted(ages, revers=True))

fruits = [ "pear", "banan", "apple", "watermelon", "lemon" ]
print("Elemrntlar soni:", len(fruits))

sonlar = list(range(0,101))
print(sonlar)

juft_sonlar = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print("Juft sonlar:" , juft_sonlar)
print("Toq sonlar:" , toq_sonlar)

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3] 
print(my_cars) 
print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)


TUPLES_OZGARMAS_ROYXAT = (" TUPLES - O'ZGARMAS RO'YXAT")

tomonlar = (20,30,52.2)
print(tomonlar)

toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)