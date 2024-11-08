from django.shortcuts import render,get_object_or_404
from .models import GameSession
from django.http import JsonResponse
import random
# 게임 첫 화면 출력(정답 함께 생성)
# 정답 : 1~100 사이의 정수
def index(request):
    answer = random.randint(1,100)
    game_session = GameSession.objects.create(answer = answer)
    context = {
        'answer' : answer,
        'game_session_id' : game_session.id,
    } 
    return render(request, 'games/index.html', context)

# user_guess와 answer이 같으면 정답과 정답 입력한 횟수 출력


def check(request,game_session_id):
    game_session = get_object_or_404(GameSession, id = game_session_id)
    if request.method == "POST":
        user_guess = int(request.POST.get('user_guess'))
        message = ''
        if user_guess < 1 or user_guess > 100:
            message = "1~100 사이의 숫자만 입력해주세요."
        elif user_guess > game_session.answer :
            message = "DOWN"
            game_session.user_guess = user_guess
            game_session.attempts += 1
            game_session.save()
        elif user_guess < game_session.answer :
            message = "UP"
            game_session.user_guess = user_guess
            game_session.attempts += 1
            game_session.save()
        else: 
            message = "정답입니다!"
            game_session.attempts += 1
            game_session.save()
        response_data = {
            'message' : message,
            'attempts' : game_session.attempts,
        }

        return JsonResponse(response_data)
    else: 
        return JsonResponse({'error' : 'Invalid Http Method!'})
