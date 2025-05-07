from django.db import models
from django.conf import settings
import psycopg2
# Example of a database connection function
def connect_to_database():
    try:
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        print("Database connection successful")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
# Create your models here.
