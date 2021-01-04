from love_novels_scrapper import LoveNovelsScrapper

urls = ["https://www.litres.ru/klassicheskaya-literatura/", "https://www.litres.ru/knigi-sovremennaya-proza/", "https://www.litres.ru/sereznoe-chtenie/ctihi-poeziya/",
        "https://www.litres.ru/knigi-uzhasy-mistika/", "https://www.litres.ru/knigi-detektivy/", "https://www.litres.ru/knigi-fentezi/",
        "https://www.litres.ru/knigi-detektivy/istoricheskie/", "https://www.litres.ru/knigi-publicistika/biografii-memuary/",
        "https://www.litres.ru/biznes-knigi/zarubezhnaya-delovaya-literatura/", "https://www.litres.ru/znaniya-navyki/biznes/best/",
        "https://www.litres.ru/knigi-psihologiya/samorazvitiye-lichnostnyy-rost/", "https://www.litres.ru/knigi-lubovnye-romany/",
        ]

web_scrapper = LoveNovelsScrapper(url=urls[-3])
