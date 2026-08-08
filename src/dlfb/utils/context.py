import os


def assets(subdir: str | None = None) -> str:
  ensure_context()
  assets_dir = os.environ["ASSETS_DIR"]
  if subdir:
    assets_dir += f"/{subdir}"
  return assets_dir


def ensure_context() -> None:
  if "ASSETS_DIR" in os.environ:
      return

  context = detect_context()

  #----- PATCH 1 by Payman Tohidifar -----
  # This patch enabales local access to dataset
  cwd = os.getcwd()
  root = os.path.dirname(cwd) if os.path.basename(cwd) == "notebooks" else cwd
  assets_dir = {
    # "local": "/content/drive/MyDrive/dlfb/assets",
    "local": root+"/data",
    "colab": "/content/assets",
  }[context]
  if not os.path.exists(assets_dir):
    raise FileNotFoundError("Could not find the assets directory.")
  os.environ["ASSETS_DIR"] = assets_dir

  #----- END OF PATCH 1 -------


def detect_context() -> str:
  is_colab = any(env_var.startswith("COLAB_") for env_var in os.environ)
  return "colab" if is_colab else "local"
