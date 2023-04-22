const siteData = require('../../src/_data/site');

module.exports = (coll) => {
  const genreList = require('./genreList')(coll);

  const maxPostsPerPage = siteData.paginate;
  const pagedPosts = [];

  Object.keys(genreList).forEach((genreName) => {
    const taggedPosts = [...coll.getFilteredByGenre(genreName)].reverse();
    const numberOfPages = Math.ceil(taggedPosts.length / maxPostsPerPage);

    for (let pageNum = 1; pageNum <= numberOfPages; pageNum++) {
      const sliceFrom = (pageNum - 1) * maxPostsPerPage;
      const sliceTo = sliceFrom + maxPostsPerPage;

      pagedPosts.push({
        genreName,
        number: pageNum,
        posts: taggedPosts.slice(sliceFrom, sliceTo),
        first: pageNum === 1,
        last: pageNum === numberOfPages
      });
    }
  });

  return pagedPosts;
};
