# Spyder-E

Spyder-E is a variation of Spyder which does not store any project-sensitive information data on disk.

# Installation

```
unalias spyder

git clone https://github.com/LandonScottBridgewater/Spyder-E/spyder_e
pip install --upgrade pip setuptools wheel
pip install spyder-kernels
pip install .

spyder_e
```

## Usage

```
spyder_e
```

# Motive

I have had trouble with IDEs not giving good session-idependance. I'm sure there's probably a way to do this by modifying an existing IDE, but I find that unreliable. I rather have an IDE that I can trust.
