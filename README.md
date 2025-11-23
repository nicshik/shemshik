# Shemshik (Схемщик)

Репозиторий для документирования практик автоматизации создания схем в Miro через AI-ассистента Comet.

---

## О проекте

**Цель**: Создать полную in-place документацию для AI-ассистента Comet по построению технических, бизнес- и продуктовых схем в веб-версии Miro.com.

**Статус**: Production-ready (v5.1)

---

## Структура репозитория

### Основная документация

- **[miro-instructions-v5.md](miro-instructions-v5.md)** - текущая версия инструкций по работе с Miro
- **[retrosp_guide.md](retrosp_guide.md)** - инструкция по модульной структуре retrospective документов
- **[git_guide.md](git_guide.md)** - требования для безопасной загрузки файлов через LLM на GitHub

### Модульная структура retrospective_v5

**Папка [`retrospective_v5/`](retrospective_v5/)** - модули для редактирования:

| Модуль | Описание | Размер |
|--------|----------|--------|
| [main.md](retrospective_v5/retrospective_v5_main.md) | Метаданные + хронология | ~3 KB |
| [errors.md](retrospective_v5/retrospective_v5_errors.md) | Ошибки и антипаттерны | ~4 KB |
| [troubleshooting.md](retrospective_v5/retrospective_v5_troubleshooting.md) | Troubleshooting guide | ~3 KB |
| [code.md](retrospective_v5/retrospective_v5_code.md) | Code templates | ~6 KB |
| [scripts.md](retrospective_v5/retrospective_v5_scripts.md) | Python scripts | ~9 KB |
| [metrics.md](retrospective_v5/retrospective_v5_metrics.md) | Benchmarks & metrics | ~7 KB |

### Объединённые версии

- **[retrospective_v5_full.md](retrospective_v5_full.md)** - полная редакторская сборка всех модулей (~22 KB)

### Автоматизация

- **[scripts/merge_retrospective.py](scripts/merge_retrospective.py)** - скрипт для автоматического объединения модулей

---

## Быстрый старт

### Для чтения документации

1. Начните с [miro-instructions-v5.md](miro-instructions-v5.md) для понимания текущего workflow
2. Изучите [retrospective_v5_full.md](retrospective_v5_full.md) для практического опыта итерации v5
3. Ознакомьтесь с [git_guide.md](git_guide.md) перед загрузкой файлов на GitHub

### Для работы с модулями

1. Редактируйте модули в папке `retrospective_v5/`
2. Объединяйте изменения через скрипт:
   ```bash
   python scripts/merge_retrospective.py v5
   ```
3. Загружайте на GitHub следуя [git_guide.md](git_guide.md)

### Для создания новой итерации

1. Создайте структуру по шаблону из [retrosp_guide.md](retrosp_guide.md)
2. Заполните модули контентом
3. Используйте merge скрипт для объединения
4. Загрузите на GitHub

---

## Основные концепции

### Модульная структура

Крупные документы разбиваются на логические модули по 2-10 KB для:
- Предотвращения потери данных
- Упрощения редактирования
- Независимого версионирования
- Автоматизации объединения

Подробнее: [retrosp_guide.md](retrosp_guide.md)

### Безопасная загрузка на GitHub

Критические требования при работе с GitHub API:
- Всегда получать актуальный SHA перед update
- Никогда не использовать заглушки в content
- Валидировать полноту содержимого
- Верифицировать размер после загрузки

Подробнее: [git_guide.md](git_guide.md)

### Итеративный процесс

1. Практическая работа в Miro (создание схемы)
2. Документирование в thread Perplexity
3. Формирование retrospective (модульная структура)
4. Загрузка на GitHub
5. Обновление miro-instructions для следующей версии

---

## Метрики проекта

### Retrospective v5 (ноябрь 2025)

- **Задача**: Воссоздание архитектурной диаграммы веб-приложения
- **Результат**: 15+ элементов, 15+ соединений
- **Время работы**: 44 минуты (было 90 минут в v5.0)
- **Success rate**: 85% (было 40%)
- **Улучшение**: -51% времени, +112% надёжности

### Структура документации

- **Модулей**: 6 (main, errors, troubleshooting, code, scripts, metrics)
- **Общий объём**: ~32 KB в модулях, ~22 KB в full версии
- **Инструкций**: 3 (miro, retrosp_guide, git_guide)
- **Скриптов**: 1 (merge_retrospective.py)

---

## Технологический стек

- **Инструмент**: Miro.com (веб-версия)
- **AI-ассистент**: Comet
- **Автоматизация**: Python 3
- **Документация**: Markdown
- **Версионирование**: Git/GitHub
- **Форматы**: .md, .py, .json

---

## Roadmap

### v6.0 (планируется)

- [ ] Интеграция findings из v5 в новую версию miro-instructions
- [ ] Добавление decision tree для hotkey compatibility
- [ ] Расширение библиотеки Python scripts
- [ ] Шаблоны для типовых архитектур (3-tier, microservices, etc.)

### Будущие улучшения

- [ ] CI/CD для автоматической проверки модулей
- [ ] Веб-интерфейс для просмотра retrospective
- [ ] Визуализация метрик по версиям
- [ ] Интеграция с Miro API (если доступна)

---

## Contributing

Проект находится в активной разработке. При внесении изменений:

1. Следуйте структуре модулей из [retrosp_guide.md](retrosp_guide.md)
2. Соблюдайте требования из [git_guide.md](git_guide.md)
3. Обновляйте метрики и benchmarks
4. Документируйте новые ошибки и решения

---

## Лицензия

Документация доступна для использования в образовательных и практических целях.

---

## Контакты

- **Репозиторий**: [github.com/nicshik/shemshik](https://github.com/nicshik/shemshik)
- **Автор**: nicshik
- **Версия**: 1.0
- **Последнее обновление**: 23 ноября 2025

---

## Благодарности

Проект создан на основе практического опыта работы с AI-ассистентом Comet и веб-версией Miro.com.

---

**Статус репозитория**: Production-ready  
**Основной документ**: [miro-instructions-v5.md](miro-instructions-v5.md)  
**Последняя итерация**: v5.1 (22 ноября 2025)
