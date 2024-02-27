import tkinter as tk
from tkinter import filedialog

class FoodDistributionEntryForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Food Distribution Entry Form")

        # Create labels and entry widgets for each item
        items = ["Item No", "Item Name", "Veg/Vegan/Non-Veg", "Calories", "Amount (lb)", "Servings"]
        for i, item in enumerate(items):
            label = tk.Label(self, text=item)
            label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.E)

            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)

        # Create upload button
        upload_button = tk.Button(self, text="Upload", command=self.upload_file)
        upload_button.grid(row=len(items), column=1, pady=10)

    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path:
            print(f"File uploaded: {file_path}")

if __name__ == "__main__":
    FoodDistributionEntryForm=FoodDistributionEntryForm
    FoodDistributionEntryForm.mainloop()