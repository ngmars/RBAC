import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import {BrowserRouter as Router,Switch, Route} from "react-router-dom";
import Auth from'./Containers/Auth/Auth';
class App extends Component {
  render () {
  return (
    <div className="App">
    <Router>
    <Switch>
        <Route path="/" exact component={Auth}/>
    </Switch>
    </Router>
    

    </div>
  );
};
}

export default App;


