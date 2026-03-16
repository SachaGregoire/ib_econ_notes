# Compile Tool Guide

This project uses `pandoc` to convert markdown into PDF, with `xelatex` as the PDF engine.

## What To Install

Install:

- `pandoc`
- A LaTeX distribution that includes `xelatex`

Recommended options:

- Windows: `Pandoc` + `MiKTeX`
- macOS: `Pandoc` + `MacTeX`
- Linux: `pandoc` + `texlive-xetex`

## Windows Setup

### 1. Install Pandoc

Download and install Pandoc from:

- https://pandoc.org/installing.html

Then confirm it works:

```powershell
pandoc --version
```

### 2. Install a LaTeX distribution

Install MiKTeX from:

- https://miktex.org/download

Then confirm `xelatex` is available:

```powershell
xelatex --version
```

If `xelatex` is not found, restart your terminal after installation.

## macOS Setup

Install with Homebrew and MacTeX:

```bash
brew install pandoc
brew install --cask mactex
```

Verify:

```bash
pandoc --version
xelatex --version
```

## Linux Setup

Ubuntu/Debian example:

```bash
sudo apt update
sudo apt install pandoc texlive-xetex
```

Verify:

```bash
pandoc --version
xelatex --version
```

## Compile Command

From the repository root:

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

## Common Problems

- `pandoc: command not found`
  Install Pandoc and reopen the terminal.

- `xelatex not found`
  Install a LaTeX distribution and make sure its binaries are on your PATH.

- Font errors
  Install `Georgia`, `Segoe UI`, and `Consolas`, or replace those font settings in `generate_command.txt`.
