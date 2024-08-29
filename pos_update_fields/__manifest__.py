{
    "name": "Pos Update Fields",
    "summary": "Actualiza templates del punto de venta",
    "description": """

    """,

    "author": "Mauricio Idrovo",
    "website": "https://www.mgidev.com.ec",
    "category": "",

    "depends": [ "point_of_sale", ],

    "licenses": "AGPL-3",

    "data": [],

    "assets": {
        "point_of_sale.assets": [
            "pos_update_fields/static/src/xml/*.xml",
            # "pos_update_fields/static/src/js/*.js",
            # "pos_update_fields/static/src/scss/*.scss"
        ]
    },

    'post_load': '',
    "installable": True,
    'auto_install': True,
    'application': True,
}