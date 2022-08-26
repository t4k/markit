# Markdown file start

![pandoc unfortunately uses the same string for img alt attributes and figcaption elements](image.jpg "Göreme Historical National Park and the Rock Sites of Cappadocia")

[t4k:]{.smallcaps} not sure if we can use the [docker://pandoc action](https://github.com/pandoc/pandoc-action-example) because we want to run the `pandoc` command independently for any `.md` source directory that has changed and it is unclear if we can embed the step inside a shell loop or conditional

we probably need to write a script to loop over changed files
