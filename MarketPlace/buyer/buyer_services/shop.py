from typing import Dict

from Exceptions import AppError, ErrorType
from buyer.models import Order
from seller.models import CatalogProduct, Product


class Shop:

    @staticmethod
    def selects_products_by_category(catalog_id: Dict[str, int]) -> list:
        """
        Selection of products included in a specific catalog.
        :param catalog_id: dict containing key - catalog_id
        :return: products (id, price, title_product) included in the catalog
        :raises AppError: if there is no catalog with this id
        """
        products = list(CatalogProduct.objects.filter(catalog_id=catalog_id['catalog_id']).values())
        if products:
            products_by_category = []
            for obj in products:
                products_by_category.extend(
                    list(Product.objects.filter(id=obj['product_id'], active_status=True).values('id', 'title_product', 'price')
                         )
                )
            return products_by_category
        else:
            raise AppError(
                {
                    'error_type': ErrorType.CATALOG_ERROR,
                    'description': 'there is no catalog with this id'
                }
            )

    @staticmethod
    def detail_product(product_id: Dict[str, int]) -> list:
        """
        Detailed information about the product.
        :param product_id: dict containing key - product_id
        :return: detailed information about the product (id, description, price, quantity,
                                                         store_name_id, title_product, active_status)
        :raises AppError: if there is no product with this id
        """
        product = list(Product.objects.filter(id=product_id['product_id']).values())
        if product:
            return product
        else:
            raise AppError(
                {
                    'error_type': ErrorType.PRODUCT_ERROR,
                    'description': 'there is no product with this id'
                }
            )

    @staticmethod
    def add_cart(profile_id: int, data: Dict[str, int]) -> None:
        """
        Authorized user adds the item to the shopping cart for further buying.
        :param profile_id: ProfileBuyer's id
        :param data: dict containing keys - product_id, quantity
        :return: None
        :raises AppError: if the requested quantity of product is not available
        """
        data['buyer_id'] = profile_id
        quantity = data['quantity']
        available_quantity = list(Product.objects.filter(id=data['product_id']).values('quantity'))[0]['quantity']
        if 0 < quantity <= available_quantity:
            Order.objects.create(**data)
        else:
            raise AppError(
                {
                    'error_type': ErrorType.AVAILABLE_PRODUCT_ERROR,
                    'description': f'You cannot add {quantity} products. Available for adding {available_quantity}'
                }
            )

    @staticmethod
    def change_cart(profile_id: int, data: Dict[str, int]) -> None:
        """
        Authorized user changes the quantity of the product in the cart.
        :param profile_id: ProfileBuyer's id
        :param data: dict containing keys - product_id, quantity
        :return: None
        :raises AppError: if the requested quantity of product is not available
        """
        quantity = data['quantity']
        available_quantity = list(Product.objects.filter(id=data['product_id']).values('quantity'))[0]['quantity']
        if 0 < quantity <= available_quantity:
            Order.objects.filter(buyer_id=profile_id, product_id=data['product_id']).update(quantity=quantity)
        else:
            raise AppError(
                {
                    'error_type': ErrorType.AVAILABLE_PRODUCT_ERROR,
                    'description': f'You cannot add {quantity} products. Available for adding {available_quantity}'
                }
            )

    @staticmethod
    def remove_cart(profile_id: int, data: Dict[str, int]) -> None:
        """
        Authorized user removes an item from the shopping cart.
        :param profile_id: ProfileBuyer's id
        :param data: dict containing key - product_id
        :return: None
        :raises AppError: if there is no such product in the cart
        """
        order = Order.objects.filter(buyer_id=profile_id, product_id=data["product_id"])
        if order:
            order.delete()
        else:
            raise AppError(
                {
                    'error_type': ErrorType.AVAILABLE_PRODUCT_ERROR,
                    'description': 'there is no such product in the cart'
                }
            )
