import enum


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

