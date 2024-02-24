import streamlit as st
import sqlite3

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create a new recipe
def create_recipe(conn, recipe_data):
    sql = ''' INSERT INTO recipes(name, ingredients, instructions)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, recipe_data)
    conn.commit()
    return cur.lastrowid

# Function to retrieve all recipes from the database
def get_all_recipes(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM recipes")
    return cur.fetchall()

def main():
    st.title("Recipe Book")

    # Create a database connection
    conn = create_connection("recipebook.db")
    if conn is None:
        st.error("Error creating database connection.")
        return

    # Create recipes table if not exists
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        instructions TEXT NOT NULL
    );
    '''
    conn.execute(create_table_sql)

    # Sidebar menu
    menu_option = st.sidebar.selectbox("Menu", ["View Recipes", "Add Recipe"])

    if menu_option == "View Recipes":
        st.header("View Recipes")
        recipes = get_all_recipes(conn)
        if not recipes:
            st.write("No recipes found.")
        else:
            for recipe in recipes:
                st.subheader(recipe[1])  # Display recipe name
                st.write("**Ingredients:**", recipe[2])  # Display ingredients
                st.write("**Instructions:**", recipe[3])  # Display instructions
                st.write("---")

    elif menu_option == "Add Recipe":
        st.header("Add Recipe")
        recipe_name = st.text_input("Recipe Name")
        ingredients = st.text_area("Ingredients")
        instructions = st.text_area("Instructions")
        if st.button("Add Recipe"):
            if recipe_name.strip() and ingredients.strip() and instructions.strip():
                recipe_data = (recipe_name, ingredients, instructions)
                create_recipe(conn, recipe_data)
                st.success("Recipe added successfully.")
            else:
                st.error("Please fill in all fields.")

if __name__ == "__main__":
    main()
