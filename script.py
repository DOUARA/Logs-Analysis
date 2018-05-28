#!/usr/bin/env python3

import psycopg2

# Database Connect
db = psycopg2.connect(database="news")
c = db.cursor()

# Query: the most popular article of all time.
c.execute("select title, count(path) from log join articles on " +
          "CONCAT('/article/', articles.slug) = log.path GROUP BY title " +
          "order by count(path) desc limit 3;")
results = c.fetchall()
print('The Most Popular Articles of all time:')
for ele in results:
    result = ele[0] + ' - ' + str(ele[1]) + 'views'
    print(result)

# Query: The Most Popular article authors of all time.
c.execute("select authors.name, count(articles.title)" +
          "from articles, authors, log where authors.id = articles.author " +
          "and CONCAT('/article/', articles.slug) = log.path " +
          "GROUP BY authors.name order by count(articles.title) desc;")
results = c.fetchall()
print('\nThe Most Popular article authors of all time:')
for ele in results:
    result = ele[0] + ' - ' + str(ele[1]) + ' views'
    print(result)

# Query: days in which more than 1% of requests leads to errors.
c.execute("select to_char(time,'MM-DD-YY'), 100*count(" +
          "case when status ='404 NOT FOUND' then 1 else null end)/" +
          "count(status) from log  GROUP BY to_char(time,'MM-DD-YY') " +
          "having 100*count(case when status ='404 NOT FOUND' " +
          "then 1 else null end)/count(status) > 1;")
results = c.fetchall()
print('\nDays in which more than 1% of requests leads to errors:')
for ele in results:
    print(ele[0])

db.close()
