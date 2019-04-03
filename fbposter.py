from time import sleep

from selenium import webdriver


def main():
    # your account user and password, path to image, links to groups and message
    usr = ""
    pwd = ""
    message = ["https://www.fiverr.com/share/Boa7W",
               "https://www.fiverr.com/share/lkzPA",
               "https://www.fiverr.com/share/R9G8x",
               "https://www.fiverr.com/share/WDmyx",
               "https://www.fiverr.com/share/y8y0q"]
    image_path = ""
    group_links = ['https://www.facebook.com/groups/121968305178198/',
                   'https://www.facebook.com/groups/762886083799826/',
                   'https://www.facebook.com/groups/769584619785908/',
                   'https://www.facebook.com/groups/getprojectsupwork/',
                   'https://www.facebook.com/groups/fiverrhelpbangladesh/',
                   'https://www.facebook.com/groups/shikhbeshobai/',
                   'https://www.facebook.com/groups/474434189348407/',
                   'https://www.facebook.com/groups/DSEntrepreneurs/']

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

    # Login to facebook
    driver.get("http://www.facebook.com")
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    c = driver.find_element_by_id('loginbutton')
    c.click()

    for group in group_links:
        # Go to the Facebook Group and
        driver.get(group)
        sleep(5)
        for messages in message:
            post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

            post_box.send_keys(messages)
            sleep(5)

            # if image_path != "":
            #     addMedia = driver.find_element_by_xpath("//*[@data-testid='media-attachment-selector']")
            #     addMedia.click()
            #
            #     # Provide picture file path
            #     driver.find_element_by_xpath("//*[@name='composer_photo']").send_keys(image_path)

            # Get the 'Post' button and click on it

            Post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
            sleep(5)
            Post_button.click()
            sleep(5)
    driver.close()


if __name__ == '__main__':
    main()
