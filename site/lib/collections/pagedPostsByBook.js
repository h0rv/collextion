const siteData = require('../../src/_data/site');

module.exports = (coll) => {
  const bookList = require('./mostCommon')(coll);

  const maxPostsPerPage = siteData.paginate;
  const pagedPosts = [];

  Object.keys(bookList).forEach((bookName) => {
    const taggedPosts = [...coll.getFilteredByTag(bookName)].reverse();
    const numberOfPages = Math.ceil(taggedPosts.length / maxPostsPerPage);

    for (let pageNum = 1; pageNum <= numberOfPages; pageNum++) {
      const sliceFrom = (pageNum - 1) * maxPostsPerPage;
      const sliceTo = sliceFrom + maxPostsPerPage;

      pagedPosts.push({
        bookName,
        number: pageNum,
        posts: taggedPosts.slice(sliceFrom, sliceTo),
        first: pageNum === 1,
        last: pageNum === numberOfPages
      });
    }
  });
  return pagedPosts;
};