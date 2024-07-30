
# Gesture-Controlled Screen Brightness

This project uses OpenCV and MediaPipe to detect hand gestures and control the brightness of the screen(s) using finger gestures.

## Features

- Detect hand gestures using OpenCV and MediaPipe.
- Control screen brightness with specific finger gestures.

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- `screen-brightness-control` (for controlling screen brightness on Windows)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/gesture-controlled-brightness.git
cd gesture-controlled-brightness
```

### Step 2: Create and activate a virtual environment

```bash
python -m venv env
```

- **Windows:**

    ```bash
    .\env\Scripts\activate
    ```

- **macOS/Linux:**

    ```bash
    source env/bin/activate
    ```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

To easily run the application, a batch file `gesturecontrol.bat` is provided.

### Step 1: Add `gesturecontrol.bat` to PATH

1. Copy the absolute path of the directory of the cloned repo.

2. Add this directory to the system PATH:
   - Press `Win + X`, then select `System`.
   - Click on `Advanced system settings`.
   - Click on `Environment Variables`.
   - Under `System variables`, find the `Path` variable, select it, and click `Edit`.
   - Click `New` and add the path to the directory where `gesturecontrol.bat` is located.
   - Click `OK` to close all dialog boxes.

Now, you can run the application by typing `gesturecontrol` in the command prompt.

## How to Use

1. Run `gesturecontrol` from the command prompt.
2. Use predefined finger gestures to control the brightness of your screen.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Note

For any issues or contributions, please open an issue or a pull request on the [GitHub repository](https://github.com/yourusername/gesture-controlled-brightness).

---

## Additional Notes

- Ensure your webcam is properly connected as it will be used to detect the hand gestures.
- Test the application in a well-lit environment for better accuracy in gesture detection.
