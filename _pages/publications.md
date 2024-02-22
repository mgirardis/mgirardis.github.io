---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

<div class="sidebar sticky"><!--<div style="width=150px;float=left;margin-top:200px;position:relative;">-->
{% include toc-publications %}
</div>

<div class="archive">
{% include base_path %}

You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.

<h1 id="toc-paper">Peer-reviewed papers</h1>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'paper' | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h2 id="toc-paper-{{ pubs_by_year.name }}">{{ pubs_by_year.name }}</h2>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<h1 id="toc-book">Books</h1>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'book' | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h2 id="toc-book-{{ pubs_by_year.name }}">{{ pubs_by_year.name }}</h2>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<h1 id="toc-proceedings">Proceedings</h1>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'proceedings' | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h2 id="toc-proceedings-{{ pubs_by_year.name }}">{{ pubs_by_year.name }}</h2>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>

<h1 id="toc-thesis">Theses</h1>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'thesis' | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h2 id="toc-thesis-{{ pubs_by_year.name }}">{{ pubs_by_year.name }}</h2>
  {% for post in pubs_by_year.items %}
    {% include archive-single-publications.html %}
  {% endfor %}
{% endfor %}
</ol>
</div>