{% comment %} 使っていないと思われる {% endcomment %}
{% extends 'layouts/base.html' %}

{% block title %}ポスト一覧 | {{ SITE_NAME}}{% endblock title %}

{% block content %}
{% if post %}
    <div class="row">
        <aside class="col-sm-4">
            <div class="card">
                <div class="card-header">
                    <h3 class="card-title">{{ post }}</h3>
                </div>
                <div class="card-body"><img src="" alt="" class="rounded img-fluid"></div>
            </div>
        </aside>
    </div>
{% else %}
    <p>該当のユーザーはまだ投稿していません。</p>
{% endif %}

{% endblock content %}