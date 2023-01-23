import sqlite3


def search_by_name(name):
    result = []
    with sqlite3.connect('data/netflix.db') as connection:
        cursor = connection.cursor()
        query = (f" SELECT title, country, release_year, listed_in, description"
                 f" FROM netflix "
                 f" WHERE title == '{name}'"
                 f" AND type = 'Movie'"
                 f" ORDER BY release_year DESC "
                 f" LIMIT 2")
        cursor.execute(query)
        pre_result = cursor.fetchall()
        if pre_result != []:
            result = {
                "title": pre_result[0][0],
                "country": pre_result[0][1],
                "release_year": pre_result[0][2],
                "genre": pre_result[0][3],
                "description": pre_result[0][4]
            }

        return result


def search_movies_by_year(year1, year2):
    result = []
    with sqlite3.connect('data/netflix.db') as connection:
        cursor = connection.cursor()
        query = (f" SELECT title, release_year"
                 f" FROM netflix "
                 f" WHERE release_year BETWEEN '{year1}' AND '{year2}'"
                 f" AND type = 'Movie'"
                 f" LIMIT 100 ")
        cursor.execute(query)
        pre_result = cursor.fetchall()
        if pre_result != []:
            for i in range(len(pre_result)):
                result.append({
                    "title": pre_result[i][0],
                    "release_year": pre_result[i][1]
                })
        return result


def search_by_rating(rating):
    result = []
    if rating == "children":
        a_r = ('G', 'TV-G')
    elif rating == "family":
        a_r = ('G', 'PG', 'PG-13', 'TV-G')
    elif rating == "adult":
        a_r = ('R', 'NC-17')
    else:
        return []
    with sqlite3.connect('data/netflix.db') as connection:
        cursor = connection.cursor()
        query = (f" SELECT title, rating, description"
                 f" FROM netflix "
                 f" WHERE rating IN {a_r}")
        cursor.execute(query)
        pre_result = cursor.fetchall()
        if pre_result != []:
            for i in range(len(pre_result)):
                result.append({
                    "title": pre_result[i][0],
                    "rating": pre_result[i][1],
                    "description": pre_result[i][2]
                })
        return result


def search_by_genre(genre):
    result = []
    with sqlite3.connect('data/netflix.db') as connection:
        cursor = connection.cursor()
        query = (f" SELECT title, description"
                 f" FROM netflix "
                 f" WHERE listed_in LIKE '%{genre}%'")
        cursor.execute(query)
        pre_result = cursor.fetchall()
        if pre_result != []:
            for i in range(len(pre_result)):
                result.append({
                    "title": pre_result[i][0],
                    "description": pre_result[i][1]
                })
        return result


def actors(actor1, actor2):
    with sqlite3.connect('data/netflix.db') as connection:
        cursor = connection.cursor()
        query = (f' SELECT netflix.cast'
                 f' FROM netflix'
                 f' WHERE "cast"'
                 f" LIKE '%{actor1}%%{actor2}%'")
        cursor.execute(query)
        r = []
        l = {}
        x = []
        result = []
        for i in cursor.fetchall():
            r.append(i[0].split(", "))
        for i in r:
            x += i
        for i in x:
            l[i] = x.count(i)
        for k, v in l.items():
            if v > 2 and k != actor1 and k != actor2:
                result.append(k)
        return(" ".join(result))


def search_film(type, release_date, genre):
    result = []
    with sqlite3.connect('data/netflix.db') as connection:
        cursor = connection.cursor()
        query = (f' SELECT title, description'
                 f' FROM netflix'
                 f" WHERE type = '{type}'"
                 f" AND release_year = '{release_date}'"
                 f' AND listed_in'
                 f" LIKE '%{genre}%'")
        cursor.execute(query)
        pre_result = cursor.fetchall()
        for i in range(len(pre_result)):
            result.append({
                "title": pre_result[i][0],
                "description": pre_result[i][1]
            })
        return result
