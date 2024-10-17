# Guide: Adding a New Linux User and Customizing Environment

This guide walks through the process of adding a new user to a Linux system, setting up SSH access, installing Miniconda, and customizing the bash prompt.

## 1. Adding a New User

1. Log in as root or a user with sudo privileges.

2. Create the new user without a password:
   ```bash
   sudo adduser --disabled-password --gecos "" vladimir_albrekht
   ```
   Replace `username` with the desired username.

3. If the home directory already exists, adjust ownership:
   ```bash
   sudo chown -R vladimir_albrekht:vladimir_albrekht /home/vladimir_albrekht
   sudo chmod 755 /home/vladimir_albrekht
   ```

## 2. Setting Up SSH Access

1. Switch to the new user:
   ```bash
   sudo su - vladimir_albrekht
   ```

2. Create and configure the SSH directory:
   ```bash
   mkdir -p ~/.ssh
   chmod 700 ~/.ssh
   touch ~/.ssh/authorized_keys
   chmod 600 ~/.ssh/authorized_keys
   ```

3. Add your public SSH key to `~/.ssh/authorized_keys`.

4. Exit the new user's shell:
   ```bash
   exit
   ```

5. Update your local SSH config file (`~/.ssh/config`):
   ```
   Host NewUserHost
     HostName your_server_ip
     User vladimir_albrekht
   ```

## 3. Installing Miniconda

1. Switch to the new user:
   ```bash
   sudo su - vladimir_albrekht
   ```

2. Download and install Miniconda:
   ```bash
   mkdir -p ~/miniconda3
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
   bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
   rm ~/miniconda3/miniconda.sh
   ```

3. Initialize Miniconda:
   ```bash
   ~/miniconda3/bin/conda init bash
   ```

4. Reload the bash configuration:
   ```bash
   source ~/.bashrc
   ```

## 4. Customizing the Bash Prompt

1. Open the `.bashrc` file:
   ```bash
   nano ~/.bashrc
   ```

2. Add the following code at the end of the file:
   ```bash
   # Conda environment display in prompt
   conda_env() {
       if [ -n "$CONDA_DEFAULT_ENV" ]; then
           echo "($CONDA_DEFAULT_ENV) "
       fi
   }

   # Set the prompt
   PS1='$(conda_env)\[\033[01;34m\]\w\[\033[00m\]\$ '
   ```

3. Save and exit the file (Ctrl+X, then Y, then Enter).

4. Reload the bash configuration:
   ```bash
   source ~/.bashrc
   ```

Your new prompt will now display the active conda environment (if any) and the current directory in blue, followed by a $ sign:

```
(base) ~/projects$ 
```

## Optional: Including Conda Version in Prompt

If you want to include the conda version in your prompt, replace the PS1 line in step 2 of the "Customizing the Bash Prompt" section with:

```bash
PS1='$(conda_env)(conda $(conda --version | cut -f2 -d" ")) \[\033[01;34m\]\w\[\033[00m\]\$ '
```

This will result in a prompt like:

```
(base) (conda 23.7.1) ~/projects$ 
```

Remember to source your `.bashrc` file or log out and log back in for changes to take effect.

## 5. Adding Custom Aliases and Functions

You can add custom aliases and functions to your `.bashrc` file to create shortcuts for frequently used commands. Here's how to do it:

1. Open your `.bashrc` file:
   ```bash
   nano ~/.bashrc
   ```

2. Add the following lines at the end of the file:

   ```bash
   # Custom aliases
   alias n='nvidia-smi'
   alias c='cd ..'

   # Custom functions
   function mkcd() {
       mkdir -p "$1" && cd "$1"
   }
   ```

3. Save and exit the file (Ctrl+X, then Y, then Enter).

4. Reload your `.bashrc` file:
   ```bash
   source ~/.bashrc
   ```

Now you have the following shortcuts:

- Type `n` to run `nvidia-smi`
- Type `c` to go up one directory (equivalent to `cd ..`)
- Use `mkcd directory_name` to create a new directory and immediately change into it

You can add more aliases and functions as needed. Here are some examples:

```bash
# More alias examples
alias update='sudo apt update && sudo apt upgrade'
alias ll='ls -alF'
alias py='python3'

# More function examples
function extract() {
    if [ -f $1 ] ; then
        case $1 in
            *.tar.bz2)   tar xjf $1     ;;
            *.tar.gz)    tar xzf $1     ;;
            *.bz2)       bunzip2 $1     ;;
            *.rar)       unrar e $1     ;;
            *.gz)        gunzip $1      ;;
            *.tar)       tar xf $1      ;;
            *.tbz2)      tar xjf $1     ;;
            *.tgz)       tar xzf $1     ;;
            *.zip)       unzip $1       ;;
            *.Z)         uncompress $1  ;;
            *.7z)        7z x $1        ;;
            *)           echo "'$1' cannot be extracted via extract()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}
```

Remember to source your `.bashrc` file or log out and log back in for changes to take effect.

These customizations can significantly speed up your command-line workflow by reducing the amount of typing needed for common tasks.