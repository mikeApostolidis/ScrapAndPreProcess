from selenium import webdriver


def driver_init():
    print("Creating Chrome Driver")

    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": r"C:\sxoli\preprocess_folder"}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless=new")  # comment it if you want headless=false
    my_driver = webdriver.Chrome(options=chrome_options)
    yield my_driver
    print("Closing Chrome Driver")
    my_driver.quit()


