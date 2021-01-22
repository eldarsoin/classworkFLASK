{% block card_body %}
@login_required
    <p>Delete post using following form:</p>
    <form action="" method="DELETE" novalidate>
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
        <input type="submit" value="DELETE"> -->
        <button type="submit" class="btn btn-outline-primary">Delete Post</button>
        <button type="submit" class="btn btn-outline-primary">Are you sure?</button>
    </form>
{% endblock %}

{% block card_footer %}
    <span>
        Back to <a href="{{ url_for('posts_list') }}">to all posts </a>.
    </span>
{% endblock %}
