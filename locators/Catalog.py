class Catalog:
    class Products:
        products = {'css': '.product-layout'}
        product_image = {'css': products['css'] + ' .image'}
        product_name = {'css': products['css'] + ' .caption h4'}

    class Buttons:
        button_group = {'css': '.button-group'}
        add_to_cart_button = {'css': button_group['css'] + ' [class="fa fa-shopping-cart"]'}
        add_to_wish_list_button = {'css': button_group['css'] + ' [class="fa fa-heart"]'}
        compare_product_button = {'css': button_group['css'] + '[class="fa fa-exchange"]'} 

    class Navigation:
        list_view = {'css': '[data-original-title="List"]'}
        grid_view = {'css': '[data-original-title="Grid"]'}

    class Sort:
        options = {'css': '#input-sort'}
        by_name_A_Z = "Name (A - Z)"
        by_name_Z_A = "Name (Z - A)"
        by_price_low_high = "Price (Low > High)"
        by_price_high_low = "Price (High > Low)"
        by_raiting_highest = "Rating (Highest)"
        by_raiting_lowest = "Rating (Lowest)"
        by_model_A_Z = "Model (A - Z)"
        by_model_Z_A = "Model (Z - A)"
        
    class Limits:
        options = {'css': '#input-limit'}
        limit_15 = "15"
        limit_25 = "25"
        limit_50 = "50"
        limit_75 = "70"
        limit100 = "100"