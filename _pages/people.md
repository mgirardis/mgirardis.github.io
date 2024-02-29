---
layout: archive-people
title: "People"
permalink: /people/
author_profile: true
---


{% include base_path %}


<p>If you're interested in joining our lab as a student or postdoc, <a href="mailto:{{ author.email }}">get in touch</a>. We are constantly looking for inspiring people who could help us steer Physics, Neuroscience and its related disciplines into progress.</p>

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