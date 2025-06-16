# Multistage Builds
To try this project manually do the following:
- Unzip the `spring-booy-docker.zip`
- Move the `Dockerfile` in the extracted folder
- Change directory into the folder.
- To built the Single Stage Image 
  - Uncomment the single stage lines (Line 3 to Line 9)
  - Build the image - `docker build -t <tag_name> .`
  - Run the container - `docker run -p 8080:8080 <tag_name>`
- To built the Multistage Image
  - Uncomment the single stage lines (Line 12 to Line 24)
  - Build the image - `docker build -t <tag_name> .`
  - Run the container - `docker run -p 8080:8080 <tag_name>`

