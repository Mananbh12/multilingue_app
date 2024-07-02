from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.shortcuts import render
from .models import Article
from django.shortcuts import render
from transformers import pipeline
from django.shortcuts import render
from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration


def home(request):
  trans = _('Hello ! I built this app to learn how to implement internationalization with Django ')
  return render(request, 'home.html', {'trans' : trans})

def translate(language):
  cur_language = get_language()
  try:
    activate(language)
    text = _('hello')
  finally:
    activate(cur_language)
  return text

def article_list(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'article_list.html', {'articles': articles})

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        chatbot_response = generate_chatbot_response(user_input)
        return render(request, 'chatbot.html', {'user_input': user_input, 'chatbot_response': chatbot_response})
    else:
        return render(request, 'chatbot.html')

def generate_chatbot_response(user_input):
    # Utilisation d'un modèle GPT-3 pré-entraîné
    chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
    response = chatbot(user_input, max_length=100, num_return_sequences=1, return_full_text=False)
    return response[0]['generated_text']

def search_view(request):
    query = request.GET.get('query', '')
    if query:
        rag_tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")
        rag_retriever = RagRetriever.from_pretrained("facebook/rag-token-base", index_name="exact")
        rag_model = RagTokenForGeneration.from_pretrained("facebook/rag-token-base", retriever=rag_retriever, tokenizer=rag_tokenizer)

        inputs = rag_tokenizer(query, return_tensors="pt")
        search_results = rag_model.generate(**inputs)
        results = rag_tokenizer.batch_decode(search_results, skip_special_tokens=True)
    else:
        results = []

    return render(request, 'search.html', {'query': query, 'results': results})