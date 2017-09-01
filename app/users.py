"""
users.py
"""
class User(object):
    """
    This class creaates new users and allows them to log in
    """

    def __init__(self):
        self.user_list = []

    def createuser(self, email, username, password, cpassword):
        """
        Saves user by creating an account
        args
            email,username,password,cPassword
        returns a list of users
        """
        user_dict = {}
        if not self.user_list:
            user_dict['email'] = email
            user_dict['username'] = username
            user_dict['password'] = password
            self.user_list.append(user_dict)
            return "Registration successful"
        else:
            for ins_user in self.user_list:
            #check if email exist
                if email == ins_user['email']:
                    return "Email already exists."
                elif username == ins_user['username']:
                    return "Username already exists."
                elif password == cpassword:
                    user_dict['email'] = email
                    user_dict['username'] = username
                    user_dict['password'] = password
                    self.user_list.append(user_dict)
                    return "Registration successful"
                return "Passwords do not match"

    def login(self, username, password):
        """
        Function that enables user to acess app by login
        args
            username, password
        returns
            render to dashboard
        """
        for ins_user in self.user_list:
            if username == ins_user['username'] and password == ins_user['password']:
                return "Welcome! Create a new shopping list"
        return "Account does not exist.Sign up"
