import tenseal as ts
from utils import read_data, write_data
from homomorphic import encrypt, decrypt


def testEncrypt():
    context = ts.context_from(read_data("keys/secret.txt"))
    data = [1000.0]
    encrptedData = encrypt(context, data).serialize()
    write_data("out/encrypted_data.txt", encrptedData)


def testDecrypt():
    context = ts.context_from(read_data("keys/secret.txt"))
    encrptedData = read_data("out/encrypted_data.txt")
    m1 = ts.lazy_ckks_vector_from(encrptedData)
    m1.link_context(context)
    print(m1.decrypt())


testDecrypt()
