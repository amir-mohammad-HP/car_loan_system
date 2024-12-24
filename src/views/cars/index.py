from typing import Any, Dict, List

from src.data.cars_view import CarsView
from lib.frame import Frame
from tkinter import ttk
from tkinter import messagebox

class CarsTable(Frame):
    frameKey = "cars_table"
    data: List[Dict[str, Any]] = []

    def refresh(self):
        mainView = self.get_frame('main_view')
        mainView.clear_widgets()
        mainView.register_widget(CarsTable())

    def create_widgets(self):
        self.clear_widgets()
        self.update_data()
        self.pack(side=self._tk.LEFT, fill=self._tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self, columns=(
            "id", 
            "model", 
            "car_production_year", 
            "license_plate", 
            "color", 
            "hourly_price", 
            "status",
            "created_at"
        ), show='headings')

        self.tree.pack(fill=self._tk.BOTH, expand=True)
       
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, anchor='center')

        for car in self.data:
            self.tree.insert("", "end", values=(
                car['uid'], 
                car['model'], 
                car['car_production_year'], 
                car['license_plate'],
                car['color'], 
                car['hourly_price'], 
                car['status'],
                car['created_at']
            ))

        scrollbar = self._tk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=self._tk.RIGHT, fill=self._tk.Y)
        hscrollbar = self._tk.Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        hscrollbar.pack(side=self._tk.BOTTOM, fill=self._tk.X)

        self.tree.configure(yscrollcommand=scrollbar.set, xscrollcommand=hscrollbar.set)

        self.edit_button = self._tk.Button(self, text="Delete", command=self.delete_selected_command)
        self.edit_button.pack(pady=5, padx=10, side=self._tk.RIGHT, fill=self._tk.BOTH, expand=True)

        self.edit_button = self._tk.Button(self, text="Edit", command=self.edit_selected_command)
        self.edit_button.pack(pady=5, padx=10, side=self._tk.RIGHT, fill=self._tk.BOTH, expand=True)

        self.add_button = self._tk.Button(self, text="Add", command=self.create_user_command)
        self.add_button.pack(pady=5, padx=10, side=self._tk.LEFT, fill=self._tk.BOTH, expand=True)


    def create_user_command(self): 
        return self.open_user_frame_form()
    
    def delete_selected_command(self):
        selected_items = list(self.tree.selection())
        if (len(selected_items) == 0):
            messagebox.showinfo("Warning", "Please choose row(s)!")
            return
        delete = messagebox.askyesno("Confirm", "Are you sure wanna delete selection(s) ?")
        if delete:
            for row in selected_items:
                item_values = self.tree.item(row, "values")
                self.delete(item_values[0])
            
            self.refresh()
        

    def edit_selected_command(self):
        selected_items = list(self.tree.selection())
        if (len(selected_items) == 0):
            messagebox.showinfo("Warning", "Please choose a row!")
            return
        
        if (len(selected_items) > 1):
            messagebox.showinfo("Warning", "Please choose only one row!")
            return
        
        selected_item:str = selected_items[0]
        item_values = self.tree.item(selected_item, "values")
        print('item values: ', item_values)
        return self.open_user_frame_form({
            "uid": item_values[0],
            "model": item_values[1],
            "car_production_year": item_values[2],
            "license_plate": item_values[3],
            "color": item_values[4],
            "hourly_price": item_values[5],
            "status": item_values[6],
            "created_at": item_values[7]
        })

    def open_user_frame_form(self, default_values: Dict[str, str | bool | None ] = {}):
        root = self.get_frame('master').master

        new_window = self._tk.Toplevel(root)
        new_window.title("افزودن کاربر")
        new_window.geometry("300x600")
        new_window.resizable(True, True)

        # Create a canvas
        canvas = self._tk.Canvas(new_window)
        canvas.pack(side=self._tk.LEFT, fill=self._tk.BOTH, expand=True)

        # Create a vertical scrollbar
        scrollbar = self._tk.Scrollbar(new_window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=self._tk.RIGHT, fill=self._tk.Y)

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        content_frame = self._tk.Frame(canvas)

        # Create a window in the canvas to hold the content frame
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # Center the content frame
        content_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
        content_frame_width = 300  # Set the width of the content frame
        content_frame_height = 600  # Set the height of the content frame
        content_frame.config(width=content_frame_width, height=content_frame_height)

        label = self._tk.Label(content_frame, text="افزودن کاربر جدید")
        label.pack(pady=(10, 5), expand=True)

        self._tk.Label(content_frame, text="Model").pack(pady=5)
        model_entry = self._tk.Entry(content_frame)
        model_entry.pack(pady=5)
        model_entry.insert(0, str(default_values.get('model', '')))

        self._tk.Label(content_frame, text="Car Production Year").pack(pady=5)
        car_production_year_entry = self._tk.Entry(content_frame)
        car_production_year_entry.pack(pady=5)
        car_production_year_entry.insert(0, str(default_values.get('car_production_year', '')))

        self._tk.Label(content_frame, text="License Plate").pack(pady=5)
        license_plate_entry = self._tk.Entry(content_frame)
        license_plate_entry.insert(0, str(default_values.get('license_plate', '')))
        license_plate_entry.pack(pady=5)

        self._tk.Label(content_frame, text="Color").pack(pady=5)
        color_entry = self._tk.Entry(content_frame)
        color_entry.insert(0, str(default_values.get('color', '')))
        color_entry.pack(pady=5)

        self._tk.Label(content_frame, text="Hourly Price").pack(pady=5)
        hourly_price_entry = self._tk.Entry(content_frame)
        hourly_price_entry.insert(0, str(default_values.get('hourly_price', '')))
        hourly_price_entry.pack(pady=5)

        check_condition_row = self._tk.Frame(content_frame)
        check_condition_row.pack(pady=5, padx=5, fill=self._tk.BOTH, expand=True)

        status = self._tk.BooleanVar()
        status.initialize(bool(default_values.get('status', False)))
        status_checkbox = self._tk.Checkbutton(check_condition_row, text="Available", variable=status)
        status_checkbox.pack(pady=5, padx=10, side=self._tk.LEFT, fill=self._tk.BOTH, expand=True)

        def submit_form():
            ''' in Method function '''
            
            user_data = {
                'model': model_entry.get(),
                'car_production_year': car_production_year_entry.get(),
                'license_plate': license_plate_entry.get(),
                'color': color_entry.get(),
                'hourly_price': hourly_price_entry.get(),
                'status': "Avalable" if status else "Unavalable",
            }
            if (default_values.get('uid', None)):
                result, error = self.edit(str(default_values.get('uid', "")), user_data)
            else:
                result, error = self.create(user_data)

            if result:
                messagebox.showinfo("Perfect 😘", "Customer information submitted successfully!")
                new_window.destroy()
                self.refresh()
            else:
                messagebox.showerror("Something went wrong 🤔", error)


        def cancel_form():
            ''' in Method function '''
            new_window.destroy()  

   
        submit_button = self._tk.Button(content_frame, text="Submit", command=submit_form)
        submit_button.pack(pady=5, padx=10, side=self._tk.LEFT, fill=self._tk.BOTH, expand=True)

        cancel_button = self._tk.Button(content_frame, text="Cancel", command=cancel_form)
        cancel_button.pack(pady=5, padx=10, side=self._tk.RIGHT, fill=self._tk.BOTH, expand=True)

        content_frame.update_idletasks()  # Update the frame's size
        canvas.config(scrollregion=canvas.bbox("all"))  # Set the scroll region to encompass the content

        # Center the content frame in the window
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        

    def update_data(self) :
        users = CarsView()
        self.data = users.query()

    def edit(self, uid: str, user: Dict[str, Any]):
        # users = UserAction()
        # return users.update(uid, **user)
        return [False, 'not implemented']

    def delete(self, uid):
        # users = UserAction()
        # return users.delete(uid)
        return [False, 'not implemented']
    
    def create(self, user: Dict[str, Any]):
        # Implement create a new user in db
        # users = UserAction()
        # return users.insert(**user)

        return [False, 'not implemented']