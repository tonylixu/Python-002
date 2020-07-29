import yaml
with open('db_settings.yml', 'r') as f:
    content = yaml.load(f, Loader=yaml.FullLoader)
print(content['database_settings'])