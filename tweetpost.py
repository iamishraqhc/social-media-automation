from time import sleep

from selenium import webdriver


def main():
    # your account user and password, path to image and message
    usr = ""
    pwd = ""
    message = ["https://www.fiverr.com/share/Boa7W @promofiverrgigs",
               "https://www.fiverr.com/share/lkzPA @promofiverrgigs",
               "https://www.fiverr.com/share/R9G8x @promofiverrgigs",
               "https://www.fiverr.com/share/WDmyx @promofiverrgigs",
               "https://www.fiverr.com/share/y8y0q @promofiverrgigs"]
    image_path = ""

    # delete cache
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference("browser.cache.disk.enable", False)
    # profile.set_preference("browser.cache.memory.enable", False)
    # profile.set_preference("browser.cache.offline.enable", False)
    # profile.set_preference("network.http.use-cache", False)

    # Path to geckodriver executable
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\ishra\OneDrive\Documents\fiverr\social-media-automation\chromedriver.exe')
    driver.implicitly_wait(15)

    # Login to twitter
    driver.get("https://twitter.com")
    sleep(3)
    elem = driver.find_element_by_name("session[username_or_email]")
    elem.send_keys(usr)
    elem = driver.find_element_by_name("session[password]")
    elem.send_keys(pwd)
    c = driver.find_element_by_class_name("EdgeButton")
    c.click()
    sleep(3)
    # Enter the text we want to post to twitter and the image
    for messages in message:
        mess = driver.find_element_by_id("tweet-box-home-timeline")
        mess.send_keys(messages)
        sleep(5)
        # ima = driver.find_element_by_name("media_empty")
        # sleep(3)
        # ima.send_keys(image_path)
        # Get the 'Post' button and click on it
        Post_button = driver.find_element_by_class_name("tweet-action")
        sleep(3)
        Post_button.click()
        sleep(3)
    driver.close()


if __name__ == '__main__':
    main()
