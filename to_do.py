import sqlite3

# Connect to the database
conn = sqlite3.connect("todos.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, item TEXT)")

# Set the voice commands to listen for
add_command = "add todo"
delete_command = "delete todo"

while True:
    # Wait for a voice command
    command = input("Enter a voice command: ")

    if command.startswith(add_command):
        # Extract the to-do item from the command
        todo_item = command[len(add_command):].strip()

        # Save the to-do item in the database
        cursor.execute("INSERT INTO todos (item) VALUES (?)", (todo_item,))
        conn.commit()
        print("To-do item added:", todo_item)
    elif command.startswith(delete_command):
        # Extract the to-do item from the command
        todo_item = command[len(delete_command):].strip()

        # Delete the to-do item from the database
        cursor.execute("DELETE FROM todos WHERE item=?", (todo_item,))
        conn.commit()
        print("To-do item deleted:", todo_item)
    else:
        # Unrecognized command
        print("Unrecognized command")

# Close the database connection
conn.close()

