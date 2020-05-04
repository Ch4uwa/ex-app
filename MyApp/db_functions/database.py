"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com

Handling database actions
"""
import sys
import os

from MyApp.hashing import Hashing

# Database might change
import sqlite3
base_path = os.path.dirname(os.path.abspath(__file__))
DBNAME = os.path.join(base_path, 'exAPP.db')


class DataBaseActions:
    def __init__(self):
        db_url = None
        db_name = None
        db_username = None
        db_password = None

    def _db_connect(self):
        try:
            with sqlite3.connect(DBNAME) as connection:
                return connection
        except Exception as e:
            print(e)
        finally:
            if connection:
                print('connected')

    def db_query(self):
        pass

    def insert_user(self, username, password):
        """
        Add a new user
        :param username:
        :param password:
        """
        if self._get_user_exists(username):
            print('Unable to add user')
        else:
            salt, key = Hashing().hash_password(password=password)
            try:
                con = self._db_connect()
                cur = con.cursor()

                query = "INSERT INTO user (user_name, key, salt) VALUES (?, ?, ?)"

                data = (username, key, salt)

                cur.execute(query, data)
                con.commit()
                cur.close()

                return True

            except sqlite3.Error as sqle:
                print(sqle)
            finally:
                if con:
                    con.close()

    def _get_user_exists(self, username):
        """
        Look for user in db
        :param username: username to look for
        :return: Bool
        """

        try:
            conn = self._db_connect()
            cur = conn.cursor()

            query = "SELECT EXISTS(SELECT user_name FROM user WHERE user_name=(?))"
            data = (username,)
            cur.execute(query, data)

            exists, = cur.fetchone()

            if exists:
                print('Exists')
                return True
            else:
                print('Register new user')
                return False

        except Exception as e:
            print(e.__class__.__name__ + f': {e}')

    def get_user_info(self, username):
        """
        Todo get more info
        Get user info from database
        :param username: Username
        :return: salt, key
        """
        try:
            conn = DataBaseActions()._db_connect()
            cur = conn.cursor()

            if self._get_user_exists(username):
                query = "SELECT salt, key FROM user WHERE user_name=?"
                data = (username,)

                cur.execute(query, data)
                salt, key = cur.fetchone()
                return salt, key
            else:
                return False

        except sqlite3.Error as se:
            print(se.__class__.__name__ + f': {se}')

    def verify_user(self, username, password):
        """
        Verify if username and password exists, and matches
        :param username: Username
        :param password: Password
        :return: bool
        """
        if self._get_user_exists(username=username):
            salt, key = self.get_user_info(username=username)
            return Hashing().verify_key(user_salt=salt, user_key=key, password=password)
        else:
            return False
