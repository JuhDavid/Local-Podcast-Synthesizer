import os
from pdf_extractor import extract_text_from_pdf
from podcast_generator import generate_podcast_script
from tts_synthesizer import synthesize_speech_with_piper

def main():
    # Ask user for the required paths and model details
    pdf_path = input("Enter the path to the research paper (PDF): ").strip().strip('"').strip("'")
    piper_dir = input("Enter the path to the Piper directory: ").strip().strip('"').strip("'")
    model_filename = input("Enter the Piper model filename (e.g., en_US-amy-medium.onnx): ").strip()
    config_filename = input("Enter the Piper config filename (e.g., en_US-amy-medium.onnx.json): ").strip()
    localai_model = input("Enter the Local AI model name (e.g., deepseek-R1:1.5b): ").strip()
    audio_title = input("Enter the title for the output audio file (without extension): ").strip()

    model_path = os.path.join(piper_dir, model_filename)
    config_path = os.path.join(piper_dir, config_filename)

    if not os.path.exists(model_path) or not os.path.exists(config_path):
        print("*" * 50)
        print("ERROR: Piper model/config files not found!")
        print(f"Missing: '{model_filename}' or '{config_filename}' in {piper_dir}")
        print("Download models here: https://github.com/rhasspy/piper/releases")
        print("*" * 50)
        return

    print("\nStep 1: Extracting text from PDF...")
    paper_text = extract_text_from_pdf(pdf_path)
    if not paper_text:
        print("Error: Failed to extract text.")
        return
    print(f"Extracted ~{len(paper_text)} characters.")

    print("\nStep 2: Generating podcast script using Local AI model...")
    script = generate_podcast_script(paper_text, localai_model)
    if not script:
        print("Error: Script generation failed.")
        return

    print("\n🔎 Preview of generated script:")
    print("-" * 40)
    print(script[:800] + "..." if len(script) > 800 else script)
    print("-" * 40)

    print("\nStep 3: Synthesizing speech with Piper...")
    audio_file = synthesize_speech_with_piper(script, piper_dir, model_filename, audio_title)
    if audio_file:
        print(f"\n✅ Podcast audio saved at: {audio_file}")
    else:
        print("Error: Speech synthesis failed.")

if __name__ == "__main__":
    main()
