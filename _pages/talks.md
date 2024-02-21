---
layout: archive
title: "Talks"
permalink: /talks/
author_profile: false
toc: true
toc_sticky: true
toc_label: "Skip to"
---

{% include toc %}

{% if site.talkmap_link == true %}
<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of all the places I've given a talk!</a></p>
{% endif %}

# Interviews and Science Outreach

<ul>
{% assign filtered_posts = site.talks | where: 'type', 'Community outreach and interviews' %}
{% for post in filtered_posts reversed %}
  {% include archive-single-talk.html %}
{% endfor %}
</ul>

# Invited Talks

<ul>
{% assign filtered_posts = site.talks | where: 'type', 'Invited talks' %}
{% for post in filtered_posts reversed %}
  {% include archive-single-talk.html %}
{% endfor %}
</ul>

# Latest Conference Presentations
<ul>
{% assign filtered_posts = site.talks | where: 'type', 'Conference presentations' %}
{% for post in filtered_posts reversed %}
  {% include archive-single-talk.html %}
{% endfor %}
</ul>
