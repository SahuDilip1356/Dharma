# Published site (GitHub Pages)

This directory is deployed when you set **Settings → Pages →** branch **`main`**, folder **`/docs`**.

- **Skills picker:** open the root of the published site (e.g. `https://sahudilip1356.github.io/Dharma/`).
- **Regenerate `index.html`** after editing any `*/SKILL.md`:

```bash
python3 scripts/generate-skills-picker.py
```

Run that from the repository root, then commit the updated `docs/index.html`.
