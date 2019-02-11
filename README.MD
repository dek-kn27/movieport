# Призначення модуля

Модуль main.py дозволяє згенерувати HTML-карту з місцями, де були зняті фільми вказаного користувачем року, а також контурами країн світу і штатів США.

# Опис структури HTML у файлі map.html

```<!DOCTYPE html>``` - означає, що браузер повинен відобразити сторінку відповідно до HTML5

```<head></head>``` - заголовкові теги (відкриваючий і закриваючий), де розташовані теги для метаданих, заголовка сторінки, стилів CSS, скриптів JavaScript тощо.

```<meta http-equiv="content-type" content="text/html; charset=UTF-8" />``` - вказує, що сторінка має mime-тип text/html і дає браузеру вказівку відображати текст у кодуванні UTF-8

```<script>L_PREFER_CANVAS=false; L_NO_TOUCH=false; L_DISABLE_3D=false;</script>``` - константи інтерактивної карти (JavaScript)

```<script src="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>```
 - зовнішні JavaScript-скрипти

   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
     - зовнішні каскадні таблиці стилів (CSS)

    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
     - задає ширину для html і body на всю ширину екрана, прибирає стандартні для браузерів відступи

    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style> - 
    встановлює абсолютне розташування карти

    <meta name="viewport" content="width=device-width,
        initial-scale=1.0, maximum-scale=1.0, user-scalable=no" /> 
        - дає мобільним браузерам вказівку відображати сторінку в натуральну величину і при зведенні/розведенні двох пальців на екрані не масштабувати все вікно разом з елементами керування

    <style>#map_6d5e722aa0cd488eaae721cb51cfe5af {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style> - ширина і розташування карти

<body></body> - теги (відкриваючий і закриваючий), всередині яких прийнято розташовувати видимий вміст, іноді всередині в кінці розташовують скрипти (як тут)

<div class="folium-map" id="map_6d5e722aa0cd488eaae721cb51cfe5af" ></div> - елемент, куди нижченаведений скрипт вставляє елементи карти. id задається для чіткого його визначення.

<script>...</script> - скрипти, які формують та вставляють карту на сторінку
 ```
# Висновок

Карта дозволяє переглянути місця, де були зняті фільми певного року, кількість, адреси й розташування таких місць, контури країн світу та штатів США.