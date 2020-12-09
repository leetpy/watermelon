自定义样式
==========

1. 创建样式文件 `source/_static/css/style.css`；

.. code-block:: css

    .wy-nav-content {
        max-width: 1400px !important;
    }

2. 创建模板 `source/_templates/layout.html`；

.. code-block::

    {% extends "!layout.html" %}
    {% block extrahead %}
        <link href="{{ pathto("_static/css/style.css", True) }}" rel="stylesheet" type="text/css">
    {% endblock %}



