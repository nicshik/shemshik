# retrospective_v5_code.md

## Code Templates & Quick Reference

### Production-Ready Templates v6.0

**Template 1: Create Rectangle**
```javascript
const createRectangleV6 = (name, x1, y1, x2, y2) => [
    // Open Shapes panel
    {"action": "leftclick", "coordinate": [32, 337]},
    {"action": "wait", "duration": 1},
    // Select Rectangle
    {"action": "leftclick", "coordinate": [96, 298]},
    {"action": "wait", "duration": 1.5},
    // Draw
    {"action": "leftclickdrag", "startcoordinate": [x1, y1], "coordinate": [x2, y2]},
    // Label
    {"action": "type", "text": name},
    {"action": "key", "text": "Escape"},
    {"action": "wait", "duration": 1}
];
```

**Template 2: Create Connection**
```javascript
const createConnectionV6 = (fromElement, toElement) => { ... }
```

**Template 3: Create Connection with Zoom**
```javascript
const createConnectionWithZoomV6 = (connections) => { ... }
```

### Constants & Configuration

**UI Coordinates (Nov 2025):** ...
**Timing Constants:** ...
**Canvas Configuration:** ...
**Helper Functions:** ...
**Complete Workflow Template:** ...
