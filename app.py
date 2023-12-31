import time
import random

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import undetected_chromedriver as uc

# write to csv file
def write_to_csv(data):
    with open('result.csv', 'a') as f:
        f.write(f'{data}\n')
    

# clear csv file
def clear_csv():
    with open('result.csv', 'w') as f:
        f.write('domain_name;sum;indexed;not_indexed;percentage\n')


def get_domains():
    with open('domains.txt', 'r') as f:
        list2 = [row.split()[0].replace('"','') for row in f]
    return list2


options = uc.ChromeOptions()
profile = r"C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\Profile 3"
options.add_argument(f"user-data-dir={profile}")
driver = uc.Chrome(options=options, use_subprocess=True)

clear_csv()
domains = get_domains()
domains_len = len(domains)
i = 1
for domain in domains:
    
    try:
        if "http" in domain:
            driver.get(f"https://search.google.com/u/0/search-console/index?resource_id={domain}")
        else:
            driver.get(f"https://search.google.com/u/0/search-console/index?resource_id=sc-domain%3A{domain}")

        time.sleep(random.randint(3,7))
        ibndex_box_values = driver.find_elements(By.XPATH, "//div[@class='nnLLaf vtZz6e']")
        
        not_indexed = ibndex_box_values[0].text
        indexed = ibndex_box_values[1].text
        pages_sum = int(not_indexed)+int(indexed)
        percentage = int(not_indexed) / pages_sum

        data = f"{domain};{pages_sum};{indexed};{not_indexed};{percentage}"
        write_to_csv(data)
        print("✅ — [",i,"/",domains_len,"] >> ", domain)
        i += 1
    except Exception as ex:
        data = f"{domain};error"
        write_to_csv(data)
        print("💔 — [",i,"/",domains_len,"] >> ", domain)
        i += 1
        # print(ex)
        continue
    
    