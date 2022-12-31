---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<h2>Peer-reviewed papers</h2>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'paper' | group_by: 'year' | reversed %}
{% for pubs_by_year in filtered_posts %}
  <h3>{{ pubs_by_year.name }}</h3>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<h2>Books</h2>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'book' | group_by: 'year' | reversed %}
{% for pubs_by_year in filtered_posts %}
  <h3>{{ pubs_by_year.name }}</h3>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<h2>Proceedings</h2>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'proceedings' | group_by: 'year' | reversed %}
{% for pubs_by_year in filtered_posts %}
  <h3>{{ pubs_by_year.name }}</h3>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<h2>Theses</h2>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'thesis' | group_by: 'year' | reversed %}
{% for pubs_by_year in filtered_posts %}
  <h3>{{ pubs_by_year.name }}</h3>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>