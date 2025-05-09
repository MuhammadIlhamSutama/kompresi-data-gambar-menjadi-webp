from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import glob, os, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

input_dir = "images"
output_dir = os.path.join(input_dir, "output")
os.makedirs(output_dir, exist_ok=True)

image_extensions = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]

def convert_single_image_to_webp(filepath, quality=80):
    ext = os.path.splitext(filepath)[1]
    if ext.lower() not in image_extensions:
        return

    filename = os.path.basename(filepath)
    name, _ = os.path.splitext(filename)
    output_path = os.path.join(output_dir, name + ".webp")

    try:
        print(f"[Convert] {filename} → {output_path}")
        im = Image.open(filepath).convert("RGB")
        im.save(output_path, "webp", quality=quality)

        # Hapus file asli setelah sukses
        if not os.path.commonpath([filepath, output_dir]) == output_dir:
            os.remove(filepath)
            print(f"[Delete] File asli dihapus: {filepath}")
    except Exception as e:
        print(f"[Error] Gagal konversi {filename}: {e}")

class WatchFolder(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(0.5)  # Delay sedikit biar file selesai disalin
            convert_single_image_to_webp(event.src_path)

if __name__ == "__main__":
    print(f"👀 Memantau folder: {input_dir}")
    event_handler = WatchFolder()
    observer = Observer()
    observer.schedule(event_handler, path=input_dir, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
