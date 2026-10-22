---
layout: archive
title: "Recursos"
permalink: /pt/resources/
lang: pt-BR
locale: pt-BR
translation_url: /resources/
author_profile: false
---

Confira alguns recursos que desenvolvemos, incluindo simulações e ferramentas para análise de dados. Outros códigos estão disponíveis no <a href="https://github.com/mgirardis" target="_blank">meu GitHub</a> e no <a href="https://github.com/neuro-physics/" target="_blank">GitHub do laboratório</a>.

<ul>
{% assign filtered_posts = site.resources | group_by: 'year' %}
{% for resources_by_year in filtered_posts reversed %}
  <h2 class="toc-item-padding"><i class="fa fa-fw fa-calendar" aria-hidden="true"></i>&nbsp;&nbsp;{{ resources_by_year.name }}</h2>
  {% for post in resources_by_year.items %}
    {% include archive-single-resources.html %}
  {% endfor %}
{% endfor %}
</ul>