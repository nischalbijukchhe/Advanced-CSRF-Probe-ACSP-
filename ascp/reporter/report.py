import csv

def generate_report(results):
    with open('results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Result"])
        for result in results:
            writer.writerow(result)

def main():
    parser = argparse.ArgumentParser(description='ACSP Reporter')
    parser.add_argument('-r', '--results', help='Results file', required=True)
    args = parser.parse_args()
    with open(args.results, 'r') as f:
        results = [line.strip().split(',') for line in f.readlines()]
    generate_report(results)

if __name__ == '__main__':
    main()
