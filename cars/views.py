from django.shortcuts import render, redirect
from .models import Car
from django.views.generic import ListView
from django.views.generic import View
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




# Create your views here.

class CarView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'Objs'



class CreateCarObj(View):
    @csrf_exempt
    def  post(self, request):
        if request.method == 'POST':
            description1 = request.POST['description']
            price1 = request.POST['price']
            quantity1 = request.POST['quantity']

            obj = Car.objects.create(
                description = description1,
                price = price1,
                quantity = quantity1
            )

            Obj = {'id':obj.id,'description':obj.description,'price':obj.price,'quantity':obj.quantity}

            data = {
                'Obj': Obj
            }
            return JsonResponse(data)



class UpdateCarObj(View):

    method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateCarObj, self).dispatch(request, *args, **kwargs)

    def  put(self, request):
        if request.method == 'PUT':
            q = QueryDict(request.body)
            id1 = q.get('id')
            description1 = q.get('description')
            price1 = q.get('price')
            quantity1 = q.get('quantity')

            obj = Car.objects.get(pk=id1)
            obj.description = description1
            obj.price = price1
            obj.quantity = quantity1
            obj.save()

            Obj = {'id':obj.id,'description':obj.description,'price':obj.price,'quantity':obj.quantity}

            data = {
                'Obj': Obj
            }
            return JsonResponse(data)




class DeleteCarObj(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteCarObj, self).dispatch(request, *args, **kwargs)


    def  delete(self, request):
        if request.method == 'DELETE':
            q = QueryDict(request.body)
            id1 = q.get('id')
            r = Car.objects.get(pk=id1)
            r.delete()

            data = {
                'deleted': True
            }
            return JsonResponse(data)
