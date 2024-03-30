import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.data_access_layer.UsersDataAccess import UsersDAO


userdao = UsersDAO()

user = userdao.get_user('asmith2')

print(user['netid'])
