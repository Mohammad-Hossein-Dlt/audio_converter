
## Install requirements

```python
pip install -r requirements.txt
```
## How does this program convert audio files to different qualities at the same time?

```python
from moviepy.editor import AudioFileClip
from concurrent.futures import ThreadPoolExecutor, as_completed

class AudioQualities(str, enum.Enum):
    q64k_bit = "64k"
    q128k_bit = "128k"
    q256k_bit = "256k"
    q320k_bit = "320k"

    @classmethod
    def directories(cls):
        return [
            cls.q64k_bit,
            cls.q128k_bit,
            cls.q256k_bit,
            cls.q320k_bit,
        ]

def make_path(*args: str, is_file: bool) -> str:
    args = [i.rstrip("/") for i in args]
    slash = "" if is_file else "/"
    path = ("/".join(args) + slash) if len(args) > 1 else (args[0] + slash) if len(args) == 1 else ""
    return path

def audio_converter(file_name, save_path, quality: str):
    raw_audio = AudioFileClip(file_name)
    new_path = make_path(save_path, quality, file_name, is_file=True)
    raw_audio.write_audiofile(
        new_path,
        bitrate=quality,
        codec="libmp3lame",
    )

with ThreadPoolExecutor(max_workers=8) as pool:
    futures = [pool.submit(audio_converter, audio_files[int(selected)], temp.path, q) for q in
               AudioQualities.directories()]
    for future in as_completed(futures):
        pass

```

