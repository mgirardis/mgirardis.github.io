---
layout: archive
title: "Publicações"
permalink: /pt/publications/
lang: pt-BR
locale: pt-BR
translation_url: /publications/
author_profile: false
---

{% include base_path %}

<p>Buscamos manter esta lista atualizada, embora algum trabalho possa estar faltando. Você também pode consultar os artigos no <a href="{{ site.author.googlescholar }}" target="_blank">perfil do Google Scholar</a>.</p>

<div class="sidebar sticky" style="width=250px;">
{% include toc-publications-pt %}
</div>

<div class="archive">
{% assign publication_types = "paper:Artigos revisados por pares,book:Livros,proceedings:Trabalhos em anais,thesis:Teses" | split: "," %}
{% for publication_type in publication_types %}
{% assign type_parts = publication_type | split: ":" %}
{% assign pubtype = type_parts[0] %}
{% assign heading = type_parts[1] %}
<h1 id="toc-{{ pubtype }}" class="toc-item-padding">{{ heading }}</h1>
{% assign filtered_posts = site.publications | where: 'pubtype', pubtype | group_by: 'year' %}
{% for pubs_by_year in filtered_posts reversed %}
<h2 id="toc-{{ pubtype }}-{{ pubs_by_year.name | slugify }}" class="toc-item-padding"><i class="fa fa-fw fa-calendar" aria-hidden="true"></i>&nbsp;&nbsp;{{ pubs_by_year.name }}</h2>
<ol reversed>
{% for post in pubs_by_year.items %}
{% include archive-single-publications.html %}
{% endfor %}
</ol>
{% endfor %}
{% endfor %}
</div>