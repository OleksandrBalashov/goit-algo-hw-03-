import asyncio
import shutil
from pathlib import Path

async def copy_files_by_extension(file_path, dest_dir):
    try:
        file_extension = file_path.suffix.lower()[1:]
        folder_for_extension = dest_dir / file_extension
        folder_for_extension.mkdir(parents=True, exist_ok=True)

        final_destination = folder_for_extension / file_path.name
        shutil.copy(file_path, final_destination)
        print(f"Файл {file_path} скопійовано до {final_destination}")
    
    except Exception as e:
        print(f"Помилка на файлі {file_path}: {e}")

async def read_folder(source_folder: Path, output_folder: Path):
    try:
        # Проходимо по всіх файлах у папці та підпапках
        for file_path in source_folder.rglob('*'):
            if file_path.is_file():
                await copy_files_by_extension(file_path, output_folder)
    except Exception as e:
        print(f"Помилка при читанні папки {source_folder}: {e}")

async def main():
    source_dir = Path(input("Введіть шлях до вихідної директорії: "))
    dest_dir = Path(input("Введіть шлях до директорії копіювання: "))

    # Перевіряємо директорію
    if not source_dir.is_dir():
        print(f"Помилка: немає такої директорії: {source_dir}")
        return

    # 'dist' за замовчуванням
    dest_folder = Path(dest_dir) if dest_dir else Path("dist")
    dest_folder.mkdir(parents=True, exist_ok=True)

    await read_folder(source_dir, dest_folder)

if __name__ == "__main__":
    asyncio.run(main())
