#!/usr/bin/python3
import requests
import csv


url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts(link=url):
    response = requests.get(link)

    if response.status_code == 200:
        print(f'Status Code: {response.status_code}')

        json_version = response.json()

        for post in json_version:
            print(post['title'])
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")

def fetch_and_save_posts(link=url):
    list_of_dictionary_to_csv = []
    
    response = requests.get(link)
    
    if response.status_code == 200:

        json_version = response.json()
        
        for post in json_version:
            dict_for_while = {}
            dict_for_while['id'] = post['id']
            dict_for_while['title'] = post['title']
            dict_for_while['body'] = post['body']
            list_of_dictionary_to_csv.append(dict_for_while)
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
    
    with open('posts.csv', 'w', newline='') as file:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in list_of_dictionary_to_csv:
            writer.writerow(item)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
