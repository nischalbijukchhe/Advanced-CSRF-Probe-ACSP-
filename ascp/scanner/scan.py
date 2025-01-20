import requests
from bs4 import BeautifulSoup
import threading

def scan_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    forms = soup.find_all('form')
    for form in forms:
        print(f"[+] Potential CSRF vulnerability found: {form['action']}")

def multi_threaded_scan(url, threads):
    threads_list = []
    for _ in range(threads):
        thread = threading.Thread(target=scan_url, args=(url,))
        threads_list.append(thread)
        thread.start()
    for thread in threads_list:
        thread.join()

def main():
    parser = argparse.ArgumentParser(description='ACSP Scanner')
    parser.add_argument('-u', '--url', help='Target URL', required=True)
    parser.add_argument('-t', '--threads', help='Number of threads', type=int, default=10)
    args = parser.parse_args()
    multi_threaded_scan(args.url, args.threads)

if __name__ == '__main__':
    main()
