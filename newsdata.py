#! /usr/local/bin/python3
import psycopg2


top_three_articles = """select title, views
from article_views
limit 3;"""

top_three_authors = """select authors.name,sum(article_views.views) as views
from article_views,authors
where authors.id = article_views.author
group by authors.name 
order by views desc
limit 3;"""

day_with_most_errors = """select * from errors
where error_percentage > 1.0;"""


def get_results(sql_query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    return results
    db.close()


if __name__ == '__main__':
    print("\n1.Top three articles are:\n")
    articles = (get_results(top_three_articles))
    for row in articles:
        print("\"%s\" - %s views" % (row[0], row[1]))

    print("\n\n2.Top three authors are:\n")
    authors = (get_results(top_three_authors))
    for row in authors:
        print("%s - %s views" % (row[0], row[1]))

    print("\n\n3.Days with more than 1% of requests lead to errors are:\n")
    errors = (get_results(day_with_most_errors))
    for row in errors:
        print("%s - %s%% errors" % (row[0], row[1]))

    print("\n")