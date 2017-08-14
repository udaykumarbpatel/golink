# golink

update the docket-compose.yml file for the volume.

```sh
Before:
      volumes:
      - /Users/udaykumarbpatel/dev/python:/opt/golink-app
After:
    volumes:
      - <path of the code>:/opt/golink-app
```

Run the following command:

```sh
docker-compose build
docker-compose up
```

Usage:
To add a link with key:

    http://localhost:3134/add?key=<key>&value=<value>

To fetch the site:

    http://localhost:3134/?key=<key>
