from flask import Flask, render_template, request, jsonify
import ctranslate2
import sentencepiece as spm
from config import ct_model_path, sp_model_path, device


app = Flask(__name__)

# 加载模型
sp = spm.SentencePieceProcessor()
sp.load(sp_model_path)
translator = ctranslate2.Translator(ct_model_path, device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    source_text = data['source_text']
    src_lang = data['src_lang']
    tgt_lang = data['tgt_lang']
    # translation logic
    # manage source
    source_sentences = source_text.split('\n')
    source_sentences = [sent.strip() for sent in source_sentences]

    # 使用 SentencePiece
    source_sents_subworded = sp.encode_as_pieces(source_sentences)
    source_sents_subworded = [[src_lang] + sent + ["</s>"] for sent in source_sents_subworded]

    # translate
    target_prefix = [[tgt_lang]] * len(source_sentences)
    translations_subworded = translator.translate_batch(source_sents_subworded, batch_type="tokens", max_batch_size=2024, beam_size=4, target_prefix=target_prefix)
    translations_subworded = [translation.hypotheses[0] for translation in translations_subworded]

    # back to words
    translated_texts = sp.decode(translations_subworded)
    translated_text = '\n'.join(translated_texts)
    print(translated_text)

    return jsonify({'translation': translated_text})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)