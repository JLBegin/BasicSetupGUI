# Python GUI setup with PyQt5
Basic code setup for GUI development with PyQt5 and its Designer tool that implements a custom widget for matplotlib and live updates using QtThreads.

&nbsp;

## Requirements

```bash
pip install pyqt5
```

&nbsp;

## Usage

Simply copy the `code` folder to start developping your own GUI. 

You can run this basic GUI by running `main.py`.

&nbsp;

## Development

There's a few things to know in order to easily update the GUI.



### Updating the UI

1. Open the `.ui` file of interest with the Designer program that comes with PyQt. Designer is usually inside `Anaconda/Library/bin/`.

2. Modify the UI (remember to rename objects with good names) and save (replacing old `.ui` file).

3. Convert to python by opening a command prompt where the `.ui` file is and type:

   ```bash
   pyuic5 yourWindowFileUi.ui > yourWindowFileUi.py
   ```

And this should work. 

> If you get a null bytes error from importing Ui_yourWindow, go to yourWindowUi.py file, remove the first line (forced encoding) and convert the file encoding with your IDE to UTF-8 (bottom right on PyCharm)

