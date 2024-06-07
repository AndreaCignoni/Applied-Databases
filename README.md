#*****************************************************************
# **Project README**
#*****************************************************************

#*****************************************************************
# **Project Overview:**
#
# Folder Structure:
#
# Innovation:
# The innovation.doc file presents my experimentalGUI program which adds extra features to the pythonApp appication stored in the PythonApp folder.
# Neo4j-Queries:
# This folder contains 6 files, corresponding to each Neo4j question.
# MySQL-Queries:
# This folder contains 6 files, corresponding to each MySQL question.
# PythonApp:
# The Python App represents the main part of the project and consists of three main components:
1. **pythonApp.py:** This is the main Python application where functions to interact with both MySQL and Neo4j databases are implemented.
2. **connDB.py:** This module handles the database connections and queries for both MySQL and Neo4j databases.
3. **experimentalGUI.py:** This file experimentally builds a basic GUI using the tkinter package to interact with the functions defined in `pythonApp.py`.
#*****************************************************************

#*****************************************************************
# **Dependencies:**
#
- Python 3.x
- pymysql (for MySQL database connection)
- mysql.connector (for MySQL database connection)
- neo4j (for Neo4j database connection)
- tkinter (for GUI development)
#
#*****************************************************************

#*****************************************************************
# **Installation:**
#
1. Ensure that Python 3.x is installed on your system.
2. Install the required dependencies:
   ```
   pip install pymysql mysql-connector-python neo4j
   ```
3. Download the following files and save them in the same directory:
   - `pythonApp.py`
   - `connDB.py`
   - `experimentalGUI.py`
#*****************************************************************

#*****************************************************************
# **Usage:**
#
1. **pythonApp.py:**
   - This file contains functions to interact with the databases.
   - Run this file to execute the functions and get answers to the questions.
#  
2. **connDB.py:**
   - This module handles the database connections and queries.
   - Ensure that database credentials and connection details are correctly configured in this file.
#   
3. **experimentalGUI.py:**
   - This file experimentally builds a basic GUI using tkinter to interact with functions defined in `pythonApp.py`.
#*****************************************************************

#*****************************************************************
# **Usage Example:**
#
1. Running `pythonApp.py`:
   ```
   python pythonApp.py
   ```
   - This will execute the functions in `pythonApp.py` and display the results in the console.
#
2. Running `experimentalGUI.py`:
   ```bash
   python experimentalGUI.py
   ```
   - This will launch the GUI where you can interact with the functions through a graphical interface.
#*****************************************************************											``	

#*****************************************************************
# **Important Notes:**
- Ensure that the databases are properly configured and accessible before running the application.
- Make sure to handle database credentials securely and avoid exposing them in the code.
- The GUI functionality is experimental and may need further refinement for production use.
#*****************************************************************

#*****************************************************************
# **Author:**
#
# Andrea Cignoni
#
# **Contact:**
#
# andreacignoni@hotmail.com
#
# **Date:**
#
# 05/05/2024
#
# **Version:**
# 
# 1.0
#*****************************************************************