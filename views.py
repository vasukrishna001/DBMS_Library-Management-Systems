from django.shortcuts import render,HttpResponse
from django.db import connection
from django.shortcuts import redirect
# Create your views here.
column_dict = {
   'books': ['book_id', 'book_Title', 'shelf_loc', 'ratings', 'book_price', 'genre', 'publisher_id', 'book_authorid'],
   'subscriptions': ['sub_type', 'days_to_return', 'sub_amount'],
   'users': ['user_id', 'user_name', 'age', 'gender', 'Occupation', 'sub_type'],
   'author': ['author_id', 'author_name', 'author_country'],
   'transactions': ['trans_id', 'user_id', 'book_id', 'borrowed_date', 'return_date'],
   'publishers': ['publisher_id', 'publisher_name', 'experience_years', 'ratings', 'books_published']
}
def delete(request,param_id):
     referring_url = request.META.get('HTTP_REFERER')
     #print(referring_url , "hh" ,param_id)
     columns = [ ]
     obj = {'url' : '/author' , 'columns' : columns,'button_name' : "author",'form_name' : "delete_author",'type' : 'delete'}
     if 'author' in referring_url:
       columns = ["Athor Id","Author Name ","Author Country "]
     elif 'books' in referring_url:
       columns = ["Book Id","Book Title ", "Shelf Location:", "Ratings", "Book Price", "Genre", "Publisher ID", "Author ID"]
       obj['url'] = '/books' 
       obj['form_name'] = "delete_books"
       obj['button_name']='books'
     elif 'users' in referring_url:
       columns = ["User_Id","User Name ", "Age", "Gender", "Occupation", "Subscription Type"]
       obj['url'] = '/users'
       obj['form_name'] = "delete_users"
       obj['button_name']='users'
     elif 'subscriptions' in referring_url:
       columns = ["Subscription Type ", "days_to_return", "Amount"]
       obj['url'] = '/subscriptions'
       obj['form_name'] = "delete_subscriptions"
       obj['button_name']='subscriptions'
     elif 'publishers' in referring_url:
       columns = ["Publisher_Id","Publisher Name ", "Experience Years ", "Ratings", "Books Published"]
       obj['url'] = '/publishers'
       obj['form_name'] = "delete_publishers"
       obj['button_name']='publishers'
     elif 'transactions' in referring_url:
       columns = ["Transaction Id","User ID", "Book ID", "Borrowed Date","Return Date"]
       obj['url'] = '/transactions'
       obj['form_name'] = "delete_transactions"
       obj['button_name']='transactions'
 
     obj['columns'] = columns  
     return render(request,'add.html',obj)
def sf(request,param_id):
     referring_url = request.META.get('HTTP_REFERER')
     #print(referring_url , "hh" ,param_id)
     columns = [ ]
     obj = {'url' : '/author' , 'columns' : columns,'button_name' : "author",'form_name' : "filter_author" ,'type' : 'get'}
     if 'author' in referring_url:
       columns = ["Athor Id","Author Name ","Author Country "]
     elif 'books' in referring_url:
       columns = ["Book Id","Book Title ", "Shelf Location:", "Ratings", "Book Price", "Genre", "Publisher ID", "Author ID"]
       obj['url'] = '/books' 
       obj['form_name'] = "filter_books"
       obj['button_name']='books'
     elif 'users' in referring_url:
       columns = ["User_Id","User Name ", "Age", "Gender", "Occupation", "Subscription Type"]
       obj['url'] = '/users'
       obj['form_name'] = "filter_users"
       obj['button_name']='users'
     elif 'subscriptions' in referring_url:
       columns = ["Subscription Type ", "days_to_return", "Amount"]
       obj['url'] = '/subscriptions'
       obj['form_name'] = "filter_subscriptions"
       obj['button_name']='subscriptions'
     elif 'publishers' in referring_url:
       columns = ["Publisher_Id","Publisher Name ", "Experience Years ", "Ratings", "Books Published"]
       obj['url'] = '/publishers'
       obj['form_name'] = "filter_publishers"
       obj['button_name']='publishers'
     elif 'transactions' in referring_url:
       columns = ["Transaction Id","User ID", "Book ID", "Borrowed Date","Return Date"]
       obj['url'] = '/transactions'
       obj['form_name'] = "filter_transactions"
       obj['button_name']='transactions'
 
     obj['columns'] = columns  
     return render(request,'add.html',obj)
def home(request):
    """
    ###row = []
    with connection.cursor() as cursor:
        
        query ='''
          INSERT INTO Author values ((select max(author_id ) from Author) + 1,  'Iyedr','pp')
        '''
        cursor.execute(query)###
         """
    return render(request,'home.html')
def main(request,param_id):
    """
    ###row = []
    with connection.cursor() as cursor:
        
        query ='''
          INSERT INTO Author values ((select max(author_id ) from Author) + 1,  'Iyedr','pp')
        '''
        cursor.execute(query)###
         """
    return render(request,'options.html',{'url' : ("/" +param_id)})
def get(request,param_id):
   row = []
   with connection.cursor() as cursor:
          query = f"select * from {param_id}"
          cursor.execute(query)###
          row = cursor.fetchall()
          #print(row)
   return render(request,'display.html',{'data' : row})      
def add(request,param_id):
     referring_url = request.META.get('HTTP_REFERER')
     #print(referring_url , "hh" ,param_id)
     columns = [ ]
     obj = {'url' : '/author' , 'columns' : columns,'button_name' : "author",'form_name' : "add_author" ,"name" : param_id,'type' : 'add'}
     if 'author' in referring_url:
       columns = ["Author Name ","Author Country "]
     elif 'books' in referring_url:
       columns = ["Book Title ", "Shelf Location:", "Ratings", "Book Price", "Genre", "Publisher ID", "Author ID"]
       obj['url'] = '/books' 
       obj['form_name'] = "filter_books"
       obj['button_name'] = 'Books'
     elif 'users' in referring_url:
       columns = ["User Name ", "Age", "Gender", "Occupation", "Subscription Type"]
       obj['url'] = '/users'
       obj['form_name'] = "filter_users"
       obj['button_name'] = 'User'
     elif 'subscriptions' in referring_url:
       columns = ["Subscription Type ", "days_to_return", "Amount"]
       obj['url'] = '/subscriptions'
       obj['form_name'] = "filter_subscriptions"
       obj['button_name'] = 'Subscription'
     elif 'publishers' in referring_url:
       columns = ["Publisher Name ", "Experience Years ", "Ratings", "Books Published"]
       obj['url'] = '/publishers'
       obj['form_name'] = "filter_publishers"
       obj['button_name'] = 'Publisher'
     elif 'transactions' in referring_url:
       columns = ["User ID", "Book ID", "Borrowed Date","Return Date"]
       obj['url'] = '/transactions'
       obj['form_name'] = "filter_transactions"
       obj['button_name'] = 'Transaction'
     obj['columns'] = columns  
     return render(request,'add.html',obj)
def filter(request,param_id,param_id2):
    temp =  list(request.POST.values())
    temp = temp[1 : ]
    #temp = list(map(lambda ele :  ele if ele.isnumeric() else "'" + ele + "'" ,temp))
    print(column_dict[param_id])
    new_list = []
    for i in range(len(temp)):
       x = temp[i].strip()
       temp[i] = temp[i].strip()
       if len(x)!=0:
        if not temp[i].isnumeric():
            temp[i] =  "'" + temp[i] + "'"
        new_list.append(column_dict[param_id][i]+ '=' + temp[i]  )

    new_list = ' and '.join(new_list)   
    print(new_list,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")    
    query = f"select * from {param_id} where {new_list}"
    print(query , "wsRFSFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    row = []
    try :
      with connection.cursor() as cursor:
        cursor.execute(query)###
        row = cursor.fetchall()
        print(row)
    except:
       row = []    
    print(temp)
    return render(request,'display.html',{'data' : row})  
def del_filter(request,param_id,param_id2):
    temp =  list(request.POST.values())
    temp = temp[1 : ]
    #temp = list(map(lambda ele :  ele if ele.isnumeric() else "'" + ele + "'" ,temp))
    print(column_dict[param_id])
    new_list = []
    for i in range(len(temp)):
       x = temp[i].strip()
       temp[i] = temp[i].strip()
       if len(x)!=0:
        if not temp[i].isnumeric():
            temp[i] =  "'" + temp[i] + "'"
        new_list.append(column_dict[param_id][i]+ '=' + temp[i]  )

    new_list = ' and '.join(new_list)   
    print(new_list,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")    
    query = f"delete from {param_id} where {new_list}"
    print(query , "wsRFSFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    row = []
    try :
      with connection.cursor() as cursor:
        cursor.execute(query)###
    except:
       row = []    
    print(temp)
    return redirect('/' + param_id)
    return render(request,'display.html',{'data' : row})  
def sum(request,param_id,param_id2):    
   #print(param_id,param_id2)
   id_name = {"author" : 'author_id'  , "books" : 'book_id' , "users" : 'user_id',"transcations" : 'trans_id',
              "publishers" : 'publisher_id'}
   new_id =  1
   with connection.cursor() as cursor:
        try : 
          query = f"select max({id_name[param_id]}) from {param_id}"
          print(query)
          cursor.execute(query)###
          row = cursor.fetchall()
          print(row)
          new_id = row[0][0] + 1 
          print(new_id)
        except:
           new_id = 1 

        temp =  list(request.POST.values())
        temp = temp[1 : ]
        data = []
        if "subscriptions" != param_id:
         data = [str(new_id)]
 
        temp = list(map(lambda ele :  ele if ele.isnumeric() else "'" + ele + "'" ,temp))
        data.extend(temp)
        sql_query = f"INSERT INTO {param_id} VALUES ({', '.join(data)})"
        cursor.execute(sql_query)###
        print(data)   
   return redirect('/' + param_id)
   return render(request,'options.html')
    
def update(request,param_id):
     referring_url = request.META.get('HTTP_REFERER')
     #print(referring_url , "hh" ,param_id)
     columns = [ ]
     obj = {'url' : '/author' , 'columns' : columns,'button_name' : "author",'form_name' : "update_author",'type': 'update','name':param_id}
     if 'author' in referring_url:
       columns = ["Author Id","Author Name ","Author Country "]
     elif 'books' in referring_url:
       columns = ["Book Id","Book Title ", "Shelf Location:", "Ratings", "Book Price", "Genre", "Publisher ID", "Author ID"]
       obj['url'] = '/books' 
       obj['form_name'] = "update_books"
       obj['button_name'] = 'books'
     elif 'users' in referring_url:
       columns = ["User Id","User Name ", "Age", "Gender", "Occupation", "Subscription Type"]
       obj['url'] = '/users'
       obj['form_name'] = "update_users"
       obj['button_name'] = 'users'
     elif 'subscriptions' in referring_url:
       columns = ["Subscription Type ", "days_to_return", "Amount"]
       obj['url'] = '/subscriptions'
       obj['form_name'] = "update_subscriptions"
       obj['button_name'] = 'subscriptions'
     elif 'publishers' in referring_url:
       columns = ["Publisher Id","Publisher Name ", "Experience Years ", "Ratings", "Books Published"]
       obj['url'] = '/publishers'
       obj['form_name'] = "update_publishers"
       obj['button_name'] = 'publishers'
     elif 'transactions' in referring_url:
       columns = ["Transaction Id","User ID", "Book ID", "Borrowed Date","Return Date"]
       obj['url'] = '/transactions'
       obj['form_name'] = "update_transactions"
       obj['button_name'] = 'transactions'
     obj['columns'] = columns  
     return render(request,'update.html',obj)
def upd(request,param_id,param_id2):
   temp =  list(request.POST.values())
   temp= temp[1:]
   ind = len(temp)
   ind = int(ind/2)
   temp_one = temp[ : ind]
   temp_two = temp[ind : ]
   print(temp_one)
   print(temp_two)
   new_list_filter = []
   temp = temp_one
   for i in range(len(temp)):
       x = temp[i].strip()
       temp[i] = temp[i].strip()
       if len(x)!=0:
        if not temp[i].isnumeric():
            temp[i] =  "'" + temp[i] + "'"
        new_list_filter.append(column_dict[param_id][i]+ '=' + temp[i]  )
   new_list_filter = ' and '.join(new_list_filter)   
   upd_list_filter = []
   temp = temp_two
   for i in range(len(temp)):
       x = temp[i].strip()
       temp[i] = temp[i].strip()
       if len(x)!=0:
        if not temp[i].isnumeric():
            temp[i] =  "'" + temp[i] + "'"
        upd_list_filter.append(column_dict[param_id][i]+ '=' + temp[i]  )
   upd_list_filter = ' , '.join(upd_list_filter)   
   query = f"update {param_id} set {upd_list_filter} where {new_list_filter}"
   #print(query)
   row = []
   try :
      with connection.cursor() as cursor:
        cursor.execute(query)###
   except:
       row = []    
   return redirect("/" + param_id)
def sp(request,param_id):
    #print(param_id)
    if param_id == 3:
        query = '''
         select users.age,users.gender,users.occupation from transactions,users 
where users.user_id = transactions.user_id and (return_date ::date - borrowed_date::date)>5
group by users.user_id having count(users.user_id)>2;



        '''
    if param_id == 2:
        query = '''
        WITH CTE_date AS     (
    SELECT MAX(Borrowed_date) AS last_borrowed FROM Transactions)
SELECT Aut.Author_name,     
COUNT(CASE  WHEN Ts.Borrowed_date>=(SELECT  DATE(last_borrowed)-INTERVAL'10 years'  FROM CTE_date) 
	        THEN 1 END) AS last_10Y ,
COUNT(CASE WHEN Ts.Borrowed_date>=(SELECT  DATE(last_borrowed) -INTERVAL'3 years'  FROM CTE_date) 
	  THEN 1 END) AS  last_3Y ,
COUNT(CASE  WHEN Ts.Borrowed_date>=(SELECT  DATE(last_borrowed)- INTERVAL'1 year'  FROM CTE_date) 
	  THEN 1 END) AS  last_Y
FROM Transactions Ts
JOIN Books  ON Ts.Book_id = Books.Book_id JOIN Author Aut ON Books.Book_authorid = Aut.Author_id
GROUP BY Aut.Author_name ORDER BY last_10Y DESC, last_3Y DESC, last_Y DESC;
          
        '''
    if param_id == 1:
      query = '''
        select TT.genre from
         (select genre, count (distinct (transactions.user_id)) as cnt
        from transactions inner join books on transactions.book_id = books.book_id
        group by genre) TT
        where TT.cnt =
        (select max(T.cnt) from
        (select genre, count (distinct (transactions.user_id)) as cnt
        from transactions inner join books on transactions.book_id = books.book_id
        group by genre) T);
          
        '''
    row = []
    #print(query)
    try :
      with connection.cursor() as cursor:
        cursor.execute(query)###
        row = cursor.fetchall()
        #print(row)
    except:
       row = []    
    return render(request,'display.html',{'data' : row})   
       
    return redirect("/")