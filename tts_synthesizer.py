import os
import subprocess
import traceback

def save_script_to_file(script, output_dir, file_name="script.txt"):
    if not script:
        print("Error: No script to save.")
        return ""
    try:
        script_path = os.path.join(output_dir, file_name)
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(script)
        print(f"✅ Script saved to: {script_path}")
        return script_path
    except Exception as e:
        print(f"Error saving script: {e}")
        traceback.print_exc()
        return ""

def synthesize_speech_with_piper(script, piper_dir, model_filename, audio_title):
    if not script:
        print("Error: No script provided for synthesis.")
        return ""

    script_path = save_script_to_file(script, piper_dir)
    if not script_path:
        return ""

    try:
        # The audio file name is taken from the user-provided title with .wav extension.
        output_audio = f"{audio_title}.wav"
        piper_cmd = [
            "powershell",
            "-Command",
            f"cd '{piper_dir}' ; cat .\\{os.path.basename(script_path)} | .\\piper.exe -m .\\{model_filename} -f {output_audio} "
        ]
        print(f"Running PowerShell command: {' '.join(piper_cmd)}")
        result = subprocess.run(piper_cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print("❌ Piper CLI failed:")
            print(result.stderr)
            return ""
        else:
            print("✅ Piper TTS synthesis successful.")
            return os.path.abspath(os.path.join(piper_dir, output_audio))
    except Exception as e:
        print(f"An error occurred during Piper synthesis: {e}")
        traceback.print_exc()
        return ""
