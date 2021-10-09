# Kurdish words extractor <br>

A simple script to extract Kurdish (Kurmanji) words from a text or file easily.

<br>

#### Usage:  <br>
- <strong>Basic:</strong><br>

```shell script
python kurdish-words-extractor.py -t "Ji ber ku ev nexweşî vedigire."
```
<br>
Output: <br>

```shell script
Ji
ber
ku
ev
nexweşî
vedigire
```
<br>

- <strong> From a file:</strong><br>
```shell script
python kurdish-words-extractor.py -f PATH_TO_INPUT_FILE
```
<br>

- <strong>Other arguments: </strong><br>

| Argument      | Usage |
| ----------- | ----------- |
| <i>-o OR --output</i>      | The file path where you want to save results      |
| <i>-d OR --delimiter</i>   | The delimiter that you want to divide between the extracted words  (default is a new line)      |