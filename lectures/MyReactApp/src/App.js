import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class Hello Extends Components{
  render(){
  return <h2> Welcome peeps</h2>;
  }
}

function Hello(props){
return<h2> Welcome {props.name}</h2>;
}

class RollCall Extends Component{
    constructor(props){
        super(props);
        this.state{
            numberPresent=0;
        }
    }
    
    _handleSubmit(e){
        e.preventDefault();
        this.setState((prevState) => ({
            numberPresent: prevState.numberPresent + 1,
        }));
    }
    
    
    render(){
       return (
       <div>
            <h3>Roll Call</h3>
            <p> There are {this.state.numberPresent} in the class </p>
            <form onSubmit = {(e) => this._handleSubmit(e)}>
            <button> Mark yourself present!</button>
            </form>
        </div>
        );
    }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <Hello name="CST438" /> //way to pass in info
        </div>
        <p className="App-intro">
          Great to be here
        </p>
      </div>
    );
  }
}

class GiveMeACat extends Component{
  constructor(props){
    super(props);
    this.state({
      fetchedData : {};
    })
  }
    componentDidMount() {
    fetch('https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best&phrase=cats', {
      headers: {
        'Content-Type': 'application/json',
        'Api-Key': 'mvavf82qwufz6zmgv5hrcsa8',
      }
    })
    .then((response) => response.json())
    .then((json) => {
      if (json.images) {
        this.setState({
          fetchedData: json.images[0].display_sizes[0]
        });
      }
    })
  }
    render(){
        return(
            <div> {this.state.fetchedData.uri ?
            <img src = {this.state.fetchedData.uri} alt = "Cuteness" /> : null} 
            </div>
            );
    }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
       Great to be here
        </p>
        <GiveMeACat />
        <RollCall />
      </div>
    );
  }
}

export default App;
