# -*- coding:utf8 -*-

import ldap3
from getpass import getpass
import logging
from ldap3 import Connection,Server,ALL,SUBTREE,MODIFY_REPLACE

#from app import app

class AdApi(object):
    server =None
    connect =None
    @staticmethod
    def init_connection():
        try:
            # AdApi.server = Server(app.config['ADSERVER'], app.config['ADSERVERPORT'], get_info=ALL)
            # password = getpass()
            # password = getpass('Password: ')
            password = 'Saiful12!'
            if(password):
                AdApi.server = Server('10.0.1.2',389,
                                    use_ssl=False)
                AdApi.connect = Connection(AdApi.server,
                                        user='FFA\Administrator',
                                        password=password,
                                        auto_bind=True)
            else:
                AdApi.init_connection()
            # AdApi.connect.start_tls()
        except Exception as e:
            logging.exception("init_connection error: %s", e)

    @staticmethod
    def list_ad_user(adconfig):
        """
        Pull the user list from the AD domain server, 1000 each time.
        :param adconfig:
        :return:
        """
        if AdApi.server is None or AdApi.connect is None:
            AdApi.init_connection()
        try:
        	# attributes = ['cn', 'givenName', 'mail', 'sAMAccountName'], custom filter attributes
            AdApi.connect.search(adconfig,
                                 '(objectclass=person)',
                                 attributes=['cn','sn','sAMAccountName','displayName','mail'],
                                 paged_size=1000,
                                 search_scope=SUBTREE)
            # ad_users_list =list()
            #
            # ad_users_list.extend(AdApi.connect.entries)
            print("AD data exporting please wait ...................................")
            data_list = []
            with open('data.py', 'w') as f:
                for user in AdApi.connect.entries:
                    data_dict = {
                        "cn": str(user.cn) if user.cn else None,
                        "account_name":str(user.sAMAccountName) if user.sAMAccountName else None,
                        "mail": str(user.mail) if user.mail else None,
                        "display_name": str(user.displayName) if user.displayName else None
                    }
                    data_list.append(data_dict)
                f.write("data=" +str(data_list))

            print("AD data exported succfully to the user_data.txt")

            # print(ad_users_list)
        except Exception as e:
            logging.exception("init_connection error: %s", e)
            AdApi.server =None
            AdApi.connect =None

# AdApi.list_ad_user('dc=francofernandez,dc=local')
AdApi.list_ad_user('ou=Franco Fernandez User,dc=saasglobal,dc=local')