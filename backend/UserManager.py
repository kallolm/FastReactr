import psycopg2
import bcrypt
import os
from pydantic import BaseModel



class User(BaseModel):
    name: str
    email: str
    password: str


class UserDataHandler():
    def __init__(self):   
        self.con = psycopg2.connect(database=os.getenv('POSTGRES_DB',default="localhost"), user=os.getenv('POSTGRES_USER',default="postgres"), password=os.getenv('POSTGRES_PASSWORD',default="password"), host=os.getenv('DB_HOST',default="localhost"), port="5432")
        self.cursor = self.con.cursor()
    
    def close(self):
        self.con.close()

    def get_user(self, data: User):
        query = "select * from public.users where email='{}'".format(data.email)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            return []
        return list(rows[0])

    def authenticate_user(self, data: User):
        if not self.check_user(data):
            return False
        user = self.get_user(data)
        return self.check_password(data.password, user[2])

    def check_user(self, data: User):
        if self.get_user(data):
            return True
        return False

    def add_user(self, data: User):
        if self.check_user(data):
            return False
        data.password = self.password_hasher(data.password)
        self.cursor.execute("INSERT INTO public.users (email,password,name) VALUES ( '{}', '{}','{}' );".format(data.email, data.password,data.name))
        self.con.commit()
        return True


    def user_db_init_data(self):
        self.add_user({'email':'pr@gm.com', 'password':'pwd','user':'kallol'})


    def password_hasher(self, plain_text_password: str):
        # Hash a password for the first time
        #   (Using bcrypt, the salt is saved into the hash itself)
        return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
