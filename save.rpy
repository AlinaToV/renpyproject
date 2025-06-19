init python:

    import json
    import os

    def get_custom_save_path(slot):
        return os.path.join(config.savedir, f"mysave_{slot}.json")

    def save_custom(slot=1):
        data = {
            "current_label": renpy.game.context().current,
            "variables": {
                "score": score,
                "flags": flags,
            }
        }
        with open(get_custom_save_path(slot), "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load_custom(slot=1):
        path = get_custom_save_path(slot)
        if not os.path.exists(path):
            return

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Загрузка переменных
        store.score = data["variables"]["score"]
        store.flags = data["variables"]["flags"]

        # Переход к сохраненной метке
        renpy.jump(data["current_label"])
