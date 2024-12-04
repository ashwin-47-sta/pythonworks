

movies=[

    {"id":1,"title":"kgf","year":2018,"language":"kanada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kanada","run_time":160},
    {"id":3,"title":"the goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},
]

movie_title=[m.get("title")for m in movies]
print(movie_title)


malayalam_movies=[m.get("title") for m in movies if m.get("language")=="malayalam"]
print(len(malayalam_movies))


 

highest_run_time_movie=max(movies,key=lambda d:d.get("run_time"))
print(highest_run_time_movie.get("title"))

hightest_runtime=highest_run_time_movie.get("run_time")
maz_runtime_movies=[m.get("title") for m in movies if m.get("run_time")==hightest_runtime]
print(maz_runtime_movies)