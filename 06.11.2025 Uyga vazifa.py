🧠 PYTHON ADVANCED — OOP ASOSIDA CHUQUR TUSHUNTIRISH
🔹 1. OOP dan Advanced darajaga o‘tish

Oddiy OOP’da siz sinf (class) yaratib, obyektlar bilan ishlaysiz.
Advanced OOP esa quyidagilarni o‘rgatadi:

Oddiy OOP	Advanced OOP
Sinf va obyekt yaratish	Metaclass bilan klasslarni boshqarish
Oddiy metodlar	Dunder (maxsus) metodlar bilan obyekt xatti-harakati
Meros olish	Ko‘p meros olish (multiple inheritance)
Atributga kirish	Descriptor va @property orqali nazorat
Oddiy funksiya	Decorator, closure, abstract class bilan struktura
Kod takrorlanadi	Reusability va Polimorfizm orqali optimizatsiya
🔹 2. Dunder metodlar (Data Model)

Dunder metodlar (double underscore) — Python’dagi yashirin “protokollar” bo‘lib, ular obyektni tabiiy Python xatti-harakati bilan uyg‘unlashtiradi.

Masalan:

__init__() — obyekt yaratilganda ishga tushadi (constructor).

__str__() — obyektni matnga aylantirganda ishlaydi (print() chaqirilganda).

__repr__() — obyektni texnik ko‘rinishda qaytaradi.

__add__(), __mul__() — matematik amallarni obyektlar orasida bajarish imkonini beradi.

__len__() — len(obj) ishlaganda avtomatik chaqiriladi.

__getitem__() — obyektni ro‘yxat kabi indekslash uchun.

👉 Misol: Siz Matrix degan sinf yaratsangiz va unga __add__() metodini yozsangiz, A + B ishlaydi, go‘yo ular oddiy sonlardek.
Bu obyektni tabiiy Python sintaksisiga integratsiya qiladi — bu Advanced OOPning yuragi.

🔹 3. @property va Enkapsulyatsiya (ma’lumotlarni himoyalash)

Oddiy sinfda atributga to‘g‘ridan-to‘g‘ri kirish mumkin:

car.speed = -10


Bu xato, chunki manfiy tezlik mantiqsiz.

Shuning uchun Advanced OOP @property dan foydalanadi:

getter — qiymatni o‘qish,

setter — qiymatni o‘zgartirish (cheklov bilan),

deleter — atributni o‘chirishni boshqaradi.

👉 Bu metod orqali siz foydalanuvchiga soddalikni saqlaysiz, lekin orqada murakkab validatsiya ishlaydi.
Ya’ni ichki kodni yashirasiz, lekin tashqi interfeys soddalashadi — bu abstraksiya va enkapsulyatsiyani birlashtiradi.

🔹 4. Descriptor mexanizmi

Descriptor — bu atributga murojaatni boshqaruvchi obyekt.
U uchta maxsus metodga ega:

__get__()

__set__()

__delete__()

U orqali siz atribut qiymatini o‘zgartirishda avtomatik tekshiruv yoki hisob-kitobni qo‘shishingiz mumkin.

Masalan:

Har safar “harorat” atributi o‘zgarganda log faylga yozish yoki avtomatik harorat birliklarini (°C ↔ °F) konvertatsiya qilish.

Descriptor — bu Python’dagi barcha property, staticmethod, classmethod va hatto dataclass ichida ishlaydigan mexanizm.

🔹 5. Abstrakt sinflar (ABC – Abstract Base Class)

Oddiy sinflarda metodni to‘liq yozasiz.
Abstrakt sinflar esa shunchaki qoidani e’lon qiladi, ammo bajarilishini bolalar sinfi yozadi.

Masalan:

“To‘lov tizimi” umumiy sinfi to‘lov_amalga_oshir() metodini talab qiladi.
“Payme”, “Click” sinflari bu metodni o‘z uslubida amalga oshiradi.

Bu tizim loyihalar uchun yagona tuzilma beradi, nazoratsiz kod yozilishini oldini oladi.

🔹 6. Polimorfizmning advanced darajasi

Polimorfizm — bir xil metod nomi turli sinflarda boshqacha ishlaydi.
Advanced OOP’da bu interfeys darajasida amalga oshiriladi:

sinf1.print()

sinf2.print()
Ammo ikkalasi ham bir xil nomli metodni bajaradi, lekin turli natija beradi.

Bu xatti-harakatni type-check qilmasdan boshqarish imkonini beradi:

for obj in obyektlar: obj.print()
Hech qayerda if isinstance(...) ishlatmasdan, obyekt o‘zi qanday bo‘lsa, shunday ishlaydi.

👉 Bu Dynamic Dispatch deyiladi va Python Advanced OOPning muhim qismi.

🔹 7. Ko‘p meros olish (Multiple Inheritance)

Oddiy OOP’da bitta ota sinfdan meros olasiz.
Advanced OOPda esa bir nechta sinfdan meros olish mumkin.

Masalan:

“SmartPhone” — bu “Phone” va “Camera” sinflaridan meros oladi.
Shunday qilib, bitta obyekt ikkala sinfning metodlaridan foydalana oladi.

Ammo bu holatda miras zanjiri (MRO — Method Resolution Order) paydo bo‘ladi, Python uni o‘zi aniqlaydi.
Advanced darajada siz bu tartibni tushunishingiz kerak, chunki noto‘g‘ri meros olish kutilmagan natija beradi.

🔹 8. Metaclass — sinflarni boshqaruvchi “klasslar”

Bu Advanced OOP’dagi eng murakkab, lekin eng kuchli qism.

Oddiy sinf obyekt yaratadi.
Metaclass esa sinfning o‘zini yaratadi.

Masalan:

Siz sinf yaratilganda avtomatik tarzda unga __str__ yoki __repr__ metodini qo‘shib qo‘yishingiz mumkin.

Yoki har bir yangi sinfni avtomatik registratsiya qiladigan tizim (masalan, Django ORM, SQLAlchemy) yaratishingiz mumkin.

Bu daraja odatda framework ishlab chiquvchilari yoki kutubxona mualliflari tomonidan ishlatiladi.

🔹 9. OOP + Functional + Asynchronous uyg‘unligi

Advanced OOP’da siz endi faqat obyekt yaratmaysiz, balki ularni:

Asinxron tarzda boshqarasiz (async def metodlar bilan),

Decorator orqali xatti-harakatini o‘zgartirasiz,

Typing bilan qat’iy tiplashtirasiz (@overload, Generic, TypeVar).

Shunday qilib, dastur strukturaviy, xavfsiz va tez ishlaydigan bo‘ladi.

🔹 10. OOP va Real loyihalarda qo‘llanish

Advanced OOP — bu teoriya emas, arxitektura.
Misollar:

Django’da har bir model — sinf.

FastAPI’da endpoint — klass yoki dekoratsiya qilingan funksiya.

AI loyihalarida Model, Dataset, Trainer sinflari OOP orqali boshqariladi.

SQLAlchemy’da har bir jadval Class orqali aniqlanadi.

Har bir murakkab tizimda OOP tamoyillari + Metaclass + Descriptor + Abstrakt interfeyslar ishlaydi.

🔹 11. Xulosa

Advanced OOP sizga quyidagilarni beradi:

✅ Kodni modulli va kengaytiriladigan qiladi.
✅ Ma’lumotlar yashirin va himoyalangan bo‘ladi.
✅ Loyihalar arxitektura jihatdan toza bo‘ladi.
✅ Har bir sinf o‘z javobgarligiga ega bo‘ladi (SRP — Single Responsibility Principle).
✅ Framework yoki kutubxona darajasida moslashuvchan kod yozish imkonini beradi.


🔷 1-BOSQICH: Sinf va obyekt (Class & Object)
📘 Nazariya:

Sinf — bu obyektlar uchun andaza.
Obyekt esa sinfning aniq nusxasi.

Sinfda:

Atributlar (property) – ma’lumotlar (ism, yosh, baho…)

Metodlar (method) – amallar (hisoblash, ko‘rsatish, o‘zgartirish…)

💻 Kod namuna:
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def salom(self):
        print(f"Salom, men {self.ism}, yoshim {self.yosh} da.")

# Obyektlar yaratish
t1 = Talaba("Dilnoza", 21)
t2 = Talaba("Alisher", 23)

t1.salom()
t2.salom()

🧠 Izoh:

__init__ — bu konstruktor; obyekt yaratilganda avtomatik ishga tushadi.

self — bu obyektning o‘zi.

t1 va t2 — bu ikkita obyekt, lekin bitta sinf asosida yaratilgan.

Har biri o‘z atributlariga ega:

t1.ism → "Dilnoza"
t2.ism → "Alisher"

🔷 2-BOSQICH: Meros olish (Inheritance)
📘 Nazariya:

Meros olish orqali yangi sinfni mavjud sinf asosida yaratamiz.
Bunda yangi sinf ota sinfning barcha metod va atributlarini meros qilib oladi.

💻 Kod namuna:
class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def info(self):
        print(f"{self.ism} — {self.yosh} yoshda")

# Bola sinf
class Talaba(Shaxs):
    def __init__(self, ism, yosh, universitet):
        super().__init__(ism, yosh)
        self.universitet = universitet

    def info(self):
        print(f"{self.ism} {self.universitet} da o‘qiydi")

t = Talaba("Dilnoza", 21, "TATU")
t.info()

🧠 Izoh:

super() — ota sinfdagi metodlarni chaqirish uchun ishlatiladi.

Agar bola sinf metodni qayta yozsa (override qilsa), Python yangisini ishlatadi.

Shu orqali polimorfizm ham yuzaga keladi.

🔷 3-BOSQICH: Polimorfizm (ko‘p shakllilik)
📘 Nazariya:

Bir xil nomdagi metodlar turli sinflarda turlicha ishlaydi.

💻 Kod namuna:
class Hayvon:
    def ovoz(self):
        print("Hayvon tovush chiqardi")

class It(Hayvon):
    def ovoz(self):
        print("Vov-vov!")

class Mushuk(Hayvon):
    def ovoz(self):
        print("Miyav!")

for x in [It(), Mushuk(), Hayvon()]:
    x.ovoz()

🧠 Izoh:

Har bir obyekt uchun ovoz() nomi bir xil, lekin natija boshqacha.

Bu polimorfizm, ya’ni “bir xil metod – turli shakllar”.

Bu orqali biz turli obyektlarni bir xil interfeys orqali boshqaramiz.

🔷 4-BOSQICH: Enkapsulyatsiya va @property
📘 Nazariya:

Enkapsulyatsiya — bu atributlarni tashqaridan to‘g‘ridan-to‘g‘ri o‘zgartirishdan himoya qilish.
@property yordamida atributga cheklov qo‘yish mumkin.

💻 Kod namuna:
class BankHisobi:
    def __init__(self, balans):
        self.__balans = balans   # Yashirin atribut

    @property
    def balans(self):
        return self.__balans

    @balans.setter
    def balans(self, qiymat):
        if qiymat < 0:
            print("Balans manfiy bo‘lishi mumkin emas!")
        else:
            self.__balans = qiymat

hisob = BankHisobi(1000)
hisob.balans = -200    # noto‘g‘ri
print(hisob.balans)

🧠 Izoh:

__balans — tashqaridan bevosita o‘zgartirib bo‘lmaydigan atribut.

@property va @setter orqali kirish nazorat ostida bo‘ladi.

Bu ma’lumot xavfsizligini ta’minlaydi.

🔷 5-BOSQICH: Abstraksiya (Abstract Base Class)
📘 Nazariya:

Abstrakt sinf — bu faqat andaza.
Undan bevosita obyekt yaratilmaydi.
Bu sinf faqat boshqa sinflar uchun majburiy metodlar ro‘yxatini belgilaydi.

💻 Kod namuna:
from abc import ABC, abstractmethod

class To‘lovTizimi(ABC):
    @abstractmethod
    def tolov_qilish(self, summa):
        pass

class Payme(To‘lovTizimi):
    def tolov_qilish(self, summa):
        print(f"{summa} so‘m Payme orqali to‘landi")

class Click(To‘lovTizimi):
    def tolov_qilish(self, summa):
        print(f"{summa} so‘m Click orqali to‘landi")

tizimlar = [Payme(), Click()]
for tizim in tizimlar:
    tizim.tolov_qilish(10000)

🧠 Izoh:

ABC va @abstractmethod — abstrakt sinfni yaratadi.

Payme va Click uni to‘ldiruvchi konkret sinflardir.

Bu interfeys yondashuvi — barcha sinflarda bir xil metodlar bo‘lishini ta’minlaydi.

🔷 6-BOSQICH: Descriptor (Advanced atribut nazorati)
📘 Nazariya:

Descriptor — bu atributga murojaat qilish jarayonini to‘liq nazorat qiluvchi obyekt.
Bu orqali siz:

qiymatni tekshirishingiz,

o‘zgartirilganda log yozishingiz,

yoki avtomatik hisob-kitobni bajartirishingiz mumkin.

💻 Kod namuna:
class Temperature:
    def __get__(self, instance, owner):
        return instance._temp

    def __set__(self, instance, value):
        if value < -273:
            raise ValueError("Absolyut nol -273°C dan past bo‘lishi mumkin emas")
        instance._temp = value

class Weather:
    temp = Temperature()

w = Weather()
w.temp = 25
print(w.temp)

🧠 Izoh:

__get__ va __set__ atributga kirish va o‘zgartirishni nazorat qiladi.

Bu @propertydan ham qudratliroq mexanizm.

Frameworklarda (masalan, Django ORM) descriptorlar keng qo‘llaniladi.

🔷 7-BOSQICH: Metaclass (Advanced konstruktor)
📘 Nazariya:

Metaclass — bu sinf yaratilish jarayonini boshqaruvchi sinf.
Oddiy sinf obyekt yaratadi, metaclass esa sinfning o‘zini yaratadi.

💻 Kod namuna:
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f"{name} sinfi yaratildi!")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

🧠 Izoh:

Har safar yangi sinf yaratilganda __new__ ishlaydi.

Bu orqali siz sinf ichiga avtomatik atribut yoki metod qo‘shishingiz mumkin.

Django, FastAPI, SQLAlchemy kabi yirik frameworklarda bu avtomatik registratsiya tizimi uchun ishlatiladi.

🔷 8-BOSQICH: Real loyiha nuqtai nazaridan
Soha	OOP elementi	Maqsad
Web (Django)	Model → Class	Ma’lumotlar bazasi jadvali
API (FastAPI)	Pydantic model	Ma’lumot validatsiyasi
AI	Model, Dataset, Trainer sinflari	Modullarni strukturalash
Cybersecurity	Auth, User, Log sinflari	Xavfsizlik va nazorat
🔷 9-BOSQICH: Advanced OOP’ning xulosasi

✅ Sinf — kodni modullarga bo‘ladi
✅ Meros — qayta foydalanish imkonini beradi
✅ Polimorfizm — moslashuvchanlikni ta’minlaydi
✅ Enkapsulyatsiya — ma’lumotni himoya qiladi
✅ Abstraksiya — interfeysni standartlashtiradi
✅ Descriptor va Metaclass — professional darajadagi nazoratni beradi


⚙️ 10-BOSQICH: ASINXRON OOP (async/await sinflarda)
📘 1. Asinxronlik nima?

Oddiy dasturlarda har bir kod ketma-ket ishlaydi — bir vazifa tugamasdan boshqasi boshlanmaydi.
Bu CPU vaqtini bekorga sarflaydi, ayniqsa:

tarmoqdan ma’lumot olishda,

fayl o‘qishda,

ma’lumotlar bazasi bilan ishlashda.

Asinxron dasturlash esa bir vaqtning o‘zida bir nechta vazifani bajarish imkonini beradi, lekin parallel emas — bitta oqim ichida navbat bilan boshqariladi.

🧠 2. OOP bilan qanday bog‘liq?

Oddiy sinflarda metodlar ketma-ket bajariladi:

class Downloader:
    def yuklab_ol(self):
        ...


Ammo Advanced OOPda siz metodlarni asinxron qilib yozishingiz mumkin:

class Downloader:
    async def yuklab_ol(self):
        ...


Bu degani: siz bu metodni chaqirganda await ishlatishingiz kerak bo‘ladi — ya’ni, “bu jarayon tugaguncha boshqalar ham ishlasin”.

💻 3. Kod misoli:
import asyncio

class Downloader:
    async def yuklab_ol(self, fayl_nomi, vaqt):
        print(f"{fayl_nomi} yuklanmoqda...")
        await asyncio.sleep(vaqt)  # yuklash jarayoni simulyatsiyasi
        print(f"{fayl_nomi} yuklandi ✅")

async def main():
    yuklagich = Downloader()
    # Uchta faylni asinxron yuklab olish
    await asyncio.gather(
        yuklagich.yuklab_ol("video.mp4", 3),
        yuklagich.yuklab_ol("kitob.pdf", 2),
        yuklagich.yuklab_ol("rasm.jpg", 1)
    )

asyncio.run(main())

🔍 4. Tahlil:

async def — bu asinxron funksiya yoki metod.

await asyncio.sleep(vaqt) — bu joyda jarayon “kutish” holatiga o‘tadi, lekin boshqa ishlar davom etadi.

asyncio.gather() — bir nechta vazifani bir vaqtda boshqarish uchun ishlatiladi.

Bu tarzda siz resurslar samaradorligini oshirasiz.

⚡ 5. OOP + Async kombinatsiyasi: real loyiha misoli

Masalan sizda “Server” klassi bor.
U kelayotgan foydalanuvchi so‘rovlarini (requests) asinxron tarzda qabul qilishi kerak.

class Server:
    async def handle_request(self, foydalanuvchi):
        print(f"{foydalanuvchi} so‘rovi qabul qilindi...")
        await asyncio.sleep(2)
        print(f"{foydalanuvchi} ga javob yuborildi ✅")

async def main():
    s = Server()
    foydalanuvchilar = ["Ali", "Dilnoza", "Jamshid", "Malika"]
    await asyncio.gather(*(s.handle_request(f) for f in foydalanuvchilar))

asyncio.run(main())


🟢 Natija:

Ali so‘rovi qabul qilindi...
Dilnoza so‘rovi qabul qilindi...
Jamshid so‘rovi qabul qilindi...
Malika so‘rovi qabul qilindi...
Ali ga javob yuborildi ✅
...

🧩 6. Asinxron sinflarda meros olish

Siz async metodlarni meros qilib olishingiz ham mumkin:

class API:
    async def ulanish(self):
        print("Serverga ulanmoqda...")
        await asyncio.sleep(1)
        print("Ulandi ✅")

class UserAPI(API):
    async def yuklab_ol(self):
        await self.ulanish()
        print("Foydalanuvchi ma’lumotlari yuklandi.")


👉 Bunda bola sinf ota sinfning asinxron metodidan foydalanmoqda (await self.ulanish()).

⚙️ 7. Asinxron __aenter__ va __aexit__ (Async Context Manager)

Oddiy with blokda fayl ochiladi va yopiladi.
Asinxron muhitda esa async with ishlatiladi.

class Connection:
    async def __aenter__(self):
        print("Ulanish o‘rnatilmoqda...")
        await asyncio.sleep(1)
        print("Ulandi ✅")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Ulanish yopilmoqda...")
        await asyncio.sleep(1)
        print("Yopildi ✅")

async def main():
    async with Connection():
        print("So‘rovlar bajarilmoqda...")

asyncio.run(main())


🔸 Bu mexanizm real tizimlarda fayl, tarmoq, DB ulanishlarini xavfsiz yopish uchun ishlatiladi.

🧮 8. Asinxron obyektlar orasida hamkorlik (Task Queue)

Advanced tizimlarda ko‘p obyektlar asinxron ishlaydi:

biri ma’lumot to‘playdi,

biri uni tahlil qiladi,

biri natijani bazaga yozadi.

Bu uchun asyncio.Queue() ishlatiladi:

class Ishchi:
    def __init__(self, nomi, navbat):
        self.nomi = nomi
        self.navbat = navbat

    async def bajar(self):
        while True:
            ish = await self.navbat.get()
            print(f"{self.nomi} '{ish}' ishini boshladi...")
            await asyncio.sleep(2)
            print(f"{self.nomi} '{ish}' ishini tugatdi ✅")
            self.navbat.task_done()

async def main():
    navbat = asyncio.Queue()
    ishchilar = [Ishchi(f"Ishchi-{i}", navbat) for i in range(1, 4)]

    # Ishchilarni ishga tushirish
    for i in ishchilar:
        asyncio.create_task(i.bajar())

    # Ishlarni navbatga qo‘shish
    for ish in ["Hisobot", "Statistika", "Grafik", "Baza yangilash"]:
        await navbat.put(ish)

    await navbat.join()

asyncio.run(main())


👉 Bu producer–consumer arxitekturasidir — real-time serverlar shu asosda ishlaydi.

🔐 9. Asinxron OOP – Afzalliklar
Afzallik	Izoh
Tez ishlaydi	Kutish vaqtida boshqa ishlar bajariladi
Resurs tejaladi	Faqat bitta oqimda ko‘p vazifa
Oson kengaytiriladi	Sinflar orqali modular tuzilma
Real-time tizimlar uchun ideal	Serverlar, API, sensorlar, monitoring uchun juda mos
🔚 10. Xulosa

Asinxron OOP — bu:

obyektlarni event loop bilan uyg‘unlashtirish,

bir vaqtning o‘zida ko‘p vazifani boshqarish,

va real tizimlarda (FastAPI, aiohttp, websockets) ishlovchi professional daraja.