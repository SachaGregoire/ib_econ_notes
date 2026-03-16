# IB Economics Notes

This repository contains IB Economics revision material for Units 2 to 4, plus helper scripts for generating economics diagrams and compiling the detailed notes into PDF.

## Files

- `IB_Economics_Topics_Units2-4.md`: topic checklist / revision outline.
- `IB_Economics_DETAILED_Units2-4.md`: detailed notes source used for PDF export.
- `generate_graphs.py`: generates all economics diagrams as PNG files.
- `generate_graphs_live.py`: runs selected diagrams and supports live watch mode.
- `generate_command.txt`: example `pandoc` command for compiling the detailed notes into PDF.
- `COMPILE_TOOL_GUIDE.md`: short setup guide for the PDF compile toolchain.

## Requirements

### PDF compilation

- `pandoc`
- A LaTeX engine with `xelatex` available on your PATH

This repo's compile command uses:

- `--pdf-engine=xelatex`
- `Georgia`, `Segoe UI`, and `Consolas` as fonts

If those fonts are missing, either install them or change the font flags in `generate_command.txt`.

### Graph generation

- Python 3
- Packages from `requirements.txt`

Install Python packages with:

```bash
pip install -r requirements.txt
```

## Compile The Notes To PDF

The example compile command is stored in `generate_command.txt`.

On Windows PowerShell, run the equivalent command from the repository root:

```powershell
pandoc "IB_Economics_DETAILED_Units2-4.md" `
--pdf-engine=xelatex `
--number-sections `
-V documentclass=report `
-V fontsize=11pt `
-V linestretch=1.2 `
-V geometry:margin=1in `
-V mainfont="Georgia" `
-V sansfont="Segoe UI" `
-V monofont="Consolas" `
-V colorlinks=true `
-V linkcolor=black `
-V urlcolor=black `
-V citecolor=black `
-o "IB_Economics_DETAILED_Units2-4.pdf"
```

If `pandoc` or `xelatex` is not installed yet, use the setup steps in `COMPILE_TOOL_GUIDE.md`.

## Generate Diagrams

Generate all diagrams:

```bash
python3 generate_graphs.py
```

List available diagram names:

```bash
python3 generate_graphs_live.py --list
```

Render one diagram:

```bash
python3 generate_graphs_live.py --only 2_3a_market_equilibrium
```

Watch one diagram and re-render on save:

```bash
python3 generate_graphs_live.py --watch --only 2_3a_market_equilibrium
```

## Notes

- `generate_graphs.py` currently writes output to the `OUT_DIR` path defined inside the script.
- `generate_graphs_live.py` can override the output folder with `--out-dir`.
