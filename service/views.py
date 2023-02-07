from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

from .validators import UserInputValidator

import urllib.parse


DEFAULT_HEADERS = {'Content-Type': 'text/html'}


class ServiceView(TemplateView):
    template_name = "service/service.html"

    def post(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        user_id, form_args = self.request.user.id, urllib.parse.parse_qs(request.body.decode("utf-8"))
        is_extract_args_valid, is_show_args_args_valid = self._put_through_validator(form_args)
        if is_extract_args_valid:
            table_name, scrape = "Table of extracted data", ScrapyTrigger()
            result = scrape.parse_data(form_args["url"], user_id)
            rendered_result = template.render(result=result, table_name=table_name)
            return HttpResponse(rendered_result, status=200, headers=DEFAULT_HEADERS)
        elif is_show_args_args_valid:
            table_name, dispatcher = "Table of already existing data", DatabaseDispatcher()
            result = dispatcher.get_exist_data(form_args, user_id)
            rendered_result = template.render(result=result, table_name=table_name)
            return HttpResponse(rendered_result, status=200, headers=DEFAULT_HEADERS)
        else:
            return HttpResponse({"result": "BAD REQUEST!"}, 200)

    @staticmethod
    def _put_through_validator(form_args):
        validator = UserInputValidator()
        is_extract_args_valid, is_show_args_args_valid = validator.valid_extract_args(form_args), False
        if not is_extract_args_valid:
            is_show_args_args_valid = validator.valid_show_args(form_args)
        return is_extract_args_valid, is_show_args_args_valid
