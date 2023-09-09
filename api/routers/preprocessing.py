from fastapi import APIRouter
from api.app.preprocessing.parse_website import parse_website
from api.app.preprocessing.web2text import find_nested_urls, folder_creation, write_content_to_file
from api.app.preprocessing.process import process

router = APIRouter(tags=["Preprocessing"])


@router.get("/preprocessing/scraping/", description="Scrapes the content from the website!")
def scrape_website_content(website_url: str):
    result = parse_website(url=website_url)
    return result


@router.post("/preprocessing/web2text", description="Converts website content to flat text files!")
def convert_web_to_text(website_url: str):
    fl_folder = folder_creation()
    urls = set()
    urls = find_nested_urls(url=website_url, file_folder=fl_folder, urls_set=urls)
    print("How many URLS = ", len(urls))
    result = write_content_to_file(url_set=urls, file_folder=fl_folder)
    return result


@router.get("/preprocessing/processing", description="Process the website text content!")
def preprocess(dataset_id: str):
    result = process(dataset_id=dataset_id)
    return result
