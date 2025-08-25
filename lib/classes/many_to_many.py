class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)


class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({m.category for m in mags})


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        authors = [a.author for a in self.articles()]
        result = [auth for auth in set(authors) if authors.count(auth) > 2]
        return result if result else None
