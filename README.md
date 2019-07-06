This is a basic nginx/Flask app that shows some basic info about HTTP requests coming into `localhost`.

Pull the repo and fire up the Docker containers:

    git clone https://github.com/herodionem/docker_load_balancer_demo.git
    cd docker_load_balancer_demo
    docker-compose up --scale app=5 -d # setting `app` to spin up 5 containers but obviously that's arbitrary...

Then you can navigate to `localhost` (no port specified as we are already listening for all incoming HTTP requests on `0.0.0.0`).
Each time you refresh the page you will see your request registered with the application. The thing to watch here will
be the container names change as your requests are distributed among the containers created from the compose command.