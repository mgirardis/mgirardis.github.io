---
layout: archive
title: "Talks"
permalink: /talks/
author_profile: false
---

<div class="sidebar sticky" style="width=250px;"><!--<div style="width=150px;float=left;margin-top:200px;position:relative;">-->
{% include toc-talks %}
</div>

<div class="archive">
{% include base_path %}

{% if site.talkmap_link == true %}
<p>Check out the <a href="/talks/talkmap.html">places</a> where I've given a talk!</p>
{% endif %}

<p>&nbsp;</p>
<h1 id="toc-outreach" class="toc-item-padding">Interviews and Science Outreach</h1>
<ul>
{% assign filtered_posts = site.talks | where: 'type', 'outreach' | group_by: 'year' %}
{% for talks_by_year in filtered_posts reversed %}
  <h2 id="toc-outreach-{{ talks_by_year.name }}" class="toc-item-padding"><i class="fa fa-fw fa-calendar" aria-hidden="true"></i>&nbsp;&nbsp;{{ talks_by_year.name }}</h2>
  {% for post in talks_by_year.items %}
    {% include archive-single-talk.html %}
  {% endfor %}
{% endfor %}
</ul>

<p>&nbsp;</p>
<h1 id="toc-invited" class="toc-item-padding">Invited Talks</h1>
<ul>
{% assign filtered_posts = site.talks | where: 'type', 'invited' | group_by: 'year' %}
{% for talks_by_year in filtered_posts reversed %}
  <h2 id="toc-invited-{{ talks_by_year.name }}" class="toc-item-padding"><i class="fa fa-fw fa-calendar" aria-hidden="true"></i>&nbsp;&nbsp;{{ talks_by_year.name }}</h2>
  {% for post in talks_by_year.items %}
    {% include archive-single-talk.html %}
  {% endfor %}
{% endfor %}
</ul>

<p>&nbsp;</p>
<h1 id="toc-conference" class="toc-item-padding">Latest Conference Presentations</h1>
<ul>
{% assign filtered_posts = site.talks | where: 'type', 'conference' | group_by: 'year' %}
{% for talks_by_year in filtered_posts reversed %}
  <h2 id="toc-conference-{{ talks_by_year.name }}" class="toc-item-padding"><i class="fa fa-fw fa-calendar" aria-hidden="true"></i>&nbsp;&nbsp;{{ talks_by_year.name }}</h2>
  {% for post in talks_by_year.items %}
    {% include archive-single-talk.html %}
  {% endfor %}
{% endfor %}
</ul>
</div>