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


User authentication is one of the hardest areas to grasp when first working with web APIs.
Without the benefit of a monolithic structure, we as developers have to deeply understand and
configure our HTTP request/response cycles appropriately.
Django REST Framework comes with a lot of built-in support for this process, including
built-in TokenAuthentication. However developers must configure additional areas like user
registration and dedicated urls/views themselves. As a result, a popular, powerful, and secure
approach is to rely on the third-party packages dj-rest-auth and django-allauth to minimize
the amount of code we have to write from scratch.
