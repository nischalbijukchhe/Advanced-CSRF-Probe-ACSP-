import argparse
from scanner import scan_url
from injector import inject_payload
from reporter import generate_report
from fuzzer import fuzz_payload
from ml import train_model
from exploits import generate_exploit
from utils import get_proxy, rotate_user_agent, encode_payload

def main():
    parser = argparse.ArgumentParser(description='Advanced CSRF Probe (ACSP)')
    parser.add_argument('-u', '--url', help='Target URL', required=True)
    parser.add_argument('-p', '--payload', help='Payload file')
    parser.add_argument('-t', '--threads', help='Number of threads', type=int, default=10)
    parser.add_argument('-f', '--fuzz', action='store_true')
    parser.add_argument('-m', '--ml', action='store_true')
    parser.add_argument('-e', '--exploit', action='store_true')
    args = parser.parse_args()

    # Scan URL
    scan_url(args.url)

    # Inject payload
    if args.payload:
        inject_payload(args.url, args.payload)

    # Generate report
    generate_report(args.url)

    # Fuzz payload
    if args.fuzz:
        fuzz_payload(args.payload)

    # Train machine learning model
    if args.ml:
        train_model()

    # Generate exploit
    if args.exploit:
        generate_exploit(args.url, args.payload)

    # Get proxy
    proxy = get_proxy()

    # Rotate user-agent
    user_agent = rotate_user_agent()

    # Encode payload
    encoded_payload = encode_payload(args.payload)

if __name__ == '__main__':
    main()
