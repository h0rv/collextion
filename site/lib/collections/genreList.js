function fromEntries (iterable) {
  return [...iterable].reduce((obj, [key, val]) => {
    obj[key] = val;

    return obj;
  }, {});
}

/* Collection output format:
{
  genreName: numberOfPostsWithGenreName,
  ...
}
*/
module.exports = (coll) => {
  const posts = require('./posts')(coll);

  const genreListArr = posts
    .reduce((genres, post) => {
      if ('genres' in post.data) {
        genres = genres.concat(post.data.genres);
      }

      return [...new Set(genres)];
    }, [])
    .map((genre) => ([
      genre,
      coll.getFilteredByGenre(genre).length
    ]))
    .sort((a, b) => b[1] - a[1]);
    
  return fromEntries(genreListArr);
};
