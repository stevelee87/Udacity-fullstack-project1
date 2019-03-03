# Udacity-fullstack-project1
First project Udacity's Fullstack Course

## Intro (from Udacity's website)
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## Project info

1) Python version - 3.6.8
2) File structure:
  - **project1.py:** Main code. Please note, if it is the first time you are running this, you may uncomment the line 83. Please note: 
     _# If it is your first time runing this code, then please discomment the next line_
     _# create_table_views(DBNAME)_ this will create SQL views in order to perform the third question of the project.
  - **README:** This file you are reading right now.
  - **output.txt:** This file contains a sample of the _project1.py_ output.
  - **news.sql:** Although this file is necessary to create the PostgreSQL role _news_, we do not uploaded it into the repository, because it is not necessarely to meet the rubric's project specifications.
