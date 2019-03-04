import psycopg2

queries = [
  '''
    SELECT
      title, count(title) AS views
    FROM
      articles, log
    WHERE path LIKE CONCAT('%',slug,'%')
    GROUP BY title
    ORDER BY views DESC
    LIMIT 3;
  ''',
  '''
    SELECT
      authors.name, count(articles.author) AS views
    FROM
      articles, log, authors
    WHERE path LIKE CONCAT('%',slug,'%')
    AND authors.id = articles.author
    GROUP BY authors.name
    ORDER BY views DESC;
  ''',
  '''
    SELECT
      date, (error*100.0/total)::NUMERIC(2,1) as error_percentage
    FROM
      table_total
    WHERE (error*100.0/total) > 1;
  '''
]

def fetch_news(query, dbname):
  db = connect_to_postgreSQL(dbname)
  c = db.cursor()
  c.execute(query)
  result = c.fetchall()
  db.close()
  return result

def connect_to_postgreSQL(dbname):
  try:
    database = psycopg2.connect(database=dbname)
  except:
    print("Could not connect to the server!")
  return database

def create_table_views(DBNAME):
    
  views_helpers = '''
    CREATE VIEW table_error AS
    SELECT
    time::timestamp::date as date, count(status) AS error
    FROM
    log
    WHERE status = '404 NOT FOUND'
    GROUP BY date;
        
    CREATE VIEW table_ok AS
    SELECT
    time::timestamp::date as date, count(status) AS ok
    FROM log
    WHERE status = '200 OK' GROUP BY date;
        
    CREATE VIEW table_total AS
    SELECT
    table_error.date, error, ok, (error+ok) AS total
    FROM
    table_error, table_ok
    where table_error.date = table_ok.date;
  '''
    
  db = connect_to_postgreSQL(DBNAME)
  c = db.cursor()
  c.execute(views_helpers)
  db.commit()
  db.close()

DBNAME = "news"
# If it is your first time runing this code, then please discomment the next line.

# create_table_views(DBNAME)

# After runing the line above for the first time, comment it again

for i in range(len(queries)):
  print("\nFetching question number {} ...\n".format(i+1))
  col1, col2 = zip(*fetch_news(queries[i], DBNAME))
  if isinstance(col1[0], str):
    max_col1_size = len(max(col1, key=len))

  half_header = round(max_col1_size/2)

  if i == 0: #First question
    print("{}Article{}  -  Views".format(half_header*" ",(half_header-len("Article"))*" "))
    for row in range(len(col1)):
      print(col1[row].ljust(max_col1_size), " - ", col2[row])


  elif i== 1: #Second question
    print("{}Author{}  -  Views".format(half_header*" ",(half_header-len("Author"))*" "))
    for row in range(len(col1)):
      print(col1[row].ljust(max_col1_size), " - ", col2[row])

  elif i== 2: #Third question
    print("    Date    - Error percentage")
    for row in range(len(col1)):
      print(str(col1[row]), " -    ", col2[row], "%")


    