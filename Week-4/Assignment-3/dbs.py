import pymysql.cursors
from werkzeug.security import generate_password_hash, check_password_hash

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='assignment',
                             cursorclass=pymysql.cursors.DictCursor)
class Users():
    def _is_email_exist(self, email: str):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM user where email=%s and isActive=%r"
                cursor.execute(sql, (email, True))
                result = cursor.fetchone()
            if result is None:
                return False, 'unused'
        except Exception as e:
            return False, str(e)
        return True, 'used'

    def login(self, email: str, password: str):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM user where email=%s and isActive=%r"
                cursor.execute(sql, (email, True))
                result = cursor.fetchone()
            if result is None:
                return False, 'wrong email or wrong password', None
            is_successful = check_password_hash(result['password'], password)
            if is_successful is False:
                return False, 'wrong email or wrong password', None
        except Exception as e:
            return False, str(e), None
        return True, 'successful', result['id']

    def get_users(self):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM user where isActive = %r"
                cursor.execute(sql, True)
                results = cursor.fetchall()
            if results is None:
                return False, 'Empty', None
        except Exception as e:
            return False, str(e), None
        return True, 'successful', results
    
    def get_user_details(self, email: str):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT id, email FROM user where email=%s and isActive = %r"
                cursor.execute(sql, (email, True))
                result = cursor.fetchone()
            if result is None:
                return False, 'wrong email',None
        except Exception as e:
            return False, str(e), None
        return True, 'successful', result

    def insert_user(self, email: str, password: str):
        try:
            is_exsit, message = self._is_email_exist(email)
            if is_exsit is False and message == 'unused':
                hashed_password = generate_password_hash(password)
                with connection.cursor() as cursor:
                    sql = "INSERT INTO user (email, password, isActive) VALUES (%s, %s, %r)"
                    cursor.execute(sql, (email, hashed_password, True))
                    connection.commit()
            else:
                return False, 'email is already used'
        except Exception as e:
            return False, str(e)
        return True, 'successful'
    
    def remove_user(self, user_id: int):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE user SET isActive = %r where id = %d"
                cursor.execute(sql, (False, user_id))
                connection.commit()
        except Exception as e:
            return False, str(e)
        return True, 'successful'
    
    def update_user(self, user_info: dict):
        try:
            string_infos = ', '.join('{}=%s'.format(field) for field in user_info)
            with connection.cursor() as cursor:
                sql = "UPDATE user SET {}".format(string_infos)
                cursor.execute(sql, user_info.values())
                connection.commit()
        except Exception as e:
            return False, str(e)
        return True, 'successful'
