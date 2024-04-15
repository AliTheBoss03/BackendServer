from django.http import JsonResponse
from .models import Bruger, CartItem
import json

def gem_bruger(request):
    if request.method == 'POST':
        # Hent data fra anmodningen
        data = json.loads(request.body)

        # Gem Bruger-oplysninger i databasen
        bruger = Bruger.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            addressLine1=data.get('addressLine1'),
            addressLine2=data.get('addressLine2'),
            city=data.get('city'),
            country=data.get('country'),
            companyName=data.get('companyName'),
            vatNumber=data.get('vatNumber'),
            orderComment=data.get('orderComment'),
            receiveMarketing=data.get('receiveMarketing'),
            termsAccepted=data.get('termsAccepted'),
            zipCode=data.get('zipCode'),
            totalPrice=data.get('totalPrice')
        )

        # Gem CartItem-oplysninger i databasen
        cart_items = data.get('cart')
        for item in cart_items:
            cart_item = CartItem.objects.create(
                user=bruger,
                currency=item.get('currency'),
                product_id=item.get('id'),
                image_url=item.get('imageUrl'),
                name=item.get('name'),
                price=item.get('price'),
                quantity=item.get('quantity'),
                rebate_percent=item.get('rebatePercent'),
                rebate_quantity=item.get('rebateQuantity'),
                upsell_product_id=item.get('upsellProductId')
            )

        # Returner en bekræftelsesbesked som JSON
        return JsonResponse({'message': 'Data gemt i databasen!'})
    else:
        # Hvis anmodningen ikke er en POST-anmodning, returnerer en fejlbesked
        return JsonResponse({'error': 'Kun POST-anmodninger er tilladt!'}, status=400)
