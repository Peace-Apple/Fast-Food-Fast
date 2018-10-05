"""
App configurations
"""

import os


class Config:
    """
    This is the parent configurations to be inherited from
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = "pass123"


class DevelopmentConfig(Config):
    """
    The configuration for the development environment
    """
    DEBUG = True
    TESTING = True
    ENV = 'development'


class TestingConfig(Config):
    """
    The configuration for testing
    """
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'pass123'


class ProductionConfig(Config):
    """
    Extra configuration for Production
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'pass123'
