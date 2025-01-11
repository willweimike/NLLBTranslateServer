# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify
import ctranslate2
import sentencepiece as spm



app = Flask(__name__)


@app.route('/')
def index():
    model_1 = "./nllb/nllb-200-600M-int8"
    model_2 = "./nllb/nllb-200-1.2B-int8"
    model_3 = "./nllb/nllb-200-3.3B-int8"
    sp_model = "./nllb/flores200_sacrebleu_tokenizer_spm.model"
    exist_1 = os.path.isdir(model_1)
    exist_2 = os.path.isdir(model_2)
    exist_3 = os.path.isdir(model_3)
    exist_sp = os.path.isfile(sp_model)

    if exist_1 is True and exist_sp is True:
        return jsonify({"Status": "OK"})
    elif exist_2 is True and exist_sp is True:
        return jsonify({"Status": "OK"})
    if exist_3 is True and exist_sp is True:
        return jsonify({"Status": "OK"})
    else:
        return jsonify(
            {
                "Status": "Service is not running correctly, please check the NLLB file"
            }
        )


@app.route('/help', methods=['GET'])
def help():
    return jsonify(
        {"Language_code": [
                {"English": "eng_Latn"},
                {"Chinese Simplified": "zho_Hans"},
                {"Chinese Traditional": "zho_Hant"},
                {"Estonian": "est_Latn"},
                {"Finnish": "fin_Latn"},
                {"French": "fra_Latn"},
                {"Hindi": "hin_Deva"},
                {"Romanian": "ron_Latn"},
                {"Latvian": "lvs_Latn"},
                {"Russian": "rus_Cyrl"},
                {"Spanish": "spa_Latn"},
                {"Turkish": "tur_Latn"},
                {"Kinyarwanda": "kin_Latn"}
            ]
        }
    )


@app.route('/translate', methods=['POST'])
def translate_text():
    device = "cpu"
    translator = None
    sp = spm.SentencePieceProcessor()

    model_1 = "./nllb/nllb-200-600M-int8"
    model_2 = "./nllb/nllb-200-1.2B-int8"
    model_3 = "./nllb/nllb-200-3.3B-int8"
    sp_model = "./nllb/flores200_sacrebleu_tokenizer_spm.model"
    exist_1 = os.path.isdir(model_1)
    exist_2 = os.path.isdir(model_2)
    exist_3 = os.path.isdir(model_3)
    exist_sp = os.path.isfile(sp_model)

    if exist_1 is True and exist_sp is True:
        sp.load(sp_model)
        translator = ctranslate2.Translator(model_1, device)

    elif exist_2 is True and exist_sp is True:
        sp.load(sp_model)
        translator = ctranslate2.Translator(model_2, device)

    elif exist_3 is True and exist_sp is True:
        sp.load(sp_model)
        translator = ctranslate2.Translator(model_3, device)
    else:
        return jsonify(
            {
                "Status": "Service is not running correctly, please check the NLLB file"
            }
        )

    data = request.get_json()
    source_text = data['source_text']
    src_lang = data['src_lang']
    tgt_lang = data['tgt_lang']
    # translation logic
    # manage source
    source_sentences = source_text.split('\n')
    source_sentences = [sent.strip() for sent in source_sentences]

    # use SentencePiece
    target_prefix = [[tgt_lang]] * len(source_sentences)
    # Subword the source sentences
    source_sents_subworded = sp.encode_as_pieces(source_sentences)
    source_sents_subworded = [[src_lang] + sent + ["</s>"] for sent in source_sents_subworded]
    # Translate the source sentences
    translations_subworded = translator.translate_batch(source_sents_subworded, batch_type="tokens",
                                                        max_batch_size=2024, beam_size=4,
                                                        target_prefix=target_prefix)
    translations_subworded = [translation.hypotheses[0] for translation in translations_subworded]
    for translation in translations_subworded:
        if tgt_lang in translation:
            translation.remove(tgt_lang)
    # De-subword the target sentences
    translations = sp.decode(translations_subworded)
    translation = "".join(translations)

    return jsonify({'translation': translation})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
