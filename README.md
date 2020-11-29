# curl static as a docker image

Status of Last Deployment:<br>
<img src="https://github.com/ahrechanychenko/curl/workflows/Docker-CI-pipeline/badge.svg?"><br>

An example of baking a static linked curl linux binary into a container alone with nothing else

To run this demo execute `./demo.sh` and follow along with the output

Check the size of the resultant docker image:
`docker images curl-static`

Cleanup:
```bash
docker rmi curl-static
```

Remove all `<empty>` images

```bash
docker image prune
```
