from abc import ABCMeta

class UserService(object):
    
    def __init__(self):
        self.user_by_id = {}
        
    def add_user(self, user_id, name, pass_hash):
        return None
    def remove_user(self, user_id):
        return None
    def add_friend_request(self, from_user_id, to_user_id):
        return None
    def approve_friend_request(self, from_user_id, to_user_id):
        return None
    def reject_friend_request(self, from_user_id, to_user_id):
        return None
    
class User(Object):
    
    def __init__(self, user_id, name, pass_hash):
        self.user_id = user_id
        self.name = name
        self.pass_hash = pass_hash
        self.friends_by_id = {}
        self.friends_ids_to_private_chats = {} # key: friend_id, value: private chat
        self.group_chats_by_id = {} # key: chat_id, value: group chats
        self.recieved_friends_requests_by_id = {} # key: friend_id, value: AddRequest
        self.sent_friends_requests_by_id = {} # key: friend_id, value: AddRequest
        
    def message_user(self, friend_id, message):
        return None
    def message_group(self, group_id, message):
        return None
    def send_friend_request(self, friend_id):
        return None
    def recieve_friend_request(self, friend_id):
        return None
    def approve_friend_request(self, friend_id):
        return None
    def reject_friend_request(self, friend_id):
        return None
    def initiate_private_chat(self, friend_id):
        """create a private chat with another user id"""
        return None
    def initiate_group_chat(self, friend_ids):
        """ create a group chat with a list of user ids"""
        return None
    
class Chat(metaclass=ABCMeta):
    
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users = set() # probably unordered, maybe hashtable
        self.messages = [] # ordered
        
class PrivateChat(Chat):
    
    def __init__(self, first_user, second_user):
        super(PrivateChat, self).__init__()
        self.users.add(first_user)
        self.users.add(second_user)
        
class GroupChat(chat):
    
    def __init__(self):
        super(GroupChat, self).__init__()
    
    def add_user(self, user_id):
        return None
    def remove_user(self, user_id):
        return None
    
class Message(object):
    
    def __init__(self, message_id, message, timestamp):
        self.message_id = message_id
        self.message = message
        self.timestamp = timestamp
        
class AddRequest(object):
    
    def __init__(self, from_user_id, to_user_id, request_status, timestamp):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.status = request_status
        self.timestamp = timestamp
        
class RequestStatus(Enum):
    
    UNREAD = 0
    READ = 1
    ACCEPTED = 2
    REJECTED = 3