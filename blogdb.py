#!/usr/bin/env python


import psycopg2


def getMostPopularArticles():
    """Return all posts from the 'database', most recent first."""
    connection = psycopg2.connect("dbname=news")
    cursor = connection.cursor()
    cursor.execute("""select articles.title, count(*) as views
            from articles, log
            where articles.slug = substr(log.path, 10)
            and log.status = '200 OK'
            group by articles.title
            order by views desc
            limit 3""")
    results = cursor.fetchall()
    connection.close()
    final_results = ""
    for result in results:
        final_results += ('{} - {} views \n').format(result[0], result[1])
    return final_results
    return results


def getMostPopularAuthors():
    """Add a post to the 'database' with the current timestamp."""
    connection = psycopg2.connect("dbname=news")
    cursor = connection.cursor()
    cursor.execute("""select authors.name, count(*) as views
        from articles, authors,log
        where articles.author = authors.id
        and articles.slug = substr(log.path, 10)
        and log.status = '200 OK'
        group by authors.name
        order by views desc
        limit 3""")
    results = cursor.fetchall()
    connection.close()
    final_results = ""
    for result in results:
        final_results += ('{} - {} views \n').format(result[0], result[1])
    return final_results


def report():
    """Add a post to the 'database' with the current timestamp."""
    connection = psycopg2.connect("dbname=news")
    cursor = connection.cursor()
    cursor.execute("""
        WITH
        totalRequests AS (
        select date(time) as day, count(*) as requests
        from log
        group by day
        order by requests desc),
        failurRequests AS (
        select date(time) as day, count(*) as failurs
        from log
        where log.status = '404 NOT FOUND'
        group by day
        order by failurs desc),
        failurRate AS (
        select totalRequests.day,
        failurRequests.failurs::float/totalRequests.requests::float * 100
        As rate
        from totalRequests,failurRequests
        where totalRequests.day = failurRequests.day
        )
        select * from failurRate where rate > 1;
        """)
    results = cursor.fetchall()
    connection.close()
    final_results = ""
    for r in results:
        final_results += "{0:%B %d, %Y} - {1:.1f}% errors".format(r[0], r[1])
    return final_results


if __name__ == '__main__':
    # store query results
    print getMostPopularArticles()
    print getMostPopularAuthors()
    print report()
