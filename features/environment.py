from selenium import webdriver
import time

def before_all(context):
    context.driver = webdriver.Chrome('./vendor/chromedriver')
    context.driver.get('localhost:8000')
    # time.sleep(5)

def before_scenario(context, scenario):
    pass

def before_step(context, scenario):
    # time.sleep(2)
    pass

def after_scenario(context, scenario):
    pass

def after_all(context):
    # time.sleep(5)
    context.driver.quit()
