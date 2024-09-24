import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
from scipy.signal import butter, filtfilt
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

def clean_audio_data(data):
    # Replace NaN and infinite values with zero
    data = np.nan_to_num(data, nan=0.0, posinf=0.0, neginf=0.0)
    return data

def separate_voices_by_frequency(audio_path, output_paths, order=5):
    try:
        # Load the audio file
        y, sr = librosa.load(audio_path, sr=None)
        
        # Convert to mono if stereo
        if len(y.shape) > 1:
            y = np.mean(y.T, axis=0)
        
        # Clean the audio data
        y = clean_audio_data(y)
        
        # Define frequency ranges for eight bands
        bands = [
            (85, 300),
            (301, 475),
            (476, 650),
            (651, 825),
            (826, 1000),
            (1001, 1500),
            (1501, 3000),
            (3001, 8000)
        ]
        
        # Apply bandpass filters and save the results
        for i, (lowcut, highcut) in enumerate(bands):
            y_filtered = bandpass_filter(y, lowcut, highcut, sr, order)
            y_filtered = clean_audio_data(y_filtered)
            sf.write(output_paths[i], y_filtered, sr)
        
        # Plot original and filtered signals
        plt.figure(figsize=(20, 18))
        plt.subplot(5, 2, 1)
        librosa.display.waveshow(y, sr=sr)
        plt.title('Original Audio')
        
        for i, (lowcut, highcut) in enumerate(bands):
            plt.subplot(5, 2, i + 2)
            y_filtered = bandpass_filter(y, lowcut, highcut, sr, order)
            y_filtered = clean_audio_data(y_filtered)
            librosa.display.waveshow(y_filtered, sr=sr)
            plt.title(f'Filtered Audio ({lowcut}-{highcut} Hz)')
        
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        print(f"Error: The file '{audio_path}' was not found.")
    except ValueError as e:
        print(f"ValueError occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while playing audio: {e}")

def create_ui():
    root = tk.Tk()
    root.title("Audio Separation and Comparison")
    
    def select_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            input_audio_path.set(file_path)
    
    def process_audio():
        paths = [
            '85_300.wav',
            '301_475.wav',
            '476_650.wav',
            '651_825.wav',
            '826_1000.wav',
            '1001_1500.wav',
            '1501_3000.wav',
            '3001_8000.wav'
        ]
        separate_voices_by_frequency(input_audio_path.get(), paths)
        messagebox.showinfo("Info", "Audio processing completed.")
    
    def play_filtered_audio():
        selected_index = int(listbox.curselection()[0])
        paths = [
            '85_300.wav',
            '301_475.wav',
            '476_650.wav',
            '651_825.wav',
            '826_1000.wav',
            '1001_1500.wav',
            '1501_3000.wav',
            '3001_8000.wav'
        ]
        play_audio(paths[selected_index])
    
    input_audio_path = tk.StringVar()
    
    tk.Label(root, text="Select an audio file:").pack(pady=10)
    tk.Entry(root, textvariable=input_audio_path, width=50).pack(pady=5)
    tk.Button(root, text="Browse", command=select_file).pack(pady=5)
    tk.Button(root, text="Process Audio", command=process_audio).pack(pady=20)
    
    tk.Label(root, text="Select a filtered audio to play:").pack(pady=10)
    listbox = tk.Listbox(root)
    bands = [
        '85-300 Hz',
        '301-475 Hz',
        '476-650 Hz',
        '651-825 Hz',
        '826-1000 Hz',
        '1001-1500 Hz',
        '1501-3000 Hz',
        '3001-8000 Hz'
    ]
    for band in bands:
        listbox.insert(tk.END, band)
    listbox.pack(pady=10)
    
    tk.Button(root, text="Play Filtered Audio", command=play_filtered_audio).pack(pady=20)
    
    root.mainloop()

input_audio_path = 'C:/Users/Amir Nikzaad/Desktop/fdd/input_audio.wav'
output_audio_paths = [
    'C:/Users/Amir Nikzaad/Desktop/fdd/85_300.wav',
    'C:/Users/Amir Nikzaad/Desktop/fdd/301_475.wav',
    'C:/Users/Amir Nikzaad/Desktop/fdd/476_650.wav',
    'C:/Users/Amir Nikzaad/Desktop/fdd/651_825.wav',
    'C:/Users/Amir Nikzaad/Desktop/fdd/826_1000.wav',
    'C:/Users/Amir Nikzaad/Desktop/fdd/1001_1500.wav',
    'C:/Users/Amir Nikzaad/Desktop/fdd/1501_3000.wav',
    'C:/Users/Amir Nikzaad/Desktop/fdd/3001_8000.wav'
]

separate_voices_by_frequency(input_audio_path, output_audio_paths)
create_ui()
