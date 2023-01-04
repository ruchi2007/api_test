
from selenium import webdriver
def test_selenium():

    url = 'http://uat-iqrashopingdemo.ml/'
    driver_path = "C:\\Users\\takia\\Documents\\workspace_python\\api_test\\chromedriver.exe"
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    print(driver.title)
    expected_title="Iqra shoping Demo"
    actual_title=driver.title
    assert expected_title==actual_title, "title is not maching"