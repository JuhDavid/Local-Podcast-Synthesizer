import re
from localai import localai_process_text, trim_localai_response

def generate_podcast_script(paper_text, localai_model, max_words=800):
    base_task = """Create a helpful podcast that explains the following text in layman's terms using lots of examples 
    to make it as illustrative as possible. Do not use any formatting characters, ONLY text. Start your response 
    with: In this segment, we will be discussing the following points: """
    # --- Paragraph-based Segmentation ---
    paragraphs = re.split(r'\n\s*\n', paper_text.strip())
    segments = []
    current_segment = []
    current_word_count = 0

    for para in paragraphs:
        para_word_count = len(para.split())
        if current_word_count + para_word_count > max_words and current_segment:
            segments.append('\n\n'.join(current_segment))
            current_segment = [para]
            current_word_count = para_word_count
        else:
            current_segment.append(para)
            current_word_count += para_word_count

    if current_segment:
        segments.append('\n\n'.join(current_segment))

    full_response = ""
    total_segments = len(segments)
    for idx, segment in enumerate(segments):
        print(f"\n🔹 Processing segment {idx + 1}/{total_segments} ({len(segment.split())} words)...")
        task = base_task  # Customize task per segment if desired
        full_response += localai_process_text(segment, task, model_name=localai_model) + "\n"

    return trim_localai_response(full_response)
