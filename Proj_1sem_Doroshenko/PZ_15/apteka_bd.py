import sqlite3 as sq
import apteka

with sq.connect('apteka.db') as con:
  cur = con.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS lekarstvennyye_sredstva (
     id_preparata INTEGER PRIMARY KEY,
     name_preparata VARCHAR NOT NULL,
     primeneniye VARCHAR,
     strana_proizvoditel VARCHAR,
     price FLOAT,
     nomer_punkta INTEGER,
     FOREIGN KEY(nomer_punkta) references aptechnyy_punkt(nomer_punkta) )""")
  # cur.executemany("INSERT INTO lekarstvennyye_sredstva VALUES (?, ?, ?, ?, ?, ?)", apteka.lek_sr)
with sq.connect('apteka.db') as con:
  cur = con.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS nalichiye_na_sklade (
     kolichestvo INTEGER,
     data_ispolzovaniya DATE,
     id_preparata INTEGER,
     FOREIGN KEY(id_preparata) references lekarstvennyye_sredstva(id_preparata)
  )""")
  # cur.executemany("INSERT INTO nalichiye_na_sklade VALUES (?, ?, ?)", apteka.nal_skl)
with sq.connect('apteka.db') as con:
  cur = con.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS aptechnyy_punkt (
     nomer_punkta INTEGER PRIMARY KEY,
     adres VARCHAR,
     zayavki VARCHAR,
     data_zayavki DATE,
     summa_zayavki FLOAT
  )""") 
#   cur.executemany("INSERT INTO aptechnyy_punkt VALUES (?, ?, ?, ?, ?)", apteka.apt_p)

# SQL-запросы на выборку данных из БД:

# #1.Вывести список всех препаратов с указанием количества их наличия на складе.
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT name_preparata, kolichestvo FROM lekarstvennyye_sredstva, nalichiye_na_sklade WHERE lekarstvennyye_sredstva.id_preparata=nalichiye_na_sklade.id_preparata")
#     result = cur.fetchall()
# print(result)

# #2. Вывести список всех препаратов, имеющихся на складе в количестве менее 10 штук.
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM nalichiye_na_sklade WHERE kolichestvo<10")
#     result = cur.fetchall()
# print(result)

# #3. Вывести список всех препаратов, которые производятся в России
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM lekarstvennyye_sredstva WHERE strana_proizvoditel='Россия'")
#     result = cur.fetchall()
# print(result)

# #4. Вывести список всех аптечных пунктов с указанием адреса и количества наличия препаратов в каждом пункте.
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT adres, kolichestvo FROM aptechnyy_punkt INNER JOIN nalichiye_na_sklade ON aptechnyy_punkt.nomer_punkta=nalichiye_na_sklade.id_preparata")
#     result = cur.fetchall()
# print(result)

# #5. Вывести список всех лекарственных препаратов, цена которых меньше 1000 руб,отсортированных по названию.
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT name_preparata FROM lekarstvennyye_sredstva WHERE price < 1000 ORDER BY name_preparata")
#     result = cur.fetchall()
# print(result)

#6. Вывести список лекарственных препаратов и их наличие на складе в каждом аптечном пункте.
# По условиям таблицы без изменения запроса выполнить невозможно, а с изменением запрос повторяется

# #7. Вывести список лекарственных препаратов, которые заканчиваются на складе в определенном аптечном пункте.
# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute("SELECT name_preparata FROM lekarstvennyye_sredstva WHERE nomer_punkta=7 and id_preparata in (SELECT id_preparata FROM nalichiye_na_sklade WHERE kolichestvo < 20)")
#    result = cur.fetchall()
# print(result)

# # 8. Вывести список аптечных пунктов, в которых есть хотя бы одно лекарственное средство срок годности которого истекает в этом месяце.
#   with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute("SELECT nomer_punkta FROM aptechnyy_punkt WHERE nomer_punkta in (SELECT nomer_punkta FROM lekarstvennyye_sredstva WHERE id_preparata in (SELECT id_preparata FROM nalichiye_na_sklade WHERE data_ispolzovaniya between '2021-01-01' and '2021-01-31'))")
#    result = cur.fetchall()
# print(result)

# SQL-запросы на выборку данных из БД:

# # 1. Обновить количество препарата "Аспирин" на складе до 100 штук:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE nalichiye_na_sklade SET kolichestvo = 100 WHERE id_preparata = 1")
#     result = cur.fetchall()
# print(result)

# # 2. Изменить дату использования для всех препаратов производства Индии:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE nalichiye_na_sklade SET data_ispolzovaniya = '2023-04-15' WHERE id_preparata in (SELECT id_preparata FROM lekarstvennyye_sredstva WHERE strana_proizvoditel = 'Индия')")
#     result = cur.fetchall()
# print(result)

# # 3. Увеличить цену препарата "Метформин" производства Германии на 20%:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE lekarstvennyye_sredstva SET price = price*1.2 WHERE name_preparata = 'Метформин' and strana_proizvoditel = 'Германия'")
#     result = cur.fetchall()
# print(result)

# # 4. Обновление цены для всех препаратов в таблице "Лекарственные средства" с учетом
# # налога в размере 20%:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE lekarstvennyye_sredstva SET price = price*1.2")
#     result = cur.fetchall()
# print(result)

# # 5. Обновление наличия препарата на складе в таблице "Наличие на складе" с учетом
# # изменения срока годности:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE nalichiye_na_sklade SET kolichestvo = kolichestvo+100, data_ispolzovaniya = '2022-09-30' WHERE data_ispolzovaniya = '2021-09-28'")
#     result = cur.fetchall()
# print(result)

# 6. Обновление наличия препарата на складе в таблице "Наличие на складе" с учетом
# поставки новых партий препарата:
#По условиям таблицы без изменения запроса выполнить невозможно, а с изменением запрос повторяется

# # 7. Обновление суммы заявки на 20% в таблице "Аптечный пункт" при изменении
# # даты заявки:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE aptechnyy_punkt SET summa_zayavki = summa_zayavki*1.2, data_zayavki = '2022-02-28' WHERE data_zayavki = '2021-02-01'")
#     result = cur.fetchall()
# print(result)

# # 8. Обновление даты использования препарата в таблице "Наличие на складе" при изменении количества
# # препарата на складе:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE nalichiye_na_sklade SET data_ispolzovaniya = '2022-04-15', kolichestvo = 0 WHERE kolichestvo = 25")
#     result = cur.fetchall()
# print(result)

# # 9. Обновление данных о препарате в таблице "Лекарственные средства" путем изменении цены:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE lekarstvennyye_sredstva SET name_preparata = 'Аспирин Экстра', price = 15 WHERE price = 12")
#     result = cur.fetchall()
# print(result)

# # 10. Обновление данных о препарате в таблице "Лекарственные средства" при изменении
# # наименования препарата:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE lekarstvennyye_sredstva SET name_preparata = 'Нурофен', primeneniye = 'Нурофен применяют при головной и зубной боли, мигрени, болезненных менструациях, невралгии, боли в спине, мышечных и ревматических болях; а также при лихорадочном состоянии при гриппе и простудных заболеваниях.' WHERE name_preparata = 'Лоперамид'")
#     result = cur.fetchall()
# print(result)

# # 11. Обновление цены препарата в таблице "Лекарственные средства" при изменении
# # страны-производителя:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE lekarstvennyye_sredstva SET strana_proizvoditel = 'Англия', price = 95 WHERE strana_proizvoditel = 'США'")
#     result = cur.fetchall()
# print(result)

# # 12. Обновление данных о препарате в таблице "Лекарственные средства" при изменении
# # страны-производителя:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE lekarstvennyye_sredstva SET strana_proizvoditel = 'Франция', price = price+10 WHERE id_preparata = 5")
#     result = cur.fetchall()
# print(result)

# 13. Обновление данных о препарате в таблице "Лекарственные средства" при изменении
# срока годности:
#Пропущено из-за INNER JOIN 

# SQL-запросы на удаление данных из БД:

# # 1. Удалить все препараты, которые просрочены на дату 2021-01-21:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM nalichiye_na_sklade WHERE data_ispolzovaniya = '2021-01-21'")
#     result = cur.fetchall()
# print(result)

# # 2. Удалить все препараты производства Индии с ценой ниже 12 долларов:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM lekarstvennyye_sredstva WHERE strana_proizvoditel = 'Индия' and price < 12")
#     result = cur.fetchall()
# print(result)

# # 3. Удалить все препараты с ценой ниже 50 долларов:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM lekarstvennyye_sredstva WHERE price < 50")
#     result = cur.fetchall()
# print(result)

# # 4. Удалить записи о заявках для препаратов, которых нет на складе:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM nalichiye_na_sklade WHERE kolichestvo = 0")
#     result = cur.fetchall()
# print(result)

# # 5. Удалить все записи о препаратах производства России:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM lekarstvennyye_sredstva WHERE strana_proizvoditel = 'Россия'")
#     result = cur.fetchall()
# print(result)

# # 6. Удалить все записи, где было количество на складе меньше 110 единиц одного препарата:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM nalichiye_na_sklade WHERE kolichestvo < 110")
#     result = cur.fetchall()
# print(result)

# # 7. Удалить все записи о препаратах, которые не используются после даты 2022-10-01:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM nalichiye_na_sklade WHERE data_ispolzovaniya < '2022-10-01'")
#     result = cur.fetchall()
# print(result)

# # 8. Удалить записи о препаратах, цена на которые была установлена выше 100 долларов:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM lekarstvennyye_sredstva WHERE price > 100")
#     result = cur.fetchall()
# print(result)

# # 9. Удалить все препараты, произведенные в Германии:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM lekarstvennyye_sredstva WHERE strana_proizvoditel = 'Германия'")
#     result = cur.fetchall()
# print(result)

# # 10. Удалить все записи о препаратах, название которых начинается на букву "А":
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM lekarstvennyye_sredstva WHERE name_preparata LIKE 'А%'")
#     result = cur.fetchall()
# print(result)

# 11. Удалить записи о заявках для препаратов, которых нет в таблице "Лекарственные
# средства":
#Не подходит условиям таблиц

# # 12. Удалить все препараты, производимые в США и стоимостью выше 50
# # долларов:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM lekarstvennyye_sredstva WHERE strana_proizvoditel = 'США' and price > 50")
#     result = cur.fetchall()
# print(result)

# 13. Удалить все записи о заявках в аптечных пунктах на препараты, произведенные в
# России:
#По условиям таблицы без изменения запроса выполнить невозможно, а с изменением запрос повторяется

# # 14. Удалить все препараты, цена на которые не указана:
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM lekarstvennyye_sredstva WHERE price = NULL")
#     result = cur.fetchall()
# print(result)
 
# 15. Удалить записи о заявках для препаратов, которые отсутствуют на складе:
#Запрос повторяется с 4
