import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from csv import writer

s = Service("/Users/siddharthatuladhar/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("http://www.nepalstock.com/todaysprice")

# show 500 rows
select = Select(driver.find_element(By.XPATH, '//*[@id="news_info-filter"]/label[3]/select'))
select.select_by_visible_text('500')
total_rows = driver.find_element(By.XPATH, '//*[@id="news_info-filter"]/input[1]')
total_rows.click()


with open("stock.csv", 'w', encoding='utf8', newline='') as x:
    writer = writer(x)
    header = ['Company Name', 'Number of Transactions', 'Max Price', 'Min Price', 'Closing Price', 'Traded Shares',
              'Amount', 'Previous Closing', 'Difference Rs.']
    writer.writerow(header)
    try:
        for i in range(3, 500):
            company_name = driver.find_element(By.XPATH, f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[2]').text
            no_of_transactions = driver.find_element(By.XPATH,
                                                     f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[3]').text
            max_price = driver.find_element(By.XPATH, f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[4]').text
            min_price = driver.find_element(By.XPATH, f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[5]').text
            close_price = driver.find_element(By.XPATH, f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[6]').text
            traded_shares = driver.find_element(By.XPATH, f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[7]').text
            amount = driver.find_element(By.XPATH, f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[8]').text
            prev_close = driver.find_element(By.XPATH, f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[9]').text
            diff = driver.find_element(By.XPATH, f'//*[@id="home-contents"]/table/tbody/tr[{i}]/td[10]').text

            info = [company_name, no_of_transactions, max_price, min_price, close_price, traded_shares, amount,
                    prev_close, diff]
            writer.writerow(info)

    except selenium.common.exceptions.NoSuchElementException:
        print('')

print("Scraping Finished")
driver.close()
driver.quit()
