from moviepy.editor import AudioFileClip

from path_manager import make_path


def audio_converter(file_name, save_path, quality: str):
    raw_audio = AudioFileClip(file_name)
    new_path = make_path(save_path, quality, file_name, is_file=True)
    raw_audio.write_audiofile(
        new_path,
        bitrate=quality,
        codec="libmp3lame",
    )