---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
toc: true
toc_sticky: true
---

{% include toc %}

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<!--<h2>Peer-reviewed papers</h2>-->

## Peer-reviewed papers

<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'paper' | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h3>{{ pubs_by_year.name }}</h3>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<!--<h2>Books</h2>-->

## Books

<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'book' | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h3>{{ pubs_by_year.name }}</h3>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<!--<h2>Proceedings</h2>-->

## Proceedings

<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'proceedings' | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h3>{{ pubs_by_year.name }}</h3>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<!--<h2>Theses</h2>-->

## Theses

<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'thesis' | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h3>{{ pubs_by_year.name }}</h3>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>
