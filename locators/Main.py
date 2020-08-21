class Main:
    class featured:
        content = {'css': '#content .row',}
        elements = {'css': content['css'] + ' .product-layout a',}
        names = {'css': elements['css'] + ' h4',}

    class main_menu:
        desktop = {'css': 'li.dropdown:nth-child(1) > a:nth-child(1)'}
        laptop_and_notebooks = {'css': 'ul.nav > li:nth-child(2) > a:nth-child(1)'}
        components = {'css': 'li.dropdown:nth-child(3) > a:nth-child(1)'}
        mp3_players = {'css': 'li.dropdown:nth-child(8) > a:nth-child(1)'}
        elements = [desktop, laptop_and_notebooks, components, mp3_players]