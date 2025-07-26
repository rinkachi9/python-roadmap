# Environment setup

This guide explains how to set up a Python development environment on **Linux**, **Windows**, and **macOS**. It includes installing Python and setting up a virtual environment (`venv`).

---

## ✅ Prerequisites

* Internet connection
* Terminal / Command Prompt access
* Administrative privileges (for system-wide installs)

---

## 🐧 Linux setup

### 1. Install Python (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Verify Installation

```bash
python3 --version
pip3 --version
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Deactivate Environment

```bash
deactivate
```

---

## 🪟 Windows setup

### 1. Download & Install Python

* Visit: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
* Download the installer.
* During installation:

  * ✅ Check "Add Python to PATH"
  * ✅ Enable "pip"
  * ✅ Install `venv` (default in recent versions)

### 2. Verify Installation

```cmd
python --version
pip --version
```

### 3. Create a Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

### 4. Deactivate Environment

```cmd
deactivate
```

---

## 🍎 macOS setup

### 1. Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python

```bash
brew install python
```

### 3. Verify Installation

```bash
python3 --version
pip3 --version
```

### 4. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Deactivate Environment

```bash
deactivate
```

---

## 📦 Recommended packages

Install useful packages in your virtual environment:

```bash
pip install --upgrade pip
pip install black flake8 mypy pytest
```

---

## 🧪 Testing the setup

Create a file `hello.py`:

```python
print("Hello, Python!")
```

Run it:

```bash
python hello.py
```

---

Your environment is now ready for Python development!
