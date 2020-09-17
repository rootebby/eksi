from selenium import webdriver
import time


browser = webdriver.Firefox()

say = 1
while True:
    time.sleep(1)
    url = "https://eksisozluk.com/sinavlarda-alinmis-komik-notlar--4117651?p={}".format(say)
    browser.get(url)

    entrys = browser.find_elements_by_css_selector(".content")

    with open(f"{say}.txt","w") as file:
        
        for entry in entrys:
            print(entry.text)
            file.write(str(entry.text) + str("\n"))

    say += 1



