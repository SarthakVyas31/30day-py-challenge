import requests
import time
import concurrent.futures

file_urls = [
    'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
    'https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf'
]

def filedownload(file_url):
    try:
        response = requests.get(file_url)
        file_name = file_url.split('/')[-1] 
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"{file_name} was downloaded......")
    except Exception as e:
        print(f"Error downloading {file_url}: {str(e)}")


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(filedownload, file_urls)

stop = time.perf_counter()


print(f"Finished in {round(start-stop)} secs")