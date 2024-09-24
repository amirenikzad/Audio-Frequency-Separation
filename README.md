# Audio Frequency Separation

## Overview
This program separates frequencies of an audio file to isolate specific sounds, such as voices of individuals from background noise, or distinguishing between male and female voices.
# The program asks you to give it the path of an audio file
![AFS](https://github.com/user-attachments/assets/576800a2-99a3-4e68-b621-447757df7c51)

# And the form of separation of signals from the beginning to the details of all audio files
![Audio Frequency Separation](https://github.com/user-attachments/assets/e946322f-67f0-4e30-a62d-6a5cd4abf9ae)


### Technologies Used
- **Python**: Core programming language.
- **Librosa**: For audio loading and display.
- **NumPy**: For numerical operations on audio data.
- **Matplotlib**: Used for plotting waveforms.
- **Soundfile**: For reading and writing audio files.
- **SciPy**: Specifically `butter` and `filtfilt` from `scipy.signal` for bandpass filtering.
- **Tkinter**: GUI library for creating the user interface.
- **Pygame**: For playing audio within the application.

## Code Overview

The program includes functionalities to:
- Load an audio file.
- Apply bandpass filters to isolate specific frequency ranges (e.g., 85-300 Hz, 301-475 Hz, etc.).
- Display original and filtered audio waveforms using Matplotlib.
- Play back the filtered audio to listen to isolated frequency bands.

### Example Usage
This script processes an audio file, separates it into different frequency bands, and provides a user interface for playback and visualization of the filtered audio.
```python
input_audio_path = 'input_audio.wav'
output_audio_paths = [
    '85_300.wav',
    '301_475.wav',
    '476_650.wav',
    '651_825.wav',
    '826_1000.wav',
    '1001_1500.wav',
    '1501_3000.wav',
    '3001_8000.wav'
]

separate_voices_by_frequency(input_audio_path, output_audio_paths)
create_ui()
```
### How to Use
1. Ensure you have Python installed on your machine.
2. Install the required libraries:
    ```bash
    pip install numpy matplotlib librosa soundfile pygame
    ```
3. Modify the script (`your_script_name.py`) to specify your input audio file (`input_audio.wav`) and output paths for filtered audio files (`output_audio_paths`).

4. Run the script:
    ```bash
    python your_script_name.py
    ```

The GUI will allow you to select an audio file, process it to separate frequencies, and listen to the filtered audio bands interactively.

---

Feel free to expand on or customize this script based on your specific needs!




