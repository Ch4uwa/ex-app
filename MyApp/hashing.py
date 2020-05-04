"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""
import hashlib
import os
import sys

users = {}  # Temp storage


class Hashing:
    def __init__(self):
        self.hash_name = 'SHA256'
        self.iterations = 100000

    def hash_password(self, password):
        """
        Hash user password
        :param password:
        :return: salt, key
        """
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(hash_name=self.hash_name, password=password.encode('utf-8'), salt=salt,
                                  iterations=self.iterations)
        return salt, key

    def verify_key(self, user_salt, user_key, password):
        """
        Verify user password

        :param user_salt: the salt used
        :param user_key: the user password key
        :param password: tried password
        :return: bool
        """
        new_key = hashlib.pbkdf2_hmac(hash_name=self.hash_name, password=password.encode('utf-8'), salt=user_salt,
                                      iterations=self.iterations)

        try:
            assert user_key == new_key
        except AssertionError:
            # sys.exit()
            return False
        else:
            return True
