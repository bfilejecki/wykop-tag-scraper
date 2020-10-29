# wykop tag scraper

In order to make the app work first you need to register new app in your wykop account see [LINK](https://www.wykop.pl/dla-programistow/nowa-aplikacja/)   
After you registered your app and obtained app key and app secret you need to create file ``secrets.yml``
with following contents:
```
    app-key: tmp-key
    app-secret: tmp-secret
```

External depencencies needed to run application can be installed via ``pip``.  
To store scraper dependencies I recommend creating virtual env for example using ``venv``.   
In order to create virtual env with ``venv`` execute following command in application directory:   
```bash
    python3 -m venv venv
```
This command creates virtual env called venv   

Now that you have virtual env next step is to install required dependencies.
```bash
    ./venv/bin/pip3 install -r requirements.txt
```

After you are done with above steps you can run application with following command:
```bash
    ./venv/bin/python3 main.py {tag_name}
```

Use ``--help`` command to explore available options.
