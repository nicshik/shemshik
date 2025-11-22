# retrosp_guide.md

## Инструкция по модульной структуре retrospective документов

Этот документ описывает правила разбиения единого файла retrospective или thread на логические модули для предотвращения потери данных и упрощения редактирования.

---

## Зачем нужна модульная структура?

### Проблемы монолитного файла
- Потеря данных при экспорте
- Сложность редактирования
- Конфликты версий
- Риск повреждения
- Медленная работа

### Преимущества модульной структуры
- Нет потери данных 
- Легко редактировать 
- Версионность 
- Автоматизация объединения
- Гибкость
- Параллельная работа

---

## Рекомендуемая структура (6 модулей)
retrospective_vX/
├── retrospective_vX_main.md           # Метаданные + хронология
├── retrospective_vX_errors.md         # Ошибки и антипаттерны
├── retrospective_vX_troubleshooting.md # Troubleshooting guide
├── retrospective_vX_code.md           # Code templates + Quick Reference
├── retrospective_vX_scripts.md        # Python/JavaScript scripts
├── retrospective_vX_metrics.md        # Benchmarks + таблицы
└── retrospective_vX_full.md           # Объединенная версия

---

## Описание модулей, примеры, workflow, best practices, примеры именования, чек-листы, практические ошибки и решения, summary.

---

**Версия**: 1.0  
**Дата**: 23 ноября 2025  
**Статус**: Production-ready  
**Применимо к**: retrospective документам, technical documentation, large markdown files
