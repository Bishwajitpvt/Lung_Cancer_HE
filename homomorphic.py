import tenseal as ts

def encrypt(context,data,Float=False):
    if Float:
        return ts.ckks_vector(context,data)
    else:
        return ts.bfv_vector(context,data)
    
def decrypt(context,encryptedData):
    m2 = ts.lazy_ckks_vector_from(encryptedData)
    m2.link_context(context)
    return m2.decrypt()[0]
