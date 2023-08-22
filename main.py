# Import the necessary modules
import cv2  # Import OpenCV library for image processing
import tkinter as tk  # Import Tkinter library for GUI
from tkinter import filedialog  # Import submodule for file dialog


# Function to get the dimensions of an image
def get_image_dimensions(image_path):
    image = cv2.imread(image_path)  # Read the image using OpenCV
    height, width, _ = image.shape  # Get dimensions (height, width, channels)
    return width, height  # Return width and height


# Function to resize an image
def resize_image(image_path, new_width, new_height):
    image = cv2.imread(image_path)  # Read the image using OpenCV
    resized_image = cv2.resize(image, (new_width, new_height))  # Resize the image
    return resized_image  # Return the resized image


# Function to open a file dialog and select an image
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")])
    if file_path:
        entry_path.delete(0, tk.END)  # Clear the entry field
        entry_path.insert(0, file_path)  # Insert the selected file path

        width, height = get_image_dimensions(file_path)  # Get image dimensions
        label_current_width.config(text=f"Current Width: {width}")  # Update label with current width
        label_current_height.config(text=f"Current Height: {height}")  # Update label with current height


# Function to resize and display the image
def resize_and_display():
    image_path = entry_path.get()  # Get the entered image path
    new_width = int(entry_width.get())  # Get the entered new width
    new_height = int(entry_height.get())  # Get the entered new height

    resized_image = resize_image(image_path, new_width, new_height)  # Resize the image

    cv2.imshow("Resized Image", resized_image)  # Display the resized image
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close the OpenCV window


# Function to download the resized image
def download_resized_image():
    image_path = entry_path.get()  # Get the entered image path
    new_width = int(entry_width.get())  # Get the entered new width
    new_height = int(entry_height.get())  # Get the entered new height

    resized_image = resize_image(image_path, new_width, new_height)  # Resize the image

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg")])  # Ask for save path
    if save_path:
        cv2.imwrite(save_path, resized_image)  # Save the resized image using OpenCV


# Create the main tkinter window
root = tk.Tk()
root.title("Image Resizer")  # Set the title of the window
root.geometry("500x400")  # Set initial window size (width x height)

# Create labels, entries, and buttons using tkinter
label_path = tk.Label(root, text="Image Path:")  # Create a label widget
label_path.pack()  # Pack the label in the GUI window

entry_path = tk.Entry(root, width=50)  # Create an entry widget for text input
entry_path.pack()  # Pack the entry in the GUI window

button_browse = tk.Button(root, text="Browse", command=open_file_dialog)  # Create a button widget with text and command
button_browse.pack()  # Pack the button in the GUI window

label_current_width = tk.Label(root, text="Current Width: -")
label_current_width.pack()

label_current_height = tk.Label(root, text="Current Height: -")
label_current_height.pack()

label_width = tk.Label(root, text="New Width:")
label_width.pack()

entry_width = tk.Entry(root)
entry_width.pack()

label_height = tk.Label(root, text="New Height:")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

button_resize = tk.Button(root, text="Resize and Display", command=resize_and_display)
button_resize.pack(pady=10)

button_download = tk.Button(root, text="Download Resized Image", command=download_resized_image)
button_download.pack()

# Start the main event loop
root.mainloop()  # This loop keeps the GUI responsive and processes events
