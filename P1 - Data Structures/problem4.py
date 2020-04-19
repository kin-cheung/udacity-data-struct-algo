class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
parent.add_user("parent_user_1")
parent.add_user("parent_user_2")

child = Group("child")
child.add_user("child_user_1")
child.add_user("child_user_2")

sub_child = Group("sub_child")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_sub_child_1 = Group("sub_sub_child_1")
sub_sub_child_2 = Group("sub_sub_child_2")
sub_sub_child_2.add_user("sub_sub_child_2_user")

sub_child.add_group(sub_sub_child_1)
sub_child.add_group(sub_sub_child_2)
child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    name = user if '/' not in user else user[0:user.find('/')]
    if name in group.get_users() :
        return True
    
    for sub_group in group.get_groups() :
        if is_user_in_group(name, sub_group) :
            return True
    
    return False

print(is_user_in_group('sub_child_user/123', parent))
# True
print(is_user_in_group('unknown/123', parent))
# False
print(is_user_in_group('parent_user_1/123', parent))
# True
print(is_user_in_group('child_user_1/123', parent))
# True
print(is_user_in_group('sub_sub_child_2_user/123', parent))
# True