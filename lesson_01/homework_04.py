
adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

clean_text_adventures = adventures_of_tom_sawer.replace("\n", " ")
# print(clean_text_adventures)

# task 02 ==
""" Замініть .... на пробіл
"""
clean_text_adventures = adventures_of_tom_sawer.replace("....", " ")
# print(clean_text_adventures)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
new_text = clean_text_adventures.split()
cleaned_new_text = " ".join(new_text)
# print(cleaned_new_text)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = 0
for word in cleaned_new_text:
    if word == "h":
        count += 1
# print(count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
for word in cleaned_new_text.split():
    if word.istitle():
        count += 1
        # print(word)

# print(count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

position_of_tom = cleaned_new_text.find("Tom")
# print(position_of_tom)
second_position_tom = cleaned_new_text.find("Tom", position_of_tom+1)
# print(second_position_tom)
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adventures_of_tom_sawer.split('.')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
forth_row = adwentures_of_tom_sawer_sentences[5].lower()
# print(forth_row)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    sentence = sentence.strip()
    if sentence.startswith('By the time'):
        print(True)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-2]
count = len(last_sentence.split())
print(count)