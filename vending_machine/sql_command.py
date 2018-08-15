from django.db import connection

class SQLCommand():
    def execute(self, cmd):
        connection.cursor().execute(cmd)


    def execute_with_result(self, cmd):
        with connection.cursor() as cursor:
            cursor.execute(cmd)
            result = cursor.fetchone()[0]
        return result

