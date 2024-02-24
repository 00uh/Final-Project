import streamlit as st
import sqlite3

# Create a connection to SQLite database
conn = sqlite3.connect('recipes.db')
c = conn.cursor()

# Create recipes table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS recipes
             (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, instructions TEXT)''')
conn.commit()

# Function to insert a recipe into the database
def add_recipe(name, ingredients, instructions):
    c.execute("INSERT INTO recipes (name, ingredients, instructions) VALUES (?, ?, ?)", (name, ingredients, instructions))
    conn.commit()

# Function to retrieve all recipes from the database
def get_all_recipes():
    c.execute("SELECT * FROM recipes")
    return c.fetchall()

# Function to display the About Us section
def about_us():
    st.subheader("About Us")
    st.write("This is a simple recipe management application developed using Python, by Syed Muhammad Umar Hameed.")
    st.write("It allows users to store, view, and manage their favorite recipes easily.")

# Main function to run the PyRecipeBook app
def main():
    st.title("Recipe Book")

    menu = ["Home", "Add Recipe", "View Recipes", "About Us"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to Recipe Book! Select an option from the sidebar menu.")

    elif choice == "Add Recipe":
        st.subheader("Add Recipe")
        recipe_name = st.text_input("Enter Recipe Name")
        ingredients = st.text_area("Enter Ingredients")
        instructions = st.text_area("Enter Instructions")
        if st.button("Add"):
            if recipe_name and ingredients and instructions:
                add_recipe(recipe_name, ingredients, instructions)
                st.success("Recipe added successfully!")
            else:
                st.warning("Please fill in all fields.")

    elif choice == "View Recipes":
        st.subheader("View Recipes")
        recipes = get_all_recipes()
        for recipe in recipes:
            st.write(f"**{recipe[1]}**")
            st.write(f"Ingredients: {recipe[2]}")
            st.write(f"Instructions: {recipe[3]}")
            st.write("")

    elif choice == "About Us":
        about_us()

if __name__ == "__main__":
    main()
