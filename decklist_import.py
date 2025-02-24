import tkinter as tk
from tkinter import messagebox

# Function to save text from the Text widget to a text file
def save_to_file():
    text = text_box.get("1.0", tk.END)  # Get all text from the text box
    try:
        with open("input.txt", "w") as file:
            file.write(text)
        messagebox.showinfo("Success", "Text successfully saved to output.txt")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Paste Decklist")

# Ensure the window is brought to the front
root.lift()  # Brings the window to the front
root.attributes('-topmost', True)  # Keeps the window on top of other windows
root.after(100, lambda: root.attributes('-topmost', False))  # Remove topmost after 100ms to allow normal interaction

# Create a Text widget (text box)
text_box = tk.Text(root, height=10, width=40)
text_box.pack(pady=10)

# Create a Save button
save_button = tk.Button(root, text="Save Text", command=save_to_file)
save_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()


# Define the function to process the file
def clean_file(input_file, output_file):
    try:
        # Open the input file for reading and output file for writing
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Iterate through each line in the input file
            for line in infile:
                # Strip leading/trailing whitespace and check if the line is not empty
                if line.strip():
                    # Check if the line starts with a digit
                    if line.lstrip()[0].isdigit():
                        # Write the line to the output file if it's not empty and starts with a number
                        outfile.write(line)
        
        print(f"File processed successfully. Cleaned content saved to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


