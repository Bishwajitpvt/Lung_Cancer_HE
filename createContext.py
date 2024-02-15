import tenseal as ts
from utils import write_data, read_data
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes = [60,40,40,60]
)
# Generate galois keys for authentication
context.generate_galois_keys()
context.global_scale = 2**40

# Extract the private key
secret_context = context.serialize(save_secret_key=True)
write_data("keys/secret.txt", secret_context)

# Create public key
context.make_context_public() #drop private key
public_context = context.serialize()
write_data("keys/public.txt", public_context)