 
from json import load

f=open("C:\\Users\\leoas\\OneDrive\\Desktop\\pythonworks\\datasets\\books.json")

data=load(f)

# for book in data:

    # print(book)

all_titles=[book.get("title")  for book in data]
# print(all_titles)

page_filter=[book.get("title") for book in data if book.get("pages")<250]

# print(page_filter)

all_genre=[book.get("genre")  for book in data]

# print(set(all_genre ))

genre_count={genre:all_genre.count(genre) for genre in all_genre}

# print(genre_count)

costly_book=max(data,key=lambda d:d.get("price"))
print(costly_book)

all_author=[book.get("author") for book in data]
author_count={auth:all_author.count(auth) for auth in all_author }
print([k for k,v in author_count.items() if v>1])