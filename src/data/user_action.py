import logging
from typing import List, Optional, Tuple
import logging
from lib.crud import CRUDInterface
from lib.db import DatabaseConnector


class UserAction(CRUDInterface):

    def insert(self, first_name: Optional[str] = None, last_name: Optional[str] = None, 
           email: Optional[str] = None, phone_number: Optional[str] = None, 
           address: Optional[str] = None, birthdate: Optional[str] = None, 
           national_id: Optional[str] = None, is_customer: Optional[bool] = None, is_staff: Optional[bool] = None,) -> Tuple[bool, str]:
        db = DatabaseConnector()
        
        # Create a list of columns and values, filtering out None values
        values = {
            'first_name': first_name ,
            'last_name': last_name ,
            'email': email ,
            'phone_number': phone_number ,
            'address': address ,
            'birthdate': birthdate ,
            'national_id': national_id ,
        }
        # if is_customer is not None:
        #     columns.append('is_customer')
        #     values.append('1' if is_customer else '0')
        # if is_staff is not None:
        #     columns.append('is_staff')
        #     values.append('1' if is_staff else '0')

        # Construct the SQL query dynamically based on the columns
        
        value_list: List[str] = [
            str(values.get('first_name', 'NUll')), 
            str(values.get('last_name', 'NUll')),
            str(values.get('email', 'NUll')),
            str(values.get('phone_number', 'NUll')),
            str(values.get('address', 'NUll')),
            str(values.get('birthdate', 'NUll')),
            str(values.get('national_id', 'NUll')),
        ]


        query = f"AddUser {"@first_name = ?, @last_name = ?, @email = ?, @phone_number = ?, @address = ?, @birthdate = ?, @national_id = ? "};"

        try:
            db.execute_query(query, value_list)
            return True, "success"
        except Exception as e:
            return False, f"{e}"
        finally:
            db.close()


    def update(self, uid:str, first_name: Optional[str] = None, last_name: Optional[str] = None, 
           email: Optional[str] = None, phone_number: Optional[str] = None, 
           address: Optional[str] = None, birthdate: Optional[str] = None, 
           national_id: Optional[str] = None, is_customer: Optional[bool] = None, is_staff: Optional[bool] = None,) -> Tuple[bool, str]:
    
        assert (len(uid.strip()) != 0), f'uid : [{uid}] must not be empty string'

        db = DatabaseConnector()
        
        # Create a list of columns and values, filtering out None values
        values = {
            'uid': uid,
            'first_name': first_name ,
            'last_name': last_name ,
            'email': email ,
            'phone_number': phone_number ,
            'address': address ,
            'birthdate': birthdate ,
            'national_id': national_id ,
            'is_customer': 1 if is_customer else 0,
            'is_staff': 1 if is_staff else 0
        }
        # if is_customer is not None:
        #     columns.append('is_customer')
        #     values.append('1' if is_customer else '0')
        # if is_staff is not None:
        #     columns.append('is_staff')
        #     values.append('1' if is_staff else '0')

        # Construct the SQL query dynamically based on the columns
        
        value_list: List[str] = [
            uid,
            str(values.get('first_name', 'NUll')), 
            str(values.get('last_name', 'NUll')),
            str(values.get('email', 'NUll')),
            str(values.get('phone_number', 'NUll')),
            str(values.get('address', 'NUll')),
            str(values.get('birthdate', 'NUll')),
            str(values.get('national_id', 'NUll')),
            str(values.get('is_customer', 'NUll')),           
            str(values.get('is_staff', 'NUll')),
        ]

        query = f"EditUserWithRole {"@uid = ?, @first_name = ?, @last_name = ?, @email = ?, @phone_number = ?, @address = ?, @birthdate = ?, @national_id = ?, @is_customer = ?, @is_staff = ? "};"

        try:
            db.execute_query(query, value_list)
            return True, "success"
        except Exception as e:
            return False, f"{e}"
        finally:
            db.close()

    def delete(self, uid: str) -> bool:
        db = DatabaseConnector()
        query = "DELETE FROM Users WHERE uid = ?"
        
        try:
            db.execute_query(query, [uid])
            return True
        except Exception as e:
            logging.error(f"Delete failed: {e}")
            return False
        finally:
            db.close()
