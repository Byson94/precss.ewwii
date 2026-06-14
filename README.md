# precss.ewwii

Ewwii plugin that provides a list of predefined classes to make it easier to work with css.

## Prerequisite

Before you get started with using precss, make sure to store your color scheme as variables like so:

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

## Installation

Installation using [eiipm](https://github.com/ewwii-sh/eiipm)

```bash
# if you prefer prebuilt
eiipm add "byson94/precss.ewwii" --prebuilt --ref <version>

# if you prefer building yourself
eiipm add "byson94/precss.ewwii"                  # Up to date with "main" branch
eiipm add "byson94/precss.ewwii" --ref <version>  # Locked to a specific version
```

Or download from [GitHub Releases](https://github.com/byson94/precss.ewwii/releases/). 
If you are downloading manually, make sure to put it in `plugins/` directory for ewwii to load it.

## Usage

Using precss is simple. Just add one of the precss classes to your widget and see the magic!

## License

Precss is under the CC0 license. It is free to use, modify, and redistribute without any restriction whatsoever.
