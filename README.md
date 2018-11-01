# Log Analysis
This's the First project of Udacity Full Stack Nanodegree, it came up with a large database containing 3 tables : Articles Authors and logs of users accessing these articles. the project requirements is to answer the following questions:
1. What are the most popular three articles of all time?
2. What are the most popular three articles of all time?
3. On which days did more than 1% of requests lead to errors?

## Purpose of this project:
stretching SQL database skills. by getting practice interacting with a live database both from the command line and from python code. and exploring a large database with over a million rows. And building and refining complex queries and use them to draw business conclusions from data.
## what Log Analysis does:
Building an informative summary from logs is a real task that comes up very often in software engineering.

## Log Analysis Setup:
- Install Vagrant
- VirtualBox
- python 2
- Clone this repository
- news database download link: [Link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Log Analysis running steps:
Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`
To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.
