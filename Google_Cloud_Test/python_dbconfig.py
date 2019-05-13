from configparser import ConfigParser
import os
 
 
def read_db_config(section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db_config.ini')
    parser = ConfigParser()
    parser.read(config_path)
 
    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, config_path))
 
    return db