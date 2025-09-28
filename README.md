# AI-transcription MP3 to TXT

Цей проєкт використовує OpenAI Whisper для транскрибування MP3-файлів у текст. 

## Вимоги
- Python 3.9+
- Встановлений пакет `openai`
- Налаштований API-ключ OpenAI (через модуль `settings` або змінні середовища, залежно від вашої інфраструктури)

## Базове використання
```python
from openai import OpenAI
from settings import settings

from process_folder import process_folder

client = OpenAI(api_key=settings.api.api_key)
process_folder("input_directory", client)
```

## Режим із таймкодами
Тепер Whisper викликається з форматом відповіді `verbose_json`, що містить сегменти з часовими мітками. Ви можете записувати транскрипції у стилі YouTube, де кожному блоку тексту відповідає таймкод початку п'ятисекундного вікна.

```python
process_folder(
    "input_directory",
    client,
    use_timestamps=True,
    interval_seconds=5,  # можна змінити тривалість вікна
)
```

Результат зберігається у відповідних `_transcripted` підтеках. Кожен блок містить два рядки: час у форматі `MM:SS`, а нижче — текст, розпізнаний у вказаному проміжку.

## Прямий виклик транскрипції
```python
from transcribe_audio import transcribe_audio, format_segments_with_timestamps

result = transcribe_audio("1.mp3", client)
if not result.get("error"):
    lines = format_segments_with_timestamps(result["segments"], interval_seconds=5)
    print("\n\n".join(lines))
```
