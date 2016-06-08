# text-substitution

This script uses the Yandex API to translate text data.
Install Yandex Translate API using:
```bash
pip install yandex.translate
```

```bash
Usage:
python textsub.py [option] <argument>
Options:
--extract-text - extract text from the sample html file and generate a .properties file.
--generate-resource <language-code> - genearate the translated .properties file in the language specified by "language-code".
--display-html - create a translated HTML page.
--help - display this help text.

Supported language codes:
{'et', 'ro', 'sq', 'da', 'sk', 'tr', 'sr', 'lt', 'el', 'sl', 'be', 'ru', 'es', 'en', 'pt', 'fr', 'no', 'mk', 'fi', 'hy'}
```
