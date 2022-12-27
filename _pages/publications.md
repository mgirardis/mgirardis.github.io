---
layout: archive
title: "Papers, books, proceedings, chapters, theses"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<ol>
  {% for post in site.publications reversed %}
  {% include archive-single-publications.html %}
{% endfor %}
</ol>