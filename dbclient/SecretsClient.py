from dbclient import *
import os
import json


class SecretsClient(dbclient):

    def get_secret_scopes_list(self, log_folder='secrets/'):
        scopes_list = self.get('/secrets/scopes/list').get('scopes', [])
        return scopes_list

    def log_all_secrets(self, log_file='secrets.log'):
        secrets_log = self.get_export_dir() + log_file
        secrets = self.get('/secrets/scopes/list')['scopes']
        with open(secrets_log, "w") as fp:
            for x in secrets:
                fp.write(json.dumps(x) + '\n')
