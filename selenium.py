import selenium webdiver


class Chrome:
    driver = webdriver.Chrome()

    def getFunc(self, driver):
        driver.get('http://google.com')

    def AssertFunc(self, driver):
        assert 'Google' in driver.source_page

    def quitFunc(self):
        close.quit()


print('sameshit')
print('sameshit')
print('sameshit')
print('sameshit')
print('sameshit')
print('sameshit')
