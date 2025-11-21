import string
from datetime import datetime
import random
from pathlib import Path

import stringcase


def make_table_name(model_class) -> str:
    characters = string.ascii_letters + string.digits
    suffix = "".join(random.choice(characters) for _ in range(8))
    return (
        stringcase.snakecase(model_class.__name__)
        + "_"
        + datetime.now().strftime("%Y_%m_%d")
        + "-"
        + suffix
    )


if __name__ == "__main__":
    path = Path(__file__)
    print(path.name)
