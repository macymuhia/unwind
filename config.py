class Config:
    pass


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


config_options = {"development": DevConfig, "production": ProdConfig}

