---
layout: archive
title: "Palestras"
permalink: /pt/talks/
lang: pt-BR
locale: pt-BR
translation_url: /talks/
author_profile: false
---

<div class="sidebar sticky" style="width=250px;">
{% include toc-talks-pt %}
</div>

<div class="archive">
{% include base_path %}

{% if site.talkmap_link == true %}
<p>Esta é uma lista de palestras recentes, apresentações em congressos, iniciativas de divulgação científica e entrevistas realizadas em parceria com o laboratório. Consulte também as <a href="/talks/talkmap.html">cidades</a> onde estivemos.</p>
{% endif %}

{% assign talk_types = "outreach:Divulgação científica,invited:Palestras convidadas,conference:Apresentações em congressos" | split: "," %}
{% for talk_type in talk_types %}
  {% assign type_parts = talk_type | split: ":" %}
  {% assign talktype = type_parts[0] %}
  {% assign heading = type_parts[1] %}
  <h1 id="toc-{{ talktype }}" class="toc-item-padding">{{ heading }}</h1>
  <ol>
  {% assign filtered_posts = site.talks | where: 'type', talktype | group_by: 'year' %}
  {% for talks_by_year in filtered_posts reversed %}
    <h2 id="toc-{{ talktype }}-{{ talks_by_year.name | slugify }}" class="toc-item-padding"><i class="fa fa-fw fa-calendar" aria-hidden="true"></i>&nbsp;&nbsp;{{ talks_by_year.name }}</h2>
    {% for post in talks_by_year.items %}
      {% include archive-single-talk.html %}
    {% endfor %}
  {% endfor %}
  </ol>
{% endfor %}
</div>