from typing import Any, Dict, List
from ...data.user_action import UserAction
from ...data.users_view import UsersView
from lib.frame import Frame
from tkinter import ttk
from tkinter import messagebox
from validator import Validator

class UsersTable(Frame):
    
    frameKey = "users_table"
    data: List[Dict[str, Any]] = []

    def refresh(self):
        mainView = self.get_frame('main_view')
        mainView.clear_widgets()
        mainView.register_widget(UsersTable())

    def create_widgets(self):
        self.clear_widgets()
        self.update_data()
        self.pack(side=self._tk.LEFT, fill=self._tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self, columns=(
            "id", "first_name", "last_name", "email", "phone_number", "address", 
            "birthdate", "national_id", "join_date", "is_customer", "is_admin"
        ), show='headings')

        self.tree.pack(fill=self._tk.BOTH, expand=True)
       
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, anchor='center')

        for user in self.data:
            self.tree.insert("", "end", values=(
                user['uid'], 
                user['first_name'], 
                user['last_name'], 
                user['email'],
                user['phone_number'], 
                user['address'], 
                user['birthdate'],
                user['national_id'], 
                user['join_date'], 
                '✅' if user.get('is_customer', False) else '❎', 
                '✅' if user.get('is_staff', False) else '❎'
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
                self.delete_user(item_values[0])
            
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
            "first_name": item_values[1],
            "last_name": item_values[2],
            "email": item_values[3],
            "phone_number": item_values[4],
            "address": item_values[5],
            "birthdate": item_values[6],
            "national_id": item_values[7],
            "join_date": item_values[8],
            "is_customer": item_values[9] == '✅',
            "is_staff": item_values[10] == '✅',
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

        self._tk.Label(content_frame, text="First Name").pack(pady=5)
        first_name_entry = self._tk.Entry(content_frame)
        first_name_entry.pack(pady=5)
        if default_values.get('first_name'):
            first_name_entry.insert(0, str(default_values.get('first_name')))

        self._tk.Label(content_frame, text="Last Name").pack(pady=5)
        last_name_entry = self._tk.Entry(content_frame)
        last_name_entry.pack(pady=5)
        last_name_entry.insert(0, str(default_values.get('last_name', '')))

        self._tk.Label(content_frame, text="Email").pack(pady=5)
        email_entry = self._tk.Entry(content_frame)
        email_entry.insert(0, str(default_values.get('email', '')))
        email_entry.pack(pady=5)

        self._tk.Label(content_frame, text="Phone Number").pack(pady=5)
        phone_number_entry = self._tk.Entry(content_frame)
        phone_number_entry.insert(0, str(default_values.get('phone_number', '')))
        phone_number_entry.pack(pady=5)

        self._tk.Label(content_frame, text="Address").pack(pady=5)
        address_entry = self._tk.Entry(content_frame)
        address_entry.insert(0, str(default_values.get('address', '')))
        address_entry.pack(pady=5)

        self._tk.Label(content_frame, text="Date of Birth (YYYY-MM-DD)").pack(pady=5)
        date_of_birth_entry = self._tk.Entry(content_frame)
        date_of_birth_entry.insert(0, str(default_values.get('birthdate', '')))
        date_of_birth_entry.pack(pady=5)

        self._tk.Label(content_frame, text="National ID").pack(pady=5)
        national_id_entry = self._tk.Entry(content_frame)
        national_id_entry.insert(0, str(default_values.get('national_id', '')))
        national_id_entry.pack(pady=(5, 50))

        check_condition_row = self._tk.Frame(content_frame)
        check_condition_row.pack(pady=5, padx=5, fill=self._tk.BOTH, expand=True)

        is_staff = self._tk.BooleanVar()
        is_staff.initialize(bool(default_values.get('is_staff', False)))
        is_staff_checkbox = self._tk.Checkbutton(check_condition_row, text="Is Staff", variable=is_staff)
        is_staff_checkbox.pack(pady=5, padx=10, side=self._tk.LEFT, fill=self._tk.BOTH, expand=True)

        is_customer = self._tk.BooleanVar()
        is_customer.initialize(bool(default_values.get('is_customer', False)))
        is_customer_checkbox = self._tk.Checkbutton(check_condition_row, text="Is Customer", variable=is_customer)
        is_customer_checkbox.pack(pady=5, padx=10, side=self._tk.RIGHT, fill=self._tk.BOTH, expand=True)

        def submit_form():
            ''' in Method function '''
            
            user_data = {
                'first_name': first_name_entry.get(),
                'last_name': last_name_entry.get(),
                'email': email_entry.get(),
                'phone_number': phone_number_entry.get(),
                'address': address_entry.get(),
                'birthdate': date_of_birth_entry.get(),
                'national_id': national_id_entry.get(),
                'is_customer': is_customer,
                'is_staff': is_staff,
            }
            if (default_values.get('uid', None)):
                result, error = self.edit_user(str(default_values.get('uid', "")), user_data)
            else:
                result, error = self.create_user(user_data)

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
        users = UsersView()
        self.data = users.query()

    def edit_user(self, uid: str, user: Dict[str, Any]):
        users = UserAction()
        return users.update(uid, **user)

    def delete_user(self, uid):
        users = UserAction()
        return users.delete(uid)
    
    def create_user(self, user: Dict[str, Any]):
        # Implement create a new user in db
        users = UserAction()
        return users.insert(**user)