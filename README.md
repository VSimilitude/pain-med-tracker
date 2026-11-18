# Pain Med Log

A personal pain-medication tracker. Single static page, no backend, no build
step. Sibling of `tooth-pain-tracker`. All entries are stored locally in the
browser's `localStorage`; nothing is sent to a server.

- One tap logs a Tylenol or ibuprofen dose at the current time (Undo in the toast).
- Each med shows a live countdown to the next allowed dose: Tylenol 4 h, ibuprofen 6 h.
- Tylenol also tracks doses in the rolling last 24 h (max 4). At the max, the
  countdown runs until the oldest of those four doses leaves the 24 h window.
- Optional 0–10 pain level: tap it within 10 minutes of a dose and it is saved
  with that dose, otherwise it is logged as its own entry.
- History tab: tap any entry to fix its time, change the pain level, or delete it.
  **Back up** exports JSON, **Restore** merges one back in.

The intervals and the daily max live in the `MEDS` table at the top of the
script in `index.html`.

## Install on iPhone

1. Open the live URL in **Safari**.
2. Tap **Share → Add to Home Screen**.
3. Launch it from the home-screen icon. It runs full-screen and works offline.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The entire app (HTML + CSS + JS in one file). |
| `manifest.json` | PWA metadata so it installs as a real app. |
| `sw.js` | Service worker: network-first, cached app shell when offline. Never touches data. |
| `icon-192.png`, `icon-512.png`, `apple-touch-icon.png` | Home-screen icons. |
| `make_icons.py` | Regenerates the icons (`python3 make_icons.py`). |

## Local development

```sh
python3 -m http.server 8000
# then visit http://localhost:8000/
```
