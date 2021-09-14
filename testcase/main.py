from testcase.page import MainPaige
import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def tearDown(self):
        self.driver.close()

    def test_example():
        print("Test")
        assert False

    def test_example_2(self):
        assert True

    def test_search_python(self):
        mainPage = page.MainPaige(self.driver)
        assert MainPaige.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_title(self):
        MainPaige = page.MainPaige()
        assert MainPaige.is_title_matches()

if __name__ == "__main__":
    unittest.main()
