# QueueApi

- Этот проект предоставляет API для управления очередями (изначально реализован под занятия в университете,но может быть использован для любых очередей).
- Фронт - NginxQueues

## Основные функции

### 1. Управление очередями
- **Создание очередей**: Возможность создавать новые очереди с различными настройками.
- **Чтение очередей**: Получение информации о текущем статусе очереди.
- **Обновление очередей**: Возможность изменения параметров очереди, таких как имя, приоритет, доступность.
- **Удаление очередей**: Удаление очереди, если она больше не требуется.

### 2. Управление тегами
- **Создание тегов**: Возможность добавлять теги для очередей, чтобы можно было их классифицировать.
- **Чтение тегов**: Получение информации о тегах, которые присвоены очередям.
- **Обновление тегов**: Возможность редактировать существующие теги.
- **Удаление тегов**: Удаление тегов, если они больше не нужны.

### 3. Управление местами в очередях
- **Занятие мест в очереди**: Возможность пользователю занять место в очереди.
- **Освобождение мест**: Освобождение места в очереди, если пользователь больше не ожидает.
- **Получение текущего положения**: Получение информации о текущем месте пользователя в очереди.

### 4. Регистрация и авторизация пользователей
- **Регистрация пользователей**: Пользователи могут зарегистрироваться в системе с предоставлением необходимых данных.
- **Авторизация пользователей**: Возможность авторизации пользователей для доступа к их учетным записям и очередям.
- **Управление пользователями**: Возможность обновления данных пользователей, включая изменение пароля и контактной информации.

### 5. Декоратор для записи данных в MongoDB
- В рамках системы был разработан **декоратор**, который автоматически записывает поступающие данные в **MongoDB**. 
- Декоратор реализует следующий процесс:
  - При вызове соответствующего эндпоинта API, декоратор перехватывает данные, **фильтрует по нашему желанию**, и отправляет их в очередь сообщений.
  - После этого, **воркер** системы обрабатывает очередь и записывает данные в базу данных MongoDB для дальнейшего использования.
- Такой подход обеспечивает асинхронную обработку запросов, улучшая производительность системы и разгружая основные эндпоинты.

### 6. Хранение токенов пользователей в Redis для максимальной производительности
- Для повышения производительности и уменьшения нагрузки на базу данных, **токены пользователей** хранятся в **Redis**. Это позволяет:
  - Быстро получать и проверять токены, не выполняя лишних запросов к основной базе данных.
  - Обеспечить высокую доступность и быстрый доступ к токенам, что критически важно для масштабируемых приложений.
- Использование Redis значительно улучшает производительность, особенно при работе с сессиями и аутентификацией.

### 7. Полное покрытие тестами
- Проект имеет **почти полное покрытие тестами**, что включает:
  - **Юнит-тесты** для проверки отдельных компонентов и бизнес-логики.
  - **Интеграционные тесты** для проверки взаимодействия между компонентами системы, такими как работа с базой данных, Redis, очередями сообщений и API.


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
