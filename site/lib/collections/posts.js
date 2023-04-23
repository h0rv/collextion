module.exports = (coll) => {
	const posts = [...coll.getFilteredByGlob('src/posts/*.md')];

	// Sort posts by their # number
	posts.sort((a, b) => {
		const aNum = parseInt(a.data.title.match(/#(\d+)/)[1]);
		const bNum = parseInt(b.data.title.match(/#(\d+)/)[1]);
		return bNum - aNum;
	});

	return posts;
};
