import React, { Component } from 'react';
import './App.css';
import Sidebar from './components/sidebar'
import Introduction from './components/introduction'
import About from './components/about'
import Timeline from './components/timeline'
import Highlights from './components/highlights'
// import New from './components/new'

class App extends Component {
  render() {
    return (
      <div id="colorlib-page">
        <div id="container-wrap">
          
         	<Sidebar></Sidebar>
				<div id="colorlib-main">
					<Introduction></Introduction>
					<About></About>
					<Timeline></Timeline>
          <Highlights></Highlights>
          	</div>
      	</div>
      </div>
    );
  }
}

export default App;
