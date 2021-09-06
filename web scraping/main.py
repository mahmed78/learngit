from bs4 import BeautifulSoup
import requests
import time

print('put some skill you dont  know about')
unfamiliar_skill=input('>')
print('filtering out{unfamiliar_skill}')


def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)

    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
#print(job)
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
#print(skills)
#print(company_name)
   # published_date=job.find('span',class_='sim-posted').text
                with open('posts/{index}.txt','W')as f:
                    f.write(f"company name:{company_name.strip()}\n")
                    f.write(f"required skills: {skills.strip()}\n")
                    f.write(f"more info: {more}")
                    f.write(f"published date: {published_date.strip()}")
                #print('')
                print(f'file saved: {index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        #time.sleep(600)
        print(f'waiting{time_wait} minutes.......')
        time.sleep(time_wait*60)