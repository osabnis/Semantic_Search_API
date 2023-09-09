from urllib.parse import urlparse
import os
import string
import uuid
import requests
from bs4 import BeautifulSoup


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(
        parsed.scheme) and '.pdf' not in url and '.jpg' not in url and '.docx' not in url


def folder_creation():
    task_id = uuid.uuid1()
    folder = r"D:/USC Academics/Semester 2/Natural Language Processing/Project/api/data/" + str(task_id) + "/"
    final_directory = os.path.join(folder, r'flat_files')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    return final_directory


def write_content_to_file(url_set, file_folder):
    try:
        print("Writing to files...")
        for url in url_set:
            text = ''
            response = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
            url_soup = BeautifulSoup(response.text, 'html.parser')
            for div in url_soup.findAll('div', {'class': 'content-area'}):
                for line in div.strings:
                    line = line.strip()
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    if not line.isspace() and line:
                        text += line + " ======> " + str(url) + '\n'
            if text:
                file = open(file_folder + "/" + str(uuid.uuid4()) + ".txt", 'w+', encoding='utf-8')
                file.write(text)
                file.close()
        return "Files Created and Stored!"
    except Exception as e:
        return "There was an issue: " + str(e)



whitelist = ['https://coronavirus.usc',
             'https://policy.usc.edu',
             'https://sites.google.com/usc.edu',
             'https://studenthealth.usc.edu']


def find_nested_urls(url, file_folder, urls_set):
    try:
        response = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            nested_url = link.get('href')
            if nested_url not in urls_set and is_valid(nested_url) and any(xs in nested_url for xs in whitelist):
                print(nested_url)
                urls_set.add(nested_url)
                find_nested_urls(nested_url, file_folder=file_folder, urls_set=urls_set)
        return urls_set
    except Exception as e:
        return "There was an issue: " + str(e)


# def convert_content_to_text(url):
#     try:
#         task_id = uuid.uuid1()
#         folder = r"D:/USC Academics/Semester 2/Natural Language Processing/Project/api/data/" + str(task_id) + "/"
#         os.mkdir(folder)
#         file_folder = folder + "flat_files"
#         os.mkdir(file_folder)
#         response = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
#         soup = BeautifulSoup(response.text, 'html.parser')
#         tag = soup.body
#         file = open(file_folder + "/" + "main.txt", "w", encoding='utf-8')
#         if tag is not None:
#             for div in soup.findAll('div', {'class': 'content-area'}):
#                 # file.write(div.text.strip())
#                 for line in div.strings:
#                     line = line.strip()
#                     line = line.translate(str.maketrans('', '', string.punctuation))
#                     if not line.isspace() and line:
#                         file.write(line + " ======> " + str(url) + '\n')
#         file.close()
#         urls = set()
#         for link in soup.find_all('a'):
#             url_1 = link.get('href')
#             if is_valid(url_1):
#                 urls.add(url_1)
#         counter = 1
#         for url in urls:
#             print(url)
#             file = open(file_folder + "/" + str(counter) + ".txt", "w", encoding='utf-8')
#             counter += 1
#             resp = requests.get(url)
#             url_soup = BeautifulSoup(resp.text, 'html.parser')
#             tags = url_soup.body
#             if tags is not None:
#                 for div in url_soup.findAll('div', {'class': 'content-area'}):
#                     # file.write(div.text.strip())
#                     for line in div.strings:
#                         line = line.strip()
#                         line = line.translate(str.maketrans('', '', string.punctuation))
#                         if not line.isspace() and line:
#                             file.write(line + " ======> " + str(url) + '\n')
#             file.close()
#         return "Files Created and Stored!"
#     except Exception as e:
#         return "There was an issue: " + str(e)

