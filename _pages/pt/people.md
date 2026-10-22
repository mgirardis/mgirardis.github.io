---
layout: archive-people
title: "Pessoas"
permalink: /pt/people/
lang: pt-BR
locale: pt-BR
translation_url: /people/
author_profile: true
---

{% include base_path %}

<p>Se você tem interesse em fazer parte do laboratório como estudante ou pós-doutorando(a), <a href="mailto:{{ site.author.email }}">entre em contato</a>. Estamos sempre em busca de pessoas inspiradoras para contribuir com o avanço da Física, da Neurociência e de áreas relacionadas.</p>

{% assign filtered_posts = site.people | group_by: 'job' %}
{% for jjob in site.people-order %}
{% assign current_job = filtered_posts | where: 'name', jjob | first %}
  {% assign translated_job = jjob %}
  {% case jjob %}
    {% when 'Principal investigator' %}{% assign translated_job = 'Pesquisador principal' %}
    {% when 'Postdoctoral researchers' %}{% assign translated_job = 'Pesquisadores de pós-doutorado' %}
    {% when 'Students' %}{% assign translated_job = 'Estudantes' %}
    {% when 'Collaborators' %}{% assign translated_job = 'Colaboradores' %}
    {% when 'Alumni' %}{% assign translated_job = 'Ex-integrantes' %}
  {% endcase %}
  <h3>{{ translated_job }}</h3>
  <ul>
  {% for post in current_job.items %}
    {% include archive-single-people.html %}
  {% endfor %}
  </ul>
{% endfor %}