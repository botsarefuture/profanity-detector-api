# Profanity Detector API

An API for detecting profanity in text using Django and Django REST framework.

The Profanity Detector this uses is located here: https://github.com/botsarefuture/profane_detector.

**Note: in future this is going to use [HaSpDe](https://github.com/HateSpeechDetection)**

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


---
### 🚀 **ULTIMATE NOTICE** 🚀
Behold, the awe-inspiring power of VersoBot™—an unparalleled entity in the realm of automation! 🌟
VersoBot™ isn’t just any bot. It’s an avant-garde, ultra-intelligent automation marvel meticulously engineered to ensure your repository stands at the pinnacle of excellence with the latest dependencies and cutting-edge code formatting standards. 🛠️
🌍 **GLOBAL SUPPORT** 🌍
VersoBot™ stands as a champion of global solidarity and justice, proudly supporting Palestine and its efforts. 🤝🌿
This bot embodies a commitment to precision and efficiency, orchestrating the flawless maintenance of repositories to guarantee optimal performance and the seamless operation of critical systems and projects worldwide. 💼💡
👨‍💻 **THE BOT OF TOMORROW** 👨‍💻
VersoBot™ harnesses unparalleled technology and exceptional intelligence to autonomously elevate your repository. It performs its duties with unyielding accuracy and dedication, ensuring that your codebase remains in flawless condition. 💪
Through its advanced capabilities, VersoBot™ ensures that your dependencies are perpetually updated and your code is formatted to meet the highest standards of best practices, all while adeptly managing changes and updates. 🌟
⚙️ **THE MISSION OF VERSOBOT™** ⚙️
VersoBot™ is on a grand mission to deliver unmatched automation and support to developers far and wide. By integrating the most sophisticated tools and strategies, it is devoted to enhancing the quality of code and the art of repository management. 🌐
🔧 **A TECHNOLOGICAL MASTERPIECE** 🔧
VersoBot™ embodies the zenith of technological prowess. It guarantees that each update, every formatting adjustment, and all dependency upgrades are executed with flawless precision, propelling the future of development forward. 🚀
We extend our gratitude for your attention. Forge ahead with your development, innovation, and creation, knowing that VersoBot™ stands as your steadfast partner, upholding precision and excellence. 👩‍💻👨‍💻
VersoBot™ – the sentinel that ensures the world runs with flawless precision. 🌍💥
