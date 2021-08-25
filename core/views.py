from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import Item, Inventory, User, Cart
from core.serializers import ItemSerializer, InventorySerializer, UserSerializer, CartSerializer

# Create your views here.

@api_view(['GET'])
def home(request):
    return HttpResponse("The Server is Up and Running!")


@api_view(['POST'])
def create_item(request):
    try:
        itemCategory = request.data.get('itemCategory')
        brand = request.data.get('brand')
        price = request.data.get('price')

        if not itemCategory or not brand or not price:
            res = {
                "Wrong Inputs": "itemCategory, brand, price are essential inputs."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        try:
            if Item.objects.get(itemCategory=itemCategory, brand=brand):
                res = {
                    "Object Already Exists": "Please check your inputs."
                }
                return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            pass

        item = Item.objects.create(
            itemCategory=itemCategory,
            brand=brand,
            price=price
        )

        item_serializer = ItemSerializer(item)

        return Response(item_serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_to_inventory(request):
    try:
        itemCategory = request.data.get('itemCategory')
        brand = request.data.get('brand')
        quantity = request.data.get('quantity')

        if not itemCategory or not brand or not quantity:
            res = {
                "Wrong Inputs": "itemCategory, brand, quantity are essential inputs."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = Item.objects.get(itemCategory=itemCategory, brand=brand)
        except:
            res = {
                    "Item Does Not Exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            inventory = Inventory.objects.get(item=item)
        except:
            res = {
                    "Wrong Input": "Inventory item already exists"
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        inventory = Inventory.objects.create(
            item=item,
            quantity=quantity
        )

        inventory_serializer = InventorySerializer(inventory)

        return Response(inventory_serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_user(request):
    try:
        userName = request.data.get('userName')
        walletAmount = request.data.get('walletAmount')

        if not userName or not walletAmount:
            res = {
                "Wrong Inputs": "userName, wallerAmount are essential inputs."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        try:
            if User.objects.get(userName=userName):
                res = {
                    "Wrong Input": "User already exists"
                }
                return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            pass

        user = User.objects.create(
            userName=userName,
            walletAmount=walletAmount
        )

        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_to_user_cart(request):
    try:
        userName = request.data.get('userName')
        itemCategory = request.data.get('itemCategory')
        brand = request.data.get('brand')
        quantity = request.data.get('quantity')

        if not userName or not itemCategory or not brand or not quantity:
            res = {
                "Wrong Inputs": "userName, itemCategory, brand, quantity are essential inputs."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = Item.objects.get(itemCategory=itemCategory, brand=brand)
        except:
            res = {
                    "Item Does not Exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            inventory = Inventory.objects.get(item=item)
        except:
            res = {
                    "Item Does Not Exist in inventory": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        try:
            user = User.objects.get(userName=userName)
        except:
            res = {
                    "User Does Not Exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            if Cart.objects.get(user=user, item=item):
                res = {
                    "Wrong Input": "Cart item already exists"
                }
                return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            pass

        if int(quantity) > inventory.quantity:
            res = {
                'Wrong Input': 'Quantity to be added in the cart cannot exceed the qunatity in the inventory'
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        cart = Cart.objects.create(
            user=user,
            item=item,
            quantity=quantity
        )

        cart_serializer = CartSerializer(cart)

        return Response(cart_serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_user_cart(request):
    try:
        userName = request.data.get('userName')
        itemCategory = request.data.get('itemCategory')
        brand = request.data.get('brand')
        quantity = request.data.get('quantity')

        if not userName or not itemCategory or not brand or not quantity:
            res = {
                "Wrong Inputs": "userName, itemCategory, brand, quantity are essential inputs."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = Item.objects.get(itemCategory=itemCategory, brand=brand)
        except:
            res = {
                    "Item Does Not Exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            inventory = Inventory.objects.get(item=item)
        except:
            res = {
                    "Item Does Not Exist in inventory": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        try:
            user = User.objects.get(userName=userName)
        except:
            res = {
                    "User Does Not Exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if int(quantity) > inventory.quantity:
            res = {
                'Wrong Input': 'Quantity to be added in the cart cannot exceed the qunatity in the inventory'
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            cart = Cart.objects.get(
                user=user,
                item=item
            )
        except:
            res = {
                    "Wrong Input": "Cart does not exist"
                }
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        
        cart.quantity = quantity
        cart.save()

        cart_serializer = CartSerializer(cart)

        return Response(cart_serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def remove_user_cart(request):
    try:
        userName = request.data.get('userName')
        itemCategory = request.data.get('itemCategory')
        brand = request.data.get('brand')

        if not userName or not itemCategory or not brand:
            res = {
                "Wrong Inputs": "userName, itemCategory, brand are essential inputs."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = Item.objects.get(itemCategory=itemCategory, brand=brand)
        except:
            res = {
                    "Item has not been created": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            inventory = Inventory.objects.get(item=item)
        except:
            res = {
                    "Item Does Not Exist in inventory": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        try:
            user = User.objects.get(userName=userName)
        except:
            res = {
                    "User Does Not Exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            cart = Cart.objects.get(
                user=user,
                item=item
            )
        except:
            res = {
                    "Wrong Input": "Cart does not exist"
                }
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        
        cart_serializer = CartSerializer(cart)
        cart.delete()

        res = {
            "Deleted Cart": cart_serializer.data
        }

        return Response(res, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getCart(request):
    try:
        userName = request.data.get('userName')

        try:
            user = User.objects.get(userName=userName)
        except:
            res = {
                    "User Does Not Exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        carts = Cart.objects.filter(user=user)

        items = Item.objects.none()

        res = []

        for cart in carts:
            res.append({
                'item': ItemSerializer(cart.item).data,
                'quantity': cart.quantity
            })

        res = {
            'cart_info': res
        }
            
        return Response(res, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def cartCheckOut(request):
    try:
        userName = request.data.get('userName')

        try:
            user = User.objects.get(userName=userName)
        except:
            res = {
                    "User Does Not Exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        carts = Cart.objects.filter(user=user)

        cart_value = 0

        for cart in carts:
            if cart.quantity > Inventory.objects.get(item=cart.item).quantity:
                res = {
                    "Items Exhausted from Inventory": cart.item.itemCategory + ' - ' + cart.item.brand
                }
                return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        for cart in carts:
            cart_value += cart.item.price * cart.quantity

        if cart_value > user.walletAmount:
            res ={
                "Wallet Amount Exceeded": "Cannot checkout the cart."
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        for cart in carts:
            inventory = Inventory.objects.get(item=cart.item)
            inventory.quantity -= cart.quantity
            inventory.save()

        res = {
            'cart_info': 'Cart successfully checked out.'
        }

        return Response(res, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

