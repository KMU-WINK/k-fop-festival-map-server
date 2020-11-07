import random
import guest.lib as lib
import hashlib

from .models import GuestToken

def createToken(model):
    enc = hashlib.md5()
    code = enc.update(str(random.randint(0, 999999)).encode('utf8'))
    token = enc.hexdigest()

    try:
        model.objects.get(token=token)
        return createToken(model)
    except model.DoesNotExist:
        return code