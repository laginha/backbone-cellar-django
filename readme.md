#README

This is an django version of the REST API supporting the [backbone.js](http://documentcloud.github.com/backbone/) tutorial from [Christophe Coenraets](https://github.com/ccoenraets). All javascript code is his, and you may check the original repository [here](https://github.com/ccoenraets/backbone-cellar).

In his posts ([part1](http://coenraets.org/blog/2011/12/backbone-js-wine-cellar-tutorial-part-1-getting-started/), [part2](http://coenraets.org/blog/2011/12/backbone-js-wine-cellar-tutorial-%E2%80%94-part-2-crud/) and [part3](http://coenraets.org/blog/2011/12/backbone-js-wine-cellar-tutorial-%E2%80%94-part-3-deep-linking-and-application-states/)) he presents a [slim](http://www.slimframework.com/) based REST API. I just thought it would be nice to have a django version (and a [rails](https://github.com/brecke/backbone-cellar-rails) one, too).

##Beware
This is **unfinished** work. Known issues:

1. After creating new wine, the data is not properly updated in the client-side.
2. After deleting wine, the number of wines duplicate in the client-side view.

##Authors
* Brecke
* Laginha

Enjoy.