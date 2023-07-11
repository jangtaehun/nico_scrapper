from requests import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium .webdriver.chrome.options import Options

def extracty_wwr_jobs(keyword):
    main_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get("{0}{1}".format(main_url, keyword))
    if response.status_code != 200:
        print("zzon ddeok")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all("li")
            job_posts.pop(-1)
            for post in job_posts:
                anchor = post.find_all("a")
                anchor = anchor[1]
                link = anchor["href"]
                company, kind, region = anchor.find_all("span", class_="company") #class에 company가 들어간 것을 전부 찾는다.
                title = anchor.find("span", class_="title") #find는 결과, find_all은 리스트
                job_data ={
                    "link" : f"https://remoteok.com{link}",
                    "company": company.string.replace(",", " "),
                    #"kind" : kind.string,
                    "location" : region.string.replace(",", " "),
                    "position" : title.string.replace(",", " ")
                }
                results.append(job_data)
        return results

print(extracty_wwr_jobs("python"))