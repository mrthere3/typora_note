import secrets
randValue = ",".join(map(str, [secrets.randbits(8) for i in range(16)]))
randValue=randValue.split(",")