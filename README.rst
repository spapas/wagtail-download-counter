.. image:: https://travis-ci.org/fourdigits/wagtail-download-counter.svg?branch=master
    :target: https://travis-ci.org/fourdigits/wagtail-download-counter
    :alt: Build status


========================
Wagtail Download Counter
========================

Wagtail Download Counter is an add-on for `Wagtail CMS <https://github.com/torchbox/wagtail>`_ that keeps track of the number of times a document has been downloaded and shows the count in the Wagtail admin interface.

Usage
=====

In your settings file add the following:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'downloadcounter',
        ...
    ]

Make sure you add ``downloadcounter`` before ``wagtail.wagtaildocs`` in the installed apps.

Run migrations and you're set.

To show the download count in the admin you need to override the ``wagtaildocs/documents/list.html`` template
(by creating a file with exactly that path in the `templates` folder of your apps) with the following content:

.. code-block:: html

    {% load i18n %}
    <table class="listing">
        <col />
        <col  />
        {% if collections %}
            <col />
        {% endif %}
        <col width="16%" />
        <thead>
            <tr class="table-headers">
                <th>
                    {% if not is_searching %}
                        <a href="{% url 'wagtaildocs:index' %}{% if not ordering == "title" %}?ordering=title{% endif %}" class="icon icon-arrow-down-after {% if  ordering == "title" %}teal{% endif %}">
                            {% trans "Title" %}
                        </a>
                    {% else %}
                        {% trans "Title" %}
                    {% endif %}
                </th>
                <th>{% trans "File" %}</th>
                {% if collections %}
                    <th>{% trans "Collection" %}</th>
                {% endif %}
                <th>
                    {% if not is_searching %}
                        <a href="{% url 'wagtaildocs:index' %}{% if not ordering == "-created_at" %}?ordering=-created_at{% endif %}" class="icon icon-arrow-down-after {% if  ordering == "-created_at" %}teal{% endif %}">
                            {% trans "Created" %}
                        </a>
                    {% else %}
                        {% trans "Created" %}
                    {% endif %}
                </th>
                <th>
                    {% trans "Times Downloaded" %}
                </th>
            </tr>
        </thead>
        <tbody>
            {% for doc in documents %}
                <tr>
                    <td class="title">
                        {% if choosing %}
                            <div class="title-wrapper"><a href="{% url 'wagtaildocs:document_chosen' doc.id %}" class="document-choice">{{ doc.title }}</a></div>
                        {% else %}
                            <div class="title-wrapper"><a href="{% url 'wagtaildocs:edit' doc.id %}">{{ doc.title }}</a></div>
                        {% endif %}
                    </td>
                    <td><a href="{{ doc.url }}" class="nolink" download>{{ doc.filename }}</a></td>
                    {% if collections %}
                        <td>{{ doc.collection.name }}</td>
                    {% endif %}
                    <td>
                        <div class="human-readable-date" title="{{ doc.created_at|date:"d M Y H:i" }}">
                            {% blocktrans with time_period=doc.created_at|timesince %}{{ time_period }} ago{% endblocktrans %}
                        </div>
                    </td>
                    <td>
                        {{ doc.downloadcount.count }}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

This is the same template with the addition of the ``doc.downloadcount.count`` column. Please notice that this will introduce a n+1
query problem to your document index page but this can't be resolved right now since wagtail doesn't easy overriding of the 
document listing queryset. This shouldn't be a problem though since only admins view that page.