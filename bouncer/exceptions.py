


class AccessDenied(Exception):
    """ This error is raised when a user is not allowed to access a resource
    
    :param user: The user who did not have the given ability.
    :param action: The action that the user did not have.
    :param subject: The resource that the user was attempting to access.
    """
    
    def __init__(self, user, action, subject):
        self.user = user
        self.action = action
        self.subject = subject

