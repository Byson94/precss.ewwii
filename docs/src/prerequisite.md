# Prerequisite

Before you get started with using precss, make sure to store your color scheme in variables like so:

```css
/* 
    You should use the exact name
    otherwise precss wont work.
*/
:root {
    --bg-surface: #1e1e2e;
    --bg-card: #252538;
    --border-color: rgba(255, 255, 255, 0.08);
    --fg-bright: #cdd6f4;
    --fg-default: #a6adc8;
    --fg-muted: #bac2de;
    --accent: #cba6f7;
    --critical: #f38ba8;
    --success: #a6e3a1;
}
```

This is what enables precss to access your colorscheme and work according to it.
