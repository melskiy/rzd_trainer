from transformers import AutoTokenizer, AutoModel


tokenizer_sbert = AutoTokenizer.from_pretrained('ai-forever/sbert_large_nlu_ru')

model_sbert = AutoModel.from_pretrained('ai-forever/sbert_large_nlu_ru')