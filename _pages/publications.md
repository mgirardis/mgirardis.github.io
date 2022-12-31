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
{% assign filtered_posts = site.publications | where: 'pubtype', 'paper' %}
{% for post in filtered_posts reversed %}
  {% include archive-single-publications.html %}
{% endfor %}
</ol>

<h2>Books</h2>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'book' %}
{% for post in filtered_posts reversed %}
  {% include archive-single-publications.html %}
{% endfor %}
</ol>

<h2>Proceedings</h2>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'proceedings' %}
{% for post in filtered_posts reversed %}
  {% include archive-single-publications.html %}
{% endfor %}
</ol>

<h2>Theses</h2>
<ol reversed>
{% assign filtered_posts = site.publications | where: 'pubtype', 'thesis' %}
{% for post in filtered_posts reversed %}
  {% include archive-single-publications.html %}
{% endfor %}
</ol>