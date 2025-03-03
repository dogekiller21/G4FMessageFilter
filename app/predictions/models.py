from enum import StrEnum


class G4FModel(StrEnum):
    deepseek_v3 = "deepseek-v3"
    deepseek_chat = "deepseek-chat"
    gemini_1_5_flash = "gemini-1.5-flash"
    gemini_2_0_flash = "gemini-2.0-flash"
    blackboxai = "blackboxai"
    blackboxai_pro = "blackboxai-pro"
    qwq_32_b = "qwq-32b"

    @classmethod
    def all(cls):
        return [item.value for item in cls]
