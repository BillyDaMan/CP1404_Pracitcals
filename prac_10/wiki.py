import wikipedia


search = input("Search (page title): ")
while search != "":
    page = wikipedia.page(search)
    print("Title:", page.title)
    print(wikipedia.summary(page))
    print("URL:", page.url)
    search = input("Search (page title): ")
print("Goodbye")
