# 🐙 Octopus Files

A versatile command-line toolkit for managing and organizing files.

> **Octopus Files is currently under development.**

## Installation

### 1. Install pipx

On Debian/Ubuntu-based systems:

```bash
sudo apt update
sudo apt install pipx
```

### 2. Make pipx available in your PATH

```bash
pipx ensurepath
```

After running this command, **restart your terminal** or log in again.

### 3. Install Octopus Files

```bash
pipx install git+https://github.com/samoraymiroy-gif/Octopus-files.git
```

### 4. Verify the installation

Check where the executable was installed:

```bash
which octopus-files
```

You should get a path similar to:

```text
/home/your-user/.local/bin/octopus-files
```

The command should now also support normal shell command completion.

## Usage

Run the tool without specifying a folder:

```bash
octopus-files
```

By default, it uses your `Downloads` folder.

You can also specify a folder:

```bash
octopus-files Documents
```

Or provide an absolute path:

```bash
octopus-files /home/user/Pictures
```

## Help

```bash
octopus-files --help
```

## Version

```bash
octopus-files --version
```

## Update

To update Octopus Files to the latest version available on GitHub:

```bash
pipx reinstall octopus-files
```

## Features

Currently, Octopus Files can:

* Count files inside a folder.
* Use the `Downloads` folder by default.
* Accept a custom folder from the command line.
* Provide a command-line interface using Python `argparse`.
* Be installed using `pipx`.

## Roadmap

Octopus Files is planned to become a general-purpose file management toolkit.

Possible future features:

* File searching
* Batch file renaming
* File organization by extension
* File copying and moving
* Duplicate file detection
* File size analysis
* More command-line options
* Shell autocomplete
* Additional file-management utilities

## Project Structure

```text
Octopus-files/
├── octopus_files/
│   ├── __init__.py
│   └── cli.py
├── pyproject.toml
└── README.md
```

## Contributing

The project is currently in its early stages. Suggestions, bug reports, and contributions are welcome.

## License

Octopus Files is licensed under the MIT License.
