import bcrypt


def hash_password(arg, _rounds=20):
    if _rounds == 0 or _rounds == None:
        rounds = 20
    else:
        rounds = _rounds

    if type(arg) == str:
        return bcrypt.hashpw(arg.encode("utf8"), bcrypt.gensalt(rounds))


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode("utf8"), hashed)


def hash_data(data):
    if not data == None:
        return {"status": True, hash: hash((data))}
