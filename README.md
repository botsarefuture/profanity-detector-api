# Profanity Detector API

An API for detecting profanity in text using Django and Django REST framework.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/botsarefuture/profanity-detector-api.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### Detect Profanity

Endpoint: `/api/detect-profanity/`

#### Request

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "This is a profane text.", "language": "en"}' http://localhost:8000/api/detect-profanity/
```

Replace `http://localhost:8000` with your API server URL.

#### Response

```json
{
    "text": "This is a profane text.",
    "language": "en",
    "profanity_detected": true
}
```

## Documentation

For detailed API documentation, refer to the [OpenAPI (Swagger) Documentation](#link-to-documentation).

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
