#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'
 
import sqlite3 as lite
import sys


#  tables
"""
CREATE TABLE "learn_foreign_words_dictionary" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "foreign_word" varchar(100) NOT NULL, 
    "translate_word" varchar(255) NOT NULL
);
"""

learn_foreign_words_dictionary_data= (
		    (1, u'acceptance', u'приём, признание, принятие, одобрение'),
		    (2, u'advanced', u'передовой, прогрессивный'),
		    (3, u'advertisement', u'рекламный, реклама, объявление, анонс'),
		    (4, u'all', u'любой, все, всё, целый'),
		    (5, u'and', u'и'),
		    (6, u'animal', u'животное, зверь'),
		    (7, u'ashes', u'зола, пепел'),
		    (8, u'at', u'при, у, возле'),
		    (9, u'at least', u'по крайней мере, хотя бы'),
		    (10, u'back', u'назад, задний, спина, спинка, поддерживать'),
		    (11, u'bark', u'кора'),
		    (12, u'because', u'потому что, так как, вследствие'),
		    (13, u'belly', u'живот'),
		    (14, u'bidding', u'торги, предложение цены'),
		    (15, u'big', u'большой, великий'),
		    (16, u'binding', u'связь, связывающий, сращивание'),
		    (17, u'bird', u'птица'),
		    (18, u'bite', u'грызть, кусать'),
		    (19, u'black', u'чёрный'),
		    (20, u'blood', u'кровь'),
		    (21, u'blow', u'дуть'),
		    (22, u'bone', u'кость'),
		    (23, u'boundary', u'граница, пограничный, черта'),
		    (24, u'breast', u'грудь'),
		    (25, u'breathe', u'дышать'),
		    (26, u'burn', u'жечь, гореть'),
		    (27, u'cannot', u'не могу'),
		    (28, u'certain', u'определённый, точный, некоторый'),
		    (29, u'child', u'ребёнок'),
		    (30, u'cloud', u'туча, облако'),
		    (31, u'cold', u'холодный'),
		    (32, u'come', u'приходить, прийти'),
		    (33, u'confluence', u'слияние, пересечение, толпа'),
		    (34, u'convert', u'переделать, переделывать, преобразовать, преобразовывать, реконструировать'),
		    (35, u'correct', u'правильный'),
		    (36, u'count', u'считать'),
		    (37, u'crawl', u'сканировать, ползать'),
		    (38, u'currently', u'в настоящее время, сейчас, настоящий, текущий'),
		    (39, u'cut', u'резать, рубить'),
		    (40, u'day', u'день'),
		    (41, u'decision', u'решение, выбор'),
		    (42, u'dictionary', u'словарь'),
		    (43, u'die', u'умирать'),
		    (44, u'different', u'различный, другой'),
		    (45, u'dig', u'копать, рыть'),
		    (46, u'dirty', u'грязный'),
		    (47, u'dog', u'собака'),
		    (48, u'doing', u'делающий'),
		    (49, u'drink', u'пить'),
		    (50, u'dry', u'сухой'),
		    (51, u'dull', u'тупой, скучный, тусклый, унылый'),
		    (52, u'during', u'втечение'),
		    (53, u'dust', u'пыль'),
		    (54, u'ear', u'ухо'),
		    (55, u'earth', u'земля'),
		    (56, u'eat', u'есть, кушать'),
		    (57, u'egg', u'яйцо'),
		    (58, u'engine', u'мотор, двигатель, механизм'),
		    (59, u'entity', u'сущность, объект'),
		    (60, u'entry', u'начальный, входной, вход, въезд'),
		    (61, u'example', u'пример, образец, экземпляр'),
		    (62, u'exhibit', u'экспонат, выставка, показывать, выставлять'),
		    (63, u'experience', u'опыт, стаж'),
		    (64, u'explosion', u'взрыв, взрывной'),
		    (65, u'eye', u'глаз'),
		    (66, u'fall', u'падать'),
		    (67, u'fallacy', u'ошибка, заблуждение'),
		    (68, u'far', u'далёкий, дальний'),
		    (69, u'fat', u'жир, сало'),
		    (70, u'father', u'отец'),
		    (71, u'fear', u'бояться'),
		    (72, u'feather', u'перо'),
		    (73, u'few', u'немного, мало, несколько'),
		    (74, u'fight', u'бороться'),
		    (75, u'fingernail', u'ноготь'),
		    (76, u'fire', u'огонь'),
		    (77, u'fish', u'рыба'),
		    (78, u'five', u'пять'),
		    (79, u'flexible', u'гибкий'),
		    (80, u'float', u'плыть, плавать, сплавляться, буй, поплавок'),
		    (81, u'flow', u'течь'),
		    (82, u'flower', u'цветок'),
		    (83, u'fly', u'летать'),
		    (84, u'fog', u'туман'),
		    (85, u'foot', u'стопа'),
		    (86, u'forest', u'лес'),
		    (87, u'four', u'четыре'),
		    (88, u'freeze', u'замерзать, замораживать, блокировать'),
		    (89, u'from scratch', u'с нуля'),
		    (90, u'fruit', u'плод, фрукт'),
		    (91, u'full', u'полный'),
		    (92, u'give', u'давать'),
		    (93, u'good', u'хороший, добрый, полезный, добро, польза'),
		    (94, u'grass', u'трава'),
		    (95, u'green', u'зелёный'),
		    (96, u'guts	', u'внутренности, кишки'),
		    (97, u'habit', u'привычка, традиция, обычай, особенность'),
		    (98, u'hair', u'волосы'),
		    (99, u'hand', u'рука, ладонь'),
		    (100, u'have', u'иметь, обладать, получать'),
		    (101, u'head', u'голова'),
		    (102, u'heart', u'сердце'),
		    (103, u'hear', u'слышать'),
		    (104, u'heavy', u'тяжёлый'),
		    (105, u'here', u'здесь, тут'),
		    (106, u'he', u'он'),
		    (107, u'hire', u'нанимать, наём'),
		    (108, u'hit', u'ударить'),
		    (109, u'hold', u'держать'),
		    (110, u'horn', u'рог'),
		    (111, u'how', u'как'),
		    (112, u'human', u'человек'),
		    (113, u'hunt', u'ловить, охотиться'),
		    (114, u'husband', u'муж, супруг'),
		    (115, u'ice', u'лёд'),
		    (116, u'if', u'если'),
		    (117, u'inconsistent', u'несовместимый, несоответствующий'),
		    (118, u'indentation', u'углубление, вырез, отпечаток, отступ'),
		    (119, u'instant', u'	момент, мгновенный, мгновение, текущий, немедленный'),
		    (120, u'interior', u'интерьер, внутренняя поверхность'),
		    (121, u'intermediate', u'средний, промежуточный'),
		    (122, u'into', u'в, к, на'),
		    (123, u'invite', u'приглашать, призывать'),
		    (124, u'involving', u'с участием, включающий, предусматривающий'),
		    (125, u'in', u'в'),
		    (126, u'issue', u'вопрос, проблема'),
		    (127, u'I', u'я'),
		    (128, u'kill', u'убивать'),
		    (129, u'knee', u'колено'),
		    (130, u'know', u'знать'),
		    (131, u'lake', u'озеро'),
		    (132, u'large', u'большой, крупный, значительный'),
		    (133, u'laugh', u'смеяться'),
		    (134, u'lead', u'вести, руководить, управлять, командовать'),
		    (135, u'leaf', u'лист'),
		    (136, u'left', u'левый'),
		    (137, u'leg', u'нога'),
		    (138, u'lie', u'лежать'),
		    (139, u'listen', u'слушать, выслушивание'),
		    (140, u'little', u'маленьки'),
		    (141, u'liver', u'печень'),
		    (142, u'live', u'жить'),
		    (143, u'long', u'длинный, долгий'),
		    (144, u'looking', u'ищущий, глядящий, следящий'),
		    (145, u'look', u'смотреть, искать'),
		    (146, u'louse', u'вошь'),
		    (147, u'male', u'мужчина, мужской'),
		    (148, u'many', u'много'),
		    (149, u'man', u'человек, мужчина'),
		    (150, u'meat', u'мясо'),
		    (151, u'mine', u'добывать, рудник, шахта'),
		    (152, u'mining', u'добыча'),
		    (153, u'moon', u'луна, месяц'),
		    (154, u'mother', u'мать'),
		    (155, u'mountain', u'гора'),
		    (156, u'mouth', u'рот'),
		    (157, u'мust have', u'должно быть'),
		    (158, u'name', u'имя'),
		    (159, u'narrow', u'узкий'),
		    (160, u'near', u'близкий'),
		    (161, u'neck', u'шея'),
		    (162, u'need', u'нужно, необходимо'),
		    (163, u'new', u'новый'),
		    (164, u'night', u'ночь'),
		    (165, u'nose', u'нос'),
		    (166, u'not', u'не'),
		    (167, u'old', u'старый'),
		    (168, u'one time', u'один раз'),
		    (169, u'one', u'один'),
		    (170, u'ongoing', u'постоянный'),
		    (171, u'opportunity', u'возможность, перспектива'),
		    (172, u'other', u'другой, иной'),
		    (173, u'pipe', u'труба'),
		    (174, u'play', u'играть'),
		    (175, u'prediction', u'прогноз, предсказание, пророчество'),
		    (176, u'produce', u'продукт, продукция, изделие, производить, изготавливать'),
		    (177, u'proposal', u'заявка, предложение'),
		    (178, u'pull', u'тянуть'),
		    (179, u'push', u'толкать, проталкивать, пихать, нажимать, продвигать'),
		    (180, u'quote', u'цитата, выдержка'),
		    (181, u'rain', u'дождь'),
		    (182, u'rating', u'ранг, разряд, оценка'),
		    (183, u'recency', u'новизна, свежесть'),
		    (184, u'red', u'красный'),
		    (185, u'related', u'связанный'),
		    (186, u'relative', u'относительный, условный, взаимный, родственник'),
		    (187, u'relevance', u'уместность, актуальность, значимость, важность'),
		    (188, u'render', u'исполнять, передавать, оказывать'),
		    (189, u'require', u'нуждаться, требовать, обязательный'),
		    (190, u'research', u'исследование, изучение, изыскание'),
		    (191, u'respective', u'соответствующий, соответственный, соответственно'),
		    (192, u'response', u'ответ, отклик'),
		    (193, u'reusable', u'многоразовый, повторно используемый'),
		    (194, u'right', u'правильный, правый'),
		    (195, u'river', u'река'),
		    (196, u'road', u'дорога, путь'),
		    (197, u'root', u'корень'),
		    (198, u'rope', u'верёвка, шнур'),
		    (199, u'rotten', u'гнилой'),
		    (200, u'round', u'круглый'),
		    (201, u'rub', u'тереть'),
		    (202, u'salt', u'соль'),
		    (203, u'sand', u'песок'),
		    (204, u'say', u'говорить, сказать'),
		    (205, u'scraping', u'выскабливание'),
		    (206, u'scrap', u'вырезка'),
		    (207, u'scratch', u'царапать'),
		    (208, u'sea', u'море'),
		    (209, u'seed', u'семя, семена'),
		    (210, u'see', u'видеть'),
		    (211, u'self', u'сам, себя, само, собственная личность'),
		    (212, u'several', u'	несколько, некоторый'),
		    (213, u'sew', u'шить'),
		    (214, u'sharp', u'чёткий, острый, определённый'),
		    (215, u'short', u'короткий'),
		    (216, u'shortcut', u'ярлык'),
		    (217, u'since', u'после, впоследствии, после того, так как'),
		    (218, u'signup', u'регистрация'),
		    (219, u'sing', u'петь'),
		    (220, u'sit', u'сидеть'),
		    (221, u'skin', u'кожа, шкура'),
		    (222, u'sky', u'небо'),
		    (223, u'sleep', u'спать'),
		    (224, u'small', u'маленький, мелкий, небольшой, низкий, слабый'),
		    (225, u'smell', u'нюхать, чуять'),
		    (226, u'smoke', u'дым'),
		    (227, u'smooth', u'гладкий, ровный'),
		    (228, u'snake', u'змея'),
		    (229, u'snow', u'снег'),
		    (230, u'someone', u'кто-то, некто'),
		    (231, u'some', u'некоторый, несколько, некий'),
		    (232, u'spending', u'затраты, расходы'),
		    (233, u'spit', u'плевать'),
		    (234, u'split', u'разделить, разделять'),
		    (235, u'spoken', u'разговорный, устный'),
		    (236, u'spreadsheet', u'таблица'),
		    (237, u'squeeze', u'сжимать'),
		    (238, u'stab', u'кольнуть, колоть'),
		    (239, u'stand', u'стоять, вставать, находиться, стенд, стойка'),
		    (240, u'star', u'звезда'),
		    (241, u'statement', u'отчет, изложение, заявление'),
		    (242, u'stats', u'статистика'),
		    (243, u'stick', u'палка'),
		    (244, u'stone', u'камень'),
		    (245, u'straight', u'прямой'),
		    (246, u'suck', u'сосать'),
		    (247, u'sun', u'солнце'),
		    (248, u'supplier', u'поставщик'),
		    (249, u'swell', u'пухнуть'),
		    (250, u'swim', u'плавать'),
		    (251, u'tail', u'хвост, конец, задний, хвостовой'),
		    (252, u'task', u'задача'),
		    (253, u'term', u'условие, срок, период'),
		    (254, u'that', u'тот, та, то'),
		    (255, u'there', u'там'),
		    (256, u'they', u'они'),
		    (257, u'thick', u'толстый'),
		    (258, u'think', u'думать'),
		    (259, u'thin', u'тонкий'),
		    (260, u'this', u'этот, эта, это'),
		    (261, u'those', u'те, то'),
		    (262, u'thou', u'ты'),
		    (263, u'three', u'три'),
		    (264, u'throw', u'бросать, кидать'),
		    (265, u'tie', u'вязать, связывать'),
		    (266, u'title', u'заголовок, заглавие, название, надпись'),
		    (267, u'tongue', u'язык'),
		    (268, u'tooth', u'зуб'),
		    (269, u'town', u'город'),
		    (270, u'tree', u'дерево'),
		    (271, u'turn', u'обращать, оборот, поворот, изменить направление'),
		    (272, u'two', u'два'),
		    (273, u'understanding', u'понимание, осмысление, соглашение'),
		    (274, u'vehicle', u'автомобиль'),
		    (275, u'vomit', u'рвать, блевать'),
		    (276, u'walk', u'ходить, идти'),
		    (277, u'warm', u'тёплый, горячий'),
		    (278, u'wash', u'мыть, умывать'),
		    (279, u'watch', u'смотреть, наблюдать, следить, караулись, вахта, дозор'),
		    (280, u'water', u'вода'),
		    (281, u'wet', u'мокрый, сырой, жидкий, мочить, влажность, сырость'),
		    (282, u'we', u'мы'),
		    (283, u'what', u'что'),
		    (284, u'when', u'когда, как только, если, хотя, который'),
		    (285, u'where', u'где'),
		    (286, u'while', u'пока, хотя, не смотря на'),
		    (287, u'white', u'белый'),
		    (288, u'who', u'кто'),
		    (289, u'wide', u'широкий'),
		    (290, u'wife', u'жена, супруга'),
		    (291, u'wind', u'ветер'),
		    (292, u'wing', u'крыло'),
		    (293, u'wipe', u'вытирать'),
		    (294, u'within', u'не позднее, втечение, внутри, в пределах'),
		    (295, u'with', u'с, от, за, у, со, причём'),
		    (296, u'woman', u'женщина'),
		    (297, u'worm', u'червь'),
		    (298, u'year', u'год'),
		    (299, u'yellow', u'жёлтый'),
		    (300, u'you', u'вы, ты'),

)
 
 
con = lite.connect('db.sqlite3')
 
with con:
    cur = con.cursor()
    
    # очистить таблицу
    cur.execute("delete from learn_foreign_words_dictionary where 1;")	
    
    # залить данные
    cur.executemany("INSERT INTO learn_foreign_words_dictionary VALUES(?, ?, ?)", learn_foreign_words_dictionary_data)
















