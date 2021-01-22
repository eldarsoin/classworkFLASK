{% block card_body %}
    <p>Update new post using following form:</p>
    <form action="" method="PUT" novalidate>
        {{ form.hidden_tag() }}
        <p>
            {{ form.title.label }}<br>
            {{ form.title(size=40)}}<br>
            {% for error in form.title.errors %}
                <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </p>
        <p>
            {{ form.body.label }}<br>
            {{ form.body(size=60)}}<br>
            {% for error in form.body.errors %}
                <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </p>
        <!-- {{ form.submit() }}
        <input type="submit" value="Update"> -->
        <button type="submit" class="btn btn-outline-primary">Update Post</button>
    </form>
{% endblock %}

{% block card_footer %}
    <span>
        Back to <a href="{{ url_for('detail_view' , id=post.id) }}">to all posts </a>.
    </span>
{% endblock %}
