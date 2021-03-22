import requests
import json


def getNumberOfMovies():

    r = requests.get('https://jsonmock.hackerrank.com/api/movies/search/?Title=maze')

    print(r.json())

    response = r.json()

    print()
    print("First Title: ", response['data'][0]['Title'])

    print()
    print("Total movies with text 'Maze' in it:", response['total'])
    print()

    travel_values = extract_values(r.json(), 'Title')
    print("All Titles: ", travel_values)


def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results


def main():
    title = 'maze'

    getNumberOfMovies()
    print()
    # print("Number of movies with Title 'Maze';", total)


if __name__ == '__main__':
    main()


def main():



if __name__ == '__main__':
    main()
