import wikipedia


def main():
    while True:
        search_phrase = input(">>>Enter a phrase:  ")
        if search_phrase != '':
            try:
                search_title = wikipedia.search(search_phrase)[0]
                print(search_title)
                print(wikipedia.summary(search_title))
                search_page = wikipedia.page(search_title)
                print(search_page.url)
            except IndexError:
                print('No result')
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)

        else:
            break


if __name__ == '__main__':
    main()
