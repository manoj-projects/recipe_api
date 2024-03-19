from django.db import connections

class MobileModel:
    @classmethod
    def login(cls, emis_username):
        # Define your raw SQL query with a parameter placeholder (%s)
        sql_query = """
            SELECT * FROM emis_userlogin eu WHERE emis_username = %s
        """
        # Execute the raw SQL query on the default database
        with connections['default'].cursor() as cursor:
            cursor.execute(sql_query, [emis_username])
            row = cursor.fetchone()  # Fetch only one row
        
        if row:
            # Process the query result into a dictionary
            login_details = dict(zip([col[0] for col in cursor.description], row))
            return login_details
        else:
            return None  # User not found
