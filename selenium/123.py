import HTMLTestRunner
import time
from selenium import webdriver
import unittest

class McTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/')

    def testBody(self):
        '''测试主体'''
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_name('username').send_keys('thy')
        self.driver.find_element_by_name('password').send_keys('123123')
        self.driver.find_element_by_xpath('//*[@id="jsLoginBtn"]').click()
        self.driver.find_element_by_xpath('/html/body/section[1]/header/div/div[1]/div/div[2]/dl').click()
        self.driver.find_element_by_xpath('/html/body/section[1]/header/div/div[1]/div/div[2]/div/div/a[2]').click()
    def testDown(self):
        self.driver.quit()


if __name__=='__main__':
    test=unittest.TestSuite()
    test.addTest(McTest('testBody'))
    file_result = open('132te.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title='McTest测试报告', description='用例的执行情况')
    runner.run(test)
    file_result.close()
# if __name__=='__main__':
#     test = unittest.TestSuite()
#     test.addTest(McTest('testBody'))
#     file_result = open('test.html', 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title='McTest测试报告', description='用例的执行情况')
#     runner.run(test)
#     file_result.close()
