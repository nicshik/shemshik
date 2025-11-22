#!/usr/bin/env python3
"""
merge_retrospective.py
Скрипт для объединения модульных файлов retrospective в единый документ
"""

import os
from pathlib import Path

def merge_retrospective_files(version="v5", input_dir=".", output_dir="."):
    """
    Объединяет части retrospective в единый файл
    
    Args:
        version: версия итерации (например "v5")
        input_dir: директория с модулями
        output_dir: директория для итогового файла
    """
    
    # Порядок файлов для объединения
    files_order = [
        f"retrospective_{version}_main.md",
        f"retrospective_{version}_errors.md",
        f"retrospective_{version}_troubleshooting.md",
        f"retrospective_{version}_code.md",
        f"retrospective_{version}_scripts.md",
        f"retrospective_{version}_metrics.md"
    ]
    
    output_content = []
    files_processed = 0
    total_chars = 0
    
    print(f"\n=== Merging retrospective {version} ===\n")
    
    for filename in files_order:
        filepath = Path(input_dir) / filename
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                char_count = len(content)
                
                # Для всех файлов кроме первого добавляем разделитель
                if output_content:
                    # Удаляем главный заголовок если есть
                    if content.startswith('# '):
                        lines = content.split('\n')
                        # Пропускаем первую строку с заголовком
                        content = '\n'.join(lines[1:]).lstrip()
                    output_content.append('\n---\n\n')
                
                output_content.append(content)
                files_processed += 1
                total_chars += char_count
                
                print(f"✓ {filename}: {char_count:,} chars")
                
        except FileNotFoundError:
            print(f"⚠ Warning: {filename} not found, skipping...")
        except Exception as e:
            print(f"✗ Error reading {filename}: {e}")
    
    if not output_content:
        print("\n✗ No files were processed!")
        return None
    
    # Объединяем весь контент
    full_content = ''.join(output_content)
    
    # Создаем выходной файл
    output_file = Path(output_dir) / f"retrospective_{version}_full.md"
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"\n{'='*50}")
        print(f"✓ Created: {output_file}")
        print(f"  Files merged: {files_processed}")
        print(f"  Total size: {len(full_content):,} chars")
        print(f"  Total size: {len(full_content.encode('utf-8')):,} bytes")
        print(f"{'='*50}\n")
        
        return str(output_file)
        
    except Exception as e:
        print(f"\n✗ Error writing output file: {e}")
        return None

if __name__ == "__main__":
    import sys
    
    # Поддержка аргумента версии
    version = sys.argv[1] if len(sys.argv) > 1 else "v5"
    
    result = merge_retrospective_files(version)
    
    if result:
        print(f"Success! Merged file available at: {result}")
    else:
        print("Failed to merge files.")
        sys.exit(1)
