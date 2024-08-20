from urllib.parse import quote_plus

# Original password
password = "Tldhdlrtm6@3("

# Encode the password
encoded_password = quote_plus(password)

# Alembic requires '%%' to escape '%'
alembic_safe_password = encoded_password.replace('%', '%%')
print(alembic_safe_password)