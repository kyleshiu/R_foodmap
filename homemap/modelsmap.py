from django.db import models
from django.db import connection
from django.shortcuts import render,redirect


class Restaurant:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from restaurantinfo")
            datas = cursor.fetchall()
        return datas
    
    def single(self,id):
        with connection.cursor() as cursor:
            cursor.execute("select * from restaurantinfo where id=%s",(id,))
            data = cursor.fetchone()
        return data

    def create(self,restaurantinfo):
        with connection.cursor() as cursor:
            sql = """INSERT INTO restaurantinfo(id,restaurantname,foodtype,address,phone,website)
                     VALUES(%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,restaurantinfo)

    def update(self,restaurantinfo):
        with connection.cursor() as cursor:
            sql = """UPDATE restaurantinfo set id=%s,restaurantname=%s,foodtype=%s,address=%s,phone=%s,website=%s
                     where id=%s"""
            cursor.execute(sql,restaurantinfo)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = "delete from restaurantinfo where id=%s"
            cursor.execute(sql,(id,))

    def select(self, request):
        with connection.cursor() as cursor:
            sql='SELECT * FROM restaurantinfo where address LIKE %s '
            cursor.execute(sql,('%' + request + '%'))
            datas = cursor.fetchall()
        return datas 
       
            
                                 
     