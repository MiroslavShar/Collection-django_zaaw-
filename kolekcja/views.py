from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from kolekcja.models import Type, Category, Metal, Coin, CollectionItem
from kolekcja.forms import CategoryForm, CoinModelForm, MetalModelForm, AddCoinToCollectionForm, CoinSearchForm
from django.contrib.auth.models import User, Group, Permission



def index_page(request):
    return render(request, 'index.html')


class CosTamView(View):
    def get(self, request):
        return redirect('home')

class Add_type(View):
    def get(self, request):
        return render(request, 'add_type.html')
    def post(self, request):
        name = request.POST.get('text')
        new_type = Type(name=name) #Type.objects.create(name=name)
        new_type.save()
        return HttpResponse('Dodane')

class Add_coin(LoginRequiredMixin,View):
    def get(self, request):
        form = CoinModelForm
        return render(request, 'add_coin.html', {'form': form})
    def post(self, request):
        form = CoinModelForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('coin')
        return render(request, 'add_coin.html', {'form': form})
    #     name = request.POST.get('name')
    #     nominal = request.POST.get('nominal')
    #     type = request.POST.get('type')
    #     category = request.POST.get('category')
    #     if name:
    #         # Coin.objects.create(name=name, nominal=nominal, type=type, category=category)
    #         new_coin = Coin(name=name)
    #         new_coin.save()
    #         return HttpResponse('Dodane')
    #     return HttpResponse('Pusta nazwa')

class Add_metal(View):
    def get(self, request):
        form = MetalModelForm
        return render(request, 'add_metal.html', {'form': form})
    def post(self, request):
        form = MetalModelForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('metal')
        return render(request, 'add_metal.html', {'form': form})

class Show_metal(View):
    def get(self, request):
        db_metal = Metal.objects.all()
        return render(request, 'show_type_metal.html',
                      {'metals': db_metal})


class UpdateMetalView(View):

    def get(self, request, id):
        metal = Metal.objects.get(pk=id)
        form = MetalModelForm(instance=metal)
        return render(request, 'add_metal.html', {'form': form})

    def post(self, request, id):
        metal = Metal.objects.get(pk=id)
        form = MetalModelForm(request.POST, instance=metal)
        if form.is_valid():
            form.save()
            return redirect('show_metal')
        return render(request, 'add_metal.html', {'form': form})

class Show_types(View):
    def get(self, request):
        db_types = Type.objects.all()
        return render(request, 'show_types.html',
                      {'types': db_types})

class Add_category(PermissionRequiredMixin, View):

    permission_required = ['kolekcja_add_category']
    def get(self, request):
        categories = Category.objects.all()
        cat_form = CategoryForm()
        return render(request, 'add_category.html', {'categories': categories, 'form': cat_form})
    def post(self, request):
        cat_id = request.POST.get('cat')
        if cat_id == '':
            cat = None
        else:
            cat = Category.objects.get(pk=cat_id)
        name = request.POST.get('name')
        if name != '':
            Category.objects.create(name=name, parent=cat)
            return redirect('add_category')
        return render(request, 'add_category.html', {'error': 'Nazwa nie może być pusta'})

class AddCategoryForm(PermissionRequiredMixin, View):

    permission_required = ['kolekcja_add_category']
    def get(self, request):
        cat_form = CategoryForm()
        return render(request, 'add_category_form.html', {'form': cat_form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cat = form.cleaned_data['category']
            Category.objects.create(name=name, parent=cat)
            return redirect('add_category_form')
        return render(request, 'add_category_form.html', {'form': form})

class Show_coin(View):
    def get(self, request):
        db_coins = Coin.objects.all()
        form = CoinSearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            db_coins = db_coins.filter(name__icontains=name)
            cat = form.cleaned_data.get('category')
            if cat:
                db_coins = db_coins.filter(category_id=cat)
            value = form.cleaned_data.get('value')
            if value:
                db_coins = db_coins.filter(value=value)
            type = form.cleaned_data.get('type')
            for t in type:
                db_coins = db_coins.filter(type=t)
        return render(request, 'show_coins.html', {'db_coins':db_coins, 'form': form})

class UpdateCoinView(UserPassesTestMixin, View):

    def test_func(self):
        user = self.request.user
        return user.username.startswith('M')

    def get(self, request, id):
        coin = Coin.objects.get(pk=id)
        form = CoinModelForm(instance=coin)
        return render(request, 'add_coin.html', {'form': form})

    def post(self, request, id):
        coin = Coin.objects.get(pk=id)
        form = CoinModelForm(request.POST, instance=coin)
        if form.is_valid():
            form.save()
            return redirect('show_coins')
        return render(request, 'add_coin.html', {'form': form})


# class Add_user(View):
#     def get(self, request):
#         form = User
#         return render(request, 'add_person.html', {'form': form})
#
#     def post(self, request):
#         form = User(request.POST)
#         if form.is_valid():
#             # username = form.cleaned_data['username']
#             # password = form.cleaned_data['password']
#             # last_name = form.cleaned_data['last_name']
#             obj = form.save()
#             return redirect('add_user')
#             # User.objects.create(username=username, last_name=last_name, password=password)
#             # return redirect('add_user')
#         return render(request, 'add_person.html', {'form': form})


class MyCollectionview(LoginRequiredMixin, View):

    def get(self, request):
        collection_items = CollectionItem.objects.filter(user=request.user)
        return render(request, 'my_collection.html', {'collection': collection_items})

class AddToCollectionCoint(LoginRequiredMixin, View):

    def get(self, request, coin_id):
        coin = Coin.objects.get(pk=coin_id)
        form = AddCoinToCollectionForm(initial={'coin': coin})
        return render(request, 'form.html', {'form': form})

    def post(self, request, coin_id):
        form =AddCoinToCollectionForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.info(request, f'dodałeś {item.coin} do kolekcji')
        else:
            messages.error(request, f'Niew udalo sie dodać {form.error}')
        return redirect('show_coins')
