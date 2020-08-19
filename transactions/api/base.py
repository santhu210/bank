import json
from django.views.generic.base import View
from django.http import HttpResponse
from django.utils.decorators import classonlymethod

class ApiBase(View):
    def __init__(self, **kwargs):
        self.status = None
        self.message = None
        self.success = None

    @classonlymethod
    def as_api_view(cls, **initkwargs):
        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            self.request = request
            self.args = args
            self.kwargs = kwargs

            return self.dispatch(request, *args, **kwargs)
        return view

    def get(self, request, *args, **kwargs):
        return self.render_response()

    def post(self, request, *args, **kwargs):
        return self.render_response()

    def set_bad_req(self, msg):
        self.success = False
        self.status = 400
        self.message = msg

    def resp_meta(self):
        self.status = self.status if self.status else 200
        self.message = self.message if self.message else 'Request successful'
        resp = {
            'success': self.success,
            'status': self.status,
            'message': self.message
        }
        return resp

    def render_response(self, **resp_args):
        self.success = True
        resp = {}
        try:
            ctxt = { 'data': None }
            data = self.get_or_create()
            resp_meta = self.resp_meta()
            ctxt['data'] = data
            resp.update(resp_meta)
            resp.update(ctxt)
            return HttpResponse(json.dumps(resp), status=self.status)
        except Exception as e:
            print(e)
            resp = {
                'success': False,
                'status': 500,
                'message': 'Something went wrong'
            }            
            return HttpResponse(json.dumps(resp), status=500)

