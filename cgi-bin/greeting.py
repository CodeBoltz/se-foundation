import cgi
form = cgi.FieldStorage()
v_name= form.getvalue("name")
print('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello %s</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
  </head>  
  <body>
    <h1>Hello %s</h1>
    
    <p>
    THis is my first website coded with python :)
    </p>
    
  </body>
</html>
'''%(v_name,v_name))
