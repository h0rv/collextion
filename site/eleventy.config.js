module.exports = (config) => {
	config.addPassthroughCopy('src/assets/img/**/*');
	config.addPassthroughCopy({ 'src/posts/img/**/*': 'assets/img/' });

	config.addWatchTarget("src/assets/js/");

	config.addLayoutAlias('default', 'layouts/default.njk');
	config.addLayoutAlias('post', 'layouts/post.njk');
	config.addLayoutAlias('mostRecs', 'layouts/mostRecs.njk');

	config.addFilter('readableDate', require('./lib/filters/readableDate'));
	config.addFilter('minifyJs', require('./lib/filters/minifyJs'));

	// config.addTransform('minifyHtml', require('./lib/transforms/minifyHtml'));

	config.addCollection('posts', require('./lib/collections/posts'));
	config.addCollection('genres', require('./lib/collections/genres'));
	config.addCollection('mostRecs', require('./lib/collections/mostRecs'));


	return {
		dir: {
			input: 'src',
			output: 'dist'
		},
		// pathPrefix: "/subfolder/",
		templateFormats: ['md', 'njk', 'html'],
		dataTemplateEngine: 'njk',
		markdownTemplateEngine: 'njk'
	};
};
