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
    render(){
        return(
            <div> cuteness ensues </div>
            );
    }
}
