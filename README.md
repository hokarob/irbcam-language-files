# Translations for IRBCAM Client
Thank you for your interest in helping us translate [IRBCAM](https://irbcam.com). We appreciate your contributions in making IRBCAM more accessible to users around the world. This README provides information on how to get started with translating the user interface (UI) and submitting your translations as Pull Requests (PRs).

## Getting Started

### Fork the Repository

1. Fork this repository to your own GitHub account by clicking the "Fork" button at the top of this page.

### Clone Your Fork

1. Clone the repository from your GitHub account to your local machine. Replace `[your_username]` with your GitHub username.

   ```bash
   git clone https://github.com/[your_username]/[repository_name].git
   ```

2. Navigate to the project directory:
    ```bash
    cd [repository_name]
    ```

### Translate
Translations are stored in `irbcam_XX.ts` files, where **XX** corresponds to the [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for a given language. The easiest way to edit the files is to use [Qt Linguist](https://doc.qt.io/qt-6/linguist-translators.html). 

### Submit Your Translation
1. Commit your changes wit ha meaningful commit message:
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

<!-- Language translations for the IRBCAM client

Use linguist to edit the TS files

On Linux ```sudo apt install qttools5-dev-tools```

Standalone binaries of linguist for Windows and MAC: [https://github.com/lelegard/qtlinguist-installers/releases](https://github.com/lelegard/qtlinguist-installers/releases) -->
