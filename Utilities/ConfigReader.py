from configparser import ConfigParser


def read_config(section, key):
    config = ConfigParser()
    config.read('/Users/anubhavsikka/PycharmProjects/BDDPOMAnubhav/ConfigurationData/config.ini')
    return config.get(section, key)

#print(read_config('env_info', 'browser'))

