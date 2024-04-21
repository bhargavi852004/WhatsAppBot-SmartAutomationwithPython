# WhatsApp Automation with PyWhatKit

This Python project utilizes the PyWhatKit library to automate WhatsApp messages sending. With just a few lines of code, you can schedule messages, send bulk messages, and even execute other actions on WhatsApp. Whether you want to send reminders, notifications, or automate routine tasks, this project provides a simple yet powerful solution.

## Usage

1. Before running the script, make sure you have WhatsApp Web logged in on your browser.
2. Before running the program make sure that you have pywhatkit imported in your python scripts
3. Run the script:

```bash
python main.py
```

4. Sit back and watch as the messages are sent automatically!

## Features

- **Message Scheduling:** Schedule messages to be sent at a specific time.
- **Bulk Messaging:** Send messages to multiple contacts at once.
- **Customization:** Easily customize message content, timing, and other parameters.
- **Youtube videos:** You can directly connect to youtube for watching videos.
- **Google Search:** you can also directly open google search engine for searching.

## Example

```python
import pywhatkit as pwk

# Send a single message
pwk.sendwhatmsg("+1234567890", "Hello, this is an automated message!", 15, 0)

# Schedule a message
pwk.sendwhatmsg("+1234567890", "This is a scheduled message.", 14, 30)
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

---

Feel free to adjust the content according to your project's specific details and requirements.
