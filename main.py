import tkinter as tk
from tkinter import messagebox

class BusManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Management System")
        self.buses = {}

        self.label_bus_number = tk.Label(root, text="Bus Number:")
        self.label_bus_number.grid(row=0, column=0, padx=5, pady=5)
        self.entry_bus_number = tk.Entry(root)
        self.entry_bus_number.grid(row=0, column=1, padx=5, pady=5)

        self.label_bus_route = tk.Label(root, text="Bus Route:")
        self.label_bus_route.grid(row=1, column=0, padx=5, pady=5)
        self.entry_bus_route = tk.Entry(root)
        self.entry_bus_route.grid(row=1, column=1, padx=5, pady=5)

        self.label_bus_driver = tk.Label(root, text="Bus Driver:")
        self.label_bus_driver.grid(row=2, column=0, padx=5, pady=5)
        self.entry_bus_driver = tk.Entry(root)
        self.entry_bus_driver.grid(row=2, column=1, padx=5, pady=5)

        self.button_add = tk.Button(root, text="Add Bus", command=self.add_bus)
        self.button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.button_display = tk.Button(root, text="Display Buses", command=self.display_buses)
        self.button_display.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.button_search = tk.Button(root, text="Search Bus", command=self.search_bus)
        self.button_search.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.button_delete = tk.Button(root, text="Delete Bus", command=self.delete_bus)
        self.button_delete.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_bus(self):
        bus_number = self.entry_bus_number.get()
        bus_route = self.entry_bus_route.get()
        bus_driver = self.entry_bus_driver.get()

        if bus_number and bus_route and bus_driver:
            self.buses[bus_number] = {
                'route': bus_route,
                'driver': bus_driver
            }
            messagebox.showinfo("Success", f"Bus {bus_number} added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def display_buses(self):
        if not self.buses:
            messagebox.showinfo("Info", "No buses in the system.")
        else:
            bus_list = "\n".join([f"Bus {bus_number} - Route: {bus_info['route']}, Driver: {bus_info['driver']}"
                                 for bus_number, bus_info in self.buses.items()])
            messagebox.showinfo("Buses", bus_list)

    def search_bus(self):
        bus_number = self.entry_bus_number.get()
        if bus_number in self.buses:
            bus_info = self.buses[bus_number]
            messagebox.showinfo("Bus Information", f"Bus {bus_number} - Route: {bus_info['route']}, "
                                                   f"Driver: {bus_info['driver']}")
        else:
            messagebox.showinfo("Info", f"Bus {bus_number} not found in the system.")

    def delete_bus(self):
        bus_number = self.entry_bus_number.get()
        if bus_number in self.buses:
            del self.buses[bus_number]
            messagebox.showinfo("Success", f"Bus {bus_number} deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showinfo("Info", f"Bus {bus_number} not found in the system.")

    def clear_entries(self):
        self.entry_bus_number.delete(0, tk.END)
        self.entry_bus_route.delete(0, tk.END)
        self.entry_bus_driver.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = BusManagementApp(root)
    root.mainloop()

