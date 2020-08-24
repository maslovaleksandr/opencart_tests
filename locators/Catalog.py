class Catalog:
    class Products:
        products = {'css': '.product-layout'}
        product_image = {'css': products['css'] + ' .image'}
        product_name = {'css': products['css'] + ' .caption h4'}

    class Buttons:
        button_group = {'css': '.button-group'}
        add_to_cart_button = {'css': button_group + ' [class="fa fa-shopping-cart"]'}
        add_to_wish_list_button = {'css': button_group + ' [class="fa fa-heart"]'}
        compare_product_button = {'css': button_group + '[class="fa fa-exchange"]'} 

    class Navigation:
        list_view = {'css': '[data-original-title="List"]'}
        grid_view = {'css': '[data-original-title="Grid"]'}
        sort_options = {'css': '#input-sort'}
        limit_options = {'css': '#input-limit'}