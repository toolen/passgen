from aiohttp import web

from passgen.settings import init_settings


def test_init_settings_with_override():
    app = web.Application()
    override_settings = {'cors_enabled': False, 'foo': 'bar'}

    init_settings(app, override_settings)

    assert app['settings']['cors_enabled'] == override_settings['cors_enabled']
    assert app['settings']['foo'] == override_settings['foo']
