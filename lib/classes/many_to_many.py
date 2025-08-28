class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Invalid author name")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # ignore attempts to change after init
        if not hasattr(self, "_name"):
            if isinstance(value, str) and len(value) > 0:
                self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        return list({m.category for m in mags}) if mags else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        # else ignore invalid values

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        # else ignore invalid values

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        arts = self.articles()
        return [a.title for a in arts] if arts else None

    def contributing_authors(self):
        authors = [a.author for a in self.articles()]
        return [auth for auth in set(authors) if authors.count(auth) > 2] or None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda m: len(m.articles()))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise Exception("Invalid Author or Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Invalid Title")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # ignore attempts to change after init
        if not hasattr(self, "_title"):
            if isinstance(value, str) and 5 <= len(value) <= 50:
                self._title = value
 

