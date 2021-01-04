from selenium import webdriver
import time
from time import sleep
from csv import writer
from csv_writer import CSVWriter


class WebScrapper(object):
    def __init__(self, **kwargs):
        self.driver = webdriver.Chrome("/home/dimdimi4/Documents/books_ai/datasets/chromedriver")
        self.url = kwargs.get("url", None)
        self.driver.get(self.url)
        self.SCROLL_PAUSE_TIME = 2
        self.used_links = []  # urls of used books
        self.book_id = 439  # id of the book
        self.csv_writer = CSVWriter(path="books2.csv")
        self.scroll_down()

    def get_books(self, page_url):  # checks all books on the page
        books = self.driver.find_elements_by_css_selector("a[data-type='elektronnaya-kniga']")  # books objects on page
        books_urls = []  # urls of the e-books
        for book in books:
            books_urls.append(book.get_attribute("href"))  # getting url of the book
        for book_url in books_urls:
            if book_url not in self.used_links:  # book was not visited before
                self.used_links.append(book_url)
                self.driver.get(book_url)  # open the book page
                sleep(2)
                title_element = self.driver.find_element_by_css_selector("h1[itemprop='name']")  # title
                title = str(title_element.text)[:-5]
                try:
                    author_element = self.driver.find_element_by_css_selector("a[class='biblio_book_author__link']")
                    author = str(author_element.text)  # getting author name
                except Exception:
                    author = None
                try:
                    author_element = self.driver.find_element_by_css_selector("a[class='biblio_book_author]")
                    author = str(author_element.text)
                except Exception:
                    pass
                try:
                    rating_element = self.driver.find_element_by_css_selector("div[class='rating-number bottomline-rating']")
                    rating = str(rating_element.get_attribute("innerHTML"))  # getting rating of the book
                    rating = rating.replace(",", ".")
                except Exception:
                    rating = None
                tags = []
                try:
                    tag_elements = self.driver.find_elements_by_css_selector("a[class='biblio_info__link']")
                    for tag_element in tag_elements:
                        tags.append(str(tag_element.text))  # adding tags of the book
                except Exception:
                    tags = None
                try:
                    volume_element = self.driver.find_element_by_css_selector("li[class='volume']")
                    volume = str(volume_element.text)  # getting number of pages in the book
                    volume = volume.split(" ")[1]
                except Exception:
                    volume = None

                image = self.driver.find_element_by_css_selector("img[id='biblio_book_cover_image']")
                image_src = str(image.get_attribute("src"))
                print(title, author, rating, volume, tags, image_src, book_url)
                dict_row = {"id": self.book_id,
                       "title": title,
                       "author": author,
                       "rating": rating,
                       "tags": tags,
                       "volume": volume,
                       }
                row = [self.book_id, title, author, rating, tags, volume, image_src, book_url]
                self.csv_writer.write_row(row=row)
                self.book_id += 1
                self.driver.get(page_url)

    def check_loader_button(self):
        try:
            loader_button = self.driver.find_element_by_css_selector("div[class='loader_button']")
            loader_button.click()
        except Exception:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_down(self):


        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.get_books(page_url=self.url)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(self.SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                self.check_loader_button()
            last_height = new_height
