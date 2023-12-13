# gsc_selenium_page_indexing_repport
Інструмент для масового імпорту даних зі звіту Page indexing Google Search Console. [Картинка](https://images.mony.com.ua/smuglyanka/170249053773_kiss_67kb.png)
Скріпт використовує ваш існуючий профіль Chrome браузера.

## Як користуватися

1. Встановити бібліотеки
```
pip install selenium
pip install undetected-chromedriver
```

2. Вказати шлях до профілю Google із яким будете працювати, замінивши USERNAME на ваш та вказавши номер профілю, у мене це "Profile 3"
```
profile = r"C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\Profile 3"
```

3. Додати список доменів у файл domains.txt. 

3.1. Якщо ви хочете отримати стату по всім доменам які є в GCS то їх можна витягнути використовуючи [XPATH Helper](https://chromewebstore.google.com/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl)

[Картинка](https://images.mony.com.ua/smuglyanka/170249003419_kiss_213kb.png)

4. Перед запуском закрити всі вікна Chrome браузера.



### Джерела
1. Selenium documentation: https://selenium-python.readthedocs.io/installation.html
2. undetected-chromedriver documentation: https://pypi.org/project/undetected-chromedriver/
3. Logic: https://www.youtube.com/watch?v=6SDzRN1aHiI


![](https://usagif.com/wp-content/uploads/2021/4fh5wi/pepefrg-4.gif)