# BlogApi
## Blog api on DRF

We have deliberately repeated several steps from our earlier examples so the pattern
of creating a new Django project and then its API should start to feel more familiar. The models
are are pure traditional Django but otherwise the URLs, views, and serializers all come from DRF.
We added a detail endpoint to our API and started to explore the power of serializers.
The Blog API is completely functional for local use at this point however there is a big problem:
anyone can update or delete an existing blog post! In other words, we do not have any
permissions in place. In the next chapter we will learn how to apply permissions to protect our
API.

Setting proper permissions is a very important part of any API. As a general strategy, it is a good
idea to set a strict project-level permissions policy such that only authenticated users can view
the API. Then make view-level or custom permissions more accessible as needed on specific API
endpoints.
