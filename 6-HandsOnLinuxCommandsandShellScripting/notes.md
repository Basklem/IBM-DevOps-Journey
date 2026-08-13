# Hands-on Introduction to Linux Commands and Shell Scripting — Notes

## Key Takeaways

- **Unix** (1960s, Bell Labs) is a family of OSs; **Linux** (1991, Linus Torvalds + 1980s GNU tools) is its free, open-source, Unix-like descendant — multi-user, multitasking, portable, and now running everything from Android phones to supercomputers and cloud data centers.
- A **distro** is a flavor of Linux built on the Linux kernel, differentiated by bundled utilities, GUI, shell, and support model — e.g., Debian/Ubuntu (community, server/desktop), RHEL/Fedora/SUSE (enterprise), Arch (DIY).
- A Linux system has five layers — UI → applications → OS → **kernel** (bridges apps and hardware via system calls) → hardware — and a tree-shaped **filesystem** rooted at `/` (`/bin`, `/usr`, `/home`, `/boot`, `/media`).
- You work in a **terminal** that passes commands to a **shell** (e.g., bash); navigate the filesystem with `cd` and paths (`~` home, `/` root, `..` parent, `.` current).
- Text editing: GUI (gedit) or command line — **nano** (modeless, Ctrl-key commands) and **vim** (Insert mode `i` vs. Command mode — `:w`, `:q`, `:q!`).
- Software ships as **.deb** or **.rpm** packages managed by package managers that resolve dependencies: apt/Update Manager (deb) and yum/PackageKit (RPM); `pip` does the same for Python libraries.
- Core command survival kit: info (`whoami`, `uname`, `df -h`, `ps`/`top`, `man`), navigation (`ls -l`, `pwd`, `cd`, `find . -name`), management (`mkdir`/`rmdir`, `touch`, `cp -r`, `mv`, `rm -r` with care, `chmod +x`), viewing (`cat`, `more`, `head`/`tail -n`, `wc -l`).
- Text wrangling: `sort`, `uniq` (consecutive duplicates only), `grep -i`, `cut -d " " -f 2`, `paste` — the building blocks of file-based data processing.
- Networking: `hostname`/`ip a` for your config, `ping` for connectivity (ICMP), `curl` to transfer data to/from URLs, `wget` to download files (with recursion).
- `tar -czf`/`-xzf` archives then gzips (tarball); `zip -r`/`unzip` compresses then bundles — archiving is for portability/backup, compression for size.

---

## Notes

### Module 1: Introduction to Linux

**Introducing Linux and Unix**
- **OS** = software that manages computer hardware/resources and lets you interact with the hardware to do useful tasks.
- **Unix** = a *family* of operating systems (Oracle Solaris, FreeBSD, HP-UX, IBM AIX, Apple macOS). History: created at AT&T Bell Labs in the 1960s for the PDP-7 → rewritten in **C** in the 1970s (made it portable across hardware) → late 1970s, UC Berkeley builds **BSD** on top (macOS later derives from BSD).
- **Linux** = a family of Unix-*like* OSs; "Linux" usually refers to a specific distribution. Built as a free, open-source version of Unix.
- Origin: 1980s **GNU** ("GNU's Not Unix," MIT) recreates Unix tools as free software → 1991 **Linus Torvalds** releases the Linux **kernel** (the OS core that talks to hardware) → 1992 GNU + Linux kernel unify into usable OSs → 1996 Tux the penguin becomes the mascot (Larry Ewing).
- Key features: free and open source (many eyes on the code → strong security), multi-user, multitasking, portable.
- Where Linux runs today: Android phones (Linux-based kernel), supercomputers, enterprise/cloud data centers, and desktops (e.g., Ubuntu).

**Linux Distributions**
- **Distro** = a specific flavor of Linux; all use the Linux kernel. Hundreds exist, each catering to an audience/task.
- Distros differ by: default utilities/apps, GUI, supported shell commands, and support model — community vs. commercial, **LTS** vs. **rolling release**.
- Notable distros:
  - **Debian** (1993): stable, reliable, fully open source; big in servers; largest community-run distro.
  - **Ubuntu** (2004): Debian-based; managed by Canonical; editions — Desktop, Server, Core (IoT).
  - **Red Hat Enterprise Linux (RHEL)**: "core" distro (not derived from another); enterprise-focused; managed by Red Hat (an IBM subsidiary).
  - **Fedora**: stable, secure (notable firewall/security features); sponsored by Red Hat, which reuses much of Fedora's code base after testing.
  - **SUSE Linux Enterprise (SLE)**: Server (SLES) and Desktop (SLED) editions; many architectures (incl. ARM/Raspberry Pi); SUSE Package Hub for extra packages.
  - **Arch Linux**: DIY, fully customizable, bleeding-edge packages — requires strong Linux knowledge; stability not the priority.

**Overview of Linux Architecture**
- Five layers, outermost → innermost:
  1. **UI** — keyboard/mouse interaction; desktop distros add a GUI.
  2. **Applications** — system tools (compilers), programming languages, shells, user apps.
  3. **OS** — system health/stability: job scheduling, timekeeping, assigning software to users, error detection, file management.
  4. **Kernel** — lowest-level software, complete control; boots first and stays in memory; bridges apps ↔ hardware via **system calls**. Four jobs: memory management, process management, device drivers, security.
  5. **Hardware** — CPU, RAM, persistent storage, screen, USB devices.
- **Filesystem**: tree structure starting at the **root directory `/`**, with access rights per file/directory. Key directories: `/bin` (user binaries — program/command code), `/usr` (user programs), `/home` (your personal working directory), `/boot` (system startup files), `/media` (temporary media like CDs/USB drives).

**Linux Terminal Overview**
- **Shell** = OS-level application that interprets commands (originally the *only* way to use Unix/Linux). Uses: move/copy files, read/write files, extract/filter data, search. Popular shells: **bash**, **zsh** (base functionality is similar).
- **Terminal** = the app where you type commands and see output. Flow: user types in terminal → shell → kernel/OS translates for hardware → results come back through shell to terminal.
- **Command line** = where you type; the cursor/**command prompt** marks where text appears.
- **Current working directory** = where the shell looks for commands/files you name; shown (fully or partially) in the prompt.
- **Paths**: `A/B` = B inside A. Special paths: `~` home directory, leading `/` = root, `..` parent directory, `.` current directory.
- Navigation with `cd`: `cd /` (root), `cd bin` (into bin), `cd ~` (home), `cd ..` (up one), and combined moves like `cd ../..` or absolute paths like `cd /home/me/documents`.
- `./ls` runs the `ls` executable from the current directory; since common commands are built into the shell, `ls` also works from anywhere.

**Creating and Editing Text Files**
- Two editor categories: **command-line** (GNU nano, vi, vim) and **GUI** (gedit); **emacs** works in both modes and is one of the oldest active open-source projects.
- **gedit** (GNOME default, preinstalled on most distros): simple general-purpose GUI editor — integrated file browser, undo/redo, search/replace with regex, plugin extensibility, syntax highlighting.
- **nano**: modeless command-line editor — `nano filename` to open; edit directly, navigate with arrows/PgUp/PgDn/Home/End; commands via Ctrl+letter shown at the bottom (e.g., Ctrl+G help, Ctrl+W "Where Is" search). Features: undo/redo, regex search/replace, syntax highlighting, auto-indent, line numbers, multiple buffers.
- **vim**: powerful *mode-based* editor (`vim` or `vim filename`). Two basic modes:
  - **Insert mode** (`i`) — type text; Esc returns to Command mode.
  - **Command mode** — everything else: `:sav filename` save new file, `:w` write changes, `:q` quit, `:q!` quit discarding unsaved changes.

**Installing Software and Updates**
- **Packages** = archive files containing what's needed to install or update software; **package managers** handle download/installation (GUI or command-line).
- Two package formats: **.deb** (Debian-based: Debian, Ubuntu, Mint) and **.rpm** (Red Hat-based: RHEL/CentOS, Fedora, openSUSE). Contents are equivalent — convert between them with the **alien** tool (`alien pkg.rpm` → deb; `alien -r pkg.deb` → rpm).
- Package manager benefits: automatic dependency resolution, update notifications, scheduled security checks (GUI ones), selective or automatic installs.
- By distro family:
  - deb GUI: **Update Manager** — checks daily, auto-installs security updates, shows others weekly.
  - deb CLI: **apt** — `sudo apt update` (refresh available packages), `sudo apt upgrade` (upgrade everything), `sudo apt install <name>`.
  - RPM GUI: **PackageKit** — starburst icon in the notification area when updates are ready.
  - RPM CLI: **yum** (Yellowdog Updater, Modified) — `sudo yum update`, `sudo yum install <name>`.
- Language-level package managers exist too, e.g., Python's **pip**/conda: `pip install pandas` finds the latest version, resolves dependencies, installs.

### Module 2: Introduction to Linux Commands

**Overview of Common Linux Shell Commands**
- A **shell** is a user interface that interprets commands and runs programs — it's both an interactive language and a scripting language (for automating tasks). Default on most Linux: **bash** ("Bourne Again Shell"); others: sh, ksh, tcsh, zsh, fish. Check yours with `printenv SHELL`; switch by typing `bash`.
- Command categories (detailed in later videos):
  - Info: `whoami`, `id`, `uname`, `ps`, `top`, `df`, `man`, `date`
  - Files: `cp`, `mv`, `rm`, `touch`, `chmod`, `wc`, `grep`
  - Directories: `ls`, `find`, `pwd`, `mkdir`, `cd`, `rmdir`
  - Printing content: `cat`, `more`, `head`, `tail`, `echo`
  - Compression/archiving: `tar`, `zip`, `unzip`
  - Networking: `hostname`, `ping`, `ifconfig`, `curl`, `wget`
- Running Linux on Windows: dual-boot partition, virtual machine, emulator (Cygwin), or **WSL** (Windows Subsystem for Linux — runs Linux binaries natively).

**Informational Commands**
- `whoami` — current username. `id` — user/group IDs (`-u` numeric user ID, add `-n` for the name).
- `uname` — OS info: alone gives kernel name; `-s -r` name + version; `-v` detailed version.
- `df` — disk usage of mounted filesystems; `-h` for human-readable units (GB/TB); `df -h ~` scopes to the home directory's disks.
- `ps` — running processes with PIDs (`-e` = all users' processes). `top` — live "task manager" with CPU/memory usage, sorted by CPU by default (`-n 3` = top 3 tasks).
- `echo` — print text or variables: `echo "string"` (quotes are best practice), `echo $PATH` for variables.
- `date` — current date/time; format with `+"..."` and `%` controls (e.g., `%j` day of year, `%Y` year, `%A` weekday).
- `man <command>` — the manual for any default command (square brackets = optional parameters); `man man` works too.

**File and Directory Navigation Commands**
- `ls` — list directory contents; takes a directory as argument (`ls Downloads`); `-l` for long format (permissions, last-modified, owner).
- `pwd` — print (present) working directory.
- `cd` — change directory using **relative** paths (relative to where you are: `cd Documents`, `cd ..`) or **absolute** paths (stand independently: `cd ~` home, `cd /home/me/Documents/Notes`).
- `find` — return paths of all files matching a criterion: `find . -name "a.txt"` (`.` = search from current directory); `-iname` = case-insensitive.

**File and Directory Management Commands**
- `mkdir test` — create a directory; `rmdir` — remove *empty* directories only (safe: can't nuke data).
- `rm file1` — remove a file; `rm -r folder1` — remove a directory and everything in it (**use with care**; prefer `rmdir` for empty dirs).
- `touch a.txt b.txt` — create empty files; on an existing file it updates the last-modified timestamp (check with `date -r file`).
- `cp src dest` — copy a file (destination filename optional; source defaults to current dir); `cp -r` to copy directories recursively.
- `mv source target_dir` — move (or rename) files and directories; can move multiple at once: `mv Notes Scripts Documents`.
- `chmod` ("change mode") — change read/write/execute permissions: a script with only `rw` gives "permission denied" when run; `chmod +x my_script.sh` makes it executable (verify with `ls -l` — look for the `x`).

**Viewing File Content**
- `cat file` — print the whole file (impractical for long files).
- `more file` — page-by-page view (page = terminal window); Space = next page, `q` = quit.
- `head file` / `tail file` — first/last 10 lines; `-n 3` to change the count.
- `wc file` — counts, output "lines words characters" (newlines count as characters!); `-l` lines only, `-w` words only, `-c` bytes only.

**Useful Commands for Wrangling Text Files**
- `sort file` — alpha-numeric line sort to stdout; `-r` reverse order.
- `uniq file` — filter out repeated lines, but only *consecutive* duplicates (a "cat" before and after "dog" lines still appears twice).
- `grep` ("global regular expression print") — return lines matching a pattern: `grep ch people.txt`; `-i` = case-insensitive.
- `cut` — extract slices/fields from each line: `-c 2-9` = characters 2–9; `-d " " -f 2` = split on space delimiter and take field 2 (e.g., last names).
- `paste file1 file2 file3` — merge lines from multiple files side by side (tab delimiter by default; `-d ","` to change) — turns parallel files into a table.

**Networking Commands**
- `hostname` — get/set the machine's hostname (`-s` drops the `.local` domain suffix; `-i` shows its IP address).
- `ip` — configure/display network interfaces: `ip a` = all interfaces (IPs, MAC addresses); `ip addr show eth0` = one device (packets sent/received, errors, drops).
- `ping url` — test connectivity: sends **ICMP** echo requests, prints a line per response (IP, round-trip ms) until Ctrl+C, then summary stats (packets sent/received/lost, min/avg/max/stddev times); `-c 5` = stop after 5 pings.
- `curl url` — transfer data to/from URLs, many protocols; `curl www.google.com` prints the page HTML; `-o file.txt` writes output to a local file.
- `wget url` — retrieve files from a URL; like curl but more specialized, with recursive download support (can grab a whole folder of files); auto-names the saved file.

**File Archiving and Compression Commands**
- **Archiving** = bundling files/directories into a single file for portability/backup; **compression** = shrinking file size by exploiting redundancy (saves storage, speeds transfers, reduces bandwidth). Distinct processes, usually combined.
- `tar` ("tape archiver") — archive/de-archive ("tarball"):
  - Create: `tar -cf notes.tar notes` (`c` = create, `f` = to/from file)
  - Create compressed: `tar -czf notes.tar.gz notes` (`z` = filter through **gzip**; `.gz` suffix helps Windows programs recognize it)
  - List contents: `tar -tf notes.tar`
  - Extract: `tar -xf notes.tar [dest]`; extract + decompress: `tar -xzf notes.tar.gz [dest]`
- `zip -r notes.zip notes` — compress *then* bundle (opposite order from tar, which bundles then gzips the whole tarball); `unzip notes.zip` extracts and decompresses.
- `ls -R` — recursively list a directory tree (handy for verifying archive/unpack results).

### Module 3: Introduction to Shell Scripting

<!-- Videos: Shell Scripting Basics · Filters, Pipes, and Variables · Useful Features of the Bash Shell · Scheduling Jobs using Cron -->

### Module 4: Final Project and Final Exam

<!-- No lecture videos — practice project (weather ETL + forecast accuracy), final project (scheduled backup script), final exam -->
