import csv
import requests

def main():
    status_dict = {"Website": "Status"}
    with open(r"check_connectivity\websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            status = requests.get(website).status_code
            status_dict[website] = "working" if status == 200 else "not working"

    with open("website_status.csv", "w", newline="") as fw:
        csv_writer = csv.writer(fw)
        for key, value in status_dict.items():
            csv_writer.writerow([key, value])

if __name__ == "__main__":
    main()
