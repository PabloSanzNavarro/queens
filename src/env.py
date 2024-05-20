import os

def set_env():
    os.chdir(get_src_dir())

def get_img_dir():
    parent_dir = os.path.dirname(get_src_dir())
    img_dir = os.path.join(parent_dir, "img")
    return img_dir

def get_src_dir():
    return os.path.dirname(os.path.abspath(__file__))