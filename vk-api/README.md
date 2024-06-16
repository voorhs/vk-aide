# VK-API

Реализованный функционал:
- аутентификация пользователя с помощью VK ID
- получение и вывод имени и фамилии

## Deployment

```bash
docker build -t vkapi .
docker run -p 8000:80 --name vkapi vkapi
```