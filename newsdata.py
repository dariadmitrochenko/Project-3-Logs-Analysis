#! /usr/bin/python3
import psycopg2


top_three_articles = """select title, views
from article_views
limit 3;"""

top_authors = """select authors.name as author_name,
sum(article_views.views) as views
from article_views,authors
where authors.id = article_views.author
group by author_name
order by views desc;"""

day_with_most_errors = """select to_char(date,'FMMonth FMDD, YYYY') as date,
round(error_percentage, 2) as error_percentage
from errors
where error_percentage > 1.0;"""


def get_results(sql_query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results


if __name__ == '__main__':
    print("\n1.Top three articles are:\n")
    articles = (get_results(top_three_articles))
    for title, views in articles:
        print('"{}" - {} views'.format(title, views))

    print("\n\n2.Top authors are:\n")
    authors = (get_results(top_authors))
    for author_name, views in authors:
        print('{} - {} views'.format(author_name, views))

    print("\n\n3.Days with more than 1% of requests lead to errors are:\n")
    errors = (get_results(day_with_most_errors))
    for date, error_percentage in errors:
        print('{} - {}%'.format(date, error_percentage))

    print("\n")
