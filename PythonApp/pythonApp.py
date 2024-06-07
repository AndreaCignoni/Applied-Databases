import connDB
import pymysql

def main():
    print("="*33)
    print("{:^33}".format("MENU"))
    print("="*33)
    print("1 - View Cities by County")
    print("2 - Update City Population")
    print("3 - Add New Person")
    print("4 - Delete Person")
    print("5 - View Countries by population")
    print("6 - Show Twinned Cities")
    print("7 - Twin with Dublin")
    print("x - Exit application")
    choice = input("Choice: ")
    if choice == "1":
        return cities_by_country()
    elif choice == "2":
        return city_population()
    elif choice == "3":
        return add_person()
    elif choice == "4":
        return delete_person()
    elif choice == "5":
        return countries_by_population()
    elif choice == "6":
        return show_twin_cities()
    elif choice == "7":
        return twin_with_Dublin()
    elif choice == "x":
        return
    else:
        print("Invalid choice. Please try again.")
 
def cities_by_country():
    country = input("Enter Country: ")
    connDB.search_cities_by_country(country)
    
def city_population():
    while True:
        city_id = int(input("Enter City ID: "))
        city_details = connDB.get_city_details_by_id(city_id)
        if city_details:
            break
        else:
            print("No city found with ID = ", city_id,"\n")
    while True:
        new_population_option = input("\n[I]ncrease/[D]ecrease Population: ").upper()
        if new_population_option == "I":
            new_population = int(input("Enter Population Increase: "))
            connDB.increase_city_population(new_population)
        elif new_population_option == "D":
            new_population = int(input("Enter Population Decrease: "))
            connDB.decrease_city_population(new_population)
    else:
        return new_population_option
        
def add_person():
    try:
        print("Add New Person")
        print("-" * 16)
        ID = int(input("ID: "))
        Name = input("Name: ")
        Age = int(input("Age: "))
        Salary = input("Salary: ")
        City = input("City: ")
        # Check if ID already exists
        if connDB.person_exists(ID):
            print("\n Error: Person ID: ", ID, " already exists \n")
            return main()
            # Check if city exists
        elif connDB.city_exists(City):
            print("\n Error: City ID: ", City, " does not exist \n")
            return main()
        else:
            connDB.add_person(ID, Name, Age, Salary, City)
        return main()
    # Printing errors returned from database query    
    except ValueError as e:
        print(e)
        return main()
    except Exception as e:
        print(e)
        return main()
def delete_person():
    try: 
        ID = input("Enter ID of Person to Delete: ")
        connDB.person_exists(ID)
        connDB.delete_person
        connDB.delete_person(ID)
        print("Person ID: ", ID," deleted \n")
        return main()
    # Printing errors returned from database query    
    except ValueError as e:
        print(e)
        return main()
    except Exception as e:
        print(e)
        return main()    
    # Returning error if the person to delete has visited cities
    except pymysql.err.IntegrityError as e:
        print("Error: Can't delete Person ID:", ID, ". He/she has visited cities.")
        return main()
        
def countries_by_population():
    print("\nCountries by Pop")
    print("-" * 16)
    while True:
        selected_operator = input("Enter < > or = : ")
        if selected_operator in ['<', '>', '=']:
            population = int(input("Enter population: "))
            results = connDB.search_countries(selected_operator, population)
            return main()
    else:
        return selected_operator

def show_twin_cities():
    twinned_cities = connDB.twinned_city()
    print("\nTwinned Cities")
    print("-" * 16)
    for city1, city2 in twinned_cities:
        print(f"{city1} <-> {city2}")
    return main()
        
def twin_with_Dublin():
    while True:
        city_id = input("Enter ID of City to twin with Dublin: ")

        # Check if Dublin exists in Neo4j
        if not connDB.check_dublin_existence():
            print("Error: Dublin does not exist in Neo4j database")
            return main()
        # Check if the city with the specified ID exists
        city_name = connDB.add_city_to_neo4j(city_id)
        if city_name:
            print(f"Dublin is now twinned with {city_name}")
            return main()
        else:
            print(f"Error: City ID: {city_id} doesn't exist in MySql database.")
            return main()


if __name__ =="__main__":
    main()