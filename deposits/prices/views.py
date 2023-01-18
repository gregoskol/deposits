import requests
from django.db.models import ExpressionWrapper, FloatField, Sum
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Active, ActiveType

total = 0


def prices(type, addr_boards, param):
    active_type = get_object_or_404(ActiveType, name=type)
    avg_prices = Active.objects.values("name").annotate(
        result=ExpressionWrapper(
            Sum("sum_price") / Sum("amount"), output_field=FloatField()
        )
    )
    actives = (
        active_type.actives.all()
        .values(
            "name",
            "description",
        )
        .annotate(
            sum_amount=Sum("amount"),
        )
    )
    url = (
        "https://iss.moex.com/iss/"
        + addr_boards
        + "securities/.json?iss.only=marketdata&marketdata.columns=SECID,"
        + param
    )
    answer = requests.get(url).json().get("marketdata").get("data")
    for active in actives:
        for list in answer:
            if list[0] == active["name"] and (
                active_type.name != "Валюта" or list[2] == "CETS"
            ):
                active["price"] = list[1]
        for avg_price in avg_prices:
            if active["name"] == avg_price["name"]:
                active["result_rouble"] = active["sum_amount"] * (
                    active["price"] - avg_price["result"]
                )
                active["result_percent"] = (100 * active["result_rouble"]) / (
                    active["sum_amount"] * avg_price["result"]
                )
                active["actual_price"] = active["price"] * active["sum_amount"]
                global total
                total += active["actual_price"]
    return actives


def sum_prices():
    actives = Active.objects.all()
    for active in actives:
        if active.sum_price is None:
            active.sum_price = active.price_of_buy * active.amount
            active.save()


def index(request):
    sum_prices()
    global total
    total = 0
    active_list = [
        prices(
            "Валюта",
            "engines/currency/markets/selt/",
            "LAST,BOARDID",
        ),
        prices(
            "Акции",
            "engines/stock/markets/shares/boards/TQBR/",
            "LAST",
        ),
        prices(
            "ETF",
            "engines/stock/markets/shares/boards/TQTF/",
            "LCURRENTPRICE",
        ),
        #        prices(
        #            "ETF заблокированный",
        #            "engines/stock/markets/shares/boards/TQTF/",
        #            "LCURRENTPRICE",
        #        ),
    ]
    template = "index.html"
    context = {
        "active_list": active_list,
        "total": total,
    }
    res = 0
    for actives in active_list:
        for active in actives:
            res += int(active["result_rouble"])
    print(f"{res} рублей по активам")
    return render(request, template, context)
