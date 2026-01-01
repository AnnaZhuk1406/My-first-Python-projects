files = [
    "photo.png",
    "homework.docx",
    "game.exe",
    "virus_free.exe",
    "suspicious_file.exe"]
bad_words = ["virus", "hack", "trojan"]
print("🔍 Антивірус починає сканування...\n")
found = 0
for file in files:
    for bad in bad_words:
        if bad in file.lower():
            print(f"⚠️ Підозрілий файл знайдено: {file}")
            found += 1
            break
    else:
        print(f"✅ Безпечний файл: {file}")
print(f"\n🛡 Сканування завершено. Знайдено загроз: {found}")
input("Натисніть Enter щоб закрити гру")
