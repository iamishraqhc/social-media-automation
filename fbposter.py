from time import sleep

from selenium import webdriver


def main():
    # your account user and password, path to image, links to groups and message
    usr = ""
    pwd = ""
    message = ["I Will Create Complete Custom Designed Wordpress Website. Please go to the following link https://www.fiverr.com/iamishraqhc/create-complete-custom-designed-wordpress-website?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=boa7w",
               "I Will Create An Ecommerce Website. Please go to the following link https://www.fiverr.com/iamishraqhc/create-an-ecommerce-website?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=lkzpa",
               "I Will Fix Any Wordpress Errors, Issues Or Problems. Please go to the following link https://www.fiverr.com/iamishraqhc/fix-any-wordpress-errors-issues-or-problems?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=r9g8x",
               "I Will Proofread And Edit Your Article In Less Than 24 Hours. Please go to the following link https://www.fiverr.com/iamishraqhc/proofread-and-edit-your-article-in-less-than-24-hours?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=wdmyx",
               "I Will Scrape, Extract, Mine Data From Any Web Into CSV And Excel. Please go to the following link https://www.fiverr.com/iamishraqhc/scrape-extract-mine-data-from-any-web-into-csv-and-excel?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=y8y0q"]
    image_path = ""
    group_links = ['https://www.facebook.com/groups/121968305178198/',
                   'https://www.facebook.com/groups/762886083799826/',
                   'https://www.facebook.com/groups/769584619785908/',
                   'https://www.facebook.com/groups/getprojectsupwork/',
                   'https://www.facebook.com/groups/1515095995417244/',
                   'https://www.facebook.com/groups/143184119689359/',
                   'https://www.facebook.com/groups/Make.Money.Online.Club24/',
                   'https://www.facebook.com/groups/makemoneyonlinee/',
                   'https://www.facebook.com/groups/778428312272760/',
                   'https://www.facebook.com/groups/212851892476720/',
                   'https://www.facebook.com/groups/allfiverrhelp/',
                   'https://www.facebook.com/groups/1048698711880571/',
                   'https://www.facebook.com/groups/455654264473214/']

    # delete cache
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference("browser.cache.disk.enable", False)
    # profile.set_preference("browser.cache.memory.enable", False)
    # profile.set_preference("browser.cache.offline.enable", False)
    # profile.set_preference("network.http.use-cache", False)

    # Path to geckodriver executable
    driver = webdriver.Chrome(
        executable_path=r'E:\freelance\social-media-automation\chromedriver.exe')
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
