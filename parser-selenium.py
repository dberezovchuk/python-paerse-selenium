from selenium import webdriver
import csv
import os

urls = []
driver = webdriver.Chrome()


driver.get('https://jobs.dou.ua/ratings/?from=doufp')
company = driver.find_elements_by_xpath("//td[@class='company-name']//a")

for c in company:
    a = c.get_attribute('href')
    url = {
        'href': a
    }
    urls.append(url)


for j in urls:
    driver.get(j['href'])
    company_info = driver.find_element_by_xpath("//div[@class='company-info']").text
    name = company_info.split()[0]
    employees = company_info.split()[2]
    location = driver.find_element_by_xpath("//div[@class='offices']").text
    site = driver.find_element_by_xpath("//div[@class='site']//a")
    site = site.get_attribute('href')


    #path = '/Test Python projects/test_selenium/company.csv'
    with open('company.csv', "a", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        #writer.writerow(['Компания', 'Количество сотрудников', 'Локация офисов', 'Сайт'])
        writer.writerow([name, employees, location, site])

    print(name, employees, location, site)



driver.quit()