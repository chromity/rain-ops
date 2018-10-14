from django.views import generic
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import logging, json, requests

# enable logging in this application
logger = logging.getLogger(__name__)

PAGE_ACCESS_TOKEN = "EAAdWAvT9jZCABAKiXOOZARBLem0LOkBEp0kjgotib4Ox5TFsE9HvLTzZCwVpE1ZBCeIKpZAoDrdDQvDF2BVQZAMSJ4N7GdMJ3CCpQGf1uEhChQ4VaSPJdmdHtPFf5fvyud9mjvYZAQbLnDYZA76p2aoMQKbdQt3dsqsq9Sdq5HwpdHXuRtAOeC2J"
APP_SECRET = "b9effab62e67e6ce0e714a69ba1fc84f"


class MainView(generic.View):


    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'nclt083198':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    logger.info(message)

                    reply_message = "Hello, I'm Rain Ops. To check the current weather analysis, type 'weather'"
                    post_facebook_message(message['sender']['id'], reply_message)
        return HttpResponse()

# helper methods

def post_facebook_message(fbid, received_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":received_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    logger.info(status.json())