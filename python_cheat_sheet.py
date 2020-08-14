import requests
from bs4 import BeautifulSoup
import datetime

def course():
    url = 'https://www.nbkr.kg/XML/daily.xml'
    page = requests.get(url).text
    valuta = BeautifulSoup(page, 'html.parser')

    id_dollar = 'USD'
    id_evro = 'EUR'
    id_rub = 'RUB'
    id_tenge = 'KZT'

    for line in valuta.currencyrates('currency'):
        for line2 in line.value:
            tyni = line2
        tag =  line
        id_v = tag['isocode']
        if id_v == id_dollar:
            som_dollar = tyni
        if id_v == id_evro:
            som_euro = tyni
        if id_v == id_rub:
            som_rub = tyni
        if id_v == id_tenge:
            som_tenge = tyni
    today = datetime.date.today()
    return som_dollar, som_euro, som_rub, som_tenge, today        
          
dollar, euro, rub, tenge, todaydata = course()
# if __name__ == "__main__":
#         print("\n",course())

# -------------------------------------------------------------------------------------

# -------Ставим ЛАЙК---------------------------

class Like(APIView):
    """Ставим лайк"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pk = request.data.get("pk")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return Response(status=201)

# -------------------------------------------------------------------------------------

# -------Работаем с типом модели группируем в сериалайзер---------------------------

    full_order = list(order) + list(content)
    results = list()
       for entry in full_order:
           item_type = entry.__class__.__name__.lower()
           if isinstance(entry, Order):
               serializer = OrderSerializer(entry)
           if isinstance(entry, Content):
               serializer = ContentSerializer(entry)
           results.append({'item_type': item_type, 'data': serializer.data})
         return Response(results)

# -------------------------------------------------------------------------------------