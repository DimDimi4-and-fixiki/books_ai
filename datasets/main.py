from scrapper import WebScrapper

urls = ["https://www.litres.ru/klassicheskaya-literatura/", "https://www.litres.ru/knigi-sovremennaya-proza/page-100/", "https://www.litres.ru/sereznoe-chtenie/ctihi-poeziya/",
        "https://www.litres.ru/knigi-uzhasy-mistika/", "https://www.litres.ru/knigi-detektivy/", "https://www.litres.ru/knigi-fentezi/",
        "https://www.litres.ru/knigi-detektivy/istoricheskie/", "https://www.litres.ru/knigi-publicistika/biografii-memuary/",
        "https://www.litres.ru/biznes-knigi/zarubezhnaya-delovaya-literatura/", "https://www.litres.ru/znaniya-navyki/biznes/",
        "https://www.litres.ru/knigi-psihologiya/samorazvitiye-lichnostnyy-rost/", "https://www.litres.ru/knigi-lubovnye-romany/",
        ]

web_scrapper = WebScrapper(url=urls[1])
