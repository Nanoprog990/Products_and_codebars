# products_and_codebars
In this repository you can find a web aplication that allows you to create an account and add yous products with their EAN13 barcode(individual product codebar) and generate the DUN14 barcode (code for boxes containing that product; Used for logistics). you will have access to a list of your product, along with both codes and a description.

Notice that in the settings.py file the SECURE_SSL_REDIRECT is set to False in order to allow us to use django's development server (that works on HTTP only). This configuration should be set to True to be deployed to a production environment.
