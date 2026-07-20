from app.core.config import get_settings

settings = get_settings()

print(settings.app.name)
print(settings.app.version)
print(settings.api.port)