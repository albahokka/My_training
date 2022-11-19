def build_profile(first, last, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = build_profile('emily', 'kim',
                        age = '27',
                        middle_name = 'shwarz'.title())
print(user_profile)