import requests

def inject_payload(url, payload):
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"[+] CSRF payload injected successfully: {url}")

def main():
    parser = argparse.ArgumentParser(description='ACSP Injector')
    parser.add_argument('-u', '--url', help='Target URL', required=True)
    parser.add_argument('-p', '--payload', help='Payload file', required=True)
    args = parser.parse_args()
    with open(args.payload, 'r') as f:
        payload = f.read()
    inject_payload(args.url, payload)

if __name__ == '__main__':
    main()
