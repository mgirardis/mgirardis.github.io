---
layout: archive
title: "Resources"
permalink: /resources/
author_profile: false
---

Find below some resources we developed, including simulations and data analysis tools. More codes are available on either
<a href="https://github.com/mgirardis" target="_blank">my github</a> or the <a href="https://github.com/neuro-physics/" target="_blank">lab's github</a>.

<ul>
{% assign filtered_posts = site.resources | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
  <h2 class="toc-item-padding"><i class="fa fa-fw fa-calendar" aria-hidden="true"></i>&nbsp;&nbsp;{{ pubs_by_year.name }}</h2>
  {% for post in pubs_by_year.items %}
    {% include archive-single-resources.html %}
  {% endfor %}
{% endfor %}
</ul>