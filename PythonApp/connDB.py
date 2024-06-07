import pymysql
import mysql.connector
from neo4j import GraphDatabase

driver = None

def neo4j_connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4jneo4j"), max_connection_lifetime=1000)

def establish_connection():
    # Establish connection to the database
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="appDBproj",
        cursorclass=pymysql.cursors.DictCursor
    )

def search_cities_by_country(country_name):
    try:
        # Create a cursor object
        db = establish_connection()
        cursor = db.cursor()

        # SQL query with a placeholder for the country name
        sql = """
        SELECT country.Name AS CountryName, city.Name AS CityName, city.District AS CityDistrict, city.Population AS CityPopulation
        FROM city
        JOIN country ON city.CountryCode = country.Code
        WHERE country.Name LIKE %s
        """

        # Execute the query with the user input as a parameter
        cursor.execute(sql, ('%' + country_name + '%',))

        # Fetch the initial 2 rows
        rows = cursor.fetchmany(2)

        if rows:
            # Display the initial result
            for row in rows:
                print(row["CountryName"], "|", row["CityName"], "|", row["CityDistrict"], "|", row["CityPopulation"])
                
            # Ask user if they want to see more
            while True:
                choice = input("-- Quit (q) --")
                if choice.lower() == 'q':
                    break
                else:
                    # Fetch next 2 cities
                    rows = cursor.fetchmany(2)
                    if rows:
                        for row in rows:
                            print(row["CountryName"], "|", row["CityName"], "|", row["CityDistrict"], "|", row["CityPopulation"])
                    else:
                        print("No more cities available.")
                        break
        else:
            print("No cities found for the country", country_name)

    except pymysql.err.ProgrammingError as e:
        print("Invalid input:", e)
    except pymysql.err.MySQLError as e:
        print("MySQL Error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the cursor and connection
        try:
            if cursor:
                cursor.close()
            if db:
                db.close()
        except Exception as e:
            print("Error closing cursor/connection:", e)

def get_city_details_by_id(city_id):
    try:
        # Create a cursor object
        db = establish_connection()
        cursor = db.cursor()

        # SQL query to retrieve city details by ID
        sql = "SELECT ID, Name, CountryCode, Population, Latitude, Longitude  FROM city WHERE ID = %s"
        
        # Execute the query with city ID as parameter
        cursor.execute(sql, (city_id,))
        
        # Fetch the city details
        city_details = cursor.fetchone()
        
        if city_details:
            city_info = ""
            for value in city_details.values():
                city_info += f"{value} | "  # Append each value to the city_info string with a pipeline
            print(city_info)
            return city_details
        else:
            return None

    except pymysql.err.MySQLError as e:
        print("MySQL Error:", e)
        return None
    finally:
        # Close the cursor and connection
        try:
            if cursor:
                cursor.close()
            if db:
                db.close()
        except Exception as e:
            print("Error closing cursor/connection:", e)

            
def increase_city_population(new_population):
    try:
        # Create a cursor object
        db = establish_connection()
        cursor = db.cursor()

        # SQL query to update population
        sql = "UPDATE city SET Population = Population + %s"
        
        # Execute the query with new population as parameter
        cursor.execute(sql, (new_population,))
        
        # Commit the changes to the database
        db.commit()
        
        # Close the cursor and database connection
        cursor.close()
        db.close()
        
    except pymysql.err.Error as e:
        print(f"Error: {e}")
        if db:
            db.rollback()  # Rollback in case of any error
        
def decrease_city_population(new_population):
    try:
        # Create a cursor object
        db = establish_connection()
        cursor = db.cursor()

        # SQL query to update population
        sql = "UPDATE city SET Population = Population - %s"
        
        # Execute the query with new population as parameter
        cursor.execute(sql, (new_population,))
        
        # Commit the changes to the database
        db.commit()
        
        # Close the cursor and database connection
        cursor.close()
        db.close()
        
    except pymysql.err.Error as e:
        print(f"Error: {e}")
        if db:
            db.rollback()  # Rollback in case of any error
            
# Function to add a person to the database
def add_person(ID, Name, Age, Salary, City):
    try:
        # Connect to MySQL database   
        db = establish_connection()
        
        # Create a cursor object
        cursor = db.cursor()

        # Insert data into the database
        sql = "INSERT INTO person (personID, personname, age, salary, city) VALUES (%s, %s, %s, %s, %s)"
        val = (ID, Name, Age, Salary, City)
        cursor.execute(sql, val)

        # Commit changes
        db.commit()

        # Close connection
        db.close()
    
    except mysql.connector.Error as err:
        print("{err.errno},", "'{err.msg}'")
        raise
    
def person_exists(ID):
    # Connect to MySQL database
    db = establish_connection()
    
    # Create a cursor object
    cursor = db.cursor()

    # Check if ID exists in the database
    cursor.execute("SELECT * FROM person WHERE personID = %s", (ID,))
    result = cursor.fetchall()

    # Close connection
    db.close()

    return bool(result)
    
def city_exists(city_id):
    # Connect to MySQL database
    db = establish_connection()
    
    # Create a cursor object
    cursor = db.cursor()

    # Check if city exists in the database
    cursor.execute("SELECT Name FROM city WHERE ID = %s", (city_id,))
    result = cursor.fetchone()

    # Close connection
    db.close()
    
# Function to delete a person from the database
def delete_person(ID):
    try:
        # Connect to MySQL database   
        db = establish_connection()
        
        # Create a cursor object
        cursor = db.cursor()

        # Insert data into the database
        sql = "DELETE FROM person WHERE personID = %s"
        val = (ID,)
        cursor.execute(sql, val)

        # Commit changes
        db.commit()

        # Close connection
        db.close()

    except mysql.connector.Error as err:
        print("{err.errno},", "'{err.msg}'")
        raise
        
def search_countries(selected_operator, population):
    try:
        # Connect to MySQL database   
        db = establish_connection()
        
        # Create a cursor object
        cursor = db.cursor()

        # Insert data into the database
        sql = f"SELECT code, name, continent, population FROM country WHERE population {selected_operator} %s"

        # Execute the query with the provided operator and population
        cursor.execute(sql, (population,))

        # Fetch the results
        results = cursor.fetchall()
        for country_info in results:
            country_data = " | ".join(map(str, country_info.values()))
            print(country_data)

        # Close connection
        db.close()

    except mysql.connector.Error as err:
        print("{err.errno},", "'{err.msg}'")
        raise
 
def twinned_city():
    if driver is None:
        neo4j_connect()
    with driver.session() as session:
        result = session.run(
            """
            MATCH (c1:City)-[:TWINNED_WITH]-(c2:City)
            RETURN DISTINCT c1.name AS city1, c2.name AS city2
            ORDER BY city1, city2
            """
        )
        twinned_cities = [(record["city1"], record["city2"]) for record in result]
        return twinned_cities
        
def check_dublin_existence():
    if driver is None:
        neo4j_connect()
    with driver.session() as session:
        result = session.run("MATCH (d:City {name: 'Dublin'}) RETURN d").single()
        return result is not None

def add_city_to_neo4j(city_id):
    # Connect to MySQL database
    db = establish_connection()
    
    # Create a cursor object
    cursor = db.cursor()

    # Fetch city information
    cursor.execute("SELECT * FROM city WHERE ID = %s", (city_id,))
    city = cursor.fetchone()

    if city:
        # Connect to Neo4j
        neo4j_connect()

        # Create Neo4j session
        with driver.session() as session:
            # Create city node if not already exists
            result = session.run(
                "MERGE (c:City {name: $name})",
                name=city['Name']
            )

            # Check if the city is already twinned with Dublin
            twinned_query = "MATCH (c:City {name: $name})-[:TWINNED_WITH]->(d:City {name: 'Dublin'}) RETURN c"
            existing_city = session.run(twinned_query, name=city['Name']).single()

            if not existing_city:
                # Create TWINNED_WITH relationship with Dublin
                session.run("MATCH (c:City {name: $name}), (d:City {name: 'Dublin'}) CREATE (c)-[:TWINNED_WITH]->(d)", name=city['Name'])

            return city['Name']  # Return city name


    # Close MySQL connection
    cursor.close()
    db.close()
    return None  # Return None if city not found