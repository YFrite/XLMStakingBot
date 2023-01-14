from dependency_injector import providers, containers
from dependency_injector.containers import DeclarativeContainer

from db.repositories.user import UserRepository


class Container(DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["bot.handlers.private.about"])
    config = providers.Configuration()

    user_repository = providers.Factory(
        UserRepository,
        session=config.session
    )
