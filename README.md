# QueueApi

## Технологии
- **FastAPI**
- **Pydantic**
- **SQLAlchemy**
- **Alembic**
- **PostgreSQL**
- **Redis**
- **MongoDb**
- **RabbitMQ**
- **Celery**
- **Docker**
- **Pytest**

## Предварительные требования
Перед запуском приложения убедитесь, что у вас установлены:

- Docker

## Инструкция по настройке
Следуйте этим шагам, чтобы настроить и запустить приложение:

### 1. Настройка переменных окружения
Переименуйте файл `.env.template` в `.env`,
а так же `.env.docker.template` в `.env.docker`:

### 2. Сборка и запуск приложения
Используйте Docker Compose для сборки и запуска приложения:

```bash
docker compose up --build -d
```

### 4. Доступ к документации API
После запуска приложения документация API доступна по следующим адресам:

- Swagger UI: [http://localhost:50000/docs](http://localhost:50000/docs)
- Redoc: [http://localhost:50000/redoc](http://localhost:50000/redoc)

### 5. Получение API ключа
Для работы с защищенными эндпоинтами:

1. Перейдите в `/api_v1/auth/register` в Swagger UI.
2. Введите имя пользователя и пароль для генерации API ключа.
3. Нажмите на кнопку "Authorize" в правом верхнем углу Swagger UI и введите сгенерированный API ключ.
4. После того как вы зарегистрировались чтобы в последующие разы получить API ключ пройдите в `/api_v1/auth//login` и также введите свой логин и пароль.

## Дополнительные возможности
### Pre-commit хуки
Для поддержания качества кода интегрированы следующие pre-commit хуки:

- **Black**: Для форматирования кода.
- **Ruff**: В качестве линтера.
