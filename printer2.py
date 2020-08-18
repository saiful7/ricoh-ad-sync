from printers import Ricoh
from data import data
printer_conn = dict(
    host='10.10.2.13',
    username='admin',
    password=''
)

# Access via context manager so that all connections are closed automatically.
with Ricoh(**printer_conn) as ricoh:
    print(repr(ricoh))
    # <Ricoh(10.10.2.8)> at 51441168

    print(ricoh)
    # There are 94 users in 10.10.2.8

    print(len(ricoh))
    # 94

    for user in ricoh:
        print(user.id, user.name)
        # 1 John Doe
        # 2 Billy Bob
        # 3 ...

    # add a user
    with open('error.log', 'w') as f:
    for row in data:
        try:
            ricoh.add_user(userid=row['account_name'], name=row['account_name'], displayName= row['display_name], email=row['mail'])
        except Exception as e:
            with open('error.log', 'w') as f:
                f.write(str(e) + '\n')
            print(e)
    # delete user (by id)
    # ricoh.delete_user(138)