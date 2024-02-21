---
layout: archive
title: "People"
permalink: /people/
author_profile: true
---


{% include base_path %}
<div class="archive">
{% assign filtered_posts = site.people | group_by: 'job' %}
{% for jjob in site.people-order %}
{% assign current_job = filtered_posts | where: 'name', jjob | first %}
  <h3>{{ current_job.name }}</h3>
  <ul>
  {% for post in current_job.items %}
    {% include archive-single-people.html %}
  {% endfor %}
  </ul>
{% endfor %}
</div>