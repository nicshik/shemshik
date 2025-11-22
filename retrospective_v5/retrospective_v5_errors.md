# retrospective_v5_errors.md

## Подробные примеры ошибок и антипаттернов

### Ошибка A: Hotkey R не создает rectangle

**Симптомы:** Нажатие R открывает панель, но не создает элемент

**Root cause:** UI изменение в Miro November 2025

**Правильный подход:**
```javascript
// РАБОТАЕТ в v6.0
{"action": "key", "text": "R"},
{"action": "wait", "duration": 1.5},
{"action": "leftclick", "coordinate": [96, 298]},  // Клик на rectangle в панели
{"action": "wait", "duration": 1},
{"action": "leftclickdrag", "startcoordinate": [100, 100], "coordinate": [200, 150]}
```

### Ошибка B: Connection не создается (hotkey L broken)

**Симптомы:** L не активирует connection mode

**Root cause:** Hotkey L отключен/сломан в Miro v6.0

**Правильный подход:**
```javascript
// РАБОТАЕТ в v6.0 - manual drag
{"action": "key", "text": "cmdplus"},  // Zoom для точности
{"action": "leftclick", "coordinate": [element1.centerX, element1.centerY]},
{"action": "wait", "duration": 1},
{"action": "leftclickdrag",
 "startcoordinate": [element1.bottomCPX, element1.bottomCPY],
 "coordinate": [element2.centerX, element2.centerY]}
```

### Ошибка C: Element moves instead of creating connection

**Симптомы:**
- Попытка создать connection
- Source element переместился
- Connection не создался

**Root cause:** Drag начался от element body, а не от connection point

**Правильный подход:**
```javascript
// BAD (будет двигать элемент):
start_coordinate: [element.x1 + 50, element.y1 + 20] // Внутри элемента

// GOOD (создаст connection):
start_coordinate: [element.x2, element.centerY] // Точно на синей точке

// BETTER (с margin):
const CONNECTION_POINT_OFFSET = 2; // pixels
start_coordinate: [
    element.x2 + CONNECTION_POINT_OFFSET,
    element.centerY
]
```

### Ошибка D: Elements created off-canvas

**Симптомы:**
- Элементы созданы, но не видны
- Canvas показывает пустое пространство
- Прокрутка не помогает

**Root cause:** Координаты превышают canvas bounds (850x700px)

**Правильный подход:**
```javascript
// MANDATORY pre-flight validation
const maxX = Math.max(...elements.map(e => e.x2));
const maxY = Math.max(...elements.map(e => e.y2));

if (maxX > 850 || maxY > 700) {
    const scale = Math.min(850 / maxX, 700 / maxY);
    console.warn(`Rescaling by ${scale.toFixed(2)}x`);
    
    elements.forEach(el => {
        el.x1 = Math.round(el.x1 * scale);
        el.x2 = Math.round(el.x2 * scale);
        el.y1 = Math.round(el.y1 * scale);
        el.y2 = Math.round(el.y2 * scale);
    });
}
```

### Ошибка E: Ghost text labels после Undo

**Симптомы:**
- Создал элемент с именем "Server"
- Сделал Cmd+Z (undo)
- Создал снова - Miro показал "Server 2"
- Следующий - "Server 3"

**Root cause:** Miro сохраняет auto-increment counter даже после undo

**Решения:**
```javascript
// Option A: Принять auto-numbering (fastest)
// Просто продолжайте, Miro обеспечит uniqueness

// Option B: Clean slate
for (let i = 0; i < 10; i++) {
    {"action": "key", "text": "cmd+z"}
}

// Option C: Unique prefixes
const element_name = `L${layer_num}_${base_name}_${timestamp}`;
// Example: "L1_Server_8432"
```

### Ошибка F: Wrong element connected

**Симптомы:**
- Connection создан, но к неправильному элементу
- Target coordinate попал в соседний элемент

**Root cause:** Zoom слишком низкий, элементы близко друг к другу

**Правильный подход:**
```javascript
// ALWAYS zoom before connections
{"action": "key", "text": "cmd+plus"},  // Repeat 2-3x для 75-100% zoom
{"action": "wait", "duration": 1},

// Затем создавать connections
// Success rate: 85-95% при zoom 75%+
// Success rate: 50-60% при zoom 42%
```
