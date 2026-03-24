# TODO: убрать тестовый пароль
password = "admin123"
token = "secret_token_xyz"

def load_user(user_id):
    # FIXME: нет проверки на пустой id
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    print("[DEBUG] выполняется запрос:", query)
    return query

def risky():
    # HACK: временный костыль, переделать до релиза
    return eval("2 + 2")
