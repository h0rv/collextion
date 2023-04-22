function fromEntries (iterable) {
    return [...iterable].reduce((obj, [key, val]) => {
      obj[key] = val;
  
      return obj;
    }, {});
  }
  
  /* Collection output format:
  {
    tagName: numberOfPostsWithTagName,
    ...
  }
  */
  module.exports = (coll) => {
    const posts = require('./posts')(coll);
  
    const bookListArr = posts
      .reduce((books, post) => {
        if ('books' in post.data) {
            books = books.concat(post.data.books);
        }
  
        return [...new Set(books)];
      }, [])
      .map((book) => ([
        book,
        coll.getFilteredByTag(book).length
      ]))
      .sort((a, b) => b[1] - a[1]);
    return fromEntries(bookListArr);
  };
  