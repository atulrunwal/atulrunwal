# deshawIndia.py
import csv
import requests
from bs4 import BeautifulSoup


f = open('jobs_data1.csv', 'a')
write_file = csv.writer(f)
# write_file.writerow(['job_title', 'company_name', 'page_url', 'desirable_candidate',
#                      'day_today_responsibility', 'experience', 'abstract', 'address', 'application_message'])


html_file = requests.get('https://www.deshawindia.com/careers/all-positions-in-systems-infrastructure-engineering-hyderabad-2786')
soup = BeautifulSoup(html_file.text, 'lxml')
# print(soup)

# # job title
job_title = soup.find('div', class_='header').h1.text
print(job_title)

# job_title = soup.find_all('div', class_='page-container-centered')
# print(job_title[1].h1.text)


# # company name
company_name = soup.find('div', class_='logo').a.svg['alt']
print(company_name)


# # url
page_url = html_file.url
print(page_url)

# # desirable candidate

# # day-today-responsibility
try:
    desirable_candidate = soup.find('div', class_='wrapper').p.text
    print(desirable_candidate)

    day_today_responsibility = soup.find('div', class_='PageTextBox').p.text
    print(day_today_responsibility)
except Exception as e:
    day_today_responsibility=None
    desirable_candidate=None

# experience
experience = 'Nan'
print(experience)
# abstract
abstract = soup.find('div', class_='specific-job-disclaimer').text
# if abstract == None:
#     abstract = 'NaN'
print(abstract)

#  address
address = soup.find('div', class_='headquarters').text
print(address)

application_message = 'Join our team in Hyderabad'
print(application_message)
# writing in csv
write_file.writerow([job_title, company_name, page_url, desirable_candidate,
                     day_today_responsibility, experience, abstract, address, application_message])
f.close()

# write_file.writerow([application_message])
# f.close()
