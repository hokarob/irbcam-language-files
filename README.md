<p align="center">
  <a href="https://github.com/hokarob/irbcam-language-files/blob/main/irbcam_no.ts"><img alt="Norwegian" src="https://hokarob.github.io/irbcam-language-files/no.svg?kill_cache=1" /></a>
  <a href="https://github.com/hokarob/irbcam-language-files/blob/main/irbcam_de.ts"><img alt="German" src="https://hokarob.github.io/irbcam-language-files/de.svg?kill_cache=1" /></a>
  <a href="https://github.com/hokarob/irbcam-language-files/blob/main/irbcam_sv.ts"><img alt="Swedish" src="https://hokarob.github.io/irbcam-language-files/sv.svg?kill_cache=1" /></a>
  <a href="https://github.com/hokarob/irbcam-language-files/blob/main/irbcam_fr.ts"><img alt="French" src="https://hokarob.github.io/irbcam-language-files/fr.svg?kill_cache=1" /></a>
  <a href="https://github.com/hokarob/irbcam-language-files/blob/main/irbcam_hu.ts"><img alt="Hungarian" src="https://hokarob.github.io/irbcam-language-files/hu.svg?kill_cache=1" /></a>
  <a href="https://github.com/hokarob/irbcam-language-files/blob/main/irbcam_lt.ts"><img alt="Lithuanian" src="https://hokarob.github.io/irbcam-language-files/lt.svg?kill_cache=1" /></a>
  <a href="https://github.com/hokarob/irbcam-language-files/blob/main/irbcam_pt.ts"><img alt="Polish" src="https://hokarob.github.io/irbcam-language-files/pt.svg?kill_cache=1" /></a>
  <a href="https://github.com/hokarob/irbcam-language-files/blob/main/irbcam_sl.ts"><img alt="Slovene" src="https://hokarob.github.io/irbcam-language-files/sl.svg?kill_cache=1" /></a>
</p>

# Translations for IRBCAM Client
Thank you for your interest in helping us translate [IRBCAM](https://irbcam.com). We appreciate your contributions in making IRBCAM more accessible to users around the world. This README provides information on how to get started with translating the user interface (UI) and submitting your translations as Pull Requests (PRs).

## Getting Started

### Install Git
Install git on your computer. Most Linux distros and MacOS already come with git installed. For Windows, you can find an installer [here](https://git-scm.com/download/win).

### Fork the Repository

1. Fork this repository to your own GitHub account by clicking the "Fork" button at the top of this page.

### Clone Your Fork

1. Clone the repository from your GitHub account to your local machine. Replace `[your_username]` with your GitHub username.

   ```bash
   git clone https://github.com/[your_username]/irbcam-language-files.git
   ```

2. Navigate to the project directory:
    ```bash
    cd [repository_name]
    ```

### Prepare Your Tools
Translations are stored in `irbcam_XX.ts` files, where **XX** corresponds to the [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for a given language. The files are formatted as XML and the easiest way is to edit with the Qt Linguist application. You can either get Linguist by installing Qt developer tools, or by using a standalone installer.

**Standalone Installers**

- [Official Linguist installer for Windows](https://download.qt.io/linguist_releases/)
- [Official Flatpak for Linux](https://flathub.org/apps/io.qt.Linguist)
- [Third party Windows/MacOS installers](https://github.com/lelegard/qtlinguist-installers/releases)



### Translate
Add or modify translations to the file(s) you want to edit. You can look in the [user manual](https://doc.qt.io/qt-6/linguist-translators.html) for Qt Linguist for instructions on how to use it. When you are done, save the file.

### Submit Your Translation
1. Commit your changes with a meaningful commit message:
    ```bash
    git add
    git commit -m "Updated translation for [Language Name]"
    ```

2. Push the changes to your GitHub repository:
    ```bash
    git push
    ```

### Create a Pull Request
1. Visit your GitHub repository and click on the "New Pull Request" button.
2. Choose the original repository (the one you forked from) as the base repository and your fork as the head repository.
3. Describe your changes and submit the Pull Request.

## Guidelines
- Use clear and consistent translations.
- Be mindful of context and ensure translations make sense within the UI.
- If you encounter any techical or terminology-related issues, feel free to ask questions in the Pull Request.
- We appreciate your help and will review your contributions as soon as possible.

## Contact
If you have any questions or ned assistance, please feel free to reach out to us on [our discussion forum](https://forum.hokarob.com).

Thank you for helping us make IRBCAM accessible to a global audience!

