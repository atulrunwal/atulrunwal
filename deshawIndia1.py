import requests
from bs4 import BeautifulSoup

# import csv

# f = open('jobs_data1.csv', 'w') write_file = csv.writer(f) write_file.writerow(['job_title', 'company_name',
# 'page_url', 'desirable_candidate','day_today_responsibility', 'experience', 'abstract', 'address',
# 'application_message'])

# '/careers/sourcing-manager-international-human-resources-operations-and-projects-hyderabad-3347'
# '/careers/front-office-tech-senior-member-technical-or-project-lead-software-developer-all-positions-hyderabad-2614'


html_file = requests.get('https://www.deshawindia.com/careers/sourcing-manager-international-human-resources'
                         '-operations-and-projects-hyderabad-33477')
soup = BeautifulSoup(html_file.text, 'lxml')
# print(soup)
# page_url = html_file.url
# experience = 'Nan'
# application_message = 'Join our team in Hyderabad'
# try:
# # job title
job_title = soup.find('div', class_='header').h1
print(job_title)

# # company name
# company_name = soup.find('div', class_='logo').a.svg['alt']
# print(company_name)


# # url


# # desirable candidate
# desirable_candidate = soup.find('div', class_='wrapper').p.text
# print(desirable_candidate)

# # day-today-responsibility
# day_today_responsibility = soup.find('div', class_='PageTextBox').p.text
# print(day_today_responsibility)

# experience


# abstract
# abstract = soup.find('div', class_='specific-job-disclaimer').text
# if abstract == None:
#     abstract = 'NaN'
# print(abstract)

#  address
# address = soup.find('div', class_='headquarters').text
# print(address)
print('everything executed properly')

# print(application_message)

# except Exception as e:
#     job_title=None
#     company_name=None
#     desirable_candidate=None
#     day_today_responsibility=None
#     abstract=None
#     address=None

# writing in csv write_file.writerow([job_title, company_name, page_url, desirable_candidate,
# day_today_responsibility, experience, abstract, address, application_message]) print('writen in file') f.close()
