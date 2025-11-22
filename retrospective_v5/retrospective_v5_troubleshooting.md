# retrospective_v5_troubleshooting.md

## Troubleshooting Decision Tree

### Проблема: Hotkey не работает

**Шаг 1: Нажали R, ничего не происходит?**
- Miro Nov 2025 → Panel > Rectangle вручную
- Координаты: [32, 337] → wait 1s → [96, 298]

**Шаг 2: Нажали L, нет эффекта?**
- BROKEN в v6.0 → только drag-соединение
- Требуется zoom 75%+ для точности

### Проблема: Элементы не видны

**Диагностика:**
1. Alt+1 → Canvas пуст?
2. Cmd+A → Select All
3. Если выделение появилось → элементы off-canvas
4. Если ничего → Cmd+Z, применить pre-flight validation

**Решение:**
```javascript
// Quick reset
{"action": "key", "text": "alt+1"},
{"action": "wait", "duration": 2}

// If still not visible
{"action": "key", "text": "cmd+a"},
{"action": "wait", "duration": 1}
// Теперь увидите selection boxes
```

### Проблема: Connection создается неправильно

**Issue #1: Element moves instead**
- CAUSE: Drag от body, не от connection point
- FIX: Start coordinate = ТОЧНО на синей точке
- PREVENTION: Zoom 75%+, click element first

**Issue #2: Wrong element connected**
- CAUSE: Zoom слишком низкий
- FIX: Zoom to 75-100%
- PREVENTION: Batch connections по viewport

**Issue #3: Connection не появляется**
- CAUSE: Target coordinate вне element bounds
- FIX: Aim for element center
- PREVENTION: Use element.centerX/centerY

### Проблема: Timing issues

**Симптомы:**
- Element не создается
- Panel не открывается
- Текст не вводится

**Решение:**
```javascript
// Increase ALL wait times by +0.5s
const WAIT_TIMES_V6 = {
    fast: 0.5,      // Escape, clicks
    standard: 1.0,   // Most operations
    slow: 1.5,       // Panel opens
    verify: 2.0      // Alt+1, zoom
};
```

### Проблема: Canvas coordination issues

**Lost on canvas?**
```javascript
// Nuclear option:
{"action": "key", "text": "alt+1"},  // Fit to screen
{"action": "wait", "duration": 2}
```

**Elements overlap?**
```javascript
// Increase spacing in coordinate plan
const SPACING = {
    horizontal_gap: 60,  // было 40
    vertical_gap: 40     // было 30
};
```

### Проблема: Performance degradation

**Symptoms:**
- Operations становятся медленнее
- UI lag увеличивается
- Success rate падает

**Solutions:**
1. Refresh browser (Cmd+R)
2. Clear Miro cache
3. Reduce zoom level
4. Close other tabs
5. Restart browser if critical

### Hotkey Compatibility Matrix

| Hotkey | v5.0 | v6.0 Nov 2025 | Workaround | Priority |
|--------|------|---------------|------------|----------|
| R      | 95%  | 95%* (panel)  | Direct panel access | HIGH |
| L      | 95%  | 0% BROKEN     | Manual drag + zoom | CRITICAL |
| O      | 90%  | 0% BROKEN     | Shapes panel | MEDIUM |
| T      | 90%  | 90%           | None needed | LOW |
| Alt+1  | 95%  | 95%           | None needed | LOW |
| Cmd+Z  | 100% | 100%          | None needed | LOW |

### Best Practices Checklist

**Перед началом работы:**
- [ ] Pre-flight validation coordinates
- [ ] Auto-rescale если needed
- [ ] Plan viewport batches
- [ ] Have Cmd+Z ready

**Во время создания элементов:**
- [ ] Use direct panel access [32, 337]
- [ ] Wait 1.5s после panel open
- [ ] Alt+1 после каждой batch (6-7 элементов)
- [ ] Verify visual confirmation

**Во время создания connections:**
- [ ] Zoom to 75-100% FIRST
- [ ] Click element to see connection points
- [ ] Start drag ONLY from blue dot
- [ ] Batch по proximity
- [ ] Alt+1 после каждой batch

**После завершения:**
- [ ] Final Alt+1 verification
- [ ] Cmd+S save
- [ ] Screenshot для documentation
- [ ] Log timing metrics
