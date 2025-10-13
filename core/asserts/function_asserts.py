def assert_user(actual_user, user_id, user_name, companies_num):
    errors = []
    assert actual_user['id'] == user_id, f'user_id should be 1, but got {user_data["id"]}'
    if actual_user['name'] != user_name:
        errors.append(f'User name: Expected "{actual_user["name"]}", got "{user_name}"')

    if len(actual_user['companies']) != companies_num:
        errors.append(f'Companies: Expected {companies_num} companies, got {len(actual_user["companies"])}')

    assert not errors, '\n'.join(errors)