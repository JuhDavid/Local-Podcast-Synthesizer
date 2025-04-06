
# 🎙Your very own Local Podcast Synthesizer

Welcome to **Podcast Synthesizer** – a fun and modular Python project that transforms any PDF into engaging podcast episodes! This project leverages a local AI model using Ollama for text processing and Piper for text-to-speech synthesis to create audio content from your documents.

In this project, we redefine the humble "PDF" as a **Podcast Delivery File (PDF)**—because every document deserves its chance to be heard!

---

## 🚀 Features

- **PDF Extraction:** Extract text from your Podcast Delivery Files (PDFs) and prepare them for audio transformation.
- **Local AI Processing:** Use your chosen local AI model to convert complex research content into a friendly podcast script.
- **Podcast Script Generation:** Segment and process the extracted text into a clear, engaging script.
- **Text-to-Speech Synthesis:** Transform your script into high-quality audio with Piper.
- **Customizable Workflow:** Easily specify file paths, models, and even the output audio file title at runtime.

---

## 📂 Project Structure

The project is organized into several modules for clarity and ease of maintenance:

```
project/
 ├── main.py                 # Orchestrates the overall workflow.
 ├── pdf_extractor.py        # Extracts text from PDFs (a.k.a. Podcast Delivery Files).
 ├── localai.py              # Interacts with the Local AI model for text processing.
 ├── podcast_generator.py    # Generates the podcast script from extracted text.
 └── tts_synthesizer.py      # Synthesizes speech using Piper.
```

---

## 🔧 Installation

1. **Clone the Repository**


2. **Set Up a Virtual Environment**


3. **Install Dependencies**


4. **Download Piper**

   Download Piper and your desired models/config files from the [Piper Releases](https://github.com/rhasspy/piper/releases) page, and place them in your designated Piper directory.

---

## ⚙️ Usage

Run the main script and follow the on-screen prompts

You'll be asked for:
- The **PDF file path** (your Podcast Delivery File).
- The **Piper directory** (where `piper.exe`, the model, and config files reside).
- The **Piper model filename** (e.g., `en_US-amy-medium.onnx`).
- The **Piper config filename** (e.g., `en_US-amy-medium.onnx.json`).
- The **local AI model name** (e.g., `deepseek-R1:1.5b`).
- A **title for your audio file** (without extension).

Watch as your PDF transforms into an engaging podcast script and then into a polished audio file!

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests. Whether you have new features, bug fixes, or suggestions, please open an issue or a pull request to discuss your ideas.


---

## 🎉 Acknowledgements

- Thanks to the [Piper project](https://github.com/rhasspy/piper) for their amazing text-to-speech engine.
- Kudos to all open-source contributors whose work has made this project possible.
- A special shoutout to you for exploring and using this project!

---

Happy Podcasting! 🎧✨

