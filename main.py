# from requests import *
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium .webdriver.chrome.options import Options
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extracty_wwr_jobs
from file import save_to_file

keyword = input("적어: ")

jobs = []
indeed = extract_indeed_jobs(keyword)
wwr = extracty_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)

# file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")
# file.write("Position,Company,Location,URL\n")

# for job in jobs:
#     file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

# file.close()
