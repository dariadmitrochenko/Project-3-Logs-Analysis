# Logs Analysis Project
A reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the *psycopg2* module to connect to the database.

by **[Daria Dmitrochenko](https://github.com/dariadmitrochenko)**

## Prerequisites
* [Python3](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

## Installing and Running
1. Download or Clone this repository in the /vagrant directory
2. Bring your Virtual Machine online by typing `vagrant up` and log in using `vagrant ssh` command in your Terminal, `cd` into `/vagrant` directory
3. Unzip newsdata.sql.zip and load the data in your local database by typing `psql -d news -f newsdata.sql` in your Terminal
4. Create views:
  * Connect to the database by typing `psql -d news`
  * Create view **article_views** by copying and pasting this:
`CREATE VIEW article_views AS SELECT title, author, name, COUNT(log.path) AS views FROM articles, log, authors WHERE log.path LIKE ('%' || articles.slug) AND authors.id = articles.author GROUP BY articles.title, articles.author, authors.name ORDER BY views desc;`
  * Create view **errors** by copying and pasting this: `CREATE VIEW errors AS SELECT date(time),100.0*sum(case log.status WHEN '200 OK' then 0 else 1 end)/count(log.status) as error_percentage FROM log group by date(time) ORDER BY error_percentage desc;`

5. Type `\q` to return to your *vagrant* directory and type `python newsdata.py` to run the python program. Your output in the Terminal should look like this:

```
1.Top three articles are:

"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views


2.Top three authors are:

Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views


3.Days with more than 1% of requests lead to errors are:

2016-07-17 - 2.2626862468027260% errors
```
