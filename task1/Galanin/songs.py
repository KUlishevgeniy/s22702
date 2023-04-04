import psycopg2
drawing = open(file_path, 'rb').read()
        # Read database configuration
conn, cursor = create_connection()
try:
            # Execute the INSERT statement
            # Convert the image data to Binary
            cursor.execute("INSERT INTO cartoon\
            (cartoonID,name,cartoonImg) " +
                    "VALUES(%s,%s,%s)",
                    (cartoonID,name, psycopg2.Binary(drawing)))
            # Commit the changes to the database
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while inserting data in cartoon table", error)
        finally:
            # Close the connection object
            conn.close()
    finally:
        # Since we do not have to do
        # anything here we will pass
        pass