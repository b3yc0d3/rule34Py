=================================
How to set Rule34 api credentials
=================================

Since Aug 19, 2025 the `api.rule34.xxx <https://rule34.xxx/index.php?page=help&topic=dapi>`_ REST API requires credentials for all requests made with the REST API. With that changes also came a rate limit of 60 request per 60 seconds.

In order to be able to make requests with `rule34Py <https://pypi.org/project/rule34Py/>`_, you now have to set the api key and your user id.

Reference the :doc:`rule34Py.rule34Py <../../api/rule34Py/rule34>` class documentation for an indication of which workflows have these limits.

Note that as of now, you need an `rule34.xxx <https://rule34.xxx>`_ account.


Setting api credentials
=======================

A `rule34.xxx <https://rule34.xxx>`_ account is required to receive REST API credentials.

#. Use any reasonable browser with javascript enabled to open any URL to the https://rule34.xxx site.

#. Login without account

#. Navigate to https://rule34.xxx/index.php?page=account&s=options

#. Scroll down to **API Access Credentials**, there you will find a long string similar to the one bellow. If you don't see a text similar to the one below, click the checkbox *Generate New Key?* and then *Save* at the bottom, revisit the site.

   .. image:: /_static/api-credentials.png

   - The `api_key` is highlighted in yellow (the long block of text with 128 letters and numbers)
   - The `user_id` is highlighted in green (the short block of seven digits)

   .. important::

        Do not share those information with anyone online!

#. Set the in the previous step retrieved credentials like the following.

   .. code-block:: python

        import rule34Py as r34
        client = r34.rule34Py()

        client.api_key="00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        client.user_id="0000000"
