class Config(object):
    """
    Common configurations4
    """

    #put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development Configurations
    """

    Debug = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production Configurations
    """
    Debug = False

app_config = {
    'development': DevelopmentConfig,
    'Production': ProductionConfig
}
