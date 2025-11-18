class DataStorage:
    def __init__(self, db_path="caltrack.db"):
        self.db_path = db_path

        print(f"INFO: Database connection established for {self.db_path}")

    def save_user_data(self, user):
        print(f"DATA: User {user.name} data saved successfully (Mock)")
        return True 

    def load_user_data(self, user_id):

        print(f"DATA: Attempting to load User ID {user_id} (Mock)")
        return None 