# dhooks fix

## This issue is in dhooks==1.1.4

Go to client.py in dhooks library, on line **118** change the following variable

```py
    URL_REGEX = r'^(?:https?://)?((canary|ptb)\.)?discord(?:app)?\.com/api/' \
                r'webhooks/(?P<id>[0-9]+)/(?P<token>[A-Za-z0-9\.\-\_]+)/?$'
```

Once you do it the `invalid url` error will be fixed.

---

> It is caused because [dhooks](https://github.com/kyb3r/dhooks) has fixed the issue on github but has not pushed it to pypi

[reference](https://github.com/kyb3r/dhooks/issues/37)
