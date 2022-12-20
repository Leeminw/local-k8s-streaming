import React from "react";
import "./index.css";
import App from "./App";
import Login from "./Login";
import SignUp from "./SignUp";
import Video from "./Video";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Box from "@material-ui/core/Box";
import Typography from "@material-ui/core/Typography";
import { Fullscreen } from "@material-ui/icons";
import VideoDetail from "./Videodetails";
function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      fsoftwareengineer, {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

class AppRouter extends React.Component {
  render() {
    return (
      <div>
        <Router>
          <div>
            <Switch>
              <Route path="/login">
                <Login />
              </Route>
              <Route path="/signup">
                <SignUp />
              </Route>
               <Route path="/video">
                 <Video />
               </Route>
              <Route path="/app">
                <App />
              </Route>
              <Route path="/videoDetail">
                <VideoDetail />
              </Route>
            </Switch>
          </div>
          <Box mt={5}>
            <Copyright />
          </Box>
        </Router>
      </div>
    );
  }
}

export default AppRouter;
