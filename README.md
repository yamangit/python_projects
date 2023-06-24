# python_projects
All kinds of python scripts and API's

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/yamangit/python_projects.git
```

### 2. Make Python environment
```bash
cd python_projects
python3 -m venv pyenv
source pyenv/bin/activate
pip install -r requirements.txt
cd Juniper_logprocrssing
```

#### 3. Run the script
```bash
python3 Script_Logprocessing.py
```
## Log samples

### 1. UI_CMDLINE_READ_LINE
```log
Jun 24 18:42:01 <hostname> <host ip>: mgd[40408]: UI_CMDLINE_READ_LINE: User '<username>', command 'show interfaces descriptions '
Jun 24 18:42:03 <hostname> <host ip>: mgd[40408]: UI_CMDLINE_READ_LINE: User '<username>', command 'show interfaces diagnostics optics xe-0/0/17 '
```
