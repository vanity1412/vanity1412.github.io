# Vu Van Thong - Chirpy Security Blog

Personal security blog based on [Jekyll Theme Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy).

The site UI defaults to English. The `EN/VI` switcher only changes interface labels such as tabs, search, panels, and theme menu. Post/page content stays in one language per file.

## Preserved data

- `assets/portfolio-assets/`: CV, images, certificates, SOC lab files, and legacy documents.
- `_posts/`: Markdown posts migrated to Jekyll/Chirpy format.
- `_tabs/projects.md`: labs, certificates, and portfolio assets.
- `_tabs/about.md`: profile information.

## New post format

Create files using:

```text
_posts/YYYY-MM-DD-post-slug.md
```

Front matter example:

```yaml
---
title: "Post title"
date: 2026-01-01 09:00:00 +0700
categories: [Blue Team, DFIR]
tags: [soc, forensics, incident-response]
description: "Short description."
---
```

## Local development

```bash
bundle install
bundle exec jekyll serve
```

If theme JS/CSS needs rebuilding:

```bash
npm install
npm run build
```
