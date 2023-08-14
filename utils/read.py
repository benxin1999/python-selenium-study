import configparser
import yaml

def read_ini():
    config = configparser.ConfigParser()
    config.read(r'D:\Career\Practice\Project\config\settings.ini', encoding='utf8')
    return config


def read_yaml():
    yaml_path = r'D:\Career\Practice\Project\data\data.yaml'
    with open(yaml_path, encoding='utf8') as f:
        data = yaml.safe_load(f)
        return data
if __name__ == '__main__':
    print(read_ini()['mysql'])