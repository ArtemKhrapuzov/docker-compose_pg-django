import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question


@csrf_exempt
def get_question(request):
    if request.method == 'POST':
        questions_num = int(request.POST.get('questions_num', 1))
        for i in range(questions_num):
            while True:
                response = requests.get('https://jservice.io/api/random')
                data = response.json()[0]
                question_id = data['id']
                question_text = data['question']
                answer_text = data['answer']
                created_at = data['created_at']
                try:
                    Question.objects.get(id=question_id)
                except Question.DoesNotExist:
                    Question.objects.create(id=question_id, question_text=question_text, answer_text=answer_text,
                                            created_at=created_at)
                    break
        try:
            question = Question.objects.latest('created_at')
            data = {
                'id': question.id,
                'question_text': question.question_text,
                'answer_text': question.answer_text,
                'created_at': question.created_at,
            }
        except Question.DoesNotExist:
            data = {}
        return JsonResponse(data)
    else:
        return JsonResponse({})
