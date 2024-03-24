# Security program that masks only the last 4 digits


def mask_security_number(security_number):
    security_number = security_number[:-4]

    return security_number + "****"

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
