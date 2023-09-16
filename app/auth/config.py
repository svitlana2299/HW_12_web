# Налаштування для JWT-токенів
SECRET_KEY = "your-secret-key"  # Секретний ключ для підпису токенів
ALGORITHM = "HS256"  # Алгоритм шифрування токенів

# Налаштування бази даних
DATABASE_URL = "postgresql://postgres:2299@localhost:5432/postgres"  # URL з'єднання з базою даних (приклад для SQLite)

# Налаштування CORS
CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
    "https://yourdomain.com",
] 