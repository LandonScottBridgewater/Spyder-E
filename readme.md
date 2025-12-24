# Spyder-E

Spyder-E is a variation of Spyder which does not store any project-sensitive information data on disk. 

!!!! WARNING !!!!!
This is not production ready. There are still many points of failure to address. It is in beta.

[Vanilla Spyder](https://github.com/spyder-ide/spyder)

## Installation
```
git clone https://github.com/LandonScottBridgewater/Spyder-E
cd spyder_e
pip install --upgrade pip setuptools wheel
pip install spyder-kernels
pip install .
```
## Usage

```
spyder_e
```
## Motive

I have had trouble with IDEs not giving good session-independence. I'm sure there's probably a way to do this by modifying an existing IDE, but I find that unreliable. I rather have an IDE that I can trust out of the box.

